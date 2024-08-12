# Blog created with Django Framework

In this project, I created a blog to familiarize myself with the Django Framework. On the index page, visitors can see a
list of all blog posts.

![Index page.](/screenshots/Index%20Page.png?raw=true)

By clicking on a post, they are redirected to the post's detail page. where they can leave a
comment, view existing comments (implemented using Django forms and models), or

![Post Page main.](./screenshots/Post%20Page.png?raw=true)

There they can leave a comment or view existing ones (implemented using Django forms and models)

![Post Page comments.](./screenshots/Add%20Comment.png?raw=true)
![Post Page comments.](./screenshots/View%20Comments.png?raw=true)

"Read Later" feature which is implemented using Django sessions turns the post's title color in
the index page to red one.

![Index Page Read Later.](./screenshots/Read%20Later%20Index.png?raw=true)

For post management, the admin can access the admin panel at http://127.0.0.1:8000/admin. Django models have been
initialized
to manage the posts data.

![Post Administration.](./screenshots/Post%20Admin.png?raw=true)

## Installation

> I assume that Python is already installed :grinning:

Clone the repository

```bash
  git clone https://github.com/aimiliospot/Personal-Blog.git
```

Create and activate virtual environment (on Windows)

```bash
  python -m venv virtualenv

  virtualenv\Scripts\activate (Windows)
```

Create and activate virtual environment (on Linux)

```bash
  python -m venv virtualenv

  source virtualenv/bin/activate (Linux)
```

Install the dependecies:

```bash
  pip install -r requirements.txt
```

## Usage

To explore the blog you have to run a test server by running the following commands

```bash
python manage.py runserver
```

Then, in your browser go to `127.0.0.1:8000/blog`

To manage posts, go to the Django administration panel in `127.0.0.1:8000/admin`. There you can login with the following
credentials:

> **Username**: admin \
> **Password**: admin

You can also create a new superuser by running this terminal command

```bash
python manage.py createsuperuser
```

## Tech Stack

[![Tech Stack](https://skillicons.dev/icons?i=python,js,html,css,django,bootstrap)](https://skillicons.dev)

## License

[MIT](https://choosealicense.com/licenses/mit/)
