"""
Module main - Interface du gestionnaire de Refuge animalier (procédural)
"""

import Animal
import Refuge


def afficher_menu() -> None:
    """Affiche le menu principal."""
    print(f"\n{'='*60}")
    print("🦁 GESTIONNAIRE DE REFUGE ANIMALIER")
    print(f"{'='*60}")
    print("1. Ajouter un Animal")
    print("2. Afficher tous les animaux")
    print("3. Retirer un Animal")
    print("0. Quitter")
    print(f"{'='*60}\n")


def ajouter_animal_interactif(mon_refuge: dict) -> None:
    """Ajoute un Animal au Refuge."""
    print("\n➕ Ajouter un Animal")
    
    nom = input("Nom: ").strip()
    if not nom:
        print("❌ Nom requis")
        return
    
    print(f"Espèces: {', '.join(Animal.ESPECES)}")
    espece = input("Espèce: ").strip()
    if espece not in Animal.ESPECES:
        print("❌ Espèce invalide")
        return
    
    try:
        age = int(input("Âge (ans): "))
        if age < 0:
            raise ValueError("Âge doit être positif")
    except ValueError:
        print("❌ Âge invalide")
        return
    
    try:
        nouvel_animal = Animal.creer_animal(nom, espece, age)
        Refuge.ajouter_animal(mon_refuge, nouvel_animal)
    except ValueError as e:
        print(f"❌ {e}")


def retirer_animal_interactif(mon_refuge: dict) -> None:
    """Retire un Animal."""
    nom = input("\nNom à retirer: ").strip()
    if nom:
        Refuge.retirer_animal(mon_refuge, nom)


def creer_animaux_demo(mon_refuge: dict) -> None:
    """Crée des animaux de démonstration."""
    animaux = [
        Animal.creer_animal("Shere Khan", "Tigre", 8, 85),
        Animal.creer_animal("Rafiki", "Singe", 15, 75),
        Animal.creer_animal("Skipper", "Pingouin", 5, 95),
        Animal.creer_animal("Zazu", "Autruche", 3, 80),
    ]
    for a in animaux:
        Refuge.ajouter_animal(mon_refuge, a)


def main() -> None:
    """Fonction principale."""
    mon_refuge = Refuge.creer_refuge("Refuge du Roi Lion", capacite=20)
    
    print("\n🌍 Initialisation du Refuge...")
    creer_animaux_demo(mon_refuge)
    
    while True:
        afficher_menu()
        choix = input("Choix: ").strip()
        
        if choix == "1":
            ajouter_animal_interactif(mon_refuge)
        elif choix == "2":
            Refuge.afficher_tous_animaux(mon_refuge)
        elif choix == "3":
            retirer_animal_interactif(mon_refuge)
        elif choix == "0":
            print("\n👋 Au revoir!\n")
            break
        else:
            print("❌ Choix invalide\n")


if __name__ == "__main__":
    main()