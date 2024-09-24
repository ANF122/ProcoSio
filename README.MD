## CPU Simulator
Ce simulateur de CPU est un outil éducatif conçu pour aider à comprendre le fonctionnement de base d'un processeur. Il simule un CPU simple avec des registres, de la mémoire, et un ensemble d'instructions de base.
Table des matières

## Introduction
Installation
Exécution du simulateur
Utilisation de l'interface
Commandes disponibles
Exemples d'utilisation
Dépannage

## Prérequis

Python 3.6 ou supérieur
Tkinter (généralement inclus avec Python)

## Installation

Assurez-vous que Python est installé sur votre système. Vous pouvez vérifier en exécutant :
Copypython --version

Vérifiez que Tkinter est installé en exécutant :
Copypython -m tkinter
Si une fenêtre s'ouvre, Tkinter est correctement installé.
Téléchargez le fichier cpu_simulator.py dans votre répertoire de travail.

## Exécution du simulateur

Ouvrez un terminal ou une invite de commande.
Naviguez jusqu'au répertoire contenant cpu_simulator.py.
Exécutez la commande :
Copypython cpu_simulator.py


## Utilisation de l'interface
L'interface du simulateur se compose de plusieurs sections :

Registres : Affiche l'état actuel des registres (A, B, C, D).
Mémoire : Montre les 16 premiers octets de la mémoire.
Journal de sortie : Affiche les messages du système et les résultats des opérations.
Entrée de commande : Permet d'entrer des commandes pour interagir avec le simulateur.

## Commandes disponibles

load [instructions] : Charge un programme dans la mémoire.
Exemple : load 1 0 1 2 0 1 8
exec : Exécute le programme chargé en mémoire.
status : Affiche l'état actuel des registres et de la mémoire.
setreg [register] [value] : Définit la valeur d'un registre.
Exemple : setreg A 42
setmem [address] [value] : Définit la valeur d'une adresse mémoire.
Exemple : setmem 0 15

## Exemples d'utilisation

Charger et exécuter un programme simple :
Copyload 1 0 1 2 0 1 8
exec
Cela charge un programme qui déplace une valeur du registre A vers B, puis s'arrête.
Définir une valeur dans un registre :
Copysetreg A 5
status

Modifier une valeur en mémoire :
Copysetmem 0 10
status


## Dépannage
Si vous rencontrez des problèmes :

Assurez-vous que Python et Tkinter sont correctement installés.
Vérifiez que vous exécutez le script depuis le bon répertoire.
Si l'interface ne s'ouvre pas, exécutez le script depuis un terminal pour voir les messages d'erreur.

Pour toute assistance supplémentaire, veuillez ouvrir une issue dans le dépôt du projet ou contacter le support.

Nous espérons que ce simulateur de CPU vous aidera à mieux comprendre les concepts de base du fonctionnement d'un processeur. Bonne exploration !
