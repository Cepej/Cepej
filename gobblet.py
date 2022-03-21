"""Module Gobblet
Attributes:
    GOBBLET_REPRÉSENTATION (dict): Constante représentant les gobblet des joueurs.
Functions:
    * interpréteur_de_commande - Génère un interpréteur de commande.
    * formater_un_gobblet - Formater la représentation graphique d'un Gobblet.
    * formater_un_joueur - Formater la représentation graphique d'un joueur et de ses piles.
    * formater_plateau - Formater la représentation graphique d'un plateau.
    * formater_jeu - Formater la représentation graphique d'un jeu.
    * formater_les_parties - Formater la liste des dernières parties.
    * récupérer_le_coup - Demander le prochain coup à jouer au joueur.
"""
from argparse import ArgumentParser

# Voici la représentation des Gobblets, n'hésitez pas à l'utiliser.
# 1 pour le joueur 1, 2 pour le joueur 2.
GOBBLET_REPRÉSENTATION = {
    1: ["▫", "◇", "◯", "□"],
    2: ["▪", "◆", "●", "■"],
}


def interpréteur_de_commande():
    """Interpreteur de commande
    Returns:
        Namespace: Un objet Namespace tel que retourné par parser.parse_args().
                   Cette objet aura l'attribut IDUL représentant l'idul du joueur
                   et l'attribut lister qui est un booléen True/False.
    """
    parser = ArgumentParser()

    # Complétez le code ici
    # vous pourriez aussi avoir à ajouter des arguments dans ArgumentParser(...)

    return parser.parse_args()


def formater_un_gobblet(gobblet):
    if gobblet == []:
        return "   "
    else : 
        return f" {((GOBBLET_REPRÉSENTATION[gobblet[0]])[gobblet[1]])} "
    """Formater un Gobblet
    Args:
        gobblet (list): liste vide ou de 2 entier [x, y] représentant le Gobblet
    Returns:
        str: Représentation du Gobblet pour le bon joueur
    """
    


def formater_un_joueur(joueur):
    jo = joueur['nom']
    jetons = joueur['piles']
    return f"{jo}: {formater_un_gobblet(jetons[0])} {formater_un_gobblet(jetons[1])} {formater_un_gobblet(jetons[2])}"
    
    


def formater_plateau(plateau):
    lig = 4
    rep = ''
    for i in plateau[:-1] :
        lig -= 1
        listeligne = []
        for u in i:
            listeligne.append(formater_un_gobblet(u))
        rep += (f"{lig}{'|'.join(listeligne)}"+'\n'+' ───┼───┼───┼───'+'\n')
    
    if plateau[-1]:
        lig -= 1
        listeligne = []
        for u in plateau[-1]:
            listeligne.append(formater_un_gobblet(u))
        rep += (f"{lig}{'|'.join(listeligne)}"+'\n'+f"  {0}   {1}   {2}   {3}")
    return rep
    


def formater_jeu(plateau, joueurs):
    """Formater un jeu
    Args:
        plateau (list): plateau de jeu 4 x 4
        joueurs (list): list de dictionnaire contenant le nom du joueurs et ses piles de Gobblet
    Returns:
        str: Représentation du jeu
    """
    pass


def formater_les_parties(parties):
    """Formater une liste de parties
    L'ordre doit être exactement la même que ce qui est passé en paramètre.
    Args:
        parties (list): Liste des parties
    Returns:
        str: Représentation des parties
    """
    pass


def récupérer_le_coup():
    """Récupérer le coup
    Returns:
        tuple: Un tuple composé d'un origine et de la destination.
               L'origine est soit un entier représentant le numéro de la pile du joueur
               ou une liste de 2 entier [x, y] représentant le Gobblet sur le plateau
               La destination estune liste de 2 entier [x, y] représentant le Gobblet
               sur le plateau
    Examples:
        Quel Gobblet voulez-vous déplacer:
        Donnez le numéro de la pile (p) ou la position sur le plateau (x,y): 0
        Où voulez-vous placer votre Gobblet (x,y): 0,1
        Quel Gobblet voulez-vous déplacer:
        Donnez le numéro de la pile (p) ou la position sur le plateau (x,y): 2,3
        Où voulez-vous placer votre Gobblet (x,y): 0,1
    """
    pass