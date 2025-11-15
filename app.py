from flask import Flask, render_template, request, jsonify, session, redirect
from flask_session import Session
from questions import trivia_1, random_question, bestOf
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
from cs50 import SQL

# initialize app
app = Flask(__name__)

# create database
db = SQL("sqlite:///statistics.db")
accounts_db = SQL("sqlite:///accounts.db")

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# create login route
@app.route("/", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            return render_template("login.html", error="Please provide a username!")
        elif not request.form.get("password"):
            return render_template("login.html", error="Please enter password!")

        user = accounts_db.execute(
            "SELECT * FROM accounts WHERE username = ?", request.form.get("username")
        )

        if len(user) != 1 or not check_password_hash(
            user[0]["hash"], request.form.get("password")
        ):
            return render_template(
                "login.html", error="Invalid username and/ or password!"
            )

        session["user_id"] = user[0]["id"]
        return redirect("/homepage")
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    usernames = accounts_db.execute("SELECT username FROM accounts")

    if request.method == "POST":
        # check whether the given 'username' is already taken from the dictionary of 'used_usernames' or not
        username = request.form.get("username")
        password = request.form.get("password")
        password_re_enter = request.form.get("password_re_enter")

        if username:
            for name in usernames:
                if username == name["username"]:
                    return render_template(
                        "register.html", error="Username already exists."
                    )
        else:
            return render_template("register.html", error="Please provide a username")

        # check if password is given and that password and pass_confirmation match
        if password and (password == password_re_enter):
            hash_password = generate_password_hash(password)
        else:
            return render_template(
                "register.html",
                error="Please check if you entered/ re-entered password correctly",
            )

        accounts_db.execute(
            "INSERT INTO accounts(username, hash) VALUES(?, ?)",
            username,
            hash_password,
        )
        id = accounts_db.execute(
            "SELECT id FROM accounts WHERE username = ? ", username
        )
        session["user_id"] = id[0]["id"]
        return redirect("/homepage")
    else:
        return render_template("register.html")


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/")
        return f(*args, **kwargs)

    return decorated_function


@app.route("/homepage", methods=["GET", "POST"])
@login_required
def homepage():
    return render_template("homepage.html")


@app.route("/search_team")
@login_required
def search():
    query = request.args.get("q")
    if query:
        teams = db.execute(
            "SELECT current_club_name FROM player_profiles WHERE current_club_name LIKE ? GROUP BY ( current_club_name )  ORDER BY ( current_club_name ) ASC LIMIT 5",
            "%" + query + "%",
        )
        print(teams)
        return jsonify(teams)
    else:
        return []


@app.route("/general_quiz", methods=["GET", "POST"])
@login_required
def general_trivia():
    if request.method == "POST":
        team_name = request.form.get("team")
        if team_name:
            try:
                question = trivia_1(team_name)
                session["team_name"] = team_name
                return render_template("general_quiz.html", question=question)
            except ValueError:
                return render_template(
                    "search_team.html",
                    error="Not enough information to start quiz. Please pick another team.",
                )

    else:
        return render_template("search_team.html")


@app.route("/guess", methods=["GET", "POST"])
@login_required
def guess_trivia():
    question, answer, possible_answers = random_question()
    return render_template(
        "guess.html",
        question=question,
        answer=answer,
        possible_answers=possible_answers,
    )


@app.route("/bestOf", methods=["GET", "POST"])
@login_required
def bestOf_trivia():
    question, answer, possible_answers = bestOf()
    return render_template(
        "best_of_season.html",
        question=question,
        answer=answer,
        possible_answers=possible_answers,
    )


@app.route("/retrieve", methods=["GET", "POST"])
@login_required
def retrieve():
    query = request.args.get("q")
    if query == "guess":
        newQuest, newAns, newPossibleAns = random_question()
        return [newQuest, newPossibleAns, newAns]
    elif query == "general":
        return trivia_1(session["team_name"])
    elif query == "bestOf":
        newQuest, newAns, newPossibleAns = bestOf()
        return [newQuest, newPossibleAns, newAns]


@app.route("/points", methods=["GET", "POST"])
def points():
    try:
        points = int(request.form.get("points"))
    except ValueError:
        pass
    if points:
        try:
            player_data = accounts_db.execute(
                "SELECT points FROM accounts WHERE id = ?", session["user_id"]
            )
            player_points = player_data[0]["points"]
            if player_points:
                player_points += points
            else:
                player_points = points
            accounts_db.execute(
                "UPDATE accounts SET points = ? WHERE id = ?",
                player_points,
                session["user_id"],
            )
        except TypeError:
            pass
    return render_template("homepage.html")


@app.route("/scoreboard")
@login_required
def scoreboard():
    return render_template(
        "scoreboard.html",
        data=accounts_db.execute(
            "SELECT id, username, points FROM accounts ORDER BY (points) DESC"
        ),
    )


if __name__ == "__main__":
    app.run()
