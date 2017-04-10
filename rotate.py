import tkinter as tk


def porte_andE(x, y, canva, i):
    """
    idée de mettre des cercles au bout des jointure pour savoir si la porte est
    relié à un autre élément ou pas
    mettre la couleur des ligne dans une variable
    """

    fond = canva.cget('bg')
    taille = 20
    nom = "and"
    sens = "E"
    arc = canva.create_arc(x+taille+5, y+taille, x-taille-5, y-taille,
                           fill=fond,
                           outline="white", tags=("porte"+str(i), "porte",  sens, nom),
                           start=-90,
                           extent=180)
    jointure_avant = canva.create_line(x+taille+5, y, x+taille+15, y,
                                       fill="white",
                                       tags=("porte"+str(i), "porte",  sens, nom))
    jointure_arriere1 = canva.create_line(x, y-13, x-15, y-13, fill="white",
                                          tags=("porte"+str(i), "porte",  sens, nom))
    jointure_arriere2 = canva.create_line(x, y+13, x-15, y+13, fill="white",
                                          tags=("porte"+str(i), "porte",  sens, nom))

    """
    mis a jour
    cca = [x+taille+15+4, y]  # centre cercle avant
    cca1 = [x-15-7, y-13]  # centre cercle arriere 1
    cca2 = [x-15-7, y+13]  # centre cercle arriere 2
    """
    cerle_avant = canva.create_oval(x+taille+15, y+7, x+taille+15+14, y-7,
                                    outline='white', fill=fond,
                                    tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                          "avant"))
    cercle_arriere1 = canva.create_oval(x-15, y-6, x-15-14, y-20,
                                        outline='white', fill=fond,
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere1"))
    cercle_arriere2 = canva.create_oval(x-15, y+6, x-15-14, y+20,
                                        outline='white', fill=fond,
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere2"))

    return 0


def porte_andO(x, y, canva, i):
    """
    porte et direction gauche

    idée de mettre des cercles au bout des jointure pour savoir si la porte est
    relié à un autre élément ou pas
    mettre la couleur des ligne dans une variable
    """

    fond = canva.cget('bg')
    taille = 20
    nom = "and"
    sens = "O"
    arc = canva.create_arc(x-taille-5, y-taille, x+taille+5, y+taille,
                           fill=fond,
                           outline="white", tags=("porte"+str(i), "porte",  sens, nom),
                           start=90,
                           extent=180)
    jointure_avant = canva.create_line(x-taille-5, y, x-taille-20, y,
                                       fill="white",
                                       tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                             "avant"))
    jointure_arriere1 = canva.create_line(x, y-15, x+15, y-15, fill="white",
                                          tags=("porte"+str(i), "porte",  sens, nom))
    jointure_arriere2 = canva.create_line(x, y+15, x+15, y+15, fill="white",
                                          tags=("porte"+str(i), "porte",  sens, nom))

    """
    mis a jour
    cca = [x-taille-27, y]  # centre cercle avant
    cca1 = [x+15+7, y-15]  # centre cercle arriere 1
    cca2 = [x+15+7, y+15]  # centre cercle arriere 2
    """
    cerle_avant = canva.create_oval(x-taille-20, y+7, x-taille-20-14, y-7,
                                    outline='white', fill=fond,
                                    tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                          "avant"))
    cercle_arriere1 = canva.create_oval(x+15, y+15+7, x+15+14, y+15-7,
                                        outline='white', fill=fond,
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere1"))
    cercle_arriere2 = canva.create_oval(x+15, y-15+7, x+15+14, y-15-7,
                                        outline='white', fill=fond,
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere2"))


    return 0


def porte_andN(x, y, canva, i):
    """
    porte et direction nord

    idée de mettre des cercles au bout des jointure pour savoir si la porte est
    relié à un autre élément ou pas
    mettre la couleur des ligne dans une variable
    """

    fond = canva.cget('bg')
    taille = 20
    nom = "and"
    sens = "N"
    arc = canva.create_arc(x-taille, y-taille-5, x+taille, y+taille+5,
                           fill=fond, outline="white",
                           tags=("porte"+str(i), "porte",  sens, nom),
                           start=0, extent=180)
    jointure_avant = canva.create_line(x, y-taille-5, x, y-taille-20,
                                       fill="white",
                                       tags=("porte"+str(i), "porte",  sens, nom))
    jointure_arriere1 = canva.create_line(x-15, y, x-15, y+15, fill="white",
                                          tags=("porte"+str(i), "porte",  sens, nom))
    jointure_arriere2 = canva.create_line(x+15, y, x+15, y+15, fill="white",
                                          tags=("porte"+str(i), "porte",  sens, nom))

    """
    mis à jour
    cca = [x, y-taille-15-7]  # centre cercle avant
    cca1 = [x-15, y+15+7]  # centre cercle arriere 1
    cca2 = [x+15, y+15+7]  # centre cercle arriere 2
    """

    cerle_avant = canva.create_oval(x+7, y-taille-15, x-7, y-taille-15-14,
                                    outline='white', fill=fond,
                                    tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                          "avant"))
    cercle_arriere1 = canva.create_oval(x-15-7, y+15, x-15+7, y+15+14,
                                        outline='white', fill=fond,
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere1"))
    cercle_arriere2 = canva.create_oval(x+15-7, y+15, x+15+7, y+15+14,
                                        outline='white', fill=fond,
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere2"))

    return 0


def porte_andS(x, y, canva, i):
    """
    porte et direction sud

    idée de mettre des cercles au bout des jointure pour savoir si la porte est
    relié à un autre élément ou pas
    mettre la couleur des ligne dans une variable
    """

    fond = canva.cget('bg')
    taille = 20
    nom = "and"
    sens = "S"
    arc = canva.create_arc(x-taille, y-taille-5, x+taille, y+taille+5,
                           fill=fond,
                           outline="white", tags=("porte"+str(i), "porte",  sens, nom),
                           start=180,
                           extent=180)
    jointure_avant = canva.create_line(x, y+taille+5, x, y+taille+20,
                                       fill="white",
                                       tags=("porte"+str(i), "porte",  sens, nom))
    jointure_arriere1 = canva.create_line(x+15, y, x+15, y-15, fill="white",
                                          tags=("porte"+str(i), "porte",  sens, nom))
    jointure_arriere2 = canva.create_line(x-15, y, x-15, y-15, fill="white",
                                          tags=("porte"+str(i), "porte",  sens, nom))

    """
    mis à jour
    cca = [x, y+taille+27]  # centre cercle avant
    cca1 = [x+15, y-15-7]  # centre cercle arriere 1
    cca2 = [x-15, y-15-7]  # centre cercle arriere 2
    """
    cerle_avant = canva.create_oval(x-7, y+taille+20, x+7, y+taille+34,
                                    outline='white',
                                    tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                          "avant"))
    cercle_arriere1 = canva.create_oval(x+8, y-15, x+22, y-15-14,
                                        outline='white',
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere1"))
    cercle_arriere2 = canva.create_oval(x-8, y-15, x-22, y-15-14,
                                        outline='white',
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere2"))

    return 0


def porte_invertE(x, y, canva, i):
    """
    idée de mettre des cercles au bout des jointure  que l'on remplira d'une
    certaine couleur si la porte est relié à un autre élément ou pas
    """

    fond = canva.cget('bg')
    taille = 15
    nom = "invert"
    sens = "E"
    triangle = canva.create_polygon(x-taille, y-taille, x-taille, y+taille,
                                    x+taille, y,
                                    tags=("porte"+str(i), "porte",  sens, nom),
                                    outline="white",
                                    fill=fond)
    # jointure servant d'entrée ou de sortie
    jointure_arriere = canva.create_line(x-taille, y, x-taille-15, y,
                                         fill='white',
                                         tags=("porte"+str(i), "porte",  sens, nom))
    jointure_avant = canva.create_line(x+taille+8, y, x+8+taille+15, y,
                                       fill='white',
                                       tags=("porte"+str(i), "porte",  sens, nom))
    # cercle servant de lien a une entree ou une sortie
    """ modification du tags """

    cercle_porte = canva.create_oval(x+taille, y+4, x+taille+8, y-4,
                                     outline='white', fill=fond,
                                     tags=("porte"+str(i), "porte",  sens, nom))
    cercle_avant = canva.create_oval(x+23+taille, y+7, x+23+taille+14, y-7,
                                     outline='white', fill=fond,
                                     tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                           "avant"))
    cercle_arriere = canva.create_oval(x-taille-15, y-7, x-taille-15-14, y+7,
                                       outline='white', fill=fond,
                                       tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                             "arriere1"))


    return 1


def porte_invertO(x, y, canva, i):
    """
    idée de mettre des cercles au bout des jointure  que l'on remplira d'une
    certaine couleur si la porte est relié à un autre élément ou pas
    """

    fond = canva.cget('bg')
    taille = 15
    nom = "invert"
    sens = "O"
    triangle = canva.create_polygon(x+taille, y+taille, x+taille, y-taille,
                                    x-taille, y,
                                    tags=("porte"+str(i), "porte",  sens, nom),
                                    outline="white",
                                    fill=fond)
    # jointure servant d'entrée ou de sortie
    jointure_arriere = canva.create_line(x+taille, y, x+taille+15, y,
                                         fill='white',
                                         tags=("porte"+str(i), "porte",  sens, nom))
    jointure_avant = canva.create_line(x-taille-8, y, x-8-taille-15, y,
                                       fill='white',
                                       tags=("porte"+str(i), "porte",  sens, nom))
    # cercle servant de lien a une entree ou une sortie
    """ modification du tags """

    cercle_porte = canva.create_oval(x-taille, y-4, x-taille-8, y+4,
                                     outline='white', fill=fond,
                                     tags=("porte"+str(i), "porte",  sens, nom))
    cercle_avant = canva.create_oval(x-23-taille, y-7, x-23-taille-14, y+7,
                                     outline='white', fill=fond,
                                     tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                           "avant"))
    cercle_arriere = canva.create_oval(x+taille+15, y+7, x+taille+15+14, y-7,
                                       outline='white', fill=fond,
                                       tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                             "arriere1"))


    return 1


def porte_invertN(x, y, canva, i):
    """
    idée de mettre des cercles au bout des jointure  que l'on remplira d'une
    certaine couleur si la porte est relié à un autre élément ou pas
    """

    fond = canva.cget('bg')
    taille = 15
    nom = "invert"
    sens = "N"
    triangle = canva.create_polygon(x+taille, y+taille, x-taille, y+taille,
                                    x, y-taille,
                                    tags=("porte"+str(i), "porte",  sens, nom),
                                    outline="white",
                                    fill=fond)
    # jointure servant d'entrée ou de sortie
    jointure_arriere = canva.create_line(x, y+taille, x, y+taille+15,
                                         fill='white',
                                         tags=("porte"+str(i), "porte",  sens, nom))
    jointure_avant = canva.create_line(x, y-taille-8, x, y-taille-8-15,
                                       fill='white',
                                       tags=("porte"+str(i), "porte",  sens, nom))
    # cercle servant de lien a une entree ou une sortie
    """ modification du tags """

    cercle_porte = canva.create_oval(x-4, y-taille, x+4, y-taille-8,
                                     outline='white', fill=fond,
                                     tags=("porte"+str(i), "porte",  sens, nom))
    cercle_avant = canva.create_oval(x-7, y-taille-23, x+7, y-taille-23-14,
                                     outline='white', fill=fond,
                                     tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                           "avant"))
    cercle_arriere = canva.create_oval(x-7, y+taille+15, x+7, y+taille+15+15,
                                       outline='white', fill=fond,
                                       tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                             "arriere1"))


    return 1


def porte_invertS(x, y, canva, i):
    """
    idée de mettre des cercles au bout des jointure  que l'on remplira d'une
    certaine couleur si la porte est relié à un autre élément ou pas
    """

    fond = canva.cget('bg')
    taille = 15
    nom = "invert"
    sens = "S"
    triangle = canva.create_polygon(x-taille, y-taille, x+taille, y-taille,
                                    x, y+taille,
                                    tags=("porte"+str(i), "porte",  sens, nom),
                                    outline="white", fill=fond)
    # jointure servant d'entrée ou de sortie
    jointure_arriere = canva.create_line(x, y-taille, x, y-taille-15,
                                         fill='white',
                                         tags=("porte"+str(i), "porte",  sens, nom))
    jointure_avant = canva.create_line(x, y+taille+8, x, y+taille+8+15,
                                       fill='white',
                                       tags=("porte"+str(i), "porte",  sens, nom))
    # cercle servant de lien a une entree ou une sortie
    """ modification du tags """

    cercle_porte = canva.create_oval(x+4, y+taille, x-4, y+taille+8,
                                     outline='white', fill=fond,
                                     tags=("porte"+str(i), "porte",  sens, nom))
    cercle_avant = canva.create_oval(x-7, y+taille+23, x+7, y+taille+23+14,
                                     outline='white', fill=fond,
                                     tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                           "avant"))
    cercle_arriere = canva.create_oval(x-7, y-taille-15, x+7, y-taille-15-15,
                                       outline='white', fill=fond,
                                       tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                             "arriere1"))


    return 1


def porte_orE(x, y, canva, i):
    """
    creation de la porte ou
    """

    fond = canva.cget('bg')
    couleur = 'white'
    t = 20
    nom = "or"
    sens = "E"
    points = [x-t, y-t, x-t, y-t, x-t, y+t, x-t, y+t, x+t, y]
    forme = canva.create_polygon(points, smooth=True, splinesteps=100,
                                 outline=couleur, fill=fond,
                                 tags=("porte"+str(i), "porte",  sens, nom))
    forme_cache = canva.create_arc(x-t-10, y-t, x-t+10, y+t,
                                   tags=("porte"+str(i), "porte",  sens, nom),
                                   fill=canva.cget('bg'), start=-90,
                                   extent=180, outline=couleur)
    ligne_cache = canva.create_line(x-t, y-t, x-t, y+t,
                                    fill=canva.cget('bg'),
                                    tags=("porte"+str(i), "porte",  sens, nom))
    # jointure servant d'entrée ou de sortie
    jointure_arriere1 = canva.create_line(x-t+9, y-10, x-t-6, y-10,
                                          fill="white",
                                          tags=("porte"+str(i), "porte",  sens, nom))
    jointure_arriere2 = canva.create_line(x-t+9, y+10, x-t-6, y+10,
                                          fill="white",
                                          tags=("porte"+str(i), "porte",  sens, nom))
    jointure_avant = canva.create_line(x+t-t/2, y, x+t-t/2+10, y, fill="white",
                                       tags=("porte"+str(i), "porte",  sens, nom))

    """
    mis à jour
    cca = [x+t-t/2+10+7, y]  # centre cercle avant
    cca1 = [x-t-6-7, y-10]  # centre cercle arriere 1
    cca2 = [x-t-6-7, y+10]  # centre cercle arriere 2
    """

    # cercle servant de lien a une entree ou une sortie
    cercle_avant = canva.create_oval(x+t-t/2+10, y-7, x+t-t/2+10+14, y+7,
                                     outline='white', fill=fond,
                                     tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                           "avant"))
    cercle_arriere1 = canva.create_oval(x-t-6, y-10-7, x-t-6-14, y-10+7,
                                        outline='white', fill=fond,
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere1"))
    cercle_arriere2 = canva.create_oval(x-t-6, y+10-7, x-t-6-14, y+10+7,
                                        outline='white', fill=fond,
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere2"))


def porte_orO(x, y, canva, i):
    """
    creation de la porte ou
    """

    fond = canva.cget('bg')
    couleur = 'white'
    t = 20
    nom = "or"
    sens = "O"
    points = [x+t, y+t, x+t, y+t, x+t, y-t, x+t, y-t, x-t, y]
    forme = canva.create_polygon(points, smooth=True, splinesteps=100,
                                 outline=couleur, fill=fond,
                                 tags=("porte"+str(i), "porte",  sens, nom))
    forme_cache = canva.create_arc(x+t+10, y+t, x+t-10, y-t,
                                   tags=("porte"+str(i), "porte",  sens, nom),
                                   fill=canva.cget('bg'), start=90,
                                   extent=180, outline=couleur)
    ligne_cache = canva.create_line(x+t, y+t, x+t, y-t,
                                    fill=canva.cget('bg'),
                                    tags=("porte"+str(i), "porte",  sens, nom))
    # jointure servant d'entrée ou de sortie
    jointure_arriere1 = canva.create_line(x+t-9, y+10, x+t+6, y+10,
                                          fill="white",
                                          tags=("porte"+str(i), "porte",  sens, nom))
    jointure_arriere2 = canva.create_line(x+t-9, y-10, x+t+6, y-10,
                                          fill="white",
                                          tags=("porte"+str(i), "porte",  sens, nom))
    jointure_avant = canva.create_line(x-t+t/2, y, x-t+t/2-10, y, fill="white",
                                       tags=("porte"+str(i), "porte",  sens, nom))

    """
    mis à jour
    cca = [x-t+t/2-10-7, y]  # centre cercle avant
    cca1 = [x+t+6+7, y-10]  # centre cercle arriere 1
    cca2 = [x+t+6+7, y+10]  # centre cercle arriere 2
    """

    # cercle servant de lien a une entree ou une sortie
    cercle_avant = canva.create_oval(x-t+t/2-10, y-7, x-t+t/2-10-14, y+7,
                                     outline='white', fill=fond,
                                     tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                           "avant"))
    cercle_arriere1 = canva.create_oval(x+t+6, y+10+7, x+t+6+14, y+10-7,
                                        outline='white', fill=fond,
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere1"))
    cercle_arriere2 = canva.create_oval(x+t+6, y-10+7, x+t+6+14, y-10-7,
                                        outline='white', fill=fond,
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere2"))




def porte_orN(x, y, canva, i):
    """
    creation de la porte ou
    """

    fond = canva.cget('bg')
    couleur = 'white'
    t = 20
    nom = "or"
    sens = "N"
    points = [x+t, y+t, x+t, y+t, x-t, y+t, x-t, y+t, x, y-t]
    forme = canva.create_polygon(points, smooth=True, splinesteps=100,
                                 outline=couleur, fill=fond,
                                 tags=("porte"+str(i), "porte",  sens, nom))
    forme_cache = canva.create_arc(x-t, y+t+10, x+t, y+t-10,
                                   tags=("porte"+str(i), "porte",  sens, nom),
                                   fill=canva.cget('bg'), start=0,
                                   extent=180, outline=couleur)
    ligne_cache = canva.create_line(x+t, y+t, x-t, y+t,
                                    fill=canva.cget('bg'),
                                    tags=("porte"+str(i), "porte",  sens, nom))
    # jointure servant d'entrée ou de sortie
    jointure_arriere1 = canva.create_line(x+10, y+t-9, x+10, y+t+6,
                                          fill="white",
                                          tags=("porte"+str(i), "porte",  sens, nom))
    jointure_arriere2 = canva.create_line(x-10, y+t-9, x-10, y+t+6,
                                          fill="white",
                                          tags=("porte"+str(i), "porte",  sens, nom))
    jointure_avant = canva.create_line(x, y-t+t/2, x, y-t+t/2-10, fill="white",
                                       tags=("porte"+str(i), "porte",  sens, nom))

    """
    mis à jour
    cca = [x, y-t+t/2-10-7]  # centre cercle avant
    cca1 = [x-10, y+t+6+7]  # centre cercle arriere 1
    cca2 = [x+10, y+t+6+7]  # centre cercle arriere 2
    """

    # cercle servant de lien a une entree ou une sortie
    cercle_avant = canva.create_oval(x-7, y-t+t/2-10, x+7, y-t+t/2-10-14,
                                     outline='white', fill=fond,
                                     tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                           "avant"))
    cercle_arriere1 = canva.create_oval(x+10+7, y+t+6, x+10-7, y+t+6+14,
                                        outline='white', fill=fond,
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere1"))
    cercle_arriere2 = canva.create_oval(x-10+7, y+t+6, x-10-7, y+t+6+14,
                                        outline='white', fill=fond,
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere2"))




def porte_orS(x, y, canva, i):
    """
    creation de la porte ou
    """

    fond = canva.cget('bg')
    couleur = 'white'
    t = 20
    nom = "or"
    sens = "S"
    points = [x-t, y-t, x-t, y-t, x+t, y-t, x+t, y-t, x, y+t]
    forme = canva.create_polygon(points, smooth=True, splinesteps=100,
                                 outline=couleur, fill=fond,
                                 tags=("porte"+str(i), "porte",  sens, nom))
    forme_cache = canva.create_arc(x+t, y-t-10, x-t, y-t+10,
                                   tags=("porte"+str(i), "porte",  sens, nom),
                                   fill=canva.cget('bg'), start=180,
                                   extent=180, outline=couleur)
    ligne_cache = canva.create_line(x-t, y-t, x+t, y-t,
                                    fill=canva.cget('bg'),
                                    tags=("porte"+str(i), "porte",  sens, nom))
    # jointure servant d'entrée ou de sortie
    jointure_arriere1 = canva.create_line(x-10, y-t+9, x-10, y-t-6,
                                          fill="white",
                                          tags=("porte"+str(i), "porte",  sens, nom))
    jointure_arriere2 = canva.create_line(x+10, y-t+9, x+10, y-t-6,
                                          fill="white",
                                          tags=("porte"+str(i), "porte",  sens, nom))
    jointure_avant = canva.create_line(x, y+t-t/2, x, y+t-t/2+10, fill="white",
                                       tags=("porte"+str(i), "porte",  sens, nom))

    """
    mis à jour
    cca = [x, y+t-t/2+10+7]  # centre cercle avant
    cca1 = [x+10, y-t-6-7]  # centre cercle arriere 1
    cca2 = [x-10, y-t-6-7]  # centre cercle arriere 2
    """

    # cercle servant de lien a une entree ou une sortie
    cercle_avant = canva.create_oval(x+7, y+t-t/2+10, x-7, y+t-t/2+10+14,
                                     outline='white', fill=fond,
                                     tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                           "avant"))
    cercle_arriere1 = canva.create_oval(x-10-7, y-t-6, x-10+7, y-t-6-14,
                                        outline='white', fill=fond,
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere1"))
    cercle_arriere2 = canva.create_oval(x+10-7, y-t-6, x+10+7, y-t-6-14,
                                        outline='white', fill=fond,
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere2"))




def porte_xorE(x, y, canva, i):

    fond = canva.cget('bg')
    couleur = 'white'
    t = 20
    nom = "xor"
    sens = "E"
    points = [x-t, y-t, x-t, y-t, x-t, y+t, x-t, y+t, x+t, y]
    forme = canva.create_polygon(points, smooth=True, splinesteps=100,
                                 outline=couleur, fill=fond,
                                 tags=("porte"+str(i), "porte",  sens, nom))
    forme_cache = canva.create_arc(x-t-10, y-t, x-t+10, y+t, fill=fond,
                                   tags=("porte"+str(i), "porte",  sens, nom), start=-90,
                                   extent=180,
                                   outline=couleur)
    ligne_cache = canva.create_line(x-t, y-t, x-t, y+t, fill=fond,
                                    tags=("porte"+str(i), "porte",  sens, nom))

    ligne_arriere = canva.create_arc(x-t-20, y-t, x-t, y+t, style="arc",
                                     start=-90, extent=180, outline=couleur,
                                     tags=("porte"+str(i), "porte",  sens, nom))
    # jointure servant d'entrée ou de sortie
    jointure_arriere1 = canva.create_line(x-t-1, y-10, x-t-16, y-10,
                                          fill=couleur, tags=("porte"+str(i), "porte",  sens,
                                                              nom))
    jointure_arriere2 = canva.create_line(x-t-1, y+10, x-t-16, y+10,
                                          fill=couleur, tags=("porte"+str(i), "porte",  sens,
                                                              nom))
    jointure_avant = canva.create_line(x+t-t/2, y, x+t-t/2+10, y, fill=couleur,
                                       tags=("porte"+str(i), "porte",  sens, nom))
    """
    mis à jour
    cca = [x+t-t/2+10+7, y]  # centre cercle avant
    cca1 = [x-t-16-7, y-10]  # centre cercle arriere 1
    cca2 = [x-t-16-7, y+10]  # centre cercle arriere 2
    """

    # cercle servant de lien a une entree ou une sortie
    cercle_avant = canva.create_oval(x+t-t/2+10, y-7, x+t-t/2+10+14, y+7,
                                     outline='white', fill=fond,
                                     tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                           "avant"))
    cercle_arriere1 = canva.create_oval(x-t-16, y-10-7, x-t-16-14, y-10+7,
                                        outline='white', fill=fond,
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere1"))
    cercle_arriere2 = canva.create_oval(x-t-16, y+10-7, x-t-16-14, y+10+7,
                                        outline='white', fill=fond,
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere2"))




def porte_xorO(x, y, canva, i):

    fond = canva.cget('bg')
    couleur = 'white'
    t = 20
    nom = "xor"
    sens = "O"
    points = [x+t, y+t, x+t, y+t, x+t, y-t, x+t, y-t, x-t, y]
    forme = canva.create_polygon(points, smooth=True, splinesteps=100,
                                 outline=couleur, fill=fond,
                                 tags=("porte"+str(i), "porte",  sens, nom))
    forme_cache = canva.create_arc(x+t+10, y+t, x+t-10, y-t, fill=fond,
                                   tags=("porte"+str(i), "porte",  sens, nom), start=90,
                                   extent=180,
                                   outline=couleur)
    ligne_cache = canva.create_line(x+t, y+t, x+t, y-t, fill=fond,
                                    tags=("porte"+str(i), "porte",  sens, nom))

    ligne_arriere = canva.create_arc(x+t+20, y+t, x+t, y-t, style="arc",
                                     start=90, extent=180, outline=couleur,
                                     tags=("porte"+str(i), "porte",  sens, nom))
    # jointure servant d'entrée ou de sortie
    jointure_arriere1 = canva.create_line(x+t+1, y+10, x+t+16, y+10,
                                          fill=couleur,
                                          tags=("porte"+str(i), "porte",  sens, nom))
    jointure_arriere2 = canva.create_line(x+t+1, y-10, x+t+16, y-10,
                                          fill=couleur,
                                          tags=("porte"+str(i), "porte",  sens, nom))
    jointure_avant = canva.create_line(x-t+t/2, y, x-t+t/2-10, y, fill=couleur,
                                       tags=("porte"+str(i), "porte",  sens, nom))
    """
    mis à jour
    cca = [x+t-t/2+10+7, y]  # centre cercle avant
    cca1 = [x-t-16-7, y-10]  # centre cercle arriere 1
    cca2 = [x-t-16-7, y+10]  # centre cercle arriere 2
    """

    # cercle servant de lien a une entree ou une sortie
    cercle_avant = canva.create_oval(x-t+t/2-10, y+7, x-t+t/2-10-14, y-7,
                                     outline='white', fill=fond,
                                     tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                           "avant"))
    cercle_arriere1 = canva.create_oval(x+t+16, y+10+7, x+t+16+14, y+10-7,
                                        outline='white', fill=fond,
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere1"))
    cercle_arriere2 = canva.create_oval(x+t+16, y-10+7, x+t+16+14, y-10-7,
                                        outline='white', fill=fond,
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere2"))




def porte_xorS(x, y, canva, i):

    fond = canva.cget('bg')
    couleur = 'white'
    t = 20
    nom = "xor"
    sens = "S"
    points = [x-t, y-t, x-t, y-t, x+t, y-t, x+t, y-t, x, y+t]
    forme = canva.create_polygon(points, smooth=True, splinesteps=100,
                                 outline=couleur, fill=fond,
                                 tags=("porte"+str(i), "porte",  sens, nom))
    forme_cache = canva.create_arc(x-t, y-t-10, x+t, y-t+10, fill=fond,
                                   tags=("porte"+str(i), "porte",  sens, nom), start=180,
                                   extent=180,
                                   outline=couleur)
    ligne_cache = canva.create_line(x-t, y-t, x+t, y-t, fill=fond,
                                    tags=("porte"+str(i), "porte",  sens, nom))

    ligne_arriere = canva.create_arc(x-t, y-t-20, x+t, y-t, style="arc",
                                     start=180, extent=180, outline=couleur,
                                     tags=("porte"+str(i), "porte",  sens, nom))
    # jointure servant d'entrée ou de sortie
    jointure_arriere1 = canva.create_line(x-10, y-t-1, x-10, y-t-16,
                                          fill=couleur,
                                          tags=("porte"+str(i), "porte",  sens, nom))
    jointure_arriere2 = canva.create_line(x+10, y-t-1, x+10, y-t-16,
                                          fill=couleur,
                                          tags=("porte"+str(i), "porte",  sens, nom))
    jointure_avant = canva.create_line(x, y+t-t/2, x, y+t-t/2+10, fill=couleur,
                                       tags=("porte"+str(i), "porte",  sens, nom))
    """
    mis à jour
    cca = [x, y+t-t/2+10+7]  # centre cercle avant
    cca1 = [x-10, y-t-16-7]  # centre cercle arriere 1
    cca2 = [x+10, y-t-16-7]  # centre cercle arriere 2
    """
    # cercle servant de lien a une entree ou une sortie
    cercle_avant = canva.create_oval(x-7, y+t-t/2+10, x+7, y+t-t/2+10+14,
                                     outline='white', fill=fond,
                                     tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                           "avant"))
    cercle_arriere1 = canva.create_oval(x-10-7, y-t-16, x-10+7, y-t-16-14,
                                        outline='white', fill=fond,
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere1"))
    cercle_arriere2 = canva.create_oval(x+10-7, y-t-16, x+10+7, y-t-16-14,
                                        outline='white', fill=fond,
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere2"))


def porte_xorN(x, y, canva, i):

    fond = canva.cget('bg')
    couleur = 'white'
    t = 20
    nom = "xor"
    sens = "N"
    points = [x+t, y+t, x+t, y+t, x-t, y+t, x-t, y+t, x, y-t]
    forme = canva.create_polygon(points, smooth=True, splinesteps=100,
                                 outline=couleur, fill=fond,
                                 tags=("porte"+str(i), "porte",  sens, nom))
    forme_cache = canva.create_arc(x+t, y+t+10, x-t, y+t-10, fill=fond,
                                   tags=("porte"+str(i), "porte",  sens, nom), start=0,
                                   extent=180,
                                   outline=couleur)
    ligne_cache = canva.create_line(x+t, y+t, x-t, y+t, fill=fond,
                                    tags=("porte"+str(i), "porte",  sens, nom))

    ligne_arriere = canva.create_arc(x+t, y+t+20, x-t, y+t, style="arc",
                                     start=0, extent=180, outline=couleur,
                                     tags=("porte"+str(i), "porte",  sens, nom))
    # jointure servant d'entrée ou de sortie
    jointure_arriere1 = canva.create_line(x+10, y+t+1, x+10, y+t+16,
                                          fill=couleur,
                                          tags=("porte"+str(i), "porte",  sens, nom))
    jointure_arriere2 = canva.create_line(x-10, y+t+1, x-10, y+t+16,
                                          fill=couleur,
                                          tags=("porte"+str(i), "porte",  sens, nom))
    jointure_avant = canva.create_line(x, y-t+t/2, x, y-t+t/2-10, fill=couleur,
                                       tags=("porte"+str(i), "porte",  sens, nom))
    """
    mis à jour
    cca = [x, y-t+t/2-10-7]  # centre cercle avant
    cca1 = [x+10, y+t+16+7]  # centre cercle arriere 1
    cca2 = [x-10, y+t+16+7]  # centre cercle arriere 2
    """
    # cercle servant de lien a une entree ou une sortie
    cercle_avant = canva.create_oval(x+7, y-t+t/2-10, x-7, y-t+t/2-10-14,
                                     outline='white', fill=fond,
                                     tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                           "avant"))
    cercle_arriere1 = canva.create_oval(x+10+7, y+t+16, x+10-7, y+t+16+14,
                                        outline='white', fill=fond,
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i),
                                              nom, "arriere1"))
    cercle_arriere2 = canva.create_oval(x-10+7, y+t+16, x-10-7, y+t+16+14,
                                        outline='white', fill=fond,
                                        tags=("porte"+str(i), "porte",  sens, "joint"+str(i), nom,
                                              "arriere2"))




if __name__ == "__main__":
    root = tk.Tk()
    root.title("Epic Robot")
    root.geometry("1000x700+1500+20")
    canva = tk.Canvas(root, bg='black')
    canva.pack(expand=True, fill='both')
    porte_andN(200, 100, canva, 1)
    # canva.bind("<Button-1>", lambda event, canva=canva, porte_xor(canva))

    root.mainloop()
