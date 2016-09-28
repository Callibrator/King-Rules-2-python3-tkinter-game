import random
import data

ignore = [(300,60,160,130)]
# is: X,Y,WIDTH,HEIGHT :)
#Don't get confused
#Default: townspace :)


class enemy:

    def __init__(self):
      self.genxy()
      self.genarmy()
      self.genitems()
      self.genstrenth()
      self.genhealth()

      while True:
       if self.check() == 0:
        break

      ignore.append((self.x,self.y,50,50))

    def genxy(self):
       self.x = random.randint(30,600)
       self.y = random.randint(30,400)
    def check(self):
      for i in range(len(ignore)):
        if self.x < ignore[i][0]+ignore[i][2] and self.y<ignore[i][1]+ignore[i][3] and self.x > ignore[i][0]-ignore[i][2] and self.y > ignore[i][1]-ignore[i][3]:
          self.genxy()
       
          return 1
      return 0

    def genarmy(self):

        for i in range(10):
            army = int((data.maxarmy / random.randint(1,5)) * random.randint(0,5) + 1)
		#Dikeo fenete :P

        self.army = army

    def genitems(self):
        items = self.army * random.randint(5,20) * 2

        if items <= 0: # :P 0 Chances 
            self.gold = 0
            self.food = 0
            self.wood = 0
            return 0

        x = random.randint(1,items)
        self.gold = x
        items -= x

        if items <= 0:
           self.food = 0
           self.wood =0
           return 0

        x = random.randint(1,items)
        self.food = x
        items -= x
        
        if items <= 0:
           self.wood = 0
           return 0
        x = random.randint(1,items)
        self.wood = x


    def genstrenth(self):
        try:
         strength =  random.randint(1,int(self.army / 3))
         
        except ValueError:
 
         strength = 1
        finally:
         self.strength = strength
    def genhealth(self):
        try:
          health = random.randint(5,int(self.army / 2))
        except ValueError:
          health = 5
        finally:
          self.health = health

