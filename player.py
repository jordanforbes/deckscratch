class Player():
    def __init__(self):
        self.hp= 0
        self.activate()
        
    def activate(self):
        self.setHP(100)
        print(f"BEEP BEEP Unit activated with {self.getHP()} health")
        return self
        
    def getHP(self):
        return self.hp 
    
    def setHP(self,hp):
        self.hp= hp
        print(f"BZZZZT my HP is now {self.getHP()}")
        return self 
    
    def takeDamage(self,dmg):
        
        

u= Player()
u.setHP(300)
