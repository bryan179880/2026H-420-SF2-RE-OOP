"""Module refuge - API minimale pour gérer un refuge d'animaux."""

from typing import Dict, List, Optional
import animal as A


def creer_refuge(nom: str, capacite: int = 10) -> Dict:
    """Crée et retourne une structure de refuge simple."""
    return {"nom": nom, "capacite": capacite, "animaux": []}


def ajouter_animal(refuge: Dict, animal: A.Animal) -> None:
    """Ajoute un animal au refuge si la capacité le permet.

    Lève ValueError si le refuge est plein ou si un animal du même nom existe.
    """
    if len(refuge["animaux"]) >= refuge["capacite"]:
        raise ValueError("Refuge plein")
    if any(a.nom == animal.nom for a in refuge["animaux"]):
        raise ValueError("Un animal avec ce nom existe déjà")
    refuge["animaux"].append(animal)


def retirer_animal(refuge: Dict, nom: str) -> Optional[A.Animal]:
    """Retire un animal par nom et le retourne, ou None si non trouvé."""
    for i, a in enumerate(refuge["animaux"]):
        if a.nom == nom:
            return refuge["animaux"].pop(i)
    return None


def afficher_tous_animaux(refuge: Dict) -> None:
    """Affiche tous les animaux du refuge."""
    if not refuge["animaux"]:
        print("Aucun animal dans le refuge.")
        return
    print(f"Animaux dans {refuge['nom']} ({len(refuge['animaux'])}/{refuge['capacite']}):")
    for a in refuge["animaux"]:
        print(f"- {a} -> bruit: {a.faire_bruit()}")
