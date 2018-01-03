#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1.9-zCasino.py: petit jeu de roulette très simplifié
import math
import random

# OpenClassrooms - Apprenez à programmer en Python - TP: tous au ZCasino
# https://openclassrooms.com/courses/apprenez-a-programmer-en-python/tp-tous-au-zcasino

# Le joueur mise sur un numéro compris entre 0 et 49
# En choisissant son numéro, il mise
# Les numéros pairs sont noire, les impairs sont de rouge
# Quand la roulette s'arrête:
# -Si numéro gagnant: gain = 3x la mise
# -Si même couleur: gain = 50% de la mise
# -Sinon la mise est perdue

#########
# TEXTE #
#########
disclamer = "Bienvenu à la roulette, vous avez un crédit de 1000€. \
    Bonne partie. "
err_plage = "Il faut saisir un nombre dans la plage indiquée! "
err_saisie = "Il faut saisir un nombre! "
msg_resultat = "\nLa bille s'arrête sur le nunéro: "
msg_numero = "\nVotre nombre est gagnant! Votre gain: "
msg_couleur = "\nVotre couleur est gagnante! Votre gain: "
msg_perdu = "\nVous perdez votre mise!"
msg_continue = "Pour arrêter la partie, tapez « n »: "
msg_solde = "Votre solde : "
msg_arret = "Vous avez décidé d'arrêter la partie avec un solde de: "
msg_final = "Votre solde à atteind 0€: la partie s'arrête"
curr_symb = "€"

#############
# VARIABLES #
#############
jeu_continu = True
credit = 1000

################
# DÉBUT DU JEU #
################
print(disclamer)

while jeu_continu is True:
    # Saisie & validation du choix
    choix_valeur = 50
    while choix_valeur >= 50 or choix_valeur < 0:
        choix_valeur = input("Quel numéro choisissez vous (0-49)?")
        try:
            choix_valeur = int(choix_valeur)
        except ValueError:
            print(err_saisie)
            choix_valeur = 50
            continue

        if choix_valeur >= 50 or choix_valeur < 0:
            print(err_plage)

    # Saisie & validation de la mise
    mise_check = False
    while mise_check is False:
        try:
            msg_mise = "Quelle est votre mise (1-" + str(credit) + "?)"
            mise = input(msg_mise)
        except SyntaxError:
            print(err_saisie)
        except NameError:
            print(err_saisie)
        else:
            try:
                mise = int(mise)
                assert mise > 0 and mise <= credit
            except ValueError:
                print(err_saisie)
            except AssertionError:
                print(err_saisie)
            else:
                mise_check = True

    # Roulette
    result_valeur = random.randrange(50)

    # Comparaison
    if result_valeur == choix_valeur:
        gain = mise * 3
        msg = msg_resultat + str(result_valeur) + msg_numero + \
            str(gain) + curr_symb
    elif result_valeur % 2 == choix_valeur % 2:
        gain = math.ceil(mise / 2)
        msg = msg_resultat + str(result_valeur) + msg_couleur + \
            str(gain) + curr_symb
    else:
        gain = 0 - mise
        msg = msg_resultat + str(result_valeur) + msg_perdu

    credit = credit + gain

    # Affichage de fin de tour
    print(msg)

    if credit > 0:
        # affiche credit
        print(msg_solde + str(credit))

        # demande de continuer
        ask_check = False
        while ask_check is False:
            try:
                ask_continue = str(input(msg_continue))
            except ValueError:
                print(err_saisie)
            else:
                ask_check = True

            if ask_continue == "n":
                # Arret demandé par le joueur
                jeu_continu = False
                print(msg_arret + str(credit) + curr_symb)

    else:
        jeu_continu = False
        # fin du jeu
        print(msg_final)