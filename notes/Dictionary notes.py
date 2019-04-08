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
            "Rochester",
            "Buffalo"
        ]
    },
}

print(complex_dictionary["NY"]["CITIES"][0])
print(complex_dictionary["NJ"]["CITIES"][2])

print(complex_dictionary.keys())
print(complex_dictionary.items())
print(nested_dictionary.items())

for key, value in complex_dictionary.items():
    print(key)
    print(value)
    print("-" * 20)

print()
for state, info in complex_dictionary.items():
    for title, desc in info.items():
        print(title)
        print(desc)
        print("-" * 20)
    print('=' * 20)

print()
for state, info in complex_dictionary.items():
    for title, desc in info.items():
        print(title)
        print(desc)
        print("-" * 20)
    print('=' * 20)

# Other Notes
states["MN"] = "Mississippi?"  # This isn't Minnesota

states["MN"] = "Minnesota"  # Fixed it.