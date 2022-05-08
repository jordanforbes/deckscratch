from Components.Unit import Unit,langs
from Langs import langs

class Player(Unit):
    def __init__(self,hp=50,lang=langs["player"]):
        self.baseHP,self.lang= hp, lang
        self.activate()
