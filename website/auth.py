from flask import Blueprint, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from datetime import date
from . import db
from .models import User
from .utils import salt_generator

from colorama import init, Fore

init(autoreset=True)

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    user = User.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password, f"{password}-{user.salt}"):
            login_user(user)
            # print(f"{Fore.GREEN}[L] {user.last_name.upper()} LOGGED IN!")  # TEST LINE
            flash("Logged in successfully!", category="success")
            return redirect(request.referrer)
        # print(f"{Fore.RED}[E] INVALID PASSWORD!")  # TEST LINE
        flash("Invalid password!", category="error")
    else:
        # print(f"{Fore.RED}[E] USER NOT FOUND!")  # TEST LINE
        flash("User not found!", category="error")
    return redirect(request.referrer)


@auth.route("/register", methods=["POST"])
def register():
    data = {
        "first_name": request.form.get("firstName"),
        "last_name": request.form.get("lastName"),
        "email": request.form.get("email"),
        "date_of_birth": date.fromisoformat(request.form.get("dateOfBirth")),
        "gender": request.form.get("gender"),
    }
    user = User.query.filter_by(email=data["email"]).first()
    if not user:
        password1 = request.form.get("password")
        password2 = request.form.get("passwordCheck")
        if password1 == password2:
            data["salt"] = salt_generator(data["email"])
            data["password"] = generate_password_hash(
                f"{password1}-{data['salt']}", method="sha256")
            user = User(**data)
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            # print(f"{Fore.GREEN}[L] NEW USER REGISTERED!")  # TEST LINE
            flash("Account created successfully!", category="success")
            return redirect(request.referrer)
        # print(f"{Fore.RED}[E] PASSWORDS DID NOT MATCH!")  # TEST LINE
        flash("Passwords don't match.", category="error")
    else:
        # print(f"{Fore.YELLOW}[W] USER ALREADY REGISTERED!")  # TEST LINE
        flash("Email already registered!", category="error")
    return redirect(request.referrer)


@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(request.referrer)


# @auth.route("/reset-password", methods=["POST"])
# def reset_password():
#     if request.method == "POST":
#         data = request.form
#         print(data)
#     return render_template("reset-password.html", username=session.get("username"))
