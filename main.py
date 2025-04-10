import os
import json

# Function for the main menu
def hoofdMenu():
    while True:
        print("\n--- Hoofmenu ---")
        print("1. Voeg student toe")
        print("2. Bekijk studenten overzicht")
        print("3. Verwijder student")
        print("4. Stoppen")
        keuze = input("Maak een keuze (1, 2, 3, 4):\n")

        if keuze == '1':
            voegStudentToe()
        elif keuze == '2':
            kiesStudent()
        elif keuze == '3':
            studentNummer = input("Voer het studentnummer in van de student die je wilt verwijderen:\n")
            verwijderStudent(studentNummer)
        elif keuze == '4':
            print("Programma afgesloten")
            break
        else:
            print("Ongeldige keuze, probeer het opnieuw")

# Function to add a student
def voegStudentToe():
    student = studentInformatie()

    # Create the file name
    bestandNaam = f'data/{student["studentnummer"]}.json'

    # Create the json file
    if os.path.exists(bestandNaam):
        overwrite = input("Dit student bestaat al. Wil je overschrijven? (ja/nee)\n").lower().strip()
        if overwrite != "ja":
            print("Cancelled")
            return

    # Write the data
    with open(bestandNaam, 'w') as file:
        json.dump(student, file, indent=2)
    print(f"{student['studentnaam']} opgeslagen in {bestandNaam}")

# Function to get the student's information
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

# Function to check if folder named "data" exists, if not it will make it
os.makedirs("data", exist_ok=True)

# Function to get the students numbers from json files
def studentNummersWeergeven():
    studentenNummers = []

    for filename in os.listdir("data"):
        if filename.endswith(".json"):
            studentNummer = filename.split('.')[0]
            studentenNummers.append(studentNummer)
    return studentenNummers

# Function to display the student's details
def studentGegevens(studentNummer):
    bestandNaam = f'data/{studentNummer}.json'

    with open(bestandNaam, 'r') as file:
        student = json.load(file)

    # To calculate the age
    from datetime import datetime

    birthdate = datetime.strptime(student['geboortedatum'], '%d/%m/%Y')
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    
    # Display the information
    email = f'{studentNummer}@mydavinci.nl'
    print('\nStudent Gegevens:')
    print(f'Naam: {student["studentnaam"]}')
    print(f'Studentnummer: {student["studentnummer"]}')
    print(f'Klas: {student["klas"]}')
    print(f'Geboortedatum: {student["geboortedatum"]}')
    print(f'Leeftijd: {age}')
    print(f'E-mail: {email}')

    delete = input('\nWil je deze student verwijderen? (ja/nee):\n').lower().strip()
    if delete == 'ja':
        verwijderStudent(studentNummer)
    else:
        terugNaarOverzicht = input("\nWil je terug naar het overzicht? (ja/nee): ").lower().strip()
        if terugNaarOverzicht == 'ja':
            kiesStudent()

# Function to delete a student
def verwijderStudent(studentNummer):
    bestandNaam = f'data/{studentNummer}.json'

    if os.path.exists(bestandNaam):
        os.remove(bestandNaam)
        print(f'Student {studentNummer} verwijderd')
    else:
        print('Student bestand niet gevonden')
    
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
    hoofdMenu()