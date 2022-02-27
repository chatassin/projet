"""
Dans ce fichier on va mettre les fonctions qui controlent les parametres
"""

import variables_globales as vg
import RPi.GPIO as GPIO
import affichage as af
from time import sleep, time


##################################################################
# SETUP

def setup():
    GPIO.setwarnings(False)  # dit au raspberry pi d'ignorer les warnings
    GPIO.setmode(GPIO.BOARD)  # choisi le mode board
    af.hello()
    af.UPDATE_SCREEN()

##################################################################
# choix du pas

def control_step():

    def step_plus():
        vg.STEP_NUM += 1
        if vg.STEP_NUM >= len(vg.STEPLIST):  # si on dépasse le dernier pas -> on revient au pas 0
            vg.STEP_NUM = 0

    def step_moins():
        vg.STEP_NUM -= 1
        if vg.STEP_NUM <= (-1):  # si on descend à -1 -> on va au dernier pas
            vg.STEP_NUM = len(vg.STEPLIST) - 1

    GPIO.setup(vg.bpp, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(vg.bpm, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
        etat1 = GPIO.input(vg.bpp)
        etat2 = GPIO.input(vg.bpm)
        if etat1==0 and etat2 == 1:
            step_moins()
            sleep(0.2)
            af.UPDATE_SCREEN()
            control_led()
        elif etat1==1 and etat2==0:
            step_plus()
            sleep(0.2)
            af.UPDATE_SCREEN()
            control_led()
##################################################################
# seq

def detect_seq():
    etat1 = GPIO.input(vg.bouton_seq1)
    etat2 = GPIO.input(vg.bouton_seq2)
    if etat1==0 and etat2 == 1:
        step_moins()
        sleep(0.2)
        af.UPDATE_SCREEN()
        control_led()
    elif etat1==1 and etat2==0:
        step_plus()
        sleep(0.2)
        af.UPDATE_SCREEN()
        control_led()

def control_seq():

    def change_seq():
        # change l'état de seq
        if vg.SEQ:
            vg.SEQ = False
        else:
            vg.SEQ = True

    GPIO.setup(vg.bl, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(vg.bpp, GPIO.RISING, callback=change_seq)

##################################################################
# LEDS


def control_led():
    #listecp = [[35,37],[37,35],[37,38],[38,37],[38,40],[40,38],[37,40],[40,37]]

    def charlieplexing():  # pas encore fini
        # fonction qui créer une liste avec les pins nécessaire pour allumer les LED
        cp = vg.cp
        leds = []

        for i in range(len(cp)-1):
            for j in range(i+1, len(cp)):
                leds.append([cp[i], cp[j]])
                leds.append([cp[j], cp[i]])
        return leds

    def light_led(led):
        # fonction qui allume le LED choisi
        print(led)
        for i in vg.cp:
            GPIO.setup(i, GPIO.IN)  # met tous les pins en mode IN

        GPIO.setup(led[0], GPIO.OUT)
        GPIO.output(led[0], GPIO.HIGH)  # met le premier pin sur HIGH
        GPIO.setup(led[1], GPIO.OUT)
        GPIO.output(led[1], GPIO.LOW)  # met le deuxieme pin sur LOW



    leds = charlieplexing()
    light_led(leds[vg.STEP_NUM])
    play_seq(leds)

def play_seq(leds):
    # allume les LEDs quand la séquence est en train d'être jouée
    while vg.SEQ:
        for i in range(len(vg.STEPLIST)-1):
            light_led(leds[i])
            sleep(1)  # il faut régler le nombre selon le tempo choisi

##################################################################
# octave

def control_octave():
    GPIO.setup(vg.bo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(vg.bo, GPIO.RISING, callback=vg.STEPLIST[vg.STEP_NUM].octave_up)

##################################################################
# Note


def control_pitch():

    GPIO.setup(vg.bnp, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(vg.bnm, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(vg.bnp, GPIO.RISING, callback=vg.STEPLIST[vg.STEP_NUM].pitch_up)
    GPIO.add_event_detect(vg.bnm, GPIO.RISING, callback=vg.STEPLIST[vg.STEP_NUM].pitch_down)

#################################################################

def rotation_decode():
    clkLastState = GPIO.input(vg.Enc.pin1)
    while True:
        clkState = GPIO.input(vg.Enc.pin1)
        dtState = GPIO.input(vg.Enc.pin2)
        if clkState != clkLastState:
                if dtState != clkState:
                        vg.Enc.value_up()
                else:
                        vg.Enc.value_down()
                print (vg.Enc.value//2)
        clkLastState = clkState
        #sleep(0.01)



##############################################################
# controle valeur du paramètre
def control_param_value():
#detecte la rotation de l'encodeur valeur du paramètre et change sa valeur dans l'objet step
    clkLastState = GPIO.input(vg.Enc.pin1)
    while True:
        clkState = GPIO.input(vg.Enc.pin1)
        dtState = GPIO.input(vg.Enc.pin2)
        if clkState != clkLastState:
                if dtState != clkState:
                        vg.STEPLIST[vg.STEP_NUM].param_up(vg.Enc_A.value)
                else:
                        vg.STEPLIST[vg.STEP_NUM].param_down(vg.Enc_A.value)
                print (vg.STEPLIST[vg.STEP_NUM].param//2)
        clkLastState = clkState
        #sleep(0.01)

    GPIO.cleanup()
    
    
#################################################################
# modifie la valeur du tempo

def control_tempo():
    while True:
        clkState = GPIO.input(vg.Enc.pin1)
        dtState = GPIO.input(vg.Enc.pin2)
        if clkState != clkLastState:
            if dtState != clkState:
                vg.TEMPO += 1
            else:
                vg.TEMPO -=1
        clkLastState = clkState
        # sleep(0.01)

#####################################################################
# effectue une fonction pendant le temps défini par le tempo et la durée du gate

def ex_time(): #mettre un for pour tous les pas
    gate_time = time() + vg.STEPLIST[0].param[0] * (vg.TEMPO/5)
    gate = time() + (vg.TEMPO/5)
    while time() < gate_time:
        print(5)
    while time() < gate:
        print(0)
