"""
Dans ce fichier on va mettre les fonctions qui controlent l'affichage
"""
import variables_globales as vg
import I2C_LCD_driver
from time import sleep

mylcd = I2C_LCD_driver.lcd()

def hello():
    """
    fonction qui permet l'affichage de l'écran d'accueil
    """

    mylcd.lcd_clear()
    
    
    fontdata1 = [
     [ 0b000000,
    0b000000,
    0b000000,
    0b000000,                #custom characters
    0b000000,
    0b000000,
    0b000000,
    0b000000 ],

    [ 0b00100,
    0b00110,
    0b00101,
    0b00100,
    0b00100,
    0b11100,
    0b11100,
    0b11100 ]
    ]

    mylcd.lcd_load_custom_chars(fontdata1)
    init = "I"
    liste = ["N","I","T","I","A","L","I","S","A","T","I","O","N","","", "", ""]
    for column in range(20):
        addr= 0xc0
        addr+=column
                    
    #print le symbole note de musique à la ligne 1
        mylcd.lcd_write(addr)
        mylcd.lcd_write_char(1)
        sleep(0.3)

    #efface le symbole note de musique
        mylcd.lcd_write(addr)
        mylcd.lcd_write_char(0)
        if column > 2 and column < 17:
            mylcd.lcd_display_string(init, 2, 3)
            init += liste[column-3]
    sleep(0.5)
    mylcd.lcd_clear()
    
def UPDATE_SCREEN():
    """
    Fonction qui va checker les valeurs du pas, de la note, du paramètre et la valeur du paramètre puis les afficher
    """
    
    # def des variables en str à afficher
    pas = str(vg.STEP_NUM+1)
    note = vg.STEPLIST[vg.STEP_NUM][0]
    nom_note = vg.NOTES[note]
    octave = str(vg.STEPLIST[vg.STEP_NUM].octave)
    tempo = str(vg.TEMPO)
    param = vg.DICO_PARAM[vg.Enc_A.value]
    val_param = str(vg.STEPLIST[vg.STEP_NUM].param[vg.Enc_A.value])
    

    # affichage des variables à  l'écran
    mylcd.lcd_display_string("STEP "+pas, 1, 0)
    mylcd.lcd_display_string(nom_note+octave, 1, 17)
    mylcd.lcd_display_string("TEMPO", 2, 0)
    mylcd.lcd_display_string(tempo, 2, 16 - len(tempo))
    mylcd.lcd_display_string("bpm", 2, 17)
    mylcd.lcd_display_string(param, 4, 0)
    mylcd.lcd_display_string(val_param, 4, 20 - len(val_param))
