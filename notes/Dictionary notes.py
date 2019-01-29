states = {
    "CA": "California",
    "NJ": "New Jersey",
    "Wi": "Wisconsin",
    "NY": "New York"
}

print(states["CA"])
print(states["Wi"])

nested_dictionary = {
    "CA": {
        "Name": "Califonia",
        "Population": 39500000 # 9,000,000
    },
    "NJ": {
        "Name": "Wisconsin",
        "Population": 9000000 # 9,000,000
    },
    "Wi": {
        "Name": "WIsconsin",
        "Populatin": 5800000 # 5,800,000
    },
    "NY": {
        "Name": "New York",
        "Population": 19500000 # 19,500,000
    },
}

print(nested_dictionary["CA"])
print(nested_dictionary["CA"]["Population"])
print(nested_dictionary["NY"]["Name"])

complex_dictionary = {
    "CA": {
        "Name": "Califonia",
        "Population": 39500000 # 9,000,000
        "City": [
            "Fresno",
            "San Fransisco",
            "Los Angeles"
        ]
    },
    "NJ": {
        "Name": "Wisconsin",
        "Population": 9000000 # 9,000,000
        "City": [
            "Newark",
            "Trenton",
            "Princeton"
        ]
    },
    "Wi": {
        "Name": "WIsconsin",
        "Populatin": 5800000 # 5,800,000
        "City": [
            "Madison",
            "Milwaukee",
            "Green ray"
        ]
    },
    "NY": {
        "Name": "New York",
        "Population": 19500000 # 19,500,000
        "City": [
            "New york city",
            "Rockster",
            "Buffalo"
        ]
    },
}
