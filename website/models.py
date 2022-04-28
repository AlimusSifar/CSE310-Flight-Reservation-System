from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):
    first_name = db.Column(db.String(16), nullable=False)
    last_name = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(128), primary_key=True)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    salt = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def get_id(self):
        return self.email

    def __repr__(self):
        return f"<User {self.email}>"


class Aircraft(db.Model):
    reg_no = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    type = db.Column(db.String(6), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    def get_id(self):
        return self.reg_no

    def __repr__(self):
        return f"<Aircraft {self.reg_no} {self.capacity} {self.name}>"


class Airport(db.Model):
    iata = db.Column(db.String(3), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    country = db.Column(db.String(32), nullable=False)
    city = db.Column(db.String(32), nullable=False)

    def get_id(self):
        return self.iata

    def __repr__(self):
        return f"<Airport {self.iata} {self.name} {self.country}>"


class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    callsign = db.Column(db.String(5), nullable=False)
    departure_id = db.Column(db.String(3), db.ForeignKey("airport.iata"), nullable=False)
    arrival_id = db.Column(db.String(3), db.ForeignKey("airport.iata"), nullable=False)
    aircraft_id = db.Column(db.String(8), db.ForeignKey("aircraft.reg_no"), nullable=False)
    weekday = db.Column(db.String(1), nullable=False)
    departure_time = db.Column(db.Time, nullable=False)
    arrival_time = db.Column(db.Time, nullable=False)
    base_price = db.Column(db.Float, nullable=False)

    aircraft = db.relationship("Aircraft", backref="flights", lazy=True)
    departure = db.relationship("Airport", foreign_keys=[departure_id], backref="departures", lazy=True)
    arrival = db.relationship("Airport", foreign_keys=[arrival_id], backref="arrivals", lazy=True)

    def dayToString(self):
        if self.weekday == "5":
            return "Saturday"
        if self.weekday == "6":
            return "Sunday"
        if self.weekday == "0":
            return "Monday"
        if self.weekday == "1":
            return "Tuesday"
        if self.weekday == "2":
            return "Wednesday"
        if self.weekday == "3":
            return "Thursday"
        if self.weekday == "4":
            return "Friday"

    def get_id(self):
        return self.id

    def __repr__(self):
        return f"<Flight {self.callsign} {self.aircraft} {self.departure} {self.arrival} {self.weekday} {self.departure_time} {self.arrival_time} {self.base_price}>"


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ref = db.Column(db.String(5), nullable=False)
    user_id = db.Column(db.String(128), db.ForeignKey("user.email"), nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flight.id"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    flight_class = db.Column(db.String(1), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    user = db.relationship("User", backref="tickets", lazy=True)
    flight = db.relationship("Flight", backref="ticket", lazy=True)

    def __repr__(self):
        return f"<Ticket {self.id} {self.ref} {self.user_id} {self.flight_id} {self.date} {self.price}>"
