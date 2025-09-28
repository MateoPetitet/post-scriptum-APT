# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 19:41:27 2025

@author: Mateo
"""
def ajout_ps():
    #entrée chemin du fichier
    fichier_entree = input("Le chemin du fichier txt stp : ")

    try:
        with open(fichier_entree, 'r', encoding='utf-8') as f:
            pass
    except FileNotFoundError:
        print(f"Tu t'es planté, '{fichier_entree}' n'existe pas.")
        return
    except Exception as e:
        print(f"Mea culpa : {e}")
        return
    
    #nom du fichier de sortie
    if fichier_entree.endswith('.txt'):
        fichier_sortie = fichier_entree.replace('.txt', '_ps.txt')
    else:
        fichier_sortie = fichier_entree + '_ps.txt'
    
    #traitement
    try:
        with open(fichier_entree, 'r', encoding='utf-8') as entree, \
             open(fichier_sortie, 'w', encoding='utf-8') as sortie:
            
            for numero_ligne, ligne in enumerate(entree):
                nb_p = numero_ligne + 1
                prefixe = "P" * nb_p + "S :"
                sortie.write(f"{prefixe} {ligne}")
        
        print(f"Prêt à spammer un max : {fichier_sortie}")
        
    except Exception as e:
        print(f"Mea culpa : {e}")

if __name__ == "__main__":
    ajout_ps()