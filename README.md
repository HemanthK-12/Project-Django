# Project Django

![image](https://github.com/HemanthK-12/Project-Django/assets/134306795/2db81996-fcfe-4b26-b9ff-6baf4cf94074)

![city_values](https://github.com/HemanthK-12/Project-Django/assets/134306795/baa165f2-9183-47f4-a0fc-5addf128c194)
![country_values](https://github.com/HemanthK-12/Project-Django/assets/134306795/61372998-7ab7-4e6f-8f94-dc602cc61766)
![countrylanguage_values](https://github.com/HemanthK-12/Project-Django/assets/134306795/8ef4199c-434a-4146-890b-2f165a03f5b3)

I'm making a django-based gui app which connects to my database in mysql and displays informations and makes it easy for querying data.

This is a Django project that includes a single app called `world_app`.

## Project Structure

- `manage.py`: Django's command-line utility for administrative tasks.
- `db.sqlite3`: The SQLite database file.
- `models.py`: Contains the models for the project.
- `world_app/`: The directory for the `world_app` application.
  - `__init__.py`: Makes `world_app` a Python package.
  - `admin.py`: Configuration for the Django admin interface.
  - `apps.py`: Configuration for the `world_app` application.
  - `migrations/`: Directory for database migration files.
  - `models.py`: Contains the models for the `world_app` application.
  - `templates/`: Directory for templates.
    - `world_app/`: Directory for `world_app` specific templates.
      - `index.html`: The main template for the `world_app` application.
  - `templatetags/`: Directory for custom template tags and filters.
    - `attr_filter.py`: Contains custom template filters.
  - `tests.py`: File for test cases.
  - `views.py`: Contains the views for the `world_app` application.
- `world_proj/`: The directory for the Django project.
  - `__init__.py`: Makes `world_proj` a Python package.
  - `asgi.py`: ASGI config for `world_proj` project.
  - `settings.py`: Settings for the `world_proj` Django project.
  - `urls.py`: The URL declarations for the `world_proj` Django project.
  - `wsgi.py`: WSGI config for `world_proj` project.

## Models

The `world_app` application has the following models:

- `City`
- `Country`
- `Countrylanguage`

## Running the Project

To run the project, use the following command:

```sh
python manage.py runserver