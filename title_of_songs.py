import json

# Charger le fichier JSON
file_path = "01_fihirana_ffpm.json"  # Remplacez par le chemin de votre fichier JSON

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Parcourir chaque entrée et ajouter le titre
for key, value in data.items():
    if "hira" in value and len(value["hira"]) > 0:
        # Vérifier si le titre est valide dans andininy 1
        andininy_1 = value["hira"][0]["tononkira"].strip()
        if andininy_1 == "" or andininy_1.startswith("("):
            # Prendre le titre dans andininy 2 si andininy 1 est vide ou invalide
            if len(value["hira"]) > 1:
                andininy_2 = value["hira"][1]["tononkira"]
                titre = andininy_2.split("\n")[0].strip()
            else:
                titre = "Titre inconnu"  # Si andininy 2 est absent
        else:
            # Prendre le titre depuis andininy 1
            titre = andininy_1.split("\n")[0].strip()

        # Enlever la virgule finale s'il y en a
        titre = titre.rstrip(",")

        # Ajouter ou mettre à jour le champ lohateny
        value["lohateny"] = titre.capitalize()

# Sauvegarder les modifications dans le fichier JSON
with open(file_path, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Fichier JSON modifié avec succès.")
