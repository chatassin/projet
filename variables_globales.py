"""
Ici on va définir nos variables
"""
from classes import *

STEPNUM = 0  # pas choisi int(0->7)
TEMPO = 100
octave = 0
SEQ = False  # si oui ou non on a lancé la séquence
PARAM_NUM = 2  # entre int(0-5)


# steps
NB_STEP=8

#exemple : S1 = [0, 1, 0, 0, 0, 0]
# step 1 = [note,octave,durée gate,ADSR,CV1,CV2]
# note = int(0->11) do=0 do#=1 etc...
# octave = int(1->5) (car on commence à l'octave 1)

#initialisation des listes
#crée une liste d'éléments de la classe STEP
STEPLIST=[]
for i in range(NB_STEP):
   STEPLIST.append(STEP())

# Dictionnaire liant les notes à leur str
DIC_PITCH = {0 : "A", 1: "A#", 2: "B", 3: "C", 4: "C#", 5: "D", 6: "D#", 7: "E", 8: "F", 9: "F#", 10: "G", 11: "G#"}

# Dictionnaire liant les param à leur str (pour l'affichage)
DIC_PARAM = {0:"Pitch", 1 : "Octave", 2: "Gate time", 3: "ADSR", 4: "CV1", 5: "CV2"}


#   pins   #

# charlieplexing
cp1 = 0  # premier pin utilisé pour le charliplexing
cp2 = 0
cp3 = 0
cp4 = 0
cp5 = 0
cp = [cp1, cp2, cp3, cp4, cp5]

# boutons
bpm = 12  # pin bouton pas+1
bpp = 7  # pin bouton pas-1
bl = 0  # pin bouton pour lancer la séquence
bo = 0  # pin bouton octave
bnp = 0  # pin bouton note+
bnm = 0  # pin bouton note-
bouton_seq1 = 0


# rotaty encoders

Enc_A = encoder()
Enc_A.pin1 = 11
Enc_A.pin2 = 13
Enc_B = encoder()
Enc_A.pin1 = 0
Enc_A.pin2 = 0
