langs={
    "unit":{
    "initialize":"*BREEN* initializing unit",
    "activate":"BEEP BEEP Unit activated",
    "vitals":"--getting vital signs--",
    "hp":"BZZZT my HP is now:",
    "damage":"BJORK I HAVE BEEN HIT FOR",
    "hpNull":"SYSTEM FAILURE",
    "die":"BOOOOM!"
    },
    "enemy":{
    "initialize":"KRSH KRSH Enemy Unit Activated",
    "activate":"SKRONK Enemy Spotted",
    "vitals":">>>scanning Enemy>>>",
    "hp":"Enemy Health is:",
    "damage":"SHWING! I have dealt the enemy",
    "hpNull":"YES! ENEMY SYSTEMS FAILING",
    "die":"KRAAASH the enemy has fallen!"
    }
}

class Player():
    def __init__(self,lang=langs["unit"],hp=100):
        self.baseHP= hp
        self.hp= 0
        self.lang=lang
        self.speak("initialize")
        self.activate()
    
    def speak(self,key):
        print(self.lang[key])
        return self 
    
    def activate(self):
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
        target.takeDamage(dmg)
        
    def lifeCheck(self):
        self.speak("vitals")
        if self.getHP()<= 0:
            self.speak("hpNull")
            return False
        else:
            return True
        
    def die(self):
        self.speak("die")
        
class Enemy(Player):
    def __init__(self,hp=30,lang=langs["enemy"]):
        print("ENEMY ROBOT APPROACHES")
        self.baseHP=hp
        self.lang=lang
        self.hp=0
        self.activate()
 
        

u= Player()
e= Enemy()
u.dealDamage(e,5)
e.dealDamage(u,4)
u.takeDamage(500)
e.takeDamage(400)

# e.activate()