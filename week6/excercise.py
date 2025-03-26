students = {
    "Emma": {"leeftijd": 21, "Wiskunde": 8.5, "Programmeren": 9.0},
    "Liam": {"leeftijd": 22, "Wiskunde": 6.5, "Programmeren": 7.5}
}
# voorbeeld: dict["Emma"] om de value (rechterkant) te krijgen

print(students.keys())
print(students["Emma"]["leeftijd"])  # Print de leeftijd van Emma.
print(students["Liam"]["Wiskunde"]())


students = [
    {
        "naam": "Emma",
        "leeftijd": 21,
        "vakken": [
            ("Wiskunde", 8.5),
            ("Programmeren", 9.0),
            ("Databases", 7.5)
        ]
    },
    {
        "naam": "Liam",
        "leeftijd": 22,
        "vakken": [
            ("Wiskunde", 6.5),
            ("Programmeren", 7.5),
            ("Databases", 8.0)
        ]
    },
    {
        "naam": "Olivia",
        "leeftijd": 20,
        "vakken": [
            ("Wiskunde", 9.0),
            ("Programmeren", 8.0),
            ("Databases", 8.5)
        ]
    }
]

# 1. Print de naam en leeftijd van elke student.
# Tip: Gebruik een for-loop om door de lijst van dictionaries te gaan.
for students in students:
    print(students["naam"])

# 2. Print het cijfer voor 'Programmeren' van elke student.
# Tip: Doorloop de geneste lijst met tuples binnen elke dictionary.

for students in students:
    print(students["vakken"]["Programmeren"])


# 3. Bereken het gemiddelde cijfer voor 'Databases' over alle studenten.
# Tip: Tel alle cijfers bij elkaar op en deel door het aantal studenten.
totaal = 0

for student in students:
    totaal += students["Databases"]
average_score = totaal / 3
print(f"{average_score:.2f}")

# \/\/ OPTIONEEL \/\/

# Voeg een nieuw vak 'Machine Learning' met cijfer 7.8 toe aan alle studenten.
# Tip: Gebruik .append() om de geneste lijst met tuples uit te breiden.

# Zoek de student met het hoogste cijfer voor 'Wiskunde'.
# Tip: Gebruik een variabele om de hoogste waarde bij te houden tijdens de loop.
