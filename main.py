import os
import json

#function to get information
def studentInformatie():
    studentNaam = input("Wat is je naam?\n")
    #check if user used only numbers
    while True:
        try:
            studentNummer = int(input("Wat is je studentnummer?\n"))
            break
        except ValueError:
            print("Fout! Je mag alleen gebruiken")
    klas = input("In welke klas zit je?\n")
    #check if the format is right
    while True:
        geboortedatum = input("Wat is je geboortedatum? (DD/MM/YYYY) \n")

        if len(geboortedatum) == 10 and geboortedatum[2] == '/' and geboortedatum[5] == '/':
            break
        print("Fout! gebruik deze format: DD/MM/YYYY")

#store information in dictionary
    student = {
        "studentnaam": studentNaam,
        "studentnummer": studentNummer,
        "klas": klas,
        "geboortedatum": geboortedatum
    }
    return student

#checks if folder named "data" exits if not it will make it
os.makedirs("data", exist_ok=True)

student = studentInformatie()

#create the file name
bestandNaam = f'data/{student['studentnummer']}.json'

#create the json file
if os.path.exists(bestandNaam):
    overwrite = input("Dit student bestaat al. Wil je overschrijven? (ja/nee)\n").lower().strip()
    if overwrite != "ja":
        print("Cancelled")
        exit()

#Write the data
with open(bestandNaam, 'w') as file:
    json.dump(student, file, indent=2)
print(f"{student['studentnaam']} opgeslagen in {bestandNaam}")