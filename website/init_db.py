from .utils import salt_generator, tuple_to_dict
from .models import Airport, Aircraft, User, Flight
from .data_ import aircrafts, airports, flights
from . import db
from datetime import date, time
from werkzeug.security import generate_password_hash
from colorama import init, Fore

init(autoreset=True)


def create_admin(kwargs=None):
    if not kwargs:
        # return
        kwargs = {
            "first_name": "Alimus",
            "last_name": "Sifar",
            "email": "alimus.sifar@g.bracu.ac.bd",
            "gender": "m",
            "date_of_birth": date.fromisoformat("1999-10-04"),
            "is_admin": True,
            "password": "admin",
        }

    salt = salt_generator(kwargs["email"])
    kwargs["salt"] = salt
    kwargs["password"] = generate_password_hash(f"{kwargs['password']}-{salt}",
                                                method="sha256")

    user = User(**kwargs)
    db.session.add(user)
    db.session.commit()
    print(f"{Fore.GREEN}[L] ADMIN ADDED!")  # LOGS


def add_airports():
    labels = ("iata", "name", "country", "city")
    datas = tuple_to_dict(airports, labels)
    for data in datas:
        airport = Airport.query.filter_by(iata=data["iata"]).first()
        if not airport:
            db.session.add(Airport(**data))
            print(f"{Fore.GREEN}[L] NEW AIRPORT ADDED!")  # LOGS
        else:
            print(f"{Fore.YELLOW}[W] AIRPORT ALREADY ADDED!")  # LOGS
    db.session.commit()


def add_aircrafts():
    labels = ("reg_no", "name", "type", "capacity")
    datas = tuple_to_dict(aircrafts, labels)
    for data in datas:
        aircraft = Aircraft.query.filter_by(reg_no=data["reg_no"]).first()
        if not aircraft:
            db.session.add(Aircraft(**data))
            print(f"{Fore.GREEN}[L] NEW AIRCRAFT ADDED!")  # LOGS
        else:
            print(f"{Fore.YELLOW}[W] AIRCRAFT ALREADY ADDED!")  # LOGS
    db.session.commit()


def add_flights():
    labels = ("callsign", "aircraft", "departure", "arrival", "weekday",
              "departure_time", "arrival_time", "base_price")
    datas = tuple_to_dict(flights, labels)
    for data in datas:
        flight = Flight.query.filter_by(
            weekday=data["weekday"],
            callsign=data["callsign"],
            departure_id=data["departure"],
            departure_time=data["departure_time"],
        ).first()
        if not flight:
            data["aircraft"] = Aircraft.query.filter_by(
                reg_no=data["aircraft"]).first()
            data["departure"] = Airport.query.filter_by(
                iata=data["departure"]).first()
            data["arrival"] = Airport.query.filter_by(
                iata=data["arrival"]).first()
            data["arrival_time"] = time.fromisoformat(data["arrival_time"])
            data["departure_time"] = time.fromisoformat(data["departure_time"])
            db.session.add(Flight(**data))
            print(f"{Fore.GREEN}[L] NEW FLIGHT ADDED!")  # LOGS
        else:
            print(f"{Fore.YELLOW}[W] FLIGHT ALREADY ADDED!")  # LOGS
    db.session.commit()


def fill_all():
    add_airports()
    add_aircrafts()
    add_flights()
