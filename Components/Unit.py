from Langs import langs

class Unit():
    def __init__(self,lang=langs["unit"],hp=100):
        self.baseHP= hp
        self.hp= 0
        self.lang=lang
        self.activate()
    
    def speak(self,key):
        print(self.lang[key])
        return self 
    
    def activate(self):
        self.speak("initialize")
        self.speak("activate")
        self.setHP(self.baseHP)
        return self
        
    def getHP(self):
        return self.hp 
    
    def setHP(self,hp):
        self.hp= hp
        self.speak("hp")
        print(f"--{self.getHP()} HP--")
        return self 
    
    def aim(self):
        return self  
        
    def takeDamage(self,dmg):
        self.speak("damage")
        print(f'{dmg} damage!')
        hp = self.getHP() - dmg 
        self.setHP(hp)
        if self.lifeCheck() == True:
            return self
        else:
            self.die()
    
    def dealDamage(self,target,dmg):
        self.speak("attack")
        target.takeDamage(dmg)
        return self
        
    def lifeCheck(self):
        self.speak("vitals")
        if self.getHP()<= 0:
            self.speak("hpNull")
            return False
        else:
            return True
        
    def die(self):
        self.speak("die")
        return self
        
class Enemy(Unit):
    def __init__(self,hp=30,lang=langs["enemy"]):
        print("ENEMY ROBOT APPROACHES")
        self.baseHP,self.lang= hp,lang
        self.activate()
        
class Player(Unit):
    def __init__(self,hp=50,lang=langs["player"]):
        self.baseHP,self.lang= hp, lang
        self.activate()
 