
class STEP:
    #Chaque step a un pitch octave et une liste correspondant aux valeurs de: gate_length, ADSR, CV1 et CV2.
    def __init__(self, pitch= 0, octave=0, param = [0,0,0,0]):
        self.pitch = pitch
        self.octave = octave
        self.param = param

    #controle du pitch
    def pitch_up(self):
        if self.pitch < 11:  # si on est pas à la note la plus haute, on monte d'une note
            self.pitch += 1

    def pitch_down(self):
        if self.pitch > 0:  # si on est pas à la note la plus basse, on descend d'une note
            self.pitch -= 1

    #controle de l'ocave
    def octave_up(self):
        self.octave += 1
        if self.octave == 5:  # quand on dépasse la dernière octave, on revient à 0
            self.octave = 0

    def param_up(self, num):
        if self.param[num] < 10:  # si on est pas au max, on augmente
            self.param[num] += 1

    def param_down(self, num):
        if self.param[num] > 0:  # si on est pas au min, on baisse
            self.param[num] -= 1

class component:

    def __init__(self,name='',pin1=0,pin2=0,state=0):
        self.name = name
        self.pin1 = pin1
        self.pin2 = pin2
        self.state = state

    @property
    def get_state(self):
        return self.state
    def change_state(self):
        self.state +=1
        if self.state == 0:
            self.state = 0
#encodeur hérite de la classe composant
class encoder(component):

    def __init__(self, value=0, name='', pin1=0, pin2=0, state=0):
        super().__init__(name, pin1, pin2, state)
        self.value = value      #ici on peut contenir un compteur qui dis quel paramètre on sélectionne

    @property
    def get_value(self):
        return self.value
    def value_up(self):
        self.value += 1
        if self.value == 4:
            self.value = 0
    def value_down(self):
        self.value -= 1
        if self.value == 0:
            self.value = 3

class button(component):
    def __init__(self, name='', pin1=0, pin2=0, state=0):
        """
        :param name:
        :param pin1: numéro du pin notation board
        :param pin2: numéro du pin notation board
        :param state: état= 1 siH IGH ou 0 si LOW
        """
        super().__init__(name, pin1, pin2, state)


class LED(component):

    def __init__(self, number=0, state=0, name='', pin1=0, pin2=0):
        super().__init__(name, pin1, pin2, state)
        self.number = number
        self.state = state          #state = 0 si low et state=1 si High



