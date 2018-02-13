"""
Author: freezed <freezed@users.noreply.github.com> 2018-02-11
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

Ce fichier fait partie du projet `roboc`

"""


# CONFIGURATION

MAP_DIRECTORY = 'cartes/'           # repertoire des fichiers carte
MAP_EXTENTION = '.txt'              # extention des fichiers carte
SAVED_GAME_FILENAME = '.backup'     # fichier de sauvegarde
DIRECTIONS = ['n', 's', 'e', 'o']   # commandes de deplacement
MAZE_ELEMENTS = {'wall': 'O',       # elements dispo dans le labyrinthe
                 'door': '.',
                 'exit': 'U',
                 'robo': 'X',
                 'trace': ' '}
MOVE_STATUS = ['bad', 'wall', 'exit', 'door', 'ok']

ERR_ = "#!@?# Oups… "
ERR_MAP_FILE = ERR_ + "carte «{}» inaccessible!"
ERR_MAP_SIZE = ERR_ + "carte «{}», dimensions incorrecte: «{} x {}»"
ERR_MAP_ROBO = ERR_ + "robo est introuvable sur la carte «{}»!"
ERR_PLAGE = ERR_ + "saisir un nombre dans la plage indiquée! "
ERR_SAISIE = ERR_ + "saisir un nombre! "

MIN_MAP_SIDE = 3
MSG_DISCLAMER = "Bienvenue dans Roboc."
MSG_AVAIBLE_MAP = "Cartes disponible: "
MSG_CHOOSE_MAP = "Choississez un numéro de carte: "
MSG_CHOOSE_MOVE = "Votre deplacement (h pour l'aide): "
MSG_SELECTED_MAP = "Vous avez fait le choix #{}, la carte «{}»."

DEBUG = False


# VARIABLES

maps_name_list = list()     # liste des maps proposees a l'utilisateur
user_select_map_id = -1     # carte choisie par l'utilisateur