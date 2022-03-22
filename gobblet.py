

from argparse import ArgumentParser

# Voici la représentation des Gobblets, n'hésitez pas à l'utiliser.
# 1 pour le joueur 1, 2 pour le joueur 2.
GOBBLET_REPRÉSENTATION = {
    1: ["▫", "◇", "◯", "□"],
    2: ["▪", "◆", "●", "■"],
}


def interpréteur_de_commande():
    parser = ArgumentParser()
    parser.add_argument('IDUL' == 'cepej')

    return parser.parse_args()



def formater_un_gobblet(gobblet):
    if gobblet == []:
        return "   "
    else :
        return f" {((GOBBLET_REPRÉSENTATION[gobblet[0]])[gobblet[1]])} "


def formater_un_joueur(joueur):
    jo = joueur['nom']
    j = joueur['piles']
    return f"{jo}: {formater_un_gobblet(j[0])} {formater_un_gobblet(j[1])} {formater_un_gobblet(j[2])}"


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
        rep += (f"{lig}{'|'.join(listeligne)}"+'\n'+f"  {0}   {1}   {2}   {3} ")
    return rep



def formater_jeu(plateau, joueur):
    longueur = []
    for j in joueur:
        lm = len(j['nom'])
        longueur.append(lm)
    lmax = max(longueur)+3
    esp = max(longueur)

    nbr = ' '*(lmax)+f"0   1   2 "+'\n'
    j0 = ' '*(esp-longueur[0])+f"{formater_un_joueur(joueur[0])}"+'\n'
    j1 = ' '*(esp-longueur[1])+f"{formater_un_joueur(joueur[1])}"+'\n'+'\n'
    grille = f"{formater_plateau(plateau)}"
    return nbr+j0+j1+grille


def formater_les_parties(parties):
    rep = ''
    num = 0
    for dic in parties:
        num += 1 
        rep += f"{num} : {dic['date']}, {(dic['joueurs'])[0]} vs {(dic['joueurs'])[1]}"
        if dic['gagnant'] != None:
            rep += f", gagnant:{dic['gagnant']}"
        rep += '\n'
    return rep


def récupérer_le_coup():
    origine =(input('Donnez le numéro de la pile (p) ou la position sur le plateau (x,y):'))
    destination = input ('Où voulez-vous placer votre gobelet (x,y):')
    return origine, destination