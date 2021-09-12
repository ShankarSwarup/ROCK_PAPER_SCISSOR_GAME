from tkinter import * 
from tkinter import ttk
import random

def name_to_number(string):
        if string=="rock":
            return 0
        elif string=="spock":
            return 1
        elif string=="paper":
            return 2
        elif string=="lizard":
            return 3
        elif string=="scissors":
            return 4
        else:
            return "out of choice"

def name_to_number(string):
        if string=="rock":
            return 0
        elif string=="spock":
            return 1
        elif string=="paper":
            return 2
        elif string=="lizard":
            return 3
        elif string=="scissors":
            return 4
        else:
            return "out of choice"
            
def number_to_name(st):
        if st==0:
            return "rock"
        elif st==1:
            return "spock"
        elif st==2:
            return "paper"
        elif st==3:
            return "lizard"
        elif st==4:
            return "scissors"
        else:
            return "out of choice"
     
def rpsls(player_choice): 
    
    print(" ")
    

    print("Player chooses"+" "+str(player_choice))

    a=name_to_number(player_choice)

    comp_number=random.randrange(0,5)
    
    comp_choice=number_to_name(comp_number)

    print("Computer chooses"+" "+str(comp_choice))
    
    if a==comp_number:
        return -1
    elif comp_number==(a-1)%5 or comp_number==(a-2)%5:
        return 1
    else:
        return 0

class game:
     def __init__(self,root):
        self.root=root      
        self.root.title("ROCK PAPER SCISSOR LIZARD SPOCK")
        self.root.geometry("500x420+300+50")
        self.root.resizable(False,False)
        self.root.config(bg='white')

        title=Label(self.root,text='ROCK PAPER SCISSOR LIZARD SPOCK',font=("algerian",10),bg="#262626",fg='white').pack(side=TOP,fill=X)

        lbl_game=Label(self.root,text='Select One Option:',font=("times new roman",15),bg='white').place(x=10,y=50)
        
        self.choice=StringVar()
        btn_rock=Button(self.root,text='Rock',command=self.rock,font=('times new roman',13),bg='red',fg='white').place(x=30,y=100,width=70,height=70)
        btn_paper=Button(self.root,text='Paper',command=self.paper,font=('times new roman',13),bg='violet',fg='white').place(x=120,y=100,width=70,height=70)
        btn_scissor=Button(self.root,text='Scissor',command=self.scissor,font=('times new roman',13),bg='grey',fg='white').place(x=210,y=100,width=70,height=70)
        btn_lizard=Button(self.root,text='Lizard',command=self.lizard,font=('times new roman',13),bg='blue',fg='white').place(x=300,y=100,width=70,height=70)
        btn_spock=Button(self.root,text='Spock',command=self.spock,font=('times new roman',13),bg='green',fg='white').place(x=400,y=100,width=70,height=70)

        lbl_result=Label(self.root,text='Result:',font=("times new roman",15),bg='white').place(x=10,y=180)
        frame_=Frame(self.root,bd=2,relief=RIDGE,bg='#d9fcff')
        frame_.place(x=10,y=220,width=470,height=180)

        self.lbl_res=Label(frame_,text='',font=("times new roman",18),bg="#d9fcff")
        self.lbl_res.place(x=0,y=0)
     
     def rock(self):
         sting="rock"
         val=rpsls(sting)
         if val==0:
             self.lbl_res.config(text=f'Computer Wins!!')
         elif val==1:
             self.lbl_res.config(text=f'Player Wins!!')
         else:
             self.lbl_res.config(text=f'Player And Computer Tie!!')

     def paper(self):
         sting="paper"
         val=rpsls(sting)
         if val==0:
             self.lbl_res.config(text=f'Computer Wins!!')
         elif val==1:
             self.lbl_res.config(text=f'Player Wins!!')
         else:
             self.lbl_res.config(text=f'Player And Computer Tie!!')
     def scissor(self):
         sting="scissors"
         val=rpsls(sting)
         if val==0:
             self.lbl_res.config(text=f'Computer Wins!!')
         elif val==1:
             self.lbl_res.config(text=f'Player Wins!!')
         else:
             self.lbl_res.config(text=f'Player And Computer Tie!!')
     def lizard(self):
         sting="lizard"
         val=rpsls(sting)
         if val==0:
             self.lbl_res.config(text=f'Computer Wins!!')
         elif val==1:
             self.lbl_res.config(text=f'Player Wins!!')
         else:
             self.lbl_res.config(text=f'Player And Computer Tie!!')
     def spock(self):
         sting="spock"
         val=rpsls(sting)
         if val==0:
             self.lbl_res.config(text=f'Computer Wins!!')
         elif val==1:
             self.lbl_res.config(text=f'Player Wins!!')
         else:
             self.lbl_res.config(text=f'Player And Computer Tie!!')


root=Tk()
obj=game(root)
root.mainloop()


    


