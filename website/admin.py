from flask import Blueprint, request, redirect, render_template, url_for, flash
from flask_login import login_required, current_user
from datetime import date, time
from . import db
from .models import Aircraft, Airport, Flight

from colorama import init, Fore

init(autoreset=True)

admin = Blueprint("admin", __name__)


@admin.route("/dashboard", methods=["GET"])
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        print(f"{Fore.RED}[E] NOT AN ADMIN!")  # TEST LINE
        flash("You are not an admin!", category="error")
        return redirect(url_for("views.user_dashboard"))
    data = {
        "aircrafts": Aircraft.query.order_by(Aircraft.name).all(),
        "airports": Airport.query.order_by(Airport.country, Airport.city).all(),
        "flights": Flight.query.all(),
    }
    return render_template("admin.html", **data, user=current_user)


@admin.route('/add-aircraft', methods=["POST"])
@login_required
def add_aircraft():
    if not current_user.is_admin:
        print(f"{Fore.RED}[E] NOT AN ADMIN!")  # TEST LINE
        flash("You are not an admin!", category="error")
        return redirect(url_for("views.home"))
    # print(request.form)  # TEST LINE
    data = {
        "reg_no": request.form.get("aircraftReg"),
        "name": request.form.get("aircraftName"),
        "type": request.form.get("aircraftType"),
        "capacity": request.form.get("aircraftCapacity"),
    }
    aircraft = Aircraft.query.filter_by(reg_no=data["reg_no"]).first()
    if not aircraft:
        aircraft = Aircraft(**data)
        db.session.add(aircraft)
        db.session.commit()
        # print(f"{Fore.GREEN}[L] NEW AIRCRAFT REGISTERED!")  # TEST LINE
        flash("Aircraft added to database!", category="success")
    else:
        # print(f"{Fore.YELLOW}[W] AIRCRAFT ALREADY REGISTERED!")  # TEST LINE
        flash("Aircraft already added!", category="alert")

    print(request.referrer)
    return redirect(request.referrer)


@admin.route('/add-airport', methods=["POST"])
@login_required
def add_airport():
    if not current_user.is_admin:
        print(f"{Fore.RED}[E] NOT AN ADMIN!")  # TEST LINE
        flash("You are not an admin!", category="error")
        return redirect(url_for("views.home"))
    # print(request.form)  # TEST LINE
    data = {
        "iata": request.form.get("iata").upper(),
        "name": request.form.get("airportName"),
        "country": request.form.get("airportCountry"),
        "city": request.form.get("airportCity"),
    }
    airport = Airport.query.filter_by(iata=data["iata"]).first()
    if not airport:
        airport = Airport(**data)
        db.session.add(airport)
        db.session.commit()
        # print(f"{Fore.GREEN}[L] NEW AIRPORT REGISTERED!")  # TEST LINE
        flash("Airport added to database!", category="success")
    else:
        # print(f"{Fore.YELLOW}[W] AIRPORT ALREADY REGISTERED!")  # TEST LINE
        flash("Airport already added!", category="alert")
    print(request.referrer)
    return redirect(request.referrer)


@admin.route('/add-flight', methods=["POST"])
@login_required
def add_flight():
    if not current_user.is_admin:
        # print(f"{Fore.RED}[E] NOT AN ADMIN!")  # TEST LINE
        flash("You are not an admin!", category="error")
        return redirect(url_for("views.home"))
    # print(request.form)  # TEST LINE
    data = {
        "callsign": request.form.get("callsign"),
        "aircraft_id": request.form.get("aircraft"),
        "weekday": request.form.get("flightDay"),
        "departure_time": time.fromisoformat(request.form.get("departureTime")),
        "arrival_time": time.fromisoformat(request.form.get("arrivalTime")),
        "departure_id": request.form.get("departingAirport"),
        "arrival_id": request.form.get("arrivingAirport"),
        "base_price": request.form.get("baseFare"),
    }
    flight = Flight.query.filter_by(
        weekday=data["weekday"],
        callsign=data["callsign"],
        departure_id=data["departure_id"],
        arrival_id=data["arrival_id"],
    ).first()
    print(flight)
    if not flight:
        flight = Flight(**data)
        db.session.add(flight)
        db.session.commit()
        # print(f"{Fore.GREEN}[L] NEW FLIGHT REGISTERED!")  # TEST LINE
        flash("Flight added to database!", category="success")
    else:
        # print(f"{Fore.YELLOW}[W] FLIGHT ALREADY REGISTERED!")  # TEST LINE
        flash("Flight already added!", category="alert")

    print(request.referrer)
    return redirect(request.referrer)


@admin.route('/delete-flight', methods=["POST"])
@login_required
def delete_flight():
    if not current_user.is_admin:
        # print(f"{Fore.RED}[E] NOT AN ADMIN!")  # TEST LINE
        flash("You are not an admin!", category="error")
        return redirect(url_for("views.home"))

    flight_id = request.form.get("flight_id"),

    Flight.query.filter_by(id=flight_id).delete()
    # db.session.delete(flight)
    db.session.commit()
    # print(f"{Fore.GREEN}[L] FLIGHT DELETED!")  # TEST LINE
    flash("Flight deleted!", category="success")
    print(request.referrer)  # TEST LINE
    return redirect(request.referrer)


@admin.route('/fill-data', methods=["GET"])
@login_required
def fill_data():
    if not current_user.is_admin:
        # print(f"{Fore.RED}[E] NOT AN ADMIN!")  # TEST LINE
        flash("You are not an admin!", category="error")
        return redirect(url_for("views.home"))
    print(f"{Fore.GREEN}[L] FILLING DATA!")
    from .init_db import fill_all
    fill_all()
    return redirect(url_for("admin.admin_dashboard"))


@admin.route('/create-admin', methods=["GET"])
def create_admin():
    if current_user.is_anonymous:
        # print(f"{Fore.RED}[E] NOT AN USER!")  # TEST LINE
        flash("You are not registered!", category="alert")
        return redirect(url_for("views.home"))
    print(f"{Fore.GREEN}[L] FILLING DATA!")
    from .init_db import create_admin
    create_admin()
    flash("Admin account created!", category="success")
    return redirect(url_for("admin.admin_dashboard"))
