# recipe-app-api/
Recipe app api source code

Author: Justin Barros


===== Setup and Run Instructions =====
1) cd recipe-app-api/
2) docker build .
3) docker-compose up
4) Install ModHeader on Chrome or similar Extension.
5) Go to localhost:8000 to view other endpoints (screenshots folder provided).
6) Create User Account: Go to http://localhost:8000/api/user/create/ and create a user.
7) Create User Token: Go to http://localhost:8000/api/user/create/token/


===== Creating Ingredients =====
1) Go to http://localhost:8000/api/recipe/ingredients/
2) Fill in the Ingredient's name field, Click the Post button, and refresh the page.
3) Repeat as needed.


===== Creating Tags =====
1) Go to http://localhost:8000/api/recipe/tags/
2) Fill in the Tag's name field, Click the Post button, and refresh the page.
3) Repeat as needed.


===== Creating Recipes =====
1) Go to http://localhost:8000/api/recipe/recipes/
2) Fill in the Recipe Title field.
3) Select any needed Ingredients.
4) Select any needed Tags.
5) Fill in the Time in Minutes that it will take to create Recipe.
6) Fill in the Price it will cost for the Recipe item.
7) (Optional) Go to http://localhost:8000/api/recipe/recipes/<recipe_id>/.
   For example, http://localhost:8000/api/recipe/recipes/1/
   Then http://localhost:8000/api/recipe/recipes/1/upload-image/
   Click the Choose File button to upload an image of the Recipe.
8) Repeat as needed.


===== Filtering Recipes =====
1) Go to http://localhost:8000/api/recipe/recipes/
2) Use '?' along with 'tags', 'ingredients' ID to filter for specific
   recipe. For example:
    - http://localhost:8000/api/recipe/recipes/?tags=2
    - http://localhost:8000/api/recipe/recipes/?ingredients=3
    - http://localhost:8000/api/recipe/recipes/?tag=1&ingredients=3


===== Filtering Tags =====
1) Go to http://localhost:8000/api/recipe/tags/
2) Filter with:
    - http://localhost:8000/api/recipe/tags/?assigned_only=1
    - http://localhost:8000/api/recipe/tags/?assigned_only=0


===== Filtering Ingredients =====
1) Go to http://localhost:8000/api/recipe/ingredients/
2) Filter with:
    - http://localhost:8000/api/recipe/ingredients/?assigned_only=1
    - http://localhost:8000/api/recipe/ingredients/?assigned_only=0


===== Updating Recipes =====
1) Go to http://localhost:8000/api/recipe/recipes/<recipe_id>/
2) Either use Raw Data or HTML tabs and update the recipes accordingly.
3) Click PUT button after selections are complete.


===== Setup Admin Accounts =====
1) Go to localhost:8000/admin to setup admin account (you can use any
   arbitrary email, it does not have to be registered).


===== Verifying Token from ME Page =====
1) Go to http://localhost:8000/api/user/me/
2) If it loads similarly to the screenshot image in
   screenshots/Token/"User Me Page Token Applied".png


                    TESTING
===== To run with Unit Tests and flake8 =====
1) docker-compose run app sh -c "python manage.py test && flake8"

