import tkinter as tk
from tkinter import *
from tkinter import ttk
import random







class Gui():
        
        def __init__(self, root):
                global ship_list
                ship_list=['ship1-lenght4']
                #ship_list=['ship1-lenght4','ship1-lenght3','ship2-lenght3','ship1-lenght2','ship2-lenght2','ship3-lenght2']
                global ship_list2
                ship_list2=['ship1-lenght4','ship1-lenght3','ship2-lenght3','ship1-lenght2','ship2-lenght2','ship3-lenght2']
                global map_size
                map_size = 12
                global square_size
                square_size=25
                global li
                li={}
                global posibilyty
                posibilyty=[]
                global li2
                li2={}
                global posibilyty2
                posibilyty2=[]
                for x in range(map_size):
                        for y in range(map_size):
                                if x==0 or y==0 or y==11 or x==11:
                                        li[(x,y)]=0
                                        li2[(x,y)]=0
                                else:
                                    li[(x,y)]=1
                                    li2[(x,y)]=1
                                    posibilyty.append((x,y))
                                    posibilyty2.append((x,y))
                
                
                self.root=root
                self.entry = tk.Entry(root)
                stvar=tk.StringVar()
                stvar.set("one")

                self.canvas=tk.Canvas(root,
                            background='grey',
                            width=square_size * map_size,
                            height=square_size * map_size,
                            highlightthickness=0)
                self.canvas2=tk.Canvas(root,
                            background='grey',
                            width=square_size * map_size,
                            height=square_size * map_size,
                            highlightthickness=0)
                self.canvas.grid(row=0,column=1)
                self.canvas2.grid(row=0,column=4)

                frame = Frame(self.root)
                frame.grid(row=0,column=0, sticky="n")
                Button0=Button(frame,text="New Game",command=lambda:self.new_game(ship_list)).grid(row = 0,column = 1, sticky = "nw")
                
                label2=Label(frame, text="Coordinates").grid(row=1,column=0, sticky="w")
                entry = tk.Entry(frame)
                entry.grid(row = 1,column = 1)
                Button1=Button(frame,text="Shoot",command=lambda:self.shoot(entry.get())).grid(row = 3,column = 1, sticky = "we")
                
                for x in li:
                        color=['white','grey']
                    #tam gdzie jest wartosc tam koloruje na odpowiedni kolor
                    
                    #rysuje mape o okreslonej wielkości
                        x_square = x[0] * square_size
                        y_square = x[1] * square_size
                        figure1=self.canvas.create_rectangle(
                                y_square,
                                x_square,
                                y_square + square_size,
                                x_square + square_size,
                                fill=color[li[x]], outline='gray5')
                        figure2=self.canvas2.create_rectangle(
                                y_square,
                                x_square,
                                y_square + square_size,
                                x_square + square_size,
                                fill=color[li[x]], outline='gray5')
                global index
                index={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J'}
                global index_rev
                index_rev={'A':1,'a':1,'B':2,'b':2,'C':3,'c':3,'D':4,'d':4,'E':5,'e':5,'F':6,'f':6,'G':7,'g':7,'H':8,'h':8,'I':9,'i':9,'J':10,'j':10}

                for x in index:
                        self.move=(x*square_size)+(square_size/2)
                        self.canvas.create_text(self.move, (square_size/2), text=index[x], fill="black")
                        self.canvas.create_text((square_size/2), self.move, text=x, fill="black")

                        self.canvas2.create_text(self.move, (square_size/2), text=index[x], fill="black")
                        self.canvas2.create_text((square_size/2), self.move, text=x, fill="black")
                
                
        def new_game(self,ship_list_now):
                window = tk.Toplevel()
                #ship selection butons
                label = ttk.Label(window,text="Please select a ship:")
                label.grid(row=0,column=0)
                current_var = tk.StringVar()
                current_value = current_var.get()
                combobox = tk.ttk.Combobox(window,textvariable=current_var,)
                combobox.grid(row=1,column=0)
                combobox['values'] = ship_list_now
                combobox['state'] = 'readonly'
                #ship coordination butons
                text = tk.StringVar()
                label2 = tk.Label( window, textvariable = text)
                label2.grid(row=2,column=0)
                description = tk.Label(window, text="Give ship start coordinates (xnum):").grid(row=3,column=0)
                name = tk.Entry(window,width=40)
                name.grid(row=4,column=0)
                #ship orientation butons
                description2 = tk.Label(window, text="Orientation for ship:").grid(row=5,column=0)
                var = IntVar()
                Radiobutton=tk.Radiobutton(window,text="upside-down",variable=var, value=0).grid(row=6,column=0)
                Radiobutton2=tk.Radiobutton(window,text="left-right",variable=var, value=1).grid(row=7,column=0)
                
                button_close = tk.Button(window, text="Add ship",command=lambda:[self.add_ship(combobox,name,var),window.destroy()])
                button_close.grid(row=8,column=0)
        def add_ship(self,what_ship,coord,orient):
                pos=6
                sh=what_ship.get()
                sh_len=sh[-1]
                sh_len=int(sh_len)
                cor=coord.get()
                cor_x=cor[0]
                cor_y=int(cor[-1])
                x_cor=index_rev[cor_x]
                actual_ship=[]
                for x in range(sh_len):
                        if orient.get()==0:
                                #li[(index_rev[cor_x],cor_y)]=2
                                actual_ship.append((int(index_rev[cor_x]),int(cor_y)))
                                cor_y+=1
                        else:
                                #li[(x_cor,cor_y)]=2
                                actual_ship.append((int(x_cor),int(cor_y)))
                                x_cor+=1
                window2 = tk.Toplevel()
                
                for x in actual_ship:
                        global posibilyty
                        if x in posibilyty:
                                correct=True
                        else:
                                correct=False
                                break

                if correct:
                

                        #adding to bord
                        for x in actual_ship:
                                li[x]=2
                                posibilyty=set(posibilyty)
                                posibilyty.discard(x)
                                posibilyty.discard((x[0]+1,x[1]))
                                posibilyty.discard((x[0]-1,x[1]))
                                posibilyty.discard((x[0],x[1]+1))
                                posibilyty.discard((x[0],x[1]-1))
                                posibilyty.discard((x[0]+1,x[1]+1))
                                posibilyty.discard((x[0]-1,x[1]-1))
                                posibilyty.discard((x[0]+1,x[1]-1))
                                posibilyty.discard((x[0]-1,x[1]+1))
                                posibilyty=list(posibilyty)
                        ship_list.remove(sh)        
                        for x in li:
                                color=['white','grey','green']
                                x_square = x[1] * square_size
                                y_square = x[0] * square_size
                                figure1=self.canvas.create_rectangle(
                                                y_square,
                                                x_square,
                                                y_square + square_size,
                                                x_square + square_size,
                                                fill=color[li[x]], outline='gray5')
                        for x in index:
                                self.move=(x*square_size)+(square_size/2)
                                self.canvas.create_text(self.move, (square_size/2), text=index[x], fill="black")
                                self.canvas.create_text((square_size/2), self.move, text=x, fill="black")

                        if len(ship_list)==0:
                                masage = tk.Label(window2, text="All ship added correctly start game").grid(row=0,column=0)
                                button = tk.Button(window2, text="Start Game",command=lambda:[self.start_game(),window2.destroy()])
                                button.grid(row=1,column=0)
                        else:
                                masage = tk.Label(window2, text="Ship added correctly add another ship").grid(row=0,column=0)
                                button = tk.Button(window2, text="Next ship",command=lambda:[self.new_game(ship_list),window2.destroy()])
                                button.grid(row=1,column=0)
                else:
                        masage = tk.Label(window2, text="Ship was added incorrectly, please try again").grid(row=0,column=0)
                        button = tk.Button(window2, text="try again",command=lambda:[self.new_game(ship_list),window2.destroy()])
                        button.grid(row=1,column=0)
                       
        def start_game(self):
                global ship_list2
                global posibilyty2
                orintation=int()
                start=()
                for x in ship_list2:
                        orintation=random.randint(0, 1)
                        chosen=True
                        while chosen:
                                start=random.choice(posibilyty2)
                                act_sh=[]
                                cor_y=start[1]
                                cor_x=start[0]
                                for y in range(int(x[-1])):
                                        if orintation==0:
                                                act_sh.append((cor_x,cor_y))
                                                cor_y+=1
                                        else:
                                                act_sh.append((cor_x,cor_y))
                                                cor_x+=1
                                for z in act_sh:
                                        if z in posibilyty2:
                                                correct=True
                                        else:
                                                correct=False
                                                break
                                if correct==True:
                                        chosen=False
                                        break
                                else:
                                        chosen=True
                                
                       
                        for z in act_sh:
                                li2[z]=2
                                posibilyty2=set(posibilyty2)
                                posibilyty2.discard(z)
                                posibilyty2.discard((z[0]+1,z[1]))
                                posibilyty2.discard((z[0]-1,z[1]))
                                posibilyty2.discard((z[0],z[1]+1))
                                posibilyty2.discard((z[0],z[1]-1))
                                posibilyty2.discard((z[0]+1,z[1]+1))
                                posibilyty2.discard((z[0]-1,z[1]-1))
                                posibilyty2.discard((z[0]+1,z[1]-1))
                                posibilyty2.discard((z[0]-1,z[1]+1))
                                posibilyty2=list(posibilyty2)
                                '''
                        for a in li2:
                                color=['white','grey','green']
                                x_square = a[1] * square_size
                                y_square = a[0] * square_size
                                figure2=self.canvas2.create_rectangle(
                                                y_square,
                                                x_square,
                                                y_square + square_size,
                                                x_square + square_size,
                                                fill=color[li2[a]], outline='gray5')
                        for t in index:
                                self.move=(t*square_size)+(square_size/2)
                                self.canvas2.create_text(self.move, (square_size/2), text=index[t], fill="black")
                                self.canvas2.create_text((square_size/2), self.move, text=t, fill="black")
                                '''

        
                                
        def shoot(self,coordinates):
                print(coordinates)
                
if __name__== '__main__':
    root=tk.Tk()
    gui=Gui(root)
    root.mainloop()
