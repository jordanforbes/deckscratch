from Components.Unit import Unit  
from Langs import langs

class Enemy(Unit):
    def __init__(self,hp=30,lang=langs["enemy"]):
        print("ENEMY ROBOT APPROACHES")
        self.baseHP,self.lang= hp,lang
        self.activate()