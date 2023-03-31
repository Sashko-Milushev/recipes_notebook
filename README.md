Recipes-Notebook

Recipes-Notebook is a web application that allows users to create, view, edit, and delete recipes. Users can sign up for an account, log in, and browse recipes created by other users. Additionally, users can like and bookmark recipes for easy access later.

Getting Started

Prerequisites

To run Recipes-Notebook, you will need:

--- Python 3.8 or later

--- Django 3.2 or later

INSTALLATION

1. Clone the repository to your local machine: ```git clone https://github.com/your-username/recipes-notebook.git```
2. Install the required dependencies: ```pip install -r requirements.txt```
3. Set up the PostgreSQL database by running the following command: ```docker-compose up```
4. Create a superuser to access the Django admin site: ```python manage.py createsuperuser```

USAGE

1. Start the development server: ```python manage.py runserver```
2. Open a web browser and navigate to http://localhost:8000.
3. (Optional) Log in to an existing account or sign up for a new one.
4. Browse recipes created by other users, create your own recipes, and like/bookmark recipes for easy access later. 

CONTRIBUTING

If you find any bugs or would like to suggest new features, feel free to create an issue or submit a pull request.

CREDITS

Recipes-Notebook was created by Sashko Milushev using Django and Bootstrap.

LICENSE

Recipes-Notebook is licensed under the MIT License. See LICENSE for more information.
