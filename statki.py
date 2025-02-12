import tkinter as tk
from tkinter import *
from tkinter import ttk
import random






class Gui():
        
        def __init__(self, root):
                global ship_list
                #ship_list=['ship1-length4']#,'ship1-length3']
                ship_list=['ship1-length4','ship1-length3','ship2-length3','ship1-length2','ship2-length2','ship3-length2']
                global ship_list2
                ship_list2=['ship1-length4','ship1-length3','ship2-length3','ship1-length2','ship2-length2','ship3-length2']
                global map_size
                map_size = 12
                global square_size
                square_size=25
                global li
                li={}
                global  possibility
                possibility=[]
                global li2
                li2={}
                global possibility2
                possibility2=[]
                global all_map_enemy
                all_map_enemy=[]
                global hitted
                hitted=False
                global shoot_first
                shoot_first=0
                global my_shp
                my_shp=[]
                global hit_list
                hit_list=[]
                global hit_iter
                hit_iter=0
                global last_hit
                last_hit=0
                global broken
                broken=[]
                global point
                point=()
                for x in range(map_size):
                        for y in range(map_size):
                                if x==0 or y==0 or y==11 or x==11:
                                        li[(x,y)]=0
                                        li2[(x,y)]=0
                                else:
                                    li[(x,y)]=1
                                    li2[(x,y)]=1
                                    possibility.append((x,y))
                                    possibility2.append((x,y))
                                    all_map_enemy.append((x,y))
                                    
                                    
                
                
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
                
                label2=Label(frame, text="Coordinates(xnum)").grid(row=1,column=0, sticky="w")
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
                
                window2 = tk.Toplevel()        
                pos=6
                sh=what_ship.get()
                sh_len=sh[-1]
                sh_len=int(sh_len)
                cor=coord.get()
                cor_x=cor[0]
                cor_y=int(cor[1:])
                if len(coord.get())>3:
                        masage = tk.Label(window2, text="You give wrong coordinates, please try again").grid(row=0,column=0)
                        button = tk.Button(window2, text="try again",command=lambda:[self.new_game(ship_list),window2.destroy()])
                        button.grid(row=1,column=0)

                if not type(cor[1:]) is int:
                        masage = tk.Label(window2, text="You give wrong coordinates, please try again").grid(row=0,column=0)
                        button = tk.Button(window2, text="try again",command=lambda:[self.new_game(ship_list),window2.destroy()])
                        button.grid(row=1,column=0)
                
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
                
                for x in actual_ship:
                        global possibility
                        if x in possibility:
                                correct=True
                        else:
                                correct=False
                                break

                if correct:
                

                        #adding to bord
                        for x in actual_ship:
                                li[x]=2
                                possibility=set(possibility)
                                possibility.discard(x)
                                possibility.discard((x[0]+1,x[1]))
                                possibility.discard((x[0]-1,x[1]))
                                possibility.discard((x[0],x[1]+1))
                                possibility.discard((x[0],x[1]-1))
                                possibility.discard((x[0]+1,x[1]+1))
                                possibility.discard((x[0]-1,x[1]-1))
                                possibility.discard((x[0]+1,x[1]-1))
                                possibility.discard((x[0]-1,x[1]+1))
                                possibility=list(possibility)
                        ship_list.remove(sh)
                        my_shp.append(actual_ship)
                        
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
                global possibility2
                orintation=int()
                start=()
                global enemy_ships
                enemy_ships=[]
                #adding computer ships
                for x in ship_list2:
                        orintation=random.randint(0, 1)
                        chosen=True
                        while chosen:
                                start=random.choice(possibility2)
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
                                        if z in possibility2:
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
                                possibility2=set(possibility2)
                                possibility2.discard(z)
                                possibility2.discard((z[0]+1,z[1]))
                                possibility2.discard((z[0]-1,z[1]))
                                possibility2.discard((z[0],z[1]+1))
                                possibility2.discard((z[0],z[1]-1))
                                possibility2.discard((z[0]+1,z[1]+1))
                                possibility2.discard((z[0]-1,z[1]-1))
                                possibility2.discard((z[0]+1,z[1]-1))
                                possibility2.discard((z[0]-1,z[1]+1))
                                possibility2=list(possibility2)
                        enemy_ships.append(act_sh)
                        
                        '''
                        #fog of war turn of
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
                #shoting enemy ships and testing if its sunken 
                        
                cor_x=index_rev[coordinates[0]]
                cor_y=int(coordinates[1:])
                coord=(cor_x,cor_y)
                window2 = tk.Toplevel()
                hit=False
                global hited_cor
                hited_cor=[]

                for each_sh in enemy_ships:
                        if coord in each_sh:
                                if li2[coord]==2 and len(each_sh)==1:
                                        li2[coord]=3
                                        for a in li2:
                                                color=['white','grey','grey','red','blue']
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
                                                
                                        enemy_ships.remove(each_sh)
                                        if len(enemy_ships)==0:
                                                masage = tk.Label(window2, text="You Won, congratulations").grid(row=0,column=0)
                                                button = tk.Button(window2, text="End",command=lambda:[root.destroy()])
                                                button.grid(row=2,column=0)
                                        else:
                                                '''for x in hited_cor:
                                                        if li2[(x[0]+1,x[1])]!=3 and li2[(x[0]+1,x[1])]!=1:
                                                                li2[coord]=4
                                                        if li2[(x[0]-1,x[1])]!=3 and li2[(x[0]-1,x[1])]!=1:
                                                                li2[coord]=4
                                                        if li2[(x[0],x[1]+1)]!=3 and li2[(x[0],x[1]+1)]!=1:
                                                                li2[coord]=4
                                                        if li2[(x[0],x[1]-1)]!=3 and li2[(x[0],x[1]-1)]!=1:
                                                                li2[coord]=4
                                                        if li2[(x[0]+1,x[1]+1)]!=3 and li2[(x[0]+1,x[1]+1)]!=1:
                                                                li2[coord]=4
                                                        if li2[(x[0]-1,x[1]-1)]!=3 and li2[(x[0]-1,x[1]-1)]!=1:
                                                                li2[coord]=4
                                                        if li2[(x[0]+1,x[1]-1)]!=3 and li2[(x[0]+1,x[1]-1)]!=1:
                                                                li2[coord]=4
                                                        if li2[(x[0]-1,x[1]+1)]!=3 and li2[(x[0]-1,x[1]+1)]!=1:
                                                                li2[coord]=4
                                                for a in li2:
                                                        color=['white','grey','green','red','blue']
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
                                                masage = tk.Label(window2, text="Ship was hit ant sunken").grid(row=0,column=0)
                                                button = tk.Button(window2, text="Next turn",command=lambda:window2.destroy())
                                                button.grid(row=2,column=0)
                                                

                                elif li2[coord]==2 and len(each_sh)!=1:
                                        each_sh.remove(coord)
                                        hited_cor.append(coord)
                                        
                                        li2[coord]=3
                                        for a in li2:
                                                color=['white','grey','grey','red','blue']
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
                                        masage = tk.Label(window2, text="Ship was hit").grid(row=0,column=0)
                                        button = tk.Button(window2, text="Next turn",command=lambda:window2.destroy())
                                        button.grid(row=2,column=0)
                                hit=True
                                break

                        else:
                                pass
                                
                if hit==False:
                        if li2[coord]!=0:
                                li2[coord]=4
                        for a in li2:
                                                color=['white','grey','grey','red','blue']
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
                        masage = tk.Label(window2, text="Ship was missed").grid(row=0,column=0)
                        button = tk.Button(window2, text="Next turn",command=lambda:window2.destroy())
                        button.grid(row=2,column=0)
                if int(coordinates[1:])<1 or int(coordinates[1:])>10:
                        masage = tk.Label(window2, text="You give wrong coordinates and lost turn").grid(row=0,column=0)
                        button = tk.Button(window2, text="Next turn",command=lambda:[root.destroy()])
                        button.grid(row=2,column=0)
                global hitted
                global hit_list
                global hit_iter
                global shoot_first
                global last_hit
                global broken
                global point
                if hitted:
                        if hit_iter==0:
                                last_hit=shoot_first
                        else:
                                last_hit=point
                        point=random.choice(hit_list)
                        hit_list.remove(point)
                        all_map_enemy.remove(point)
                        if li[point]==2:
                                hit_iter+=1
                                broken.append(point)
                                li[point]=3
                                
                                if point[0] != last_hit[0] or point[1] != last_hit[1]:  
                                        if (point[0]+1, point[1] + 1) in hit_list:
                                                hit_list.remove((point[0]+1, point[1]+1))
                                        if (point[0]-1, point[1] - 1) in hit_list:
                                                hit_list.remove((point[0]-1, point[1]-1))
                                        if (point[0]+1, point[1] - 1) in hit_list:
                                                hit_list.remove((point[0]+1, point[1]-1))
                                        if (point[0]-1, point[1] + 1) in hit_list:
                                                hit_list.remove((point[0]-1, point[1]+1))
                                if point[0] != last_hit[0]:
                                        if (point[0]+1,point[1]) not in hit_list and (point[0]+1,point[1]) not in broken:
                                                hit_list.append((point[0]+1,point[1]))
                                        if (point[0]-1,point[1]) not in hit_list and (point[0]-1,point[1])not in broken:
                                                hit_list.append((point[0]-1,point[1]))
                                elif point[1] != last_hit[1]:
                                        if (point[0],point[1]+1) not in hit_list and (point[0],point[1]+1) not in broken:
                                                hit_list.append((point[0],point[1]+1))
                                        if (point[0],point[1]-1) not in hit_list and (point[0],point[1]-1) not in broken:
                                                hit_list.append((point[0],point[1]-1))
                                if point[0]==1 and (point[0] - 1, point[1]) in hit_list:
                                        hit_list.remove((point[0] - 1, point[1]))
                                if point[0]==10 and (point[0] + 1, point[1]) in hit_list:
                                        hit_list.remove((point[0] + 1, point[1]))
                                if point[1]==1 and (point[0] , point[1]-1) in hit_list:
                                        hit_list.remove((point[0] , point[1]-1))
                                if point[1]==10 and (point[0] , point[1]+1) in hit_list:
                                        hit_list.remove((point[0] , point[1]+1))
                                
                               
                                
                                
                                for ship_num in range(len(my_shp)):
                                                
                                                if point in my_shp[ship_num]:
                                                        ship=my_shp[ship_num]
                                                        ship.remove(point)
                                                        my_shp[ship_num]=ship
                                                        
                                                        if len(my_shp[ship_num])==0:
                                                                my_shp.remove(my_shp[ship_num])
                                                                if len(my_shp)==0:
                                                                        masage = tk.Label(window2, text="Enemy win the game").grid(row=1,column=0)
                                                                        button = tk.Button(window2, text="End",command=lambda:[root.destroy()])
                                                                        button.grid(row=2,column=0)
                                                                else:
                                                                        masage = tk.Label(window2, text="Enemy hit you and sunken ").grid(row=1,column=0)
                                                                        button = tk.Button(window2, text="Next turn",command=lambda:window2.destroy())
                                                                        button.grid(row=2,column=0)
                                                                hit_list=[]
                                                                hit_iter=0
                                                                hitted=False
                                                                for each in broken: 
                                                                        for ax,ay in [(-1, 0), (1, 0), (0, -1), (0, 1),(-1,-1),(1,1),(1,-1),(-1,1)]:
                                                                                if li[(each[0] + ax, each[1] + ay)]==1:
                                                                                        li[(each[0] + ax, each[1] + ay)]=4
                                                                                        all_map_enemy.remove((each[0] + ax, each[1] + ay))
                                                                break
                                                        else:
                                                
                                                                masage = tk.Label(window2, text="Enemy hit you").grid(row=1,column=0)
                                                                button = tk.Button(window2, text="Next turn",command=lambda:window2.destroy())
                                                                button.grid(row=2,column=0)
                                                                break
                                for a in li:
                                        color=['white','grey','green','red','blue']
                                        x_square = a[1] * square_size
                                        y_square = a[0] * square_size
                                        figure=self.canvas.create_rectangle(
                                                                y_square,
                                                                x_square,
                                                                y_square + square_size,
                                                                x_square + square_size,
                                                                fill=color[li[a]], outline='gray5')
                                for t in index:
                                        self.move=(t*square_size)+(square_size/2)
                                        self.canvas.create_text(self.move, (square_size/2), text=index[t], fill="black")
                                        self.canvas.create_text((square_size/2), self.move, text=t, fill="black")
                        else:
                                                                        
                                li[point]=4
                                if point in hit_list:
                                        hit_list.remove(point)
                        
                                for a in li:
                                        color=['white','grey','green','red','blue']
                                        x_square = a[1] * square_size
                                        y_square = a[0] * square_size
                                        figure=self.canvas.create_rectangle(
                                                                y_square,
                                                                x_square,
                                                                y_square + square_size,
                                                                x_square + square_size,
                                                                fill=color[li[a]], outline='gray5')
                                for t in index:
                                        self.move=(t*square_size)+(square_size/2)
                                        self.canvas.create_text(self.move, (square_size/2), text=index[t], fill="black")
                                        self.canvas.create_text((square_size/2), self.move, text=t, fill="black")
                                masage = tk.Label(window2, text="Enemy missed you").grid(row=1,column=0)
                                button = tk.Button(window2, text="Next turn",command=lambda:window2.destroy())
                                button.grid(row=2,column=0)      
                else:
                        
                        shoot_first=random.choice(all_map_enemy)
                        all_map_enemy.remove(shoot_first)
                        if li[shoot_first]==2:
                        
                                hitted=True
                                hit_iter=0
                                broken.append(shoot_first)
                                neighbors = [(shoot_first[0] + dx, shoot_first[1] + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
                                hit_list=[n for n in neighbors if 0 < n[0] < 11 and 0 < n[1] < 11]
                                li[shoot_first]=3
                                for ship_num in range(len(my_shp)):
                                        if shoot_first in my_shp[ship_num]:
                                                        ship=my_shp[ship_num]
                                                        ship.remove(shoot_first)
                                                        my_shp[ship_num]=ship
                                                        break
                                for a in li:
                                                color=['white','grey','green','red','blue']
                                                x_square = a[1] * square_size
                                                y_square = a[0] * square_size
                                                figure=self.canvas.create_rectangle(
                                                                        y_square,
                                                                        x_square,
                                                                        y_square + square_size,
                                                                        x_square + square_size,
                                                                        fill=color[li[a]], outline='gray5')
                                for t in index:
                                                self.move=(t*square_size)+(square_size/2)
                                                self.canvas.create_text(self.move, (square_size/2), text=index[t], fill="black")
                                                self.canvas.create_text((square_size/2), self.move, text=t, fill="black")

                                masage = tk.Label(window2, text="Enemy hit you").grid(row=1,column=0)
                                button = tk.Button(window2, text="Next turn",command=lambda:window2.destroy())
                                button.grid(row=2,column=0)
                        else:
                                hitted=False
                                li[shoot_first]=4
                                for a in li:
                                                color=['white','grey','green','red','blue']
                                                x_square = a[1] * square_size
                                                y_square = a[0] * square_size
                                                figure=self.canvas.create_rectangle(
                                                                        y_square,
                                                                        x_square,
                                                                        y_square + square_size,
                                                                        x_square + square_size,
                                                                        fill=color[li[a]], outline='gray5')
                                for t in index:
                                                self.move=(t*square_size)+(square_size/2)
                                                self.canvas.create_text(self.move, (square_size/2), text=index[t], fill="black")
                                                self.canvas.create_text((square_size/2), self.move, text=t, fill="black") 
                                masage = tk.Label(window2, text="Enemy missed you").grid(row=1,column=0)
                                button = tk.Button(window2, text="Next turn",command=lambda:window2.destroy())
                                button.grid(row=2,column=0)
                                

if __name__== '__main__':
    root=tk.Tk()
    gui=Gui(root)
    root.mainloop()
