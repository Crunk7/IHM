import tkinter as tk
import time as t
import rotate as r
# from PIL import ImageTk, Image
"""
image = Image.open("./chat.jpg")
photo = ImageTk.PhotoImage(image)
"""
"""
- test si il y superposition de porte et annule la creation si oui
(overlapping fonction tkinter )
- test si la porte supprimé a des cercles blanc:
    si oui cherche le lien associee et le supprime
    si non ne fait que supprimer la porte
    fonction devant etre utilisee pour la rotation pour refaire une liaison
    avec la nouvelle porte
- peut etre modifier la creation de lien pour qu'elle se fasse automatiquement
lorsqu'on clic sur une entree ou une sortie
"""
i = 0  # variable comptant les portes
coordonne = []


def intersection(l1, l2):
    """
    cherche le premier objet etant a la fois dans l1 et l2
    """
    for a in l1:
        for b in l2:
            if a == b:
                return a


def testlier(canva, j, position):
    """
    test si le joint de la porte 'j' a la position est lié ou pas
    """
    objet1 = canva.find_withtag("joint"+str(j))
    objet2 = canva.find_withtag(position)
    objet3 = intersection(objet1, objet2)
    print("intersection", canva.gettags(objet3))
    couleur = canva.itemcget(objet3, "fill")
    print("couleur", couleur)
    if couleur == canva.cget("background"):
        return False
    elif couleur == 'white':
        return True
    else:
        # en cas d'erreur
        return -1


def afficher_create_robot():
    """
    a revoir: faire dans un autre module avec une fonction generique
    parametre : fenetre_x, fenetre_y
    fenetre_x.pack_forget()
    fenetre_y.pack(expand=True, fill='both')
    """
    global fenetre_robot1, fenetre_menu
    fenetre_menu.pack_forget()
    fenetre_robot1.pack(expand=True, fill='both')


def afficher_menu():
    global fenetre_robot1, fenetre_menu
    fenetre_robot1.pack_forget()
    fenetre_menu.pack(expand=True, fill='both')


def clic(canva, bouton):
    """
    revoir nom fonction
    creation de la porte dans le canva apres avoir clique sur le bouton de la
    porte voulue
    UNDO : faire par rapport aux derniers boutons appuyé (lastbutton)
    """
    global i
    canva.unbind("<Button-1>")
    if (bouton == 'and'):
        canva.bind("<Button-1>", lambda event, canva=canva:
                   create_and(event, canva))
    elif (bouton == 'or'):
        canva.bind("<Button-1>", lambda event, canva=canva:
                   create_or(event, canva))
    elif (bouton == 'invert'):
        canva.bind("<Button-1>", lambda event, canva=canva:
                   create_invert(event, canva))
    elif (bouton == 'xor'):
        canva.bind("<Button-1>", lambda event, canva=canva:
                   create_xor(event, canva))
    elif(bouton == 'supp'):
        canva.bind("<Button-1>", lambda event, canva=canva:
                   supprimer(event, canva))
    elif(bouton == 'undo'):
        canva.delete('porte'+str(i-1))
    elif(bouton == 'lien'):
        canva.bind("<Button-1>", lambda event, canva=canva:
                   create_lien1(event, canva))
    print(coordonne)
    lastbutton = bouton


"""
creation des portes et stockage des coordonnees de chaque porte dans une liste
à l'indice i.
"""


def create_and(event, canva):
    """
    creee une porte and aux coordonnees cliquees
    """
    global i, coordonne
    r.porte_andE(event.x, event.y, canva, i)
    coordonne += [[event.x, event.y, "on"]]
    i += 1


def create_or(event, canva):
    """
    creee une porte or aux coordonnees cliquees
    """
    global i, coordonne
    r.porte_orE(event.x, event.y, canva, i)
    coordonne += [[event.x, event.y, "on"]]
    i += 1


def create_invert(event, canva):
    """
    creee une porte invert aux coordonnees cliquees
    """
    global i, coordonne
    r.porte_invertE(event.x, event.y, canva, i)
    coordonne += [[event.x, event.y, "on"]]
    i += 1


def create_xor(event, canva):
    """
    creee une porte xor aux coordonnees cliquees
    """
    global i, coordonne
    r.porte_xorE(event.x, event.y, canva, i)
    coordonne += [[event.x, event.y, "on"]]
    i += 1


def tourner_gauche(event, canva):
    """
    recupere l'identificateur i et les coordonnees de la porte sur lequel il a
    clique puis la supprime et en creer une autre dans le sens suivant avec le
    meme identificateur et aux memes coordonnees
    E : est
    O : ouest
    N : nord
    S : sud
    tag sous la forme : tags=("porte"+str(i), "porte",  sens, nom ...)
    avec sens in (E, O, N, S) et nom in (and, or, invert, xor)
    """
    global i, coordonne
    nom = canva.gettags("current")
    j = nom[0][-1]
    print ("nom : ", nom)
    # prend la liste des objets de la porte concernee
    liste = canva.find_withtag("porte"+str(j))
    # recupere mes coordonnees de la porte
    x = coordonne[int(j)][0]
    y = coordonne[int(j)][1]
    print("liste ", liste)
    """
    j'ai pris liste[0] mais n'importe quel index aurait pu marché tant qu'on
    ne depasse pas la taille de la liste, car toutes les formes de la porte
    contiennent le sens et le nom
    """
    if "E" in canva.gettags(liste[0]):
        if "and" in canva.gettags(liste[0]):
            canva.delete(nom[0])
            r.porte_andN(x, y, canva, int(j))
        elif "or" in canva.gettags(liste[0]):
            canva.delete(nom[0])
            r.porte_orN(x, y, canva, int(j))
        elif "invert" in canva.gettags(liste[0]):
            canva.delete(nom[0])
            r.porte_invertN(x, y, canva, int(j))
        elif "xor" in canva.gettags(liste[0]):
            canva.delete(nom[0])
            r.porte_xorN(x, y, canva, int(j))

    elif "N" in canva.gettags(liste[0]):
        if "and" in canva.gettags(liste[0]):
            canva.delete(nom[0])
            r.porte_andO(x, y, canva, int(j))
        elif "or" in canva.gettags(liste[0]):
            canva.delete(nom[0])
            r.porte_orO(x, y, canva, int(j))
        elif "invert" in canva.gettags(liste[0]):
            canva.delete(nom[0])
            r.porte_invertO(x, y, canva, int(j))
        elif "xor" in canva.gettags(liste[0]):
            canva.delete(nom[0])
            r.porte_xorO(x, y, canva, int(j))

    elif "O" in canva.gettags(liste[0]):
        if "and" in canva.gettags(liste[0]):
            canva.delete(nom[0])
            r.porte_andS(x, y, canva, int(j))
        elif "or" in canva.gettags(liste[0]):
            canva.delete(nom[0])
            r.porte_orS(x, y, canva, int(j))
        elif "invert" in canva.gettags(liste[0]):
            canva.delete(nom[0])
            r.porte_invertS(x, y, canva, int(j))
        elif "xor" in canva.gettags(liste[0]):
            canva.delete(nom[0])
            r.porte_xorS(x, y, canva, int(j))

    elif "S" in canva.gettags(liste[0]):
        if "and" in canva.gettags(liste[0]):
            canva.delete(nom[0])
            r.porte_andE(x, y, canva, int(j))
        elif "or" in canva.gettags(liste[0]):
            canva.delete(nom[0])
            r.porte_orE(x, y, canva, int(j))
        elif "invert" in canva.gettags(liste[0]):
            canva.delete(nom[0])
            r.porte_invertE(x, y, canva, int(j))
        elif "xor" in canva.gettags(liste[0]):
            canva.delete(nom[0])
            r.porte_xorE(x, y, canva, int(j))


def supprimer(event, canva):
    """
    supprime l'image de la porte mais ses coordonnees restent dans la variable
    coordonne
    """
    global i, coordonne
    nom = canva.gettags("current")
    j = nom[0][-1]
    canva.tag_unbind("porte"+j, "<Button-1>")
    # supprime l'image de la porte et on met son etat a off dans coordonne
    j = nom[0][-1]
    print("j = ", j)
    coordonne[int(j)][2] = "off"
    canva.delete(nom[0])


def create_lien1(event, canva):
    """
    recupere le premier clic sur une jointure (cercle) d'une porte
    test si le cercle est deja lie, s'il est deja lie, reinitialise la creation
    du lien
    exemple de tag:
    tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom, "avant"))
    """
    widget1 = canva.find_withtag("current")
    l_tag1 = (canva.gettags(widget1))
    j = l_tag1[0][-1]
    pos1 = l_tag1[-2]  # tag arriere1 ou arriere2 ou avant
    # recherche de la position l'element cliqué
    objet1 = canva.find_withtag("joint"+str(j))
    objet2 = canva.find_withtag(pos1)
    objet3 = intersection(objet1, objet2)
    if ((("joint"+str(j)) in l_tag1) and not (testlier(canva, j, pos1))):
        canva.itemconfig(widget1, fill='white')
        x1 = event.x
        y1 = event.y
        canva.unbind("<Button-1>")
        canva.bind("<Button-1>", lambda event, canva=canva:
                   create_lien2(event, x1, y1, widget1, canva))

    elif testlier(canva, j, pos1):
        canva.unbind("<Button-1>")
        canva.bind("<Button-1>", lambda event, canva=canva:
                   create_lien1(event, canva))

    else:
        canva.unbind("<Button-1>")
        canva.bind("<Button-1>", lambda event, canva=canva:
                   create_lien1(event, canva))


def create_lien2(event, x, y, widget1, canva):
    """
    recoit les coordonne du cercle precedent et recupere le deuxieme clic pour
    creer donc le lien entre les deux cercles. test si les deux cercles font
    partie d'une meme porte.
    test si le cercle est deja lie
    a faire: reconnaissance de l'entree ou de la sortie
    """
    l_tag1 = (canva.gettags(widget1))
    k = l_tag1[0][-1]  # identificateur premier point
    pos1 = l_tag1[-2]  # position premier point

    widget2 = canva.find_withtag("current")  # objet cliqué
    l_tag2 = (canva.gettags(widget2))  # tags de l'objet cliqué
    j = l_tag2[0][-1]  # identificateur deuxieme point
    pos2 = l_tag2[-2]  # position deuxieme point
    # test si l'objet cliqué est un cercle, s'il n'est pas dans la meme porte
    # et s'il n'est pas deja lié
    if ((("joint"+str(j)) in l_tag2) and (j != k) and
       not(testlier(canva, j, pos2))):
        canva.itemconfig(widget2, fill='white')
        ligne = canva.create_line(x, y, event.x, event.y, fill='white',
                                  tags="lien")
        canva.unbind("<Button-1>")

    elif j == k:
        print("tu essayes de lier l'entree et la sortie d'une meme porte")
        canva.itemconfig(widget1, fill=canva.cget('background'))
        canva.unbind("<Button-1>")
        canva.bind("<Button-1>", lambda event, canva=canva:
                   create_lien1(event, canva))

    elif testlier(canva, j, pos2):
        canva.itemconfig(widget1, fill=canva.cget('background'))
        print("ce point est deja lié")
        canva.unbind("<Button-1>")
        canva.bind("<Button-1>", lambda event, canva=canva:
                   create_lien1(event, canva))

    else:
        canva.itemconfig(widget1, fill=canva.cget('background'))
        canva.unbind("<Button-1>")
        canva.bind("<Button-1>", lambda event, canva=canva:
                   create_lien1(event, canva))
        # mettre une fonction pour afficher une bulle d'aide

def create_radar(canva):
    global i
    radar1 = canva.create_rectangle


def fenetre_menu(root):
    """
    creation du menu principal
    """
    # INITIALISATION
    """
    revoir nom variable des canva contenant les elements de la fenetre associee
    """
    fenetre_menu = tk.Canvas(root, width=1280, height=768, bg='black')
    cadremenu = tk.Frame(fenetre_menu, borderwidth=2, relief='solid',
                         bg='black')
    nom = tk.Label(cadremenu, text='MENU')
    bouton_jeu = tk.Button(cadremenu, text='JEU',
                           command=afficher_create_robot)
    bouton_option = tk.Button(cadremenu, text='OPTIONS')
    bouton_aide = tk.Button(cadremenu, text='AIDE')
    bouton_credit = tk.Button(cadremenu, text='CREDIT')
    bouton_quitter = tk.Button(cadremenu, text='QUITTER', command=root.quit)

    # PACKAGE
    fenetre_menu.pack(expand=True, fill='both')
    cadremenu.pack(fill='both', pady=200)
    nom.pack()
    bouton_jeu.pack()
    bouton_option.pack()
    bouton_aide.pack()
    bouton_credit.pack()
    bouton_quitter.pack()

    return (fenetre_menu, cadremenu, nom, bouton_jeu, bouton_option,
            bouton_aide, bouton_credit, bouton_quitter)


def fenetre_robot(root):
    """
    fenetre contenant la creation du robot
    """
    # INITIALISATION
    # fenetre robot contient tous les elements concernant la creation du robot
    """
    revoir nom variable des canva contenant les elements de la fenetre associee
    revoir la taille des boutons pour qu'ils aient tous la meme taille
    """
    fenetre_robot = tk.Canvas(root, width=1280, height=768, bg='grey25')
    canva = tk.Canvas(fenetre_robot, bg='black')
    # cadre contient les boutons associes
    cadre = tk.Frame(fenetre_robot, borderwidth=2, relief='solid', bg='white',
                     width=175)
    # cadre contenant les boutons retour au menu et undo
    cadre2 = tk.Frame(fenetre_robot, relief='solid', bg='white', height=40)
    # bouton robot

    bouton_porte_and = tk.Button(cadre, text='AND', background='black',
                                 foreground='white',
                                 command=lambda canva=canva, bouton='and':
                                 clic(canva, bouton))
    bouton_porte_or = tk.Button(cadre, text='OR', background='black',
                                foreground='white',
                                command=lambda canva=canva, bouton='or':
                                clic(canva, bouton))
    bouton_porte_invert = tk.Button(cadre, text='INVERT', background='black',
                                    foreground='white',
                                    command=lambda canva=canva,
                                    bouton='invert': clic(canva, bouton))
    bouton_porte_xor = tk.Button(cadre, text='XOR', background='black',
                                 foreground='white',
                                 command=lambda canva=canva, bouton='xor':
                                 clic(canva, bouton))
    bouton_lien = tk.Button(cadre, text='Lien', background='black',
                            foreground='white',
                            command=lambda canva=canva, bouton='lien':
                            clic(canva, bouton))
    bouton_supp = tk.Button(cadre, text='Supprimer', background='black',
                            foreground='white', command=lambda canva=canva,
                            bouton='supp': clic(canva, bouton))

    # a placer en haut à gauche
    bouton_sauver = tk.Button(cadre2, text='Sauver', background='black',
                              foreground='white', command=lambda canva=canva,
                              bouton='sauver': clic(canva, bouton))
    bouton_charger = tk.Button(cadre2, text='Charger', background='black',
                               foreground='white', command=lambda canva=canva,
                               bouton='charger': clic(canva, bouton))
    bouton_undo = tk.Button(cadre2, text='undo', background='black',
                            foreground='white', command=lambda canva=canva,
                            bouton='undo': clic(canva, bouton))
    bouton_retourmenu = tk.Button(cadre2, text='Retour', background='black',
                                  foreground="white", padx=20,
                                  command=afficher_menu)

    # PACKAGE
    bouton_retourmenu.pack()
    # fenetre_robot.pack(expand=True, fill='both')
    cadre2.pack(side='top', fill=tk.X)
    cadre.pack(side='right', fill=tk.Y)
    canva.pack(expand=True, fill='both')
    bouton_porte_and.pack()
    bouton_porte_or.pack()
    bouton_porte_invert.pack()
    bouton_porte_xor.pack()
    bouton_lien.pack()
    bouton_supp.pack()

    bouton_sauver.pack(side='left')
    bouton_charger.pack(side='left')
    bouton_undo.pack(side='left')
    bouton_retourmenu.pack(side='left')

    # bindings
    canva.tag_bind("porte", "<Button-3>", lambda event, canva=canva:
                   tourner_gauche(event, canva))
    """
    creation des radars, noir -> éteint, blanc -> allumé

    """

    return fenetre_robot, canva, cadre


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Epic Robot")
    root.geometry("1280x768+1500+20")
    (fenetre_menu, cadremenu, nom, bouton_jeu, bouton_option, bouton_aide,
     bouton_credit, bouton_quitter) = fenetre_menu(root)
    fenetre_robot1, canva, cadre = fenetre_robot(root)
    # canva.bind("<Button-1>", lambda event, canva=canva, porte_xor(canva))

    root.mainloop()
