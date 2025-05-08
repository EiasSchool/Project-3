import os
import json

# function to get information
def studentInformatie():
    studentNaam = input("Wat is je naam?\n")
    # check if user used only numbers
    while True:
        try:
            studentNummer = int(input("Wat is je studentnummer?\n"))
            break
        except ValueError:
            print("Fout! Je mag alleen gebruiken")
    klas = input("In welke klas zit je?\n")
    # check if the format is right
    while True:
        geboortedatum = input("Wat is je geboortedatum? (DD/MM/YYYY) \n")
        if len(geboortedatum) == 10 and geboortedatum[2] == '/' and geboortedatum[5] == '/':
            break
        print("Fout! gebruik deze format: DD/MM/YYYY")

    # store information in dictionary
    student = {
        "studentnaam": studentNaam,
        "studentnummer": studentNummer,
        "klas": klas,
        "geboortedatum": geboortedatum
    }
    return student

# checks if folder named "data" exists if not it will make it
os.makedirs("data", exist_ok=True)

# ======= MENU =======
while True:
    print("\n--- MENU ---")
    print("1. Student toevoegen")
    print("2. Student details bekijken")
    print("3. Student verwijderen")
    print("4. Student aanpassen")
    print("5. Stoppen")
    keuze = input("Kies een optie:\n")

    if keuze == "1":
        student = studentInformatie()
        bestandNaam = f"data/{student['studentnummer']}.json"

        if os.path.exists(bestandNaam):
            overwrite = input("Dit student bestaat al. Wil je overschrijven? (ja/nee)\n").lower().strip()
            if overwrite != "ja":
                print("Geannuleerd.")
                continue

        with open(bestandNaam, 'w') as file:
            json.dump(student, file, indent=2)
        print(f"{student['studentnaam']} opgeslagen in {bestandNaam}")

    elif keuze == "2":
        studentnummer = input("Voer studentnummer in:\n")
        bestandNaam = f"data/{studentnummer}.json"
        if os.path.exists(bestandNaam):
            with open(bestandNaam, 'r') as file:
                student = json.load(file)
                print(f"Naam: {student['studentnaam']}")
                print(f"Studentnummer: {student['studentnummer']}")
                print(f"Klas: {student['klas']}")
                print(f"Geboortedatum: {student['geboortedatum']}")
                aanpassen = input("Wil je deze student aanpassen? (ja/nee)\n").lower().strip()
                if aanpassen == "ja":
                    # hier hergebruik je de bestaande aanpasfunctionaliteit
                    nieuwe_naam = input(f"Nieuwe naam ({student['studentnaam']}): ") or student['studentnaam']
                    nieuwe_klas = input(f"Nieuwe klas ({student['klas']}): ") or student['klas']
                    nieuwe_geboortedatum = input(f"Nieuwe geboortedatum ({student['geboortedatum']}): ") or student['geboortedatum']
                    student['studentnaam'] = nieuwe_naam
                    student['klas'] = nieuwe_klas
                    student['geboortedatum'] = nieuwe_geboortedatum
                    with open(bestandNaam, 'w') as file:
                        json.dump(student, file, indent=2)
                    print("Student succesvol aangepast.")
        else:
            print("Student niet gevonden.")

    elif keuze == "3":
        studentnummer = input("Voer studentnummer in:\n")
        bestandNaam = f"data/{studentnummer}.json"
        if os.path.exists(bestandNaam):
            os.remove(bestandNaam)
            print("Student verwijderd.")
        else:
            print("Student niet gevonden.")

    elif keuze == "4":
        studentnummer = input("Voer studentnummer in:\n")
        bestandNaam = f"data/{studentnummer}.json"
        if os.path.exists(bestandNaam):
            with open(bestandNaam, 'r') as file:
                student = json.load(file)
            print("Laat leeg om oude waarde te behouden.")
            nieuwe_naam = input(f"Nieuwe naam ({student['studentnaam']}): ") or student['studentnaam']
            nieuwe_klas = input(f"Nieuwe klas ({student['klas']}): ") or student['klas']
            nieuwe_geboortedatum = input(f"Nieuwe geboortedatum ({student['geboortedatum']}): ") or student['geboortedatum']
            student['studentnaam'] = nieuwe_naam
            student['klas'] = nieuwe_klas
            student['geboortedatum'] = nieuwe_geboortedatum
            with open(bestandNaam, 'w') as file:
                json.dump(student, file, indent=2)
            print("Student succesvol aangepast.")
        else:
            print("Student niet gevonden.")

    elif keuze == "5":
        print("Tot ziens!")
        break

    else:
        print("Ongeldige keuze.")
