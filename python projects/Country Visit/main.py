travel_log = [
    {
        "Country": "France",
        "Visites": 12,
        "Cities": ["Paris", "Lille", "Digon"]
    },

    {
        "Country": "Germany",
        "Visites": 5,
        "Cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country():
    new_country = {}
    list_for_cities = []
    country_visit = input("Which country do you visit: ").title()
    cities = input("Which cities do you want to see: e.g: city name, city name, ... ").capitalize()
    list_for_cities.append(cities)
    time_visit = int(input("What time do you want to visit: "))

    new_country["Country"] = country_visit
    new_country["Visites"] = time_visit
    new_country["Cities"] = list_for_cities

    travel_log.append(new_country)

add_new_country()
print(travel_log)