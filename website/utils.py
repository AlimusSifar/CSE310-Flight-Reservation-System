import random as rd
import datetime as dt
from pytz import timezone

# LOCAL VARIABLES
visits = 0


# FUNCTIONS
def salt_generator(text):
    sref = (ord(ch) for ch in text)
    rd.seed(sum(sref))
    symbols = ("abcdefghijklmnopqrstuvwxyz"
               "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
               "0123456789!@#$%^&*()_+-?")
    return "".join((rd.choice(symbols) for _ in range(10)))


def ticket_ref_generator(user_id, date):
    tref = (ord(ch) for ch in f"{user_id}{date}")
    rd.seed(sum(tref))
    symbols = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"
               "0123456789")
    return "".join((rd.choice(symbols) for _ in range(5)))


def tuple_to_dict(datas, labels):
    return [{k: v for k, v in zip(labels, data)} for data in datas]


def date_to_day(date_: "str | dt.date"):
    if isinstance(date_, str):
        date_ = dt.date.fromisoformat(date_)

    if isinstance(date_, dt.date):
        return date_.weekday()


def decode_flight_class(flight_class):
    if flight_class == "0":
        return "Economy"
    elif flight_class == "1":
        return "Business"
    elif flight_class == "2":
        return "First Class"
    else:
        return None


def visitor_log(visitor_ip):
    global visits
    visits += 1
    print(visits, visitor_ip)  # Test Line
    # if visitor_ip == "172.18.0.1":
    #     return
    with open("./website/static/visitors.log", "a") as log:
        datetime_ = dt.datetime.now(tz=timezone("Asia/Dhaka"))
        log.write(f"{datetime_}, {visitor_ip}\n")
