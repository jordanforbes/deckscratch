def p(x):
    print(x)

#Unit Class    
class Unit():
    def __init__(self,name="player",hp=100,block=10):
        self.name=name
        self.hp=hp
        self.block=block
        self.strength=0
        self.dexterity=0
        self.poison=0
        
    #show stats
    def showName(self):
        return self.name
        
    def showHP(self):
        return self.hp
    
    def showBlock(self):
        return self.block 
    
    def showSTR(self):
        return self.strength
    
    def showDEX(self):
        return self.dexterity
    
    def showPSN(self):
        return self.poison
    
    def printStats(self):
        print("name",self.name)
        print("hp",self.hp)
        print("block",self.block)
    
    #change stats
    def addHP(self,hp):
        self.hp +=hp 
        return self
    
    def addBlock(self,block):
        self.block +=block +self.dexterity
        return self
    
    def addSTR(self,s):
        self.strength+=s
        return self
    
    def addDEX(self,d):
        self.dexterity+=d  
        return self
        
    #process Damage 
    def takeDamage(self,dmg):
        self.addBlock(-dmg)
        if self.block<0:
            self.addHP(self.block)
            self.block=0
        return self
    
    def dealDamage(self,target,dmg):
        stre = self.showSTR()
        dmg+= stre 
        target.takeDamage(dmg)
        return self
 
#Iron Wave
def ironWave(player,target):
    player.addBlock(5).dealDamage(target,5)
        
#strike
def strike(player,target):
    player.dealDamage(target,8)
    
#guard 
def guard(player):
    player.addBlock(5)
        

##main loop##
u= Unit()
e= Unit("enemy",20,2)
print("$$$stats$$$")
u.printStats()
e.printStats()
print("###Iron Wave###")
ironWave(u,e)
print("$$$stats$$$")
u.printStats()
e.printStats()