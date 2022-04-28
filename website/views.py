from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from datetime import date
from . import db
from .models import Airport, Flight, Ticket

from .utils import date_to_day, ticket_ref_generator

from colorama import init, Fore
init(autoreset=True)

views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
def home():
    data = {
        "airports": Airport.query.order_by(Airport.name).all(),
    }
    return render_template("index.html", **data, user=current_user)


@views.route("/search", methods=["GET"])
def search_results():
    data = {
        "departing_airport": request.args.get("departingAirport"),
        "arriving_airport": request.args.get("arrivingAirport"),
        "departing_date": request.args.get("departingDate"),
        "flight_class": request.args.get("flightClass"),
        "adults": request.args.get("adults"),
        "childs": request.args.get("childs"),
    }
    data["flights"] = Flight.query.filter_by(
        departure_id=data['departing_airport'],
        arrival_id=data['arriving_airport'],
        weekday=date_to_day(data['departing_date'])).all()
    return render_template("search_results.html", **data, user=current_user)


@views.route("/booking", methods=["POST"])
@login_required
def booking():
    # print(request.form)  # TEST LINE
    flight = Flight.query.get(request.form.get("flight_id"))
    data = {
        "passengerName": f"{current_user.first_name} {current_user.last_name}",
        "flight_id": flight.id,
        "fromDestination": flight.departure.name,
        "toDestination": flight.arrival.name,
        "departureDate": request.form.get("departing_date"),
        "departureTime": flight.departure_time,
        "class": request.form.get("flight_class"),
        "adults": request.form.get("adults"),
        "children": request.form.get("childs"),
        "price": request.form.get("price"),
    }
    # print(data)  # TEST LINE
    return render_template("booking_confirmation.html", data=data, user=current_user)


@views.route("/booking-confirmation", methods=["POST"])
@login_required
def booking_confirmation():
    # print(request.form)  # TEST LINE
    date_ = request.form.get("departure_date")
    data = {
        "ref": ticket_ref_generator(current_user.email, date_),
        "user_id": current_user.email,
        "flight_id": request.form.get("flight_id"),
        "date": date.fromisoformat(date_),
        "flight_class": request.form.get("flight_class"),
        "price": request.form.get("price"),
    }
    ticket = Ticket(**data)
    # print(ticket)  # TEST LINE
    db.session.add(ticket)
    db.session.commit()
    # print(f"{Fore.GREEN}[L] NEW FLIGHT BOOKED!")  # TEST LINE
    flash("Booking confirmed!", category="success")
    return redirect(url_for("views.user_dashboard"))


@views.route("/dashboard", methods=["GET"])
@login_required
def user_dashboard():
    # print(request.referrer)  # TEST LINE
    data = {
        "tickets": Ticket.query.filter_by(user_id=current_user.email).all()
    }
    # print(data)  # TEST LINE
    return render_template("user.html", **data, user=current_user)


@views.route("/manage-flight", methods=["GET", "POST"])
def manage_flight():
    if request.method == "GET":
        return redirect(url_for("views.home"))
    # print(request.form)  # TEST LINE
    data = {
        "ticket": Ticket.query.filter_by(ref=request.form.get("ticket_id"), user_id=request.form.get("email")).first(),
    }
    # print(data)  # TEST LINE
    return render_template("manage-flight-result.html", **data, user=current_user)
