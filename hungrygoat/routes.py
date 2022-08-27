from flask import flash, render_template, request, redirect, session, url_for
from hungrygoat import app, db, mongo
from werkzeug.security import generate_password_hash, check_password_hash
from hungrygoat.models import Users


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/recipes")
def recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    return render_template("add_recipe.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if user already exists
        existing_user = Users.query.filter(
            Users.user_name == request.form.get("user_name").lower()).all()

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        
        user = Users(
            user_name=request.form.get("user_name").lower(),
            email=request.form.get("email").lower(),
            password=generate_password_hash(request.form.get("password")),
        )

        db.session.add(user)
        db.session.commit()

        # query postgress db to get the id of the user
        # saves the user_id into a variable
        new_user = Users.query.get_or_404(user.id)

        # add user to mongoDB
        user_profile = {
            "user_id": str(new_user.id),
            "fave_recipes": [],
            "my_recipes": []
        }

        mongo.db.users.insert_one(user_profile)

        # puts user into 'session' cookie
        session["user"] = request.form.get("user_name")
        flash("Registration successful!")
        return redirect(url_for("register", username=session["user"]))
       
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")
