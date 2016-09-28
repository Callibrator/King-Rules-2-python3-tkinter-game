from tkinter import *
import os
import random
import npc
import data
from tkinter.messagebox import showinfo
import windows
from tkinter.simpledialog import askstring

root = Tk()
root.title('King Rules 2')
root.config(bg='black')


frame = Frame(width=800,height=600,bg='black')
frame.pack()

#Loading Grass
grass = PhotoImage(file='data' + os.sep +'grass.gif')
#loading buildings
enemyhouse = PhotoImage(file='data' + os.sep + 'tent.gif')
baracks1 = PhotoImage(file='data' + os.sep + 'baracks.gif')
baracks2 = PhotoImage(file='data' + os.sep + 'baracks2.gif')
baracks3 = PhotoImage(file = 'data' + os.sep + 'baracks3.gif')
hospital = PhotoImage(file = 'data' + os.sep + 'hospital.gif')
farm1 = PhotoImage(file = 'data' + os.sep + 'farm.gif')
farm2 = PhotoImage(file = 'data' + os.sep + 'farm2.gif')
townhall = PhotoImage(file = 'data' + os.sep + 'townhall.gif')
forester = PhotoImage(file='data' + os.sep + 'forester.gif')
mine = PhotoImage(file='data'+ os.sep+'mine.gif')
smithy = PhotoImage(file='data'+os.sep+'smithy.gif')
temple = PhotoImage(file='data' + os.sep + 'temple.gif')
house = PhotoImage(file='data'+os.sep + 'house.gif')
wall = PhotoImage(file='data'+os.sep +'wall.gif')
tavern = PhotoImage(file='data'+os.sep+'tavern.gif')
#Loading Our town
hall1 = PhotoImage(file='data' + os.sep + 'mainhall1.gif')
hall2 = PhotoImage(file='data' + os.sep + 'mainhall2.gif')
hall3 = PhotoImage(file='data' + os.sep + 'mainhall3.gif')
hall4 = PhotoImage(file='data' + os.sep + 'mainhall4.gif')
#Loading Resources
foodimg  = PhotoImage(file = 'data' + os.sep + 'food.gif')
goldimg  = PhotoImage(file = 'data' + os.sep + 'gold.gif')
woodimg  = PhotoImage(file = 'data' + os.sep + 'wood.gif')
armyimg  = PhotoImage(file = 'data' + os.sep + 'army.gif')
river = PhotoImage(file = 'data' + os.sep + 'river.gif')
forest = PhotoImage(file = 'data' + os.sep + 'forest.gif')


Label(frame,image=goldimg).place(x=0,y=10)
Label(frame,text='Gold',bg='black',fg='red').place(x=40,y=10)
golddisp = Label(frame,text='0',bg='black',fg='red')
golddisp.place(x=40,y=30)

Label(frame,image=woodimg).place(x=200,y=10)
Label(frame,text='Wood',bg='black',fg='red').place(x=240,y=10)
wooddisp = Label(frame,text='0',bg='black',fg='red')
wooddisp.place(x=240,y=30)

Label(frame,image=foodimg).place(x=400,y=10)
Label(frame,text='Food',bg='black',fg='red').place(x=440,y=10)
fooddisp = Label(frame,text='0',bg='black',fg='red')
fooddisp.place(x=440,y=30)

Label(frame,image=armyimg).place(x=600,y=10)
Label(frame,text='Army',bg='black',fg='red').place(x=640,y=10)
armydisp = Label(frame,text='0',bg='black',fg='red')
armydisp.place(x=640,y=30)




         


Enemys = []
gui = Canvas(frame)
gui.pack(side=LEFT,pady=60,fill=X)
gui.config(width=800,height=500)



def makeenemys():
    if len(Enemys) > 4:
       return 0 #The maximun enemys that we can get is 9 :)

    x = random.randint(1,5)
    for i in range(x):
        Enemys.append(npc.enemy())

def maketown():
    data.view='town'
    for x in range(17):
        for y in range(12):
            gui.create_image(50*x,50*y,image=grass)
    

    gui.create_image(350,45,image=townhall)
    gui.create_image(545,85,image=mine)
    gui.create_image(565,210,image=forester)
    gui.create_image(445,250,image=farm1)
    gui.create_image(361,250,image=house)
    gui.create_image(306,250,image=house)
    gui.create_image(670,275,image=river)
    gui.create_image(670,100,image=forest)
    gui.create_image(670,150,image=forest)
    gui.create_image(730,100,image=forest)
    gui.create_image(730,150,image=forest)
    gui.create_image(35,280,image=forest)
    gui.create_image(150,280,image=forest)
    gui.create_image(161,350,image=forest)
    gui.create_image(44,350,image=forest)

    if data.halllevel > 3 and data.halllevel < 8:
       gui.create_image(300,300,image=house)
       gui.create_image(350,300,image=house)

    elif data.halllevel > 7 and data.halllevel < 14:
       gui.create_image(300,300,image=house)
       gui.create_image(350,300,image=house)
       gui.create_image(35,60,image=house)
       gui.create_image(90,60,image=house)

    elif data.halllevel > 13:
       gui.create_image(300,300,image=house)
       gui.create_image(350,300,image=house)
       gui.create_image(35,60,image=house)
       gui.create_image(90,60,image=house)
       gui.create_image(35,100,image=house)
       gui.create_image(90,100,image=house)
    
    if data.barackslevel > 0 and data.barackslevel < 5:
          gui.create_image(205,105,image=baracks1)
    elif data.barackslevel > 4 and data.barackslevel < 10:
          gui.create_image(205,105,image=baracks2)
    elif data.barackslevel > 9:
          gui.create_image(205,105,image=baracks3)

    if data.hospitallevel > 0:
          gui.create_image(185,205,image=hospital)

    if data.smithylevel > 0:
          gui.create_image(295,165,image=smithy)

    if data.templelevel > 0:
          gui.create_image(400,135,image=temple)


    if data.farms > 1 and data.farms < 3:
          gui.create_image(495,250,image=farm2)

    elif data.farms > 2 and data.farms < 5:
          gui.create_image(495,250,image=farm2)
          gui.create_image(450,298,image=farm1)
    elif data.farms > 4 and data.farms < 10:
          gui.create_image(495,250,image=farm2)
          gui.create_image(495,298,image=farm1)
          gui.create_image(450,298,image=farm1)
    elif data.farms >9:
          gui.create_image(495,250,image=farm2)
          gui.create_image(495,298,image=farm1)
          gui.create_image(450,298,image=farm1)
          gui.create_image(450,355,image=farm1)
          gui.create_image(500,355,image=farm1)

    if data.walllevel > 0:
          gui.create_image(402,450,image=wall)

    if data.tavernlevel > 0:
          gui.create_image(465,180,image=tavern)

            

def makeworld():
    data.view='world'
    for x in range(17):
        for y in range(12):
            gui.create_image(50*x,50*y,image=grass)
            
        for i in range(len(Enemys)):
            gui.create_image(Enemys[i].x,Enemys[i].y,image=enemyhouse)
            gui.create_text(Enemys[i].x,Enemys[i].y+15,text='Enemy Size',font=('Arial',10,'bold'))
            gui.create_text(Enemys[i].x,Enemys[i].y+30,text=str(Enemys[i].army),font=('Arial',10,'bold'))
	    
   #mainHall
    if data.halllevel > 0 and data.halllevel < 10:
         gui.create_image(300,60,image=hall1)
         gui.create_text(300,90,text='Your town',font=('Arial',12,'bold'),fill='green') 
    elif data.halllevel > 9 and data.halllevel < 15:
         gui.create_image(300,60,image=hall2)
         gui.create_text(300,90,text='Your town',font=('Arial',12,'bold'),fill='green')
    elif data.halllevel > 14 and data.halllevel < 20:
         gui.create_image(300,60,image=hall3)
         gui.create_text(300,110,text='Your town',font=('Arial',12,'bold'),fill='green')  
    elif data.halllevel > 19:
         gui.create_image(300,60,image=hall4)
         gui.create_text(300,130,text='Your town',font=('Arial',12,'bold'),fill='green')     
      
def display():
    golddisp['text'] = data.gold
    wooddisp['text'] = data.wood
    fooddisp['text'] = data.food

    armydisp['text'] = data.army
    if data.view == 'world':
        makeworld()
    elif data.view == 'town':
        maketown()
    else:
         data.view = 'world'
         makeworld()



def menu():
    win = Toplevel()
    win.title('King Rules 2')
    #win.grab_set()
    win.focus_set()
    win.config(bg='black',width=200,height=220) 
    def save():
     name = askstring('Save','Name of the save:')
     if name == '':
       showinfo('Save','Save can\'t be without name')
       win.destroy()
       return 0

     if name == None:
        win.destroy()
        return 0

     if os.path.isdir('Saves') == False:
        os.mkdir('Saves')

     fl = open('Saves'+os.sep+name,'w')
     fl.write('data.gold = '+str(data.gold)+'\n')
     fl.write('data.wood = '+str(data.wood)+'\n')
     fl.write('data.food = '+str(data.food)+'\n')
     fl.write('data.army = '+str(data.army)+'\n')
     fl.write('data.maxarmy = '+str(data.maxarmy)+'\n')
     fl.write('data.halllevel = '+str(data.halllevel)+'\n')
     fl.write('data.barackslevel = '+str(data.barackslevel)+'\n')
     fl.write('data.gamedays = '+str(data.gamedays)+'\n')
     fl.write("data.view = '"+str(data.view)+"'\n")
     fl.write('data.dayjobs = '+str(data.dayjobs)+'\n')
     fl.write('data.armyhealth = '+str(data.armyhealth)+'\n')
     fl.write('data.armystrenghtmin = '+str(data.armystengthmin)+'\n')
     fl.write('data.armystrenghtmax = '+str(data.armystrengthmax)+'\n')
     fl.write('data.armyupdate = '+str(data.armyupdate)+'\n')
     fl.write('data.killescape = '+str(data.killescape)+'\n')
     fl.write('data.farms = '+str(data.farms)+'\n')
     fl.write('data.smithylevel = '+str(data.smithylevel)+'\n')
     fl.write('data.templelevel = '+str(data.templelevel)+'\n')
     fl.write('data.hospitallevel = '+str(data.hospitallevel)+'\n')
     fl.write('data.foresterlevel = '+str(data.foresterlevel)+'\n')
     fl.write('data.minelevel = '+str(data.minelevel)+'\n')
     fl.write('data.walllevel = '+str(data.walllevel)+'\n')
     fl.write("data.update = '"+str(data.update)+"'\n")
     fl.write('data.happynes = '+str(data.happynes)+'\n')
     fl.write('data.peoplesintown = '+str(data.peoplesintown)+'\n')
     fl.write('data.maxpeoplesintown = '+str(data.maxpeoplesintown)+'\n')
     fl.write('data.gifts = '+str(data.gifts)+'\n')
     fl.write('data.tavernlevel = '+str(data.tavernlevel)+'\n')
     fl.write("data.attack = '"+str(data.attack)+"'\n")
     fl.close()

     showinfo('Save','Save succesfully completed')
     win.destroy()
     return 0

    def load():
      x = askstring('Load','Please enter the name of the save')
      if x == '':
       showinfo('Load','There is no save with this name')
       win.destroy()
       return 0
      if x == None:
        win.destroy()
        return 0

      if os.path.isfile('Saves'+os.sep+x) == False:
        showinfo('Load','There is no save with this name')
        win.destroy()
        return 0
      
      fl = open('Saves'+os.sep+x,'r')
      for i in range(29):
        l = fl.readline()
        exec(l)

      fl.close()
      display()
      showinfo('Load','Save succesfully loaded')
      win.destroy()
      return 0

    def info():
        showinfo('INFO','This **Game** created by Callibrator\nUsing python 3.2')
        win.destroy()
        return 0

    Button(win,text='Continue',bg='black',fg='red',width=13,command=win.destroy).pack(side=TOP,padx=25,pady=10)  
    Button(win,text='Load Game',bg='black',fg='red',width=13,command=load).pack(side=TOP,padx=25,pady=10)   
    Button(win,text='Save Game',bg='black',fg='red',width=13,command=save).pack(side=TOP,padx=25,pady=10) 
    Button(win,text='Info',bg='black',fg='red',width=13,command=info).pack(side=TOP,padx=25,pady=10)
    Button(win,text='Exit',bg='black',fg='red',width=13,command=root.destroy).pack(side=TOP,padx=25,pady=10) 

    win.mainloop()

def report():
    win = Toplevel()
    win.title('King Rules 2')
    win.grab_set()
    win.focus_set()

    frame = Frame(win,bg='black',width=270,height=130)
    frame.pack()

    Label(frame,text='Gold: ' + str(data.gold),bg='black',fg='red').place(x=20,y=10)
    Label(frame,text='Happynes: ' + str(data.happynes),bg='black',fg='red').place(x=130,y=10)
    Label(frame,text='Food: ' + str(data.food),bg='black',fg='red').place(x=20,y=30)
    Label(frame,text='Peoples in town: ' + str(data.peoplesintown),bg='black',fg='red').place(x=130,y=30)
    Label(frame,text='Wood: ' + str(data.wood),bg='black',fg='red').place(x=20,y=50)
    Label(frame,text='Max peoples in town: ' + str(data.maxpeoplesintown),bg='black',fg='red').place(x=130,y=50)
    Label(frame,text='Army: ' + str(data.army)+ ' / '+ str(data.maxarmy),bg='black',fg='red').place(x=20,y=70)
    Label(frame,text='Days: ' + str(data.gamedays),bg='black',fg='red').place(x=130,y=70)
    Button(frame,text='Continue',bg='black',fg='red',command=win.destroy,width=35).place(x=20,y=100)

    win.mainloop()

def attackwin(enemy):
    win = Toplevel()
    win.title('King Rules 2')
    win.config(bg = 'Black')
    win.focus_set()

    

    try:
      win.grab_set()
    except TclError:
      pass

    def doAttack(yourarmy):
       yourarmy = float(yourarmy)
       returnday = random.randint(1,3)
       yourarmy = int(yourarmy)
       survive = 0

       totalarmysend = yourarmy

       if totalarmysend == 0:
           showinfo('Battle','You can\'t Attack without army')
           win.destroy()
           return 0

       yourstrenght = random.randint(data.armystengthmin,data.armystrengthmax)


       data.maxarmy -= totalarmysend
       data.army -= totalarmysend

       #Battle Begin :)
       
       yu = (yourarmy * data.armyhealth) + yourstrenght
       en = (enemy.army * enemy.health) + enemy.strength

       x = yu-en

       
       yourarmy = x / data.armyhealth

       if (x / data.armyhealth) > totalarmysend:
          yourarmy = totalarmysend #In case that you have too powerfull army :)

                                   
       yourarmy = int(yourarmy)

       if yourarmy == 0:
          yourarmy = 1 #You can't win the battle and return back to the castle 0 soldiers :D



       def survived(army,mainarmy):


         surv = 0

         if army <= 0:
            looptimes = mainarmy
         elif army > 0:
            looptimes = mainarmy - army


         for i in range(looptimes):
           x = random.randint(0,100)
           if x <= data.killescape:
              surv +=1
         return surv


       if x < 0:
         survive = survived(yourarmy,totalarmysend)
         if survive > 0:
             msg = 'You loose the battle\nSome say that there are some survived soldiers and will return soon'
             data.dayjobs.append((data.gamedays + returnday,'data.army += '+str(survive)))
             data.dayjobs.append((data.gamedays + returnday,'showinfo("Battle","Some soldier\'s Have return from the battle alive Soldiers Returned: '+str(survive)+'")'))
             data.dayjobs.append((data.gamedays + returnday,'data.maxarmy += '+str(survive)))

         else:
             msg = 'You loose the battle\nYou didn\'t found even the bodys of your soldier\'s'

         showinfo('Battle',msg)
         data.maxarmy += totalarmysend
         data.maxarmy -= survive
         enemy.army -= int(yu / 6)
         win.destroy()
         makeworld()
         return 0
       else:
         var1 = yourarmy

         survive = survived(var1,totalarmysend)

         
         showinfo('Battle','You win the battle\nYour army will return in %d days'%returnday)

         data.dayjobs.append((data.gamedays+returnday,'data.maxarmy += '+str(totalarmysend)))
         data.dayjobs.append((data.gamedays+returnday,'data.gold += '+str(enemy.gold))) 
         data.dayjobs.append((data.gamedays+returnday,'data.wood += '+str(enemy.wood))) 
         data.dayjobs.append((data.gamedays+returnday,'data.food += '+str(enemy.food))) 
         data.dayjobs.append((data.gamedays+returnday,'data.army += '+str(int(yourarmy+survive))))
         data.dayjobs.append((data.gamedays+returnday,'showinfo("Battle","Your army have return. Army returned: '+str(yourarmy + survive)+' Gold Taken: '+str(enemy.gold)+' Wood Taken: '+str(enemy.wood) + " Food Taken: "+str(enemy.food)+'")'))
         Enemys.remove(enemy)

         makeworld()
         win.destroy()
	 

   
    if data.army == 0:
       showinfo('Army','You can\'t Attack\nYou have no army')
       win.destroy()
       return 0

    yarmy = StringVar()
    yarmy.set('0')

    Label(win,text='Enemys army size: ' + str(enemy.army),fg='red',bg='black').pack(side=TOP,pady=5,padx=10)
    Label(win,text='Your army size: ' + str(data.army),fg='red',bg='black').pack(side=TOP,pady=5,padx=10)

    sendarmy = Scale(win,from_=0,to=data.army,orient='horizontal',variable=yarmy,bg='black',fg='red',tickinterval = (data.army / 5))
    sendarmy.pack(side=TOP,pady=5,padx=10)

    Button(win,text='Attack',bg='black',fg='red',command=lambda:doAttack(yarmy.get())).pack(side=TOP,pady=5,padx=10)
    Button(win,text='Back',bg='black',fg='red',command=win.destroy).pack(side=TOP,pady=5,padx=10)

    win.mainloop()


def incomingAttack():
   if data.attack == 'no':
       return 0
   
   x = random.randint(0,100)
   #print(x)
   if x > 49:
      return 0

   data.attack = 'no'
   data.dayjobs.append((data.gamedays+random.randint(3,8),"data.attack='yes'"))
   food = random.randint(int((10 * data.food)/ 100),int((25 * data.food)/100)) #10%-25% :)
   gold = random.randint(int((10 * data.gold)/ 100),int((25 * data.gold)/100)) #10%-25% :)
   wood = random.randint(int((10 * data.wood)/ 100),int((25 * data.wood)/100)) #10%-25% :)
   army = random.randint(0,data.maxarmy+10) + (data.walllevel * 10)

   #print('Army: %d'%army)


   if data.walllevel > 0:
       army -= random.randint((data.walllevel * 10)-5,(data.walllevel*10)+5)

   if army < 1:
     showinfo('Attack','Some barbarian\'s attack on your village\nThey don\'t pass even the wall')
     return 0

   #print('--Army: %d'%army)
   
   yourarmy = data.army
   x = army
   army -= data.army
   data.army -= x
   
   
   def survived():
     if data.army < 1:
       looptimes = yourarmy
       data.army = 0
     else:
       looptimes = yourarmy - data.army

     for i in range(looptimes):
       alive = random.randint(0,100)
       if alive <= data.killescape:
          data.army += 1

   if data.army < 0:
      survived()
      showinfo('Attack','Some barbarians attacked on your town. You loose the battle\nAlive Soldiers: '+str(data.army)+'\nstolen goods:\nGold: '+str(gold)+' Wood: '+str(wood)+' Food: '+str(food))
      data.gold -= gold
      data.food -= food
      data.wood -= wood
   else:
      survived()
      showinfo('Attack','Some barbarians attack on your town you win the battle\nAlive soldiers: '+str(data.army))

   

def sleep():
    data.gamedays += 1
    prevjobs = []  
    msg = 'Report of Day:\n'

    for i in range(len(data.dayjobs)):
       if data.dayjobs[i][0] == data.gamedays:
          exec(data.dayjobs[i][1])
          prevjobs.append(data.dayjobs[i])


    for i in prevjobs:
        data.dayjobs.remove(i)

        #Let's delete the done jobs to release space on memory :)
        #Before i write the code i wrote this...
        #for i in data.dayjobs:
        #  if data.gamedays == i[0]:
        #     exec(i)
        #     data.dayjobs.remove(i)
        # i'am a novice and it took me 5 minit's to relalise
        # WTF is going wrong... :P


    #------------------------------
    data.gold += data.minelevel * 25
    data.wood += data.foresterlevel * 15
    data.food += data.farms * 5
    
    if data.food - data.army < 0:
        data.happynes -= 5
        msg += '!You have no food to keep your army strenght your army will leave...\n'
        data.army -= 2
        if data.army < 0:
         data.army = 0
    else:
        data.food -= data.army

    if data.food - data.gifts < 0:
        msg += '!You can\'t give gifts to your people\n'
        data.gifts = 0
    else:
        data.happynes += data.gifts * 5
        data.food -= data.gifts
    
    data.happynes -= data.peoplesintown
    if data.happynes < 0:
       data.happynes = 0
    elif data.happynes > 100:
       data.happynes = 100



    if data.happynes > 50 and data.peoplesintown < data.maxpeoplesintown:
        data.peoplesintown +=2
        if data.peoplesintown > data.maxpeoplesintown:
           data.peoplesintown = data.maxpeoplesintown

    elif data.happynes < 50:
        data.peoplesintown -= 2
        if data.peoplesintown < 0:
           data.peoplesintown = 0
        msg += '!Your people start leaving from town give them some gifts\n'

    data.gold += data.peoplesintown

    #print('Gold: %d'%data.gold)
    #print('Wood: %d'%data.wood)
    #print('Food: %d'%data.food)
    #print('Army: %d'%data.army)
    #print('Max Army: %d'%data.maxarmy)
    #print('Happynes: %d'%data.happynes)
    #print('peoples: %d'%data.peoplesintown)
    #print('Max peoples: %d'%data.maxpeoplesintown)


    #print(msg)
    
    if msg != 'Report of Day:\n':
        showinfo('Report',msg)

    incomingAttack()

    makeenemys()
    display()



Button(frame,text='Show Town',bg='black',fg='red',command=maketown,width=10).place(x=1,y=575)
Button(frame,text='Show World',bg='black',fg='red',command=makeworld,width=10).place(x=730,y=575)
Button(frame,text='Sleep',bg='black',fg='red',command=sleep,width=10).place(x=80,y=575)
Button(frame,text='Status',bg='black',fg='red',command=report,width=10).place(x=650,y=575)
Button(frame,text='Menu',bg='black',fg='red',command=menu,width=10).place(x=350,y=575)






def button1event(event):
   # print('X: %d,Y: %d'%(event.x,event.y))

    if data.view == 'world':

     if data.halllevel > 0 and data.halllevel < 10:
        if event.x < 325 and event.x > 275 and event.y > 35 and event.y < 85:
         maketown()
     elif data.halllevel > 9 and data.halllevel < 15:
        if event.x < 325 and event.x > 275 and event.y > 35 and event.y < 85:
         maketown()
     elif data.halllevel > 14 and data.halllevel < 20:
        if event.x < 300 + 55 and event.x > 300 - 55 and event.y > 60 -45 and event.y < 60 + 45:
         maketown() 
     elif data.halllevel > 19:
        if event.x < 300 + 50 and event.x > 300 - 50 and event.y > 60 -55 and event.y < 60 + 55:
         maketown() 
     
     for i in range(len(Enemys)):
       if event.x > Enemys[i].x -18 and event.x < Enemys[i].x + 18 and event.y > Enemys[i].y - 18 and event.y < Enemys[i].y + 18:
        attackwin(Enemys[i])

    elif data.view == 'town':

       if event.x < 375 and event.x > 325 and event.y > 15 and event.y < 75:
          windows.hall()

       if event.x < 470 and event.x > 420 and event.y > 225 and event.y < 275:
          windows.farm()

       if event.x < 570 and event.x > 520 and event.y > 60 and event.y < 110:
          windows.mine()

       if event.x < 590 and event.x > 540 and event.y > 185 and event.y < 235:
          windows.forester()

       if data.barackslevel > 0 and data.barackslevel < 5:
          if event.x < 238 and event.x > 180 and event.y > 80 and event.y < 133:
            windows.baracks()
       elif data.barackslevel > 4 and data.barackslevel < 10:
          if event.x < 243 and event.x > 155 and event.y > 89 and event.y < 148:
            windows.baracks()
       elif data.barackslevel > 9:
          if event.x < 243 and event.x > 155 and event.y > 57 and event.y < 151:
            windows.baracks()

       if data.hospitallevel > 0:
          if event.x < 205 and event.x > 165 and event.y > 185 and event.y < 225:
            windows.hospital()

       if data.smithylevel > 0:
          if event.x < 320 and event.x > 270 and event.y > 140 and event.y < 190:
             windows.smithy()
        
       if data.templelevel > 0:
          if event.x < 425 and event.x > 375 and event.y > 106 and event.y < 164:
             windows.temple()

       if data.walllevel > 0:

          if event.x < 800 and event.x > 0 and event.y > 417 and event.y < 480:
             windows.wall()

       if data.tavernlevel > 0:
          if event.x < 490 and event.x > 440 and event.y < 205 and event.y > 155:
             windows.tavern()



 



if data.view == 'world':
   makeworld()
elif data.view == 'town':
   maketown()
else:
   data.view == 'world'
   makeworld()
   #:/ 


makeenemys()
display()
gui.bind('<Button-1>',button1event)
root.mainloop()
