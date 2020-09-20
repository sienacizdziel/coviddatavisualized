import os

#import sqlite3

#import click
#from flask import current_app, g
#from flask.cli import with_appcontext

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
#from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
#from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

'''
db_name = 'cases.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached

'''
# Custom filter
# app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# <img src="https://www.countryflags.io/:be/:shiny/:size.png">

# Configure CS50 Library to use SQLite database

db = SQL("sqlite:///cases.db")



# Make sure API key is set
# if not os.environ.get("API_KEY"):
#     raise RuntimeError("API_KEY not set")


# def get_db():
#     if 'db' not in g:
#         g.db = sqlite3.connect(
#             current_app.config['sqlite:///cases.db'],
#             detect_types=sqlite3.PARSE_DECLTYPES
#         )
#         g.db.row_factory = sqlite3.Row

#     return g.db


# def close_db(e=None):
#     db = g.pop('db', None)

#     if db is not None:
#         db.close()

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        name = request.form.get("country")

        #people refers to total cases
        population = db.execute("SELECT population FROM cases WHERE location =:location ORDER BY date DESC", location=name)
        pos = db.execute("SELECT total_cases FROM cases WHERE location =:location ORDER BY date DESC", location=name)
        deaths = db.execute("SELECT total_deaths FROM cases WHERE location = :location ORDER BY date DESC", location=name)
        age = db.execute("SELECT median_age FROM cases WHERE location = :location ORDER BY date DESC", location=name)

        return render_template("result.html", country= name, population=population[0]["population"], pos= pos[0]["total_cases"], deaths=deaths[0]["total_deaths"], age=age[0]["median_age"])
    else:
        return render_template("index.html")



# @app.after_request
# def after_request(response):
#     response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     response.headers["Expires"] = 0
#     response.headers["Pragma"] = "no-cache"
#     return response

# def close_db(e=None):
#     db = g.pop('db', None)
#     if db is not None:
#         db.close()


'''
def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)

# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
'''