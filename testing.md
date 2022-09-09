# **Testing** 
## **Validation**

- ### **HTML Files**
    I validated the HTML with W3 Validation Service. The results can be seen below;
    - **home.html & base.html** ![](hungrygoat/static/images/readme/validation/welcome.png)
    - **recipes**![](hungrygoat/static/images/readme/validation/recipes.png)
    - **login**![](hungrygoat/static/images/readme/validation/login.png)
    - **register**![](hungrygoat/static/images/readme/validation/register.png)
    - **profile**![](hungrygoat/static/images/readme/validation/profile.png)
    - **add recipe** ![](hungrygoat/static/images/readme/validation/add_recipe.png)
    - **edit recipe** ![](hungrygoat/static/images/readme/validation/edit_recipe.png)
    - **add category** ![](hungrygoat/static/images/readme/validation/add_category.png)
    - **edit cateogry** ![](hungrygoat/static/images/readme/validation/edit_category.png)
- ### **CSS**
    The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to test the style.css file.
        ![](hungrygoat/static/images/readme/validation/css-validation.png)

- ### **JavaScrip**
  [JSHint Validator](https://jshint.com/) was used to validate all JavaScript files.
  ![](hungrygoat/static/images/readme/validation/js-validation.png)

- ### **Python**
  - [PEP8 Online](http://pep8online.com/) validator was used to test the routes.py file.
  ![](hungrygoat/static/images/readme/validation/pep8.png)


## **Testing User Stories**
 - **First-time User**
      - Be able to understand the purpose of the site easily
        -  The landing page greets users with a welcome message introducing the site.
      ![](hungrygoat/static/images/readme/user_stories/homepage.png)
      - Be able to easily navigate throughout the site
        - The navbar is accessible throughout the site, with clearly named links.
        - The navbar options change depending on whether a user is logged in or not.
        - The navbar changes to a sidenav on smaller screens.
          ![](hungrygoat/static/images/readme/nav-no-user.png) 
          ![](hungrygoat/static/images/readme/nav-user.png) 
      - Experience good responsive design and access the site from different devices
        - The site look good on all screen sizes
        ![](hungrygoat/static/images/readme/amiresponsive2.png)
      - Access recipes without having to create an account
        - All recipes are available to be viewed by all users, logged in or not. 
      - Access a variety of veggie & vegan recipes for different meals of the day
        ![](hungrygoat/static/images/readme/recipes.png)
      - Be able to filter the recipes using ingredients and recipe title
        - The search bar allows users to search with title or ingredients
         ![](hungrygoat/static/images/readme/user_stories/searchbar.png)
      - Have the option to register an account
        - The option to register is available to all users that are not logged in at that moment. The register page is clearly labelled on the navbar. 
        ![](hungrygoat/static/images/readme/user_stories/register.png) 
    - **Returing User**
      - Be able to login to their account
        - Users that have an existing account can select the login page and login into their account.
        ![](hungrygoat/static/images/readme/user_stories/login.png) 
      - Share their own recipes
        - Once a user has logged in they can click the "Add recipe button" and submit their own recipes. There are two "Add Recipe", one is placed on the Profile page and the second one is on the recipes page. ![](hungrygoat/static/images/readme/user_stories/recipes.png) ![](hungrygoat/static/images/readme/user_stories/add_recipe.png)
      - Find the recipes they have shared on their profile page
        - Once the user is logged in, the profile button is displayed on their navbar and they can access their profile where they can find the recipes they have shared![](hungrygoat/static/images/readme/nav-user.png)![](hungrygoat/static/images/readme/user_stories/profile.png)
      - Edit the recipes they have added 
        - An edit button appears on the recipe card if the logged in user, is the users who shared the recipe 
      - Delete the recipes they have added
        - A delete button appears on the recipe card if the logged in user, is the users who shared the recipe  
    - **Admin**
      - Be able to add new recipes.
        - The admin user can add recipes by clicking on the "Add Recipe" button on the profile page 
        - The admin user can add recipes by clicking on the "Add Recipe" button on the recipe page 
      - Be able to edit recipes created by any user
        - When the admin user accesses the recipe page, all recipe cards have an edit button
      - Be able to to delete existing recipes created by any user.
         - When the admin user accesses the recipe page, all recipe cards have an delete button![](hungrygoat/static/images/readme/user_stories/admin-recipes.png)