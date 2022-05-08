from Components.Unit import Unit  
from Components.Player import Player 
from Components.Enemy import Enemy 

print("$$$$$$start$$$$$$")
u= Unit()
p= Player()
e= Enemy()
u.dealDamage(e,5)
e.dealDamage(u,4)
print("&&&&&end&&&&")