def create_filters(app):
    @app.context_processor
    def flight_filter_1():
        def dayToString(flight):
            return flight.dayToString()

        return dict(dayToString=dayToString)

    @app.context_processor
    def flight_filter_2():
        def _12Hours(_24_hours):
            # convert 24 hours to 12 hours format
            return _24_hours.strftime("%I:%M %p")

        return dict(_12Hours=_12Hours)

    @app.context_processor
    def flight_filter_3():
        def calculate_fare(base, adults, childs, class_type):
            multiplier = {
                "0": 1,
                "1": 1.25,
                "2": 1.5,
            }
            base = int(base)
            adults = int(adults)
            childs = int(childs)
            return round(base * (adults + childs * .85) * multiplier[class_type])

        return dict(calculate_fare=calculate_fare)

    @app.context_processor
    def flight_filter_4():
        def flight_class(class_type):
            return {
                "0": "Economy",
                "1": "Business",
                "2": "First Class",
            }[class_type]
        return dict(flight_class=flight_class)
