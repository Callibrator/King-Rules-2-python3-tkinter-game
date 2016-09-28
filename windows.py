from tkinter import *
import data
from tkinter.messagebox import showinfo
import random

def hall():
   win = Toplevel()
   win.title('Hall')
   win.focus_set()
   try:
     win.grab_set()
   except TclError:
     pass

   def update():
      if data.update == 'no':
         showinfo('Update','You can\'t update this building yet\nOther update in progress')
         win.destroy()
         return 0

     
      if data.gold < data.halllevel * 300:
         showinfo('Update','You don\'t Have the Gold to update this building')
         win.destroy()
         return 0

      data.update = 'no'
      data.gold -= data.halllevel * 300
      data.dayjobs.append((data.gamedays + data.halllevel,"data.update = 'yes'"))
      data.dayjobs.append((data.gamedays + data.halllevel,'data.halllevel += 1'))
      data.dayjobs.append((data.gamedays + data.halllevel,'data.maxpeoplesintown = data.halllevel * 25'))
      showinfo('Update','You must wait '+str(data.halllevel) +' Days to finish the update')
      win.destroy()
      return 0

   def buildhospital():
       if data.update == 'no':
           showinfo('Update','You can\'t Build this yet\nOther update in progress')
           win.destroy()
           return 0
       if data.hospitallevel > 0:
           showinfo('Update','You have alredy build this building')
           win.destroy()
           return 0


       if messagebox.askyesno('Update','This cost: 1000 Gold and take 2 days\nContinue?') == False:
            win.destroy()
            return 0

       if data.gold < 1000:
            showinfo('Update','You don\'t have the gold to update this building')
            win.destroy()
            return 0

       data.gold -= 1000
       data.update = 'no'
       data.dayjobs.append((data.gamedays + 2,"data.update = 'yes'"))
       data.dayjobs.append((data.gamedays + 2,'data.hospitallevel += 1'))
       data.dayjobs.append((data.gamedays + 2,'data.killescape += 10'))

       showinfo('Update','You must wait 2 days')
       win.destroy()
       return 0

   def smithy():
       if data.update == 'no':
           showinfo('Update','You can\'t Build this yet\nOther update in progress')
           win.destroy()
           return 0
       if data.smithylevel > 0:
           showinfo('Update','You have alredy build this building')
           win.destroy()
           return 0


       if messagebox.askyesno('Update','This cost: 200 Gold and take 2 days\nContinue?') == False:
            win.destroy()
            return 0

       if data.gold < 200:
            showinfo('Update','You don\'t have the gold to update this building')
            win.destroy()
            return 0

       data.gold -= 200
       data.update = 'no'
       data.dayjobs.append((data.gamedays + 2,"data.update = 'yes'"))
       data.dayjobs.append((data.gamedays + 2,'data.smithylevel += 1'))
       showinfo('Update','You must wait 2 Days')
       win.destroy()
       return 0


   def baracks():
       if data.update == 'no':
           showinfo('Update','You can\'t Build this yet\nOther update in progress')
           win.destroy()
           return 0
       if data.barackslevel > 0:
           showinfo('Update','You have alredy build this building')
           win.destroy()
           return 0


       if messagebox.askyesno('Update','This cost: 250 Gold and take 2 days\nContinue?') == False:
            win.destroy()
            return 0

       if data.gold < 250:
            showinfo('Update','You don\'t have the gold to update this building')
            win.destroy()
            return 0

       data.gold -= 250
       data.update = 'no'
       data.dayjobs.append((data.gamedays + 2,"data.update = 'yes'"))
       data.dayjobs.append((data.gamedays + 2,'data.barackslevel += 1'))
       showinfo('Update','You must wait 2 Days')
       win.destroy()
       return 0
      
         
   def temple():
       if data.update == 'no':
           showinfo('Update','You can\'t Build this yet\nOther update in progress')
           win.destroy()
           return 0
       if data.templelevel > 0:
           showinfo('Update','You have alredy build this building')
           win.destroy()
           return 0


       if messagebox.askyesno('Update','This cost: 100 Gold and take 1 days\nContinue?') == False:
            win.destroy()
            return 0

       if data.gold < 100:
            showinfo('Update','You don\'t have the gold to update this building')
            win.destroy()
            return 0

       data.gold -= 100
       data.update = 'no'
       data.dayjobs.append((data.gamedays + 2,"data.update = 'yes'"))
       data.dayjobs.append((data.gamedays + 2,'data.templelevel += 1'))
       showinfo('Update','You must wait 2 Days')
       win.destroy()
       return 0

   def wall():
       if data.update == 'no':
           showinfo('Update','You can\'t Update this yet\nOther update in progress')
           win.destroy()
           return 0

       x = 200
       y = 1

       if data.walllevel != 0:
            x = data.walllevel * 400
            y = data.walllevel

       if messagebox.askyesno('Update','This cost: '+str(x)+' Gold and take '+str(y)+' days\nCurret Level: '+str(data.walllevel) +'\nContinue?') == False:
            win.destroy()
            return 0

       if data.gold < x:
            showinfo('Update','You don\'t have the gold to update this building')
            win.destroy()
            return 0

       data.gold -= x
       data.update = 'no'
       data.dayjobs.append((data.gamedays + y,"data.update = 'yes'"))
       data.dayjobs.append((data.gamedays + y,'data.walllevel += '+str(y)))
       showinfo('Update','You must wait '+str(y)+' Days')
       win.destroy()
       return 0

   def tavern():
       if data.update == 'no':
           showinfo('Update','You can\'t Update this yet\nOther update in progress')
           win.destroy()
           return 0

       if data.tavernlevel > 0:
           showinfo('Update','You have alredy build this building')
           win.destroy()
           return 0

       if messagebox.askyesno('Update','This cost 100 gold, 40 wood and 1 Day\nDo you wan\'t to continue?') == False:
          win.destroy()
          return 0

       if data.gold < 100:
          showinfo('Update','You need more gold')
          win.destroy()
          return 0

       if data.wood < 40:
          showinfo('Update','You need more wood')
          win.destroy()
          return 0

       data.gold -= 100
       data.wood -= 40
       data.update = 'no'
       data.dayjobs.append((data.gamedays+1,"data.update='yes'"))
       data.dayjobs.append((data.gamedays+1,'data.tavernlevel +=1'))
       showinfo('Update','You must wait 1 Day')
       win.destroy()
       return 0


   frame = Frame(win,width=220,height=250,bg='black')
   frame.pack()

   Label(frame,text='This is the hall of your town\nHere you can create new buildings\nAnd update your town',bg = 'black',fg = 'red').place(x=30,y=2)
   Button(frame,text='Update',bg='black',fg='red',width=6,command=update).place(x=5,y=75)
   Label(frame,text='--> ' + str(data.halllevel) + ' Day(s) Cost: ' + str(data.halllevel * 300) + ' Gold\nCurret Level: '+str(data.halllevel),bg='black',fg='red').place(x=70,y=75)
   Label(frame,text='Create Buildings',bg='black',fg='red').place(x=70,y=110)
   Button(frame,text='Smithy',bg='black',fg='red',width=6,command=smithy).place(x=5,y=140)
   Button(frame,text='Barracks',bg='black',fg='red',width=9,command=baracks).place(x=80,y=140)
   Button(frame,text='Hospital',bg='black',fg='red',width=6,command=buildhospital).place(x=165,y=140)
   Button(frame,text='Temple',bg='black',fg='red',width=6,command=temple).place(x=5,y=180)
   Button(frame,text='Update Wall',bg='black',fg='red',width=9,command=wall).place(x=80,y=180)
   Button(frame,text='Tavern',bg='black',fg='red',width=6,command=tavern).place(x=165,y=180)
   Button(frame,text='Back',bg='black',fg='red',width=33,command=win.destroy).place(x=5,y=220)
   win.mainloop()

def baracks():
   win = Toplevel()
   win.title('Hall')
   win.focus_set()
   try:
     win.grab_set()
   except TclError:
     pass

   def update():
    if data.barackslevel >= data.halllevel:
       showinfo('Update','You must update your hall first')
       win.destroy()
       return 0

    if data.update == 'no':
     showinfo('Update','You can\'t Update this yet\nOther update in progress')
     win.destroy()
     return 0

    if data.gold < data.halllevel * 250:
     showinfo('Update','You don\'t have the gold to update this building')
     win.destroy()
     return 0
    

    data.gold -= data.halllevel * 250
    data.update = 'no'
    data.dayjobs.append((data.gamedays + (data.barackslevel * 2),"data.update = 'yes'"))
    data.dayjobs.append((data.gamedays + (data.barackslevel * 2),'data.barackslevel += 1'))
    data.dayjobs.append((data.gamedays + (data.barackslevel * 2),'data.maxarmy += 10'))
    showinfo('Update','You must wait '+str(data.barackslevel * 2) + ' Days')
    win.destroy()
    return 0

   frame = Frame(win,width=250,height=200,bg='black')
   frame.pack()

   Label(frame,text='Baracks Here you can Create army',bg='black',fg='red').place(x=15,y=2)
   Button(frame,text='Update',bg='black',fg='red',width=5,command=update).place(x=5,y=40)
   Label(frame,text='--> Day(s): '+str(data.halllevel * 2) + ' Cost: '+str(data.halllevel * 250)+' Gold\nCurret Level: '+str(data.halllevel),bg='black',fg='red').place(x=80,y=40)

   def recruit(army):
     if messagebox.askyesno('Baracks','This cost: '+str(army * 5)+' Gold\nDo you wan\'t to Continue?') == False:
        win.destroy()
        return 0

     if data.gold < army * 5:
        showinfo('Baracks','You don\'t have the gold')
        win.destroy()
        return 0
     
     data.gold -= army * 5
     data.army += army
     showinfo('Baracks','You have succesfully recruit the soldier\'s')
     win.destroy()
     return 0


   if data.army >= data.maxarmy:
       Label(frame,text='You can\'t recruit more soldier\'s\nMaximun Reached',fg='red',bg='black').place(x=15,y=120)
   else:
       rec =  IntVar()
       Label(frame,text='Recruit New Army',bg='black',fg='red').place(x=80,y=90)
       Scale(frame,orient='horizontal',variable=rec,from_=0,to=data.maxarmy - data.army,width=10,bg='black',fg='red',length=240).place(x=5,y=120)
       Button(frame,text='Recruit',bg='black',fg='red',width=5,command = lambda:recruit(rec.get())).place(x=5,y=165)


   Button(frame,text='Back',fg='red',bg='black',command=win.destroy,width=5).place(x=180,y=165)
   win.mainloop()

def smithy():
    win = Toplevel()
    win.title('Smithy')
    win.focus_set()

    try:
      win.grab_set()
    except TclError:
      pass

    def update():
      if data.smithylevel >= data.halllevel:
         showinfo('Update','You must update your hall first')
         win.destroy()
         return 0
      if data.gold <  data.smithylevel * 100:
         showinfo('Update','You need more gold')
         win.destroy()
         return 0
      if data.update == 'no':
         showinfo('Update','You can\'t Update this yet\nOther update in progress')
         win.destroy()
         return 0

      data.gold -= data.smithylevel * 100
      data.update = 'no'
      data.dayjobs.append((data.gamedays + data.smithylevel,"data.update = 'yes'"))
      data.dayjobs.append((data.gamedays + data.smithylevel,'data.smithylevel += 1'))
      showinfo('Update','You must wait '+ str(data.smithylevel) + ' Days')
      win.destroy()
      return 0

    def updatestr():
        if data.armyupdate[0] >= data.smithylevel:
           showinfo('Update','You must update your smithy first')
           win.destroy()
           return 0

        cost = data.armyupdate[0] * 500
        if data.armyupdate[0] == 0:
           cost = 500
        
        if data.gold < cost:
           showinfo('Update','You need more gold')
           win.destroy()
           return 0
        
        data.gold -= cost
        data.armyupdate[0] += 1
        data.armystengthmin += 1
        data.armystrengthmax += 1
        showinfo('Update','You have update your army weapons')
        win.destroy()
        return 0
          
    
    def updatehealth():
        if data.armyupdate[1] >= data.smithylevel:
           showinfo('Update','You must update your smithy first')
           win.destroy()
           return 0 

        cost = data.armyupdate[1] * 1000

        if data.armyupdate[1] == 0:
           cost = 1000

        if data.gold < cost:
           showinfo('Update','You need more gold')
           win.destroy()
           return 0


        data.gold -= cost
        data.armyupdate[1] += 1
        data.armyhealth += 5
        showinfo('Update','You have update your army armor')
        win.destroy()

    frame = Frame(win,width=250,height=200,bg='black')
    frame.pack()

    Label(frame,text='Here you can update your army equipment',bg='black',fg='red').place(x=1,y=3)
    Button(frame,text = 'Update Weapon',bg='black',fg='red',width=12,command=updatestr).place(x=1,y=40)
    Label(frame,text='Curret Level: '+str(data.armyupdate[0])+'\nDamage: '+str(data.armystengthmin) +'-'+str(data.armystrengthmax),bg='black',fg='red').place(x=110,y=40)
    Button(frame,text = 'Update Armor',bg='black',fg='red',width=12,command=updatehealth).place(x=1,y=80)
    Label(frame,text='Curret Level: '+str(data.armyupdate[1])+'\nHealth: '+str(data.armyhealth),bg='black',fg='red').place(x=110,y=80)
    Button(frame,text = 'Update Building',bg='black',fg='red',width=12,command=update).place(x=1,y=120)
    Label(frame,text='Curret Level: '+str(data.smithylevel) +'\nCost: ' +str(data.smithylevel * 100)+' Gold \nAnd ' +str(data.smithylevel) +' Days',bg='black',fg='red').place(x=110,y=120)
    Button(frame,text='Back',bg='black',fg='red',width=12,command=win.destroy).place(x=1,y=160)


    win.mainloop()

def hospital():
    win = Toplevel()
    win.title('Hospital')
    win.focus_set()

    try:
      win.grab_set()
    except TclError:
      pass

    def update():
      if data.update == 'no':
        showinfo('Update','You can\'t Update this yet\nOther update in progress')
        win.destroy()
        return 0
      

      if data.gold < data.hospitallevel * 500:
         showinfo('Update','You need more Gold')
         win.destroy()
         return 0

      if data.wood < data.hospitallevel * 100:
         showinfo('Update','You need more wood')
         win.destroy()
         return 0

      if data.hospitallevel >= data.halllevel:
         showinfo('Update','You must update your hall first')
         win.destroy()
         return 0

      if data.hospitallevel == 10:
         showinfo('Update','You can\'t update this building is alredy on maximun level')
         win.destroy()
         return 0

      data.gold -= data.hospitallevel * 500
      data.wood -= data.hospitallevel * 100
      data.update = 'no'
      data.dayjobs.append((data.gamedays + (data.hospitallevel * 2),"data.update = 'yes'"))
      data.dayjobs.append((data.gamedays + (data.hospitallevel * 2),'data.hospitallevel += 1'))
      data.dayjobs.append((data.gamedays + (data.hospitallevel * 2),'data.killescape += 10'))
      showinfo('Update','You must wait ' + str(data.hospitallevel * 2) + ' Days')
      win.destroy()
      return 0

    frame = Frame(win,width=200,height=250,bg='black')
    frame.pack()

    Label(frame,text='This buildings reduces the chances\nTo get killed your soldiers in battle',bg='black',fg='red').place(x=5,y=3)
    Button(frame,text='Update',bg='black',fg='red',width=30,command=update).place(x=5,y=60)
    Label(frame,text='Curret Level: '+str(data.hospitallevel)+' Cost: '+str(data.hospitallevel * 500)+' Gold\nand '+str(data.hospitallevel * 100) + ' Wood\nNeed: '+str(data.hospitallevel * 2)+' Days',bg='black',fg='red').place(x=30,y=100)

    Label(frame,text= str(data.killescape)+'% Chances to save a soldier',bg='black',fg='red').place(x=30,y=160)
    Button(frame,text='Back',fg='red',bg='black',width=30,command=win.destroy).place(x=5,y=200)
    win.mainloop()

def temple():
    win = Toplevel()
    win.title('Temple')
    win.focus_set()

    try:
      win.grab_set()
    except TclError:
      pass

    def update():
       if data.templelevel >= data.halllevel:
           showinfo('Update','You must update your hall first')
           win.destroy()
           return 0
       if data.gold < data.templelevel * 100:
           showinfo('Update','You need more gold')
           win.destroy()
           return 0
       if data.wood < data.templelevel * 100:
           showinfo('Update','You need more wood')
           win.destroy()
           return 0

       if data.update == 'no':
          showinfo('Update','You can\'t Update this yet\nOther update in progress')
          win.destroy()
          return 0

       data.gold -= data.templelevel * 100
       data.wood -= data.templelevel * 100
       data.update = 'no'
       data.dayjobs.append((data.gamedays + data.templelevel,"data.update = 'yes'"))
       data.dayjobs.append((data.gamedays + data.templelevel,'data.templelevel += 1'))
       showinfo('Update','You must wait ' + str(data.templelevel)+' Days')
       win.destroy()
       return 0

    frame = Frame(win,bg='black',width=250,height=250)
    frame.pack()

    Label(frame,text='Here you can offer gifts to the god\'s\nand win their blessing',bg='black',fg='red').place(x=40,y=3)
    Button(frame,text='update',bg='black',fg='red',width=6,command=update).place(x=5,y=45)
    Label(frame,bg='black',fg='red',text='need: '+str(data.templelevel * 100)+' Gold, '+str(data.templelevel * 100)+' Wood\n'+str(data.templelevel)+' Day(s) Curret Level: '+str(data.templelevel)).place(x=70,y=40)

    offer = StringVar()
    offer.set('1')
    value = IntVar()

    bar = Scale(frame,bg='black',fg='red',from_=0,to=data.gold,length=230,orient='horizontal',variable=value)
    bar.place(x=5,y=110)

    def set(x):  
      value.set(0)
      print(value.get())
      if x == '1':
        bar.config(to=data.gold)
      elif x == '2':
        bar.config(to=data.wood)
      elif x == '3':
        bar.config(to=data.food)

    def donate():
      x1 = offer.get()
      x2 = value.get()
      if x2 == 0:
        showinfo('Offer','Please choose how many of this item you wan\'t to donate')
        win.destroy()
        return 0
 
      msg = ''
      x3 = random.randint(1,x2 + (data.templelevel * 10))
 

      if x1 == '1':
        data.gold -= x2
        if data.army < data.maxarmy:
           x4 = random.randint(1,3)
        else:
           x4 = random.randint(1,2)
      
        if x4 == 1:
          data.wood += x3
          msg = 'The Gods give you ' + str(x3)+' Wood'
        elif x4 == 2:
          data.food += x3
          msg = 'The Gods give you ' + str(x3)+' Food'
        elif x4 == 3:
         if data.army + x3 >= data.maxarmy:
            msg = 'The Gods give you ' + str(data.maxarmy - data.army)+ ' Soldiers'
            data.army = data.maxarmy
         else:
            data.army += x3
            msg = 'The Gods give you ' + str(x3) + ' Soldiers'

      if x1 == '2':
        data.wood -= x2
        if data.army < data.maxarmy:
           x4 = random.randint(1,3)
        else:
           x4 = random.randint(1,2)
      
        if x4 == 1:
          data.gold += x3
          msg = 'The Gods give you ' + str(x3)+' Gold'
        elif x4 == 2:
          data.food += x3
          msg = 'The Gods give you ' + str(x3)+' Food'
        elif x4 == 3:
         if data.army + x3 >= data.maxarmy:
            msg = 'The Gods give you ' + str(data.maxarmy - data.army)+ ' Soldiers'
            data.army = data.maxarmy
         else:
            data.army += x3
            msg = 'The Gods give you ' + str(x3) + ' Soldiers'

      if x1 == '3':
        data.food -= x2
        if data.army < data.maxarmy:
           x4 = random.randint(1,3)
        else:
           x4 = random.randint(1,2)
      
        if x4 == 1:
          data.gold += x3
          msg = 'The Gods give you ' + str(x3)+' Gold'
        elif x4 == 2:
          data.wood += x3
          msg = 'The Gods give you ' + str(x3)+' Wood'
        elif x4 == 3:
         if data.army + x3 >= data.maxarmy:
            msg = 'The Gods give you ' + str(data.maxarmy - data.army)+ ' Soldiers'
            data.army = data.maxarmy
         else:
            data.army += x3
            msg = 'The Gods give you ' + str(x3) + ' Soldiers'

      showinfo('Dontate',msg)
      win.destroy()
      return 0



    Radiobutton(frame,text='Gold',bg='black',fg='red',variable=offer,value=1,width=5,command=lambda:set(offer.get())).place(x=5,y=80)
    Radiobutton(frame,text='Wood',bg='black',fg='red',variable=offer,value=2,width=5,command=lambda:set(offer.get())).place(x=80,y=80)
    Radiobutton(frame,text='Food',bg='black',fg='red',variable=offer,value=3,width=5,command=lambda:set(offer.get())).place(x=160,y=80)
    

    Button(frame,text='Donate',width=38,bg='black',fg='red',command=donate).place(x=5,y=160)
    Button(frame,text='Back',width=38,bg='black',fg='red',command=win.destroy).place(x=5,y=200)

    win.mainloop()

def wall():
    win = Toplevel()
    win.title('Wall')
    win.focus_set()

    try:
      win.grab_set()
    except TclError:
      pass

    def update():
       if data.update == 'no':
          showinfo('Update','You can\'t Update this yet\nOther update in progress')
          win.destroy()
          return 0
       if data.gold < data.walllevel * 600:
          showinfo('Update','You need more gold')
          win.destroy()
          return 0

       if data.wood < data.walllevel * 300:
          showinfo('Update','You need more wood')
          win.destroy()
          return 0
       
       data.gold -= data.walllevel * 600
       data.wood -= data.walllevel * 300
       data.update = 'no'
       data.dayjobs.append((data.gamedays+(data.walllevel*2),"data.update = 'yes'"))
       data.dayjobs.append((data.gamedays+(data.walllevel*2),'data.walllevel +=1'))
       showinfo('Update','You must wait '+str(data.walllevel * 2)+' Days')
       win.destroy()
       return 0

    frame = Frame(win,bg='black',width=200,height=200)
    frame.pack()

    Label(frame,text='Walls The wall protect your\ntown from incoming attacks',bg='black',fg='red').place(x=30,y=3)
    Button(frame,text='Update',bg='black',fg='red',width=30,command=update).place(x=2,y=40)
    Label(frame,text='Curret Level: '+str(data.walllevel)+' Curret Defence: '+str((data.walllevel*10)-5)+'-'+str((data.walllevel*10)+5)+'\nNeeds for update:\n'+str(data.walllevel * 600)+' Gold '+str(data.walllevel * 300)+' Wood\nAnd '+str(data.walllevel*2)+' Day(s)',bg='black',fg='red').place(x=5,y=80)
    Button(frame,text='Back',width=30,bg='black',fg='red',command=win.destroy).place(x=2,y=160)
    win.mainloop()

def farm():
    win = Toplevel()
    win.title('Farms')
    win.focus_set()

    try:
      win.grab_set()
    except TclError:
      pass

    def update():
       if data.gold < 100:
         showinfo('Update','You need more gold')
         win.destroy()
         return 0

       if data.wood < 20:
         showinfo('Update','You need more wood')
         win.destroy()
         return 0

       if data.update == 'no':
          showinfo('Update','You can\'t Update this yet\nOther update in progress')
          win.destroy()
          return 0 

       data.update ='no'
       data.gold -= 100
       data.wood -= 20
       data.dayjobs.append((data.gamedays + 1,"data.update = 'yes'"))
       data.dayjobs.append((data.gamedays + 1,'data.farms +=1'))
       showinfo('Update','You must wait 1 Day')
       win.destroy()
       return 0

    frame = Frame(win,width=220,height=180,bg='black')
    frame.pack()

    Label(frame,text='The Farms gives you some food per day\nYou need the food\nto keep your army strenght',bg='black',fg='red').place(x=1,y=2)

    Button(frame,text='Build a Farm',bg='black',fg='red',width=33,command=update).place(x=5,y=60)
    Label(frame,text='Cost: 100 gold, 20 wood and 1 Day',bg='black',fg='red').place(x=20,y=100)
    Label(frame,text='Curret Farms: '+str(data.farms)+' incoming food per day: '+str(data.farms*5),bg='black',fg='red').place(x=5,y=120)
    Button(frame,text='Back',bg='black',fg='red',command=win.destroy,width=33).place(x=5,y=140)


    win.mainloop()

def mine():
    win = Toplevel()
    win.title('Mine')
    win.focus_set()

    try:
      win.grab_set()
    except TclError:
      pass

    def update():
     if data.gold < 50:
       showinfo('Update','You need more Gold')
       win.destroy()
       return 0

     if data.wood < 100:
       showinfo('Update','You need more wood')
       win.destroy()
       return 0

     if data.update == 'no':
          showinfo('Update','You can\'t Update this yet\nOther update in progress')
          win.destroy()
          return 0

     data.update = 'no'
     data.gold -= 50
     data.wood -= 100
     data.dayjobs.append((data.gamedays + 1,"data.update='yes'"))
     data.dayjobs.append((data.gamedays + 1,'data.minelevel +=1'))
     showinfo('Update','You must wait 1 Day')
     win.destroy()
     return 0
   
    frame = Frame(win,bg='black',width=200,height=160)
    frame.pack()

    Label(frame,text='The Mine gives you some gold per day\nYou need the gold to update your town',bg='black',fg='red').place(x=5,y=3)
    Button(frame,text='Update',bg='black',fg='red',width=30,command=update).place(x=5,y=40)
    Label(frame,text='Cost: 50 Gold, 100 Wood and 1 Day',bg='black',fg='red').place(x=20,y=80)
    Label(frame,text='Curret Level: '+str(data.minelevel)+' Gold per day: '+str(data.minelevel * 25),bg='black',fg='red').place(x=20,y=100)
    Button(frame,text='Back',fg='red',bg='black',width=30,command=win.destroy).place(x=5,y=120)



    win.mainloop()

def forester():
    win = Toplevel()
    win.title('Forester')
    win.focus_set()

    try:
      win.grab_set()
    except TclError:
      pass

    def update():
     if data.gold < 100:
       showinfo('Update','You need more Gold')
       win.destroy()
       return 0

     if data.wood < 10:
       showinfo('Update','You need more wood')
       win.destroy()
       return 0

     if data.update == 'no':
          showinfo('Update','You can\'t Update this yet\nOther update in progress')
          win.destroy()
          return 0

     data.update = 'no'
     data.gold -= 100
     data.wood -= 20
     data.dayjobs.append((data.gamedays + 1,"data.update='yes'"))
     data.dayjobs.append((data.gamedays + 1,'data.foresterlevel +=1'))
     showinfo('Update','You must wait 1 Day')
     win.destroy()
     return 0
   
    frame = Frame(win,bg='black',width=220,height=160)
    frame.pack()

    Label(frame,text='The forester give you some wood per day\nyou can use it yo update your town',bg='black',fg='red').place(x=2,y=3)
    Button(frame,text='Update',bg='black',fg='red',width=33,command=update).place(x=5,y=40)
    Label(frame,text='Cost: 100 Gold, 10 Wood and 1 Day',bg='black',fg='red').place(x=20,y=80)
    Label(frame,text='Curret Level: '+str(data.foresterlevel)+' wood per day: '+str(data.foresterlevel*15),bg='black',fg='red').place(x=20,y=100)
    Button(frame,text='Back',fg='red',bg='black',width=33,command=win.destroy).place(x=5,y=120)



    win.mainloop()

def tavern():
    win = Toplevel()
    win.title('Tavern')
    win.focus_set()

    try:
      win.grab_set()
    except TclError:
      pass

    frame = Frame(win,bg='black',width=200,height=170)
    frame.pack()

    def offer():
       a = x.get()
       #print('X: %s'%a)
       #print('Type : %s'%type(a))
       try:
          a = int(a)
          data.gifts = a
          showinfo('Tavern',str(a)+' Gifts = '+str(a*5)+' Happynes per day')
          win.destroy()
          return 0
          
          
       except Exception:
          win.destroy()  
          return 0

    def check():
       a = x.get()
       try:
         a = int(a)
         ch.config(text=str(a) + ' Gifts = '+str(a*5)+' Happynes per day')
       except Exception:
          win.destroy()
          return 0
         

    Label(frame,text='Here you can give food\nas gift to your people\n to keep them happy',bg='black',fg='red').place(x=50,y=3)
    x = Entry(frame,width=3,bg='black',fg='red')
    x.place(x=5,y=65)
    x.insert(0,data.gifts)
    Button(frame,text='Offer',bg='black',fg='red',width=8,command=offer).place(x=40,y=60)
    Button(frame,text='Check Happynes',bg='black',fg='red',width=13,command=check).place(x=100,y=60)
    ch = Label(frame,text=str(data.gifts) +' Gifts = '+str(data.gifts * 5)+' Happynes per day',bg='black',fg='red')
    ch.place(x=10,y=100)
    Button(frame,text='Back',fg='red',bg='black',width=30,command=win.destroy).place(x=5,y=130)

    win.mainloop()

