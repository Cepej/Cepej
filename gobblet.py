
from argparse import ArgumentParser 
"importe un module"

# Voici la représentation des Gobblets, n'hésitez pas à l'utiliser.
# 1 pour le joueur 1, 2 pour le joueur 2.
GOBBLET_REPRÉSENTATION = {
    1: ["▫", "◇", "◯", "□"],
    2: ["▪", "◆", "●", "■"],
}


def interpréteur_de_commande():
    "interprète la commande "
    parser = ArgumentParser()
    parser.add_argument('IDUL', help ='Idul du joueur')
    parser.add_argument('-l',dest = 'lister', help = 'lister les parties existantes')
    return parser.parse_args()



def formater_un_gobblet(gobblet):
    "formate un gobblet"
    if gobblet == []:
        return "   "
    else :
        return f" {((GOBBLET_REPRÉSENTATION[gobblet[0]])[gobblet[1]])} "


def formater_un_joueur(joueur):
    "formate un joeur"
    jo = joueur['nom']
    j = joueur['piles']
    return f"{jo}: {formater_un_gobblet(j[0])} {formater_un_gobblet(j[1])} {formater_un_gobblet(j[2])}"


def formater_plateau(plateau):
    "formate le plateau"
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
    "formate le jeu"
    longueur = []
    for j in joueur:
        lm = len(j['nom'])
        longueur.append(lm)
    lmax = max(longueur)+3
    esp = max(longueur)

    nbr = ' '*(lmax)+"0   1   2 "+'\n'
    j0 = ' '*(esp-longueur[0])+f"{formater_un_joueur(joueur[0])}"+'\n'
    j1 = ' '*(esp-longueur[1])+f"{formater_un_joueur(joueur[1])}"+'\n'+'\n'
    grille = f"{formater_plateau(plateau)}"
    return nbr+j0+j1+grille


def formater_les_parties(parties):
    "formate les parties"
    rep = ''
    num = 0
    party = parties['parties']
    for dic in party:
        num += 1
        rep += f"{num} : {dic['date']}, {(dic['joueurs'])[0]} vs {(dic['joueurs'])[1]}"
        if dic['gagnant'] is not None:
            rep += f", gagnant:{dic['gagnant']}"
        rep += '\n'
    return rep


def récupérer_le_coup():
    "récupère le coup"
    orig =input('Donnez le numéro de la pile (p) ou la position sur le plateau (x,y):')
    if len(orig) <= 2 :
        origine = int(orig)
    else:
        origine = [int(orig[0]),int(orig[-1])]
    dest = input ('Où voulez-vous placer votre gobelet (x,y):')
    destination = [int(dest[0]),int(dest[-1])]
    return origine, destination
