from flask import flash, render_template, request, redirect, session, url_for
from hungrygoat import app, db, mongo
from werkzeug.security import generate_password_hash, check_password_hash
from hungrygoat.models import Users, Category


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html", recipes=recipes)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    return render_template("add_recipe.html")


@app.route("/categories")
def categories():
    """
    checks if user is superadmin
    if not, user is redirected to recipes page
    """
    if "user" not in session or session["user"] != "admin":
        flash("You must be a superadmin to manage categories of recipes!")
        return redirect(url_for("recipes"))

    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():

    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to manage categories!")
        return redirect(url_for("profile"))

    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to manage categories!")
        return redirect(url_for("get_tasks"))
    
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


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
    if "user" in session:
        flash("You're already logged in!")
        return redirect(url_for('profile'))

    if request.method == "POST":
        # check if username exists
        existing_user = Users.query.filter(
            Users.user_name == request.form.get("user_name").lower()).all()

        if existing_user:
            request.form.get("user_name")
            # password check
            if check_password_hash(existing_user[0].password, request.form.get(
                    "password")):
                session["user"] = request.form.get("user_name").lower()
                flash("Welcome {}".format(request.form.get("user_name")))
                return redirect(url_for("profile", user_name=session["user"]))
            else:
                # invalid password
                flash("Incorrect username or password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/profile/", methods=["GET", "POST"])
def profile():
    return render_template("profile.html")


@app.route("/logout")
def logout():
    """ removes user from session cookie """
    flash("You have been logged out. See you soon!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")
