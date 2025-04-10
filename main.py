import os
import json

# Function to get information
def studentInformatie():
    studentNaam = input("Wat is je naam?\n")
    # Check if user used only numbers
    while True:
        try:
            studentNummer = int(input("Wat is je studentnummer?\n"))
            break
        except ValueError:
            print("Fout! Je mag alleen gebruiken")
    klas = input("In welke klas zit je?\n")
    # Check if the format is right
    while True:
        geboortedatum = input("Wat is je geboortedatum? (DD/MM/YYYY) \n")

        if len(geboortedatum) == 10 and geboortedatum[2] == '/' and geboortedatum[5] == '/':
            break
        print("Fout! gebruik deze format: DD/MM/YYYY")

    # Store information in dictionary
    student = {
        "studentnaam": studentNaam,
        "studentnummer": studentNummer,
        "klas": klas,
        "geboortedatum": geboortedatum
    }
    return student

# Checks if folder named "data" exists, if not it will make it
os.makedirs("data", exist_ok=True)

student = studentInformatie()

# Create the file name
bestandNaam = f'data/{student["studentnummer"]}.json'

# Create the json file
if os.path.exists(bestandNaam):
    overwrite = input("Dit student bestaat al. Wil je overschrijven? (ja/nee)\n").lower().strip()
    if overwrite != "ja":
        print("Cancelled")
        exit()

# Write the data
with open(bestandNaam, 'w') as file:
    json.dump(student, file, indent=2)
print(f"{student['studentnaam']} opgeslagen in {bestandNaam}")

# Function to get the students numbers from json files
def studentNummersWeergeven():
    studentenNummers = []

    for filename in os.listdir("data"):
        if filename.endswith(".json"):
            studentNummer = filename.split('.')[0]
            studentenNummers.append(studentNummer)
    return studentenNummers

# Function to display the students numbers
def studentGegevens(studentNummer):
    bestandNaam = f'data/{studentNummer}.json'

    with open(bestandNaam, 'r') as file:
        student = json.load(file)

    # To calculate the age
    from datetime import datetime

    birthdate = datetime.strptime(student['geboortedatum'], '%d/%m/%Y')
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    
    # Diplay the informations
    email = f'{studentNummer}@mydavinci.nl'
    print('\nStudent Gegevens:')
    print(f'Naam: {student["studentnaam"]}')
    print(f'Studentnummer: {student["studentnummer"]}')
    print(f'Klas: {student["klas"]}')
    print(f'Geboortedatum: {student["geboortedatum"]}')
    print(f'Leeftijd: {age}')
    print(f'E-mail: {email}')

    terugNaarOverzicht = input("\nWil je terug naar het overzicht? (ja/nee): ").lower().strip()
    if terugNaarOverzicht == 'ja':
        kiesStudent()

# Function for the user to choose a student number
def kiesStudent():
    studentenNummers = studentNummersWeergeven()

    if not studentenNummers:
        print("Er zijn geen studenten opgeslagen")
        return None
    
    print("Beschikbare studentnummers:")
    for nummer in studentenNummers:
        print(nummer)
    
    # Ask if want to continue
    geselecteerdNummer = input("Kies een studentnummer om de details in te zien:\n")

    if geselecteerdNummer in studentenNummers:
        print(f"Je hebt gekozen voor studentnummer {geselecteerdNummer}")
        studentGegevens(geselecteerdNummer)
    else:
        print("Ongeldig studentnummer")

if __name__ == "__main__":
    kiesStudent()