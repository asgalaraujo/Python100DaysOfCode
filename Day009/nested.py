cidades_visitadas = {
    "Brasil": ["São Paulo", "Jandira", "Barueri"],
    "Argentina": ["Buenos Aires","Cordoba"]
}

print (cidades_visitadas["Brasil"][0])

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][0])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lillie", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}

print(travel_log["Germany"]["cities_visited"][2])