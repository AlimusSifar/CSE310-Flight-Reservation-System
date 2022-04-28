airports = [
    # ("__iata__", "__name__", "__country__", "__city__"),
    ("DAC", "Hazrat Shahjalal International Airport", "Bangladesh", "Dhaka"),
    ("CGP", "Shah Amanat International Airport", "Bangladesh", "Chittagong"),
    ("CXB", "Cox's Bazar Airport", "Bangladesh", "Cox's Bazar"),
    ("ZYL", "Osmani International Airport", "Bangladesh", "Sylhet"),
    ("BZL", "Barisal Airport", "Bangladesh", "Barisal"),
    ("JSR", "Jessore Airport", "Bangladesh", "Jessore"),
    ("RJH", "Shah Makhdum Airport", "Bangladesh", "Rajshahi"),
    ("SPD", "Saidpur Airport", "Bangladesh", "Saidpur"),
    ("CCU", "Kolkata International Airport", "India", "Kolkata"),
    ("DEL", "Indira Gandhi International Airport", "India", "New Delhi"),
    # ("MED", "Prince Mohammad bin Abdulaziz Airport", "Saudi Arabia", "Medina"),
    # ("JED", "King Abdulaziz International Airport", "Saudi Arabia", "Jeddah"),
    # ("RUH", "King Khalid International Airport", "Saudi Arabia", "Riyadh"),
    # ("DOH", "Hamad International Airport", "Qatar", "Doha"),
    # ("DXB", "Dubai International Airport", "United Arab Emirates", "Dubai"),
    # ("AUH", "Abu Dhabi International Airport", "United Arab Emirates",
    #  "Abu Dhabi"),
    # ("LHR", "Heathrow Airport", "United Kingdom", "London"),
    # ("MAN", "Manchester Airport", "United Kingdom", "Manchester"),
]

aircrafts = [
    # ("__reg__", "__name__", "__type__", "__capacity__"),
    # ("__reg__", "__name__", "__type__", "__capacity__"),
    # ("__reg__", "__name__", "__type__", "__capacity__"),
    ("A6-ECY", "Boeing 777-31H(ER)", "B77W", "360"),
    ("A6-ECZ", "Boeing 777-31H(ER)", "B77W", "360"),
    ("HZ-AK24", "Boeing 777-368(ER)", "B77W", "360"),
    ("VT-ILR", "Airbus A321-252NX", "A21N", "240"),
    ("S2-AFL", "Boeing 737-83N", "B738", "200"),
    ("S2-AFM", "Boeing 737-83N", "B738", "200"),
    ("S2-AKE", "De Havilland Canada Dash 8-400", "DH8D", "90"),
    ("S2-AKF", "De Havilland Canada Dash 8-400", "DH8D", "90"),
    ("S2-AHM", "Boeing 777-3E9(ER)", "B77W", "420"),
    ("S2-AHN", "Boeing 777-3E9(ER)", "B77W", "420"),
    ("S2-AJX", "Boeing 787-9 Dreamliner", "B789", "290"),
    ("S2-AJY", "Boeing 787-9 Dreamliner", "B789", "290"),
    ("S2-AHF", "ATR 72-500", "AT75", "70"),
    ("S2-AHG", "ATR 72-500", "AT75", "70"),
    ("S2-AEQ", "Boeing 737-8HO", "B738", "160"),
    # ("S2-AHH", "ATR 72-500", "AT75", "70"),
]

flights = [
    # ("callsign", "aircraft", "departure", "arrival", "weekday", "departure_time", "arrival_time", "base_price"),
    ("BG605", "S2-AKE", "DAC", "ZYL", "0", "20:45:00", "21:30:00", "4000"),
    ("BG606", "S2-AKE", "ZYL", "DAC", "0", "22:15:00", "23:15:00", "4000"),
    ("BG605", "S2-AKE", "DAC", "ZYL", "1", "20:45:00", "21:30:00", "4000"),
    ("BG606", "S2-AKE", "ZYL", "DAC", "1", "22:15:00", "23:15:00", "4000"),
    ("BG605", "S2-AKE", "DAC", "ZYL", "2", "20:45:00", "21:30:00", "4000"),
    ("BG606", "S2-AKE", "ZYL", "DAC", "2", "22:15:00", "23:15:00", "4000"),
    ("BG605", "S2-AKE", "DAC", "ZYL", "4", "20:45:00", "21:30:00", "4000"),
    ("BG606", "S2-AKE", "ZYL", "DAC", "4", "22:15:00", "23:15:00", "4000"),
    ("BG605", "S2-AKE", "DAC", "ZYL", "5", "20:45:00", "21:30:00", "4000"),
    ("BG606", "S2-AKE", "ZYL", "DAC", "5", "22:15:00", "23:15:00", "4000"),
    ("BG467", "S2-AKE", "DAC", "JSR", "0", "17:45:00", "18:45:00", "4000"),
    ("BG468", "S2-AKE", "JSR", "DAC", "0", "19:15:00", "20:15:00", "4000"),
    ("BG467", "S2-AKF", "DAC", "RJH", "6", "14:00:00", "11:50:00", "3500"),
    ("BG468", "S2-AKF", "RJH", "DAC", "6", "15:30:00", "16:30:00", "4000"),
    ("BG467", "S2-AKE", "DAC", "BZL", "5", "11:00:00", "11:50:00", "3500"),
    ("BG468", "S2-AKE", "BZL", "DAC", "5", "12:15:00", "13:10:00", "4000"),
    ("BG467", "S2-AEQ", "DAC", "CXB", "1", "15:00:00", "16:00:00", "3500"),
    ("BG468", "S2-AEQ", "CXB", "DAC", "1", "12:15:00", "13:10:00", "4000"),
    # ("BG101", "AC-ABC", "DAC", "DOH", "0", "22:00:00", "04:00:00", "8500"),
    # ("BG102", "AC-ABC", "DOH", "DAC", "0", "12:15:00", "13:10:00", "4000"),
]
