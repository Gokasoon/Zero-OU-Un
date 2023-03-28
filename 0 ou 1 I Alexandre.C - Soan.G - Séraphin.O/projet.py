# GVOKA Soan    OUTREBON Seraphin   CHARPENTIER Alexandre       


####################################################modules
from tkinter import * 
import time, os


####################################################VARIABLES
offset=170
offset2=50

img_active=[]

i_porte = {}
i_porte["1"]=list()
i_porte["0"]=list()

num_niv=0
l=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

solu = [
        [[1],[]],                    #1
        [[1],[]],                    #2
        [[1],[]],                    #3
        [[],[1]],                    #4
        [[],[1]],                    #5
        [[1],[]],                    #6
        [[2],[1]],                   #7
        [[],[1]],                    #8
        [[],[1]],                    #9
        [[1,2],[]],                  #10
        [[1],[2,3,4]],               #11
        [[1,3],[2]],                 #12
        [[1,2],[3]],                 #13
        [[],[1,2]],                  #14
        [[2,3],[1]],                 #15
        [[2],[1]],                   #16
        [[1,3],[2]],                 #17
        [[1,2,3],[4]],               #18
        [[3],[1,2]],                 #19
        [[2],[1]],                   #20
        [[2],[1]],                   #21
        [[1,2],[]],                  #22
        [[1,3],[2]],                 #23
        [[3,4],[1,2]],               #24
        [[1,2,3,4],[]],              #25
        [[2,3,4,5],[1,6]],           #26
        [[1,3,5],[2,4]],             #27
        [[3,4,5],[1,2]],             #28
        [[],[1,2,3,4,5]],            #29
        [[1,3],[2,4,5]],             #30
        [[1,2,4,5],[3,6,7,8]]        #bonus
        ]



####################################################creation de la fenetre 

Mafenetre=Tk()
Mafenetre.geometry("1920x1080")

####################################################IMAGES

# get the absolute path of the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

niveau_img=PhotoImage(file=os.path.join(script_dir, "ressources/quitter.png"))
jouer_img=PhotoImage(file=os.path.join(script_dir, "ressources/joui.png"))
menu_img=PhotoImage(file=os.path.join(script_dir, "ressources/menu_bien.png"))
cjouer_img=PhotoImage(file=os.path.join(script_dir, "ressources/commentjouerFR.png"))
fleche_img=PhotoImage(file=os.path.join(script_dir, "ressources/feulaiche.png"))
ok_img=PhotoImage(file=os.path.join(script_dir, "ressources/ok.png"))
menu_but_img=PhotoImage(file=os.path.join(script_dir, "ressources/menu_but.png"))
croix_img=PhotoImage(file=os.path.join(script_dir, "ressources/croix.png"))
check_img=PhotoImage(file=os.path.join(script_dir, "ressources/check.png"))
size_img=PhotoImage(file=os.path.join(script_dir, "ressources/size.png"))
vide_img=PhotoImage(file=os.path.join(script_dir, "ressources/vide.png"))
niveaux_img=PhotoImage(file=os.path.join(script_dir, "ressources/Niveaux.png"))
cj1=PhotoImage(file=os.path.join(script_dir, "ressources/c_j_1.png"))
cj2=PhotoImage(file=os.path.join(script_dir, "ressources/c_j_2.png"))

lvl1_img=PhotoImage(file=os.path.join(script_dir, "ressources/lvl1.png"))
lvl2_img=PhotoImage(file=os.path.join(script_dir, "ressources/lvl2.png"))
lvl3_img=PhotoImage(file=os.path.join(script_dir, "ressources/lvl3.png"))
lvl4_img=PhotoImage(file=os.path.join(script_dir, "ressources/lvl4.png"))
lvl5_img=PhotoImage(file=os.path.join(script_dir, "ressources/lvl5.png"))
lvl6_img=PhotoImage(file=os.path.join(script_dir, "ressources/lvl6.png"))
lvl7_img=PhotoImage(file=os.path.join(script_dir, "ressources/lvl7.png"))
lvl8_img=PhotoImage(file=os.path.join(script_dir, "ressources/lvl8.png"))
lvl9_img=PhotoImage(file=os.path.join(script_dir, "ressources/lvl9.png"))
lvl10_img=PhotoImage(file=os.path.join(script_dir, "ressources/lvl10.png"))
lvl11_img=PhotoImage(file=os.path.join(script_dir, "ressources/Lvl11.png"))
lvl12_img=PhotoImage(file=os.path.join(script_dir, "ressources/Lvl12.png"))
lvl13_img=PhotoImage(file=os.path.join(script_dir, "ressources/Lvl13.png"))
lvl14_img=PhotoImage(file=os.path.join(script_dir, "ressources/Lvl14.png"))
lvl15_img=PhotoImage(file=os.path.join(script_dir, "ressources/Lvl15.png"))
lvl16_img=PhotoImage(file=os.path.join(script_dir, "ressources/Lvl16.png"))
lvl17_img=PhotoImage(file=os.path.join(script_dir, "ressources/Lvl17.png"))
lvl18_img=PhotoImage(file=os.path.join(script_dir, "ressources/Lvl18.png"))
lvl19_img=PhotoImage(file=os.path.join(script_dir, "ressources/Lvl19.png"))
lvl20_img=PhotoImage(file=os.path.join(script_dir, "ressources/Lvl20.png"))
lvl21_img=PhotoImage(file=os.path.join(script_dir, "ressources/Lvl21.png"))
lvl22_img=PhotoImage(file=os.path.join(script_dir, "ressources/Lvl22.png"))
lvl23_img=PhotoImage(file=os.path.join(script_dir, "ressources/Lvl23.png"))
lvl24_img=PhotoImage(file=os.path.join(script_dir, "ressources/Lvl24.png"))
lvl25_img=PhotoImage(file=os.path.join(script_dir, "ressources/Lvl25.png"))
lvl26_img=PhotoImage(file=os.path.join(script_dir, "ressources/Lvl26.png"))
lvl27_img=PhotoImage(file=os.path.join(script_dir, "ressources/Lvl27.png"))
lvl28_img=PhotoImage(file=os.path.join(script_dir, "ressources/Lvl28.png"))
lvl29_img=PhotoImage(file=os.path.join(script_dir, "ressources/Lvl29.png"))
lvl30_img=PhotoImage(file=os.path.join(script_dir, "ressources/Lvl30.png"))
lvlbonus_img=PhotoImage(file=os.path.join(script_dir, "ressources/Lvl_bonus.png"))
lvlfin_img=PhotoImage(file=os.path.join(script_dir, "ressources/fin.png"))
lvlselect_img=PhotoImage(file=os.path.join(script_dir, "ressources/select.png"))
i1=PhotoImage(file=os.path.join(script_dir, "ressources/1.png"))
i2=PhotoImage(file=os.path.join(script_dir, "ressources/2.png"))
i3=PhotoImage(file=os.path.join(script_dir, "ressources/3.png"))
i4=PhotoImage(file=os.path.join(script_dir, "ressources/4.png"))
i5=PhotoImage(file=os.path.join(script_dir, "ressources/5.png"))
i6=PhotoImage(file=os.path.join(script_dir, "ressources/6.png"))
i7=PhotoImage(file=os.path.join(script_dir, "ressources/7.png"))
i8=PhotoImage(file=os.path.join(script_dir, "ressources/8.png"))
i9=PhotoImage(file=os.path.join(script_dir, "ressources/9.png"))
i10=PhotoImage(file=os.path.join(script_dir, "ressources/10.png"))
i11=PhotoImage(file=os.path.join(script_dir, "ressources/11.png"))
i12=PhotoImage(file=os.path.join(script_dir, "ressources/12.png"))
i13=PhotoImage(file=os.path.join(script_dir, "ressources/13.png"))
i14=PhotoImage(file=os.path.join(script_dir, "ressources/14.png"))
i15=PhotoImage(file=os.path.join(script_dir, "ressources/15.png"))
i16=PhotoImage(file=os.path.join(script_dir, "ressources/16.png"))
i17=PhotoImage(file=os.path.join(script_dir, "ressources/17.png"))
i18=PhotoImage(file=os.path.join(script_dir, "ressources/18.png"))
i19=PhotoImage(file=os.path.join(script_dir, "ressources/19.png"))
i20=PhotoImage(file=os.path.join(script_dir, "ressources/20.png"))
i21=PhotoImage(file=os.path.join(script_dir, "ressources/21.png"))
i22=PhotoImage(file=os.path.join(script_dir, "ressources/22.png"))
i23=PhotoImage(file=os.path.join(script_dir, "ressources/23.png"))
i24=PhotoImage(file=os.path.join(script_dir, "ressources/24.png"))
i25=PhotoImage(file=os.path.join(script_dir, "ressources/25.png"))
i26=PhotoImage(file=os.path.join(script_dir, "ressources/26.png"))
i27=PhotoImage(file=os.path.join(script_dir, "ressources/27.png"))
i28=PhotoImage(file=os.path.join(script_dir, "ressources/28.png"))
i29=PhotoImage(file=os.path.join(script_dir, "ressources/29.png"))
i30=PhotoImage(file=os.path.join(script_dir, "ressources/30.png"))


img_lvl=[menu_img,lvl1_img,lvl2_img,lvl3_img,lvl4_img,lvl5_img,lvl6_img,lvl7_img,lvl8_img,
         lvl9_img,lvl10_img,lvl11_img,lvl12_img,lvl13_img,lvl14_img,lvl15_img,lvl16_img,
         lvl17_img,lvl18_img,lvl19_img,lvl20_img,lvl21_img,lvl22_img,lvl23_img,lvl24_img,
         lvl25_img,lvl26_img,lvl27_img,lvl28_img,lvl29_img,lvl30_img,lvlbonus_img,lvlfin_img]

img_autre=[cj1,cj2,croix_img,check_img,size_img,vide_img,lvlselect_img,niveaux_img]

img_n=[i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,i21,i22,i23,i24,i25,i26,i27,i28,i29,i30]
####################################################CANVAS

can1=Canvas(Mafenetre,width=1930 ,height=1080 ,bg='#323232')

can1.place(x=-2 ,y=-2 )

####################################################FONCTIONS

        
 
def get_i(type_):
        if type_ == "":
            return [valeur for valeur in i_porte.values()]

        
        if type_ != "":
            return i_porte.get(type_)
        
def get_key(index_):
    a = get_i("")
    k = list(i_porte.keys())

    for i in a:
        if index_ in i:

            position = a.index(i)
            return k[position]

        
def verif(index):

        for v in i_porte.values():
            if index in v:
                return("oui")
            else:
                return("non")

def chgm(index,porte):
    
    if verif(index) == "oui":
        a = get_key(index)
        if a == porte:
            pass
        else:
            i_porte[a].remove(index)
            i_porte[porte].append(index)


def taille(i):
    return sum([len(i) for i in get_i("")])

def chgm2(index):

    if get_key(index) == "1":

        i_porte["1"].remove(index)
        i_porte["0"].append(index)
    elif get_key(index) == "0":

        i_porte["0"].remove(index)
        i_porte["1"].append(index)

def quel_niv():
    global num_niv
    if num_niv == 0:
        lvl1()
        l[1]=True
    if num_niv == 1:
        lvl2() 
        l[2]=True
    if num_niv == 2:
        lvl3()  
        l[3]=True
    if num_niv == 3:
        lvl4() 
        l[4]=True
    if num_niv == 4:
        lvl5() 
        l[5]=True
    if num_niv == 5:
        lvl6() 
        l[6]=True
    if num_niv == 6:
        lvl7() 
        l[7]=True
    if num_niv == 7:
        lvl8() 
        l[8]=True
    if num_niv == 8:
        lvl9()         
        l[9]=True
    if num_niv == 9:
        lvl10() 
        l[10]=True
    if num_niv == 10:
        lvl11()  
        l[11]=True
    if num_niv == 11:
        lvl12()         
        l[12]=True    
    if num_niv == 12:
        lvl13()   
        l[13]=True
    if num_niv == 13:
        lvl14()         
        l[14]=True
    if num_niv == 14:
        lvl15() 
        l[15]=True
    if num_niv == 15:
        lvl16() 
        l[16]=True
    if num_niv == 16:
        lvl17() 
        l[17]=True
    if num_niv == 17:
        lvl18() 
        l[18]=True
    if num_niv == 18:
        lvl19() 
        l[19]=True
    if num_niv == 19:
        lvl20() 
        l[20]=True
    if num_niv == 20:
        lvl21() 
        l[21]=True
    if num_niv == 21:
        lvl22() 
        l[22]=True
    if num_niv == 22:
        lvl23() 
        l[23]=True
    if num_niv == 23:
        lvl24() 
        l[24]=True
    if num_niv == 24:
        lvl25() 
        l[25]=True
    if num_niv == 25:
        lvl26() 
        l[26]=True
    if num_niv == 26:
        lvl27() 
        l[27]=True
    if num_niv == 27:
        lvl28() 
        l[28]=True
    if num_niv == 28:
        lvl29() 
        l[29]=True
    if num_niv == 29:
        lvl30() 
        l[30]=True
    if num_niv == 30:
        lvlbonus() 
        
    if num_niv == 31:
        lvlfin() 

def niv():
    global num_niv,solu,i_porte
    cpt=0

    for elt in get_i('1'):
        if elt not in solu[num_niv][0]:
            break
        cpt+=1
        
    for elt in get_i('0'):
        if elt not in solu[num_niv][1]:
            break
        cpt+=1

    if cpt == (len(solu[num_niv][0])+len(solu[num_niv][1])):
        num_niv += 1
        img_active.append(can1.create_image(1210+offset,650+offset2, anchor = NW, image=img_autre[3]))
        can1.update()
        time.sleep(1)
        quel_niv()
    else:
        a=can1.create_image(1210+offset,650+offset2, anchor = NW, image=img_autre[2])
        can1.update()
        time.sleep(1)
        can1.delete(a)
        can1.update()
        

def set_i(a):
    global i_porte, portes, b
    i_porte = {'1': [], '0': []}
    for i in range(1,a+1):
        i_porte['0'].append(i)
    cpt=-1
    for elt in portes:
        cpt+=1
        elt.coo(a)
        elt.img_reset(cpt,b)
    
        
def set_niv():
    for elt in autre:
        elt.place_forget()
        
    for elt in img_active:
        can1.delete(elt)
    
    for elt in b:
        elt.place_forget()
        
    for elt in n:
        elt.place_forget()
        
    bou10.place(x=310+offset,y=650+offset2)
    ok.place(x=1150+offset,y=650+offset2)
    
def place(i):
    compt=0
    for elt in b:
        compt+=1
        if compt==i+1:
            break
        elt.place(x=portes[b.index(elt)].co+offset,y=578+offset2)
    
def size_fct(i):
    global offset,offset2
    if i==1:
        size1.config(image=img_autre[3],width=34,height=35,bd=0)
        size2.config(image=img_autre[5],width=34,height=35,bd=0)
        size3.config(image=img_autre[5],width=34,height=35,bd=0)
        offset=170
        offset2=100
    elif i==2:
        size2.config(image=img_autre[3],width=34,height=35,bd=0)
        size1.config(image=img_autre[5],width=34,height=35,bd=0)
        size3.config(image=img_autre[5],width=34,height=35,bd=0)
        offset=0
        offset2=30
    elif i==3:
        size3.config(image=img_autre[3],width=34,height=35,bd=0)
        size1.config(image=img_autre[5],width=34,height=35,bd=0)
        size2.config(image=img_autre[5],width=34,height=35,bd=0)
        offset=-100
        offset2=-40
        
    bou9.place_forget()
    jouer.place_forget()
    comment_jouer.place_forget()
    niv_but.place_forget()
    for elt in img_active:
        can1.delete(elt)
    bou9.place(x=435+offset,y=480)
    jouer.place(x=685+offset,y=480)
    comment_jouer.place(x=(930+offset),y=480)
    niv_but.place(x=685+offset,y=600)
    img_active.append(can1.create_image(213+offset,0, anchor = NW, image=img_lvl[0]))
    can1.update()
    img_active.append(can1.create_image(0,350, anchor = NW, image=img_autre[4]))
    can1.update()

def niv_selec(i):
    global num_niv
    num_niv=i-1
    print(num_niv)
    quel_niv()

####################################################CLASSES

class Porte:
    
    def __init__(self,type_,i):
        
        self.type = type_
        self.i = i
        i_porte[self.type].append(self.i)
        self.img = PhotoImage(file=os.path.join(script_dir, "ressources/zewo.png"))
        self.img_i = "zero"
        self.co = 0
    
    def img_reset(self,i,b):
        self.img = PhotoImage(file=os.path.join(script_dir, "ressources/zewo.png"))
        self.img_i = "zero"
        b[i].config(image=self.img,width=50,height=50,bd=0)

    def img_chgm(self, b, i):
        if self.img_i == "zero":
            self.img = PhotoImage(file=os.path.join(script_dir, "ressources/de.png"))
            self.img_i = "un"
        elif self.img_i == "un":
            self.img = PhotoImage(file=os.path.join(script_dir, "ressources/zewo.png"))
            self.img_i = "zero"
        b[i].config(image=self.img, width=50, height=50, bd=0)


    def coo(self,nb_porte):
        if nb_porte == 1:
            self.co=750
        elif nb_porte%2 == 1:
            self.co=(775-(((nb_porte//2)+1)-self.i)*50)-25
        else:
            self.co=(775-(((nb_porte//2)+1)-self.i)*50)
####################################################OBJETS

p1=Porte("0",1)
p2=Porte("0",2)
p3=Porte("0",3)
p4=Porte("0",4)
p5=Porte("0",5)
p6=Porte("0",6)
p7=Porte("0",7)
p8=Porte("0",8)

portes=[p1,p2,p3,p4,p5,p6,p7,p8]


####################################################BOUTONS

porte1 = Button(Mafenetre,text="",command=lambda:[chgm2(p1.i),p1.img_chgm(b,0)])
porte2 = Button(Mafenetre,text="",command=lambda:[chgm2(p2.i),p2.img_chgm(b,1)])
porte3 = Button(Mafenetre,text="",command=lambda:[chgm2(p3.i),p3.img_chgm(b,2)])
porte4 = Button(Mafenetre,text="",command=lambda:[chgm2(p4.i),p4.img_chgm(b,3)])
porte5 = Button(Mafenetre,text="",command=lambda:[chgm2(p5.i),p5.img_chgm(b,4)])
porte6 = Button(Mafenetre,text="",command=lambda:[chgm2(p6.i),p6.img_chgm(b,5)])
porte7 = Button(Mafenetre,text="",command=lambda:[chgm2(p7.i),p7.img_chgm(b,6)])
porte8 = Button(Mafenetre,text="",command=lambda:[chgm2(p8.i),p8.img_chgm(b,7)])

porte1.config(image=p1.img,width=50,height=50,bd=0)
porte2.config(image=p2.img,width=50,height=50,bd=0)
porte3.config(image=p3.img,width=50,height=50,bd=0)
porte4.config(image=p4.img,width=50,height=50,bd=0)
porte5.config(image=p5.img,width=50,height=50,bd=0)
porte6.config(image=p6.img,width=50,height=50,bd=0)
porte7.config(image=p7.img,width=50,height=50,bd=0)
porte8.config(image=p8.img,width=50,height=50,bd=0)

n1 = Button(Mafenetre,text="",command=lambda:[niv_selec(1)])
n2 = Button(Mafenetre,text="",command=lambda:[niv_selec(2)])
n3 = Button(Mafenetre,text="",command=lambda:[niv_selec(3)])
n4 = Button(Mafenetre,text="",command=lambda:[niv_selec(4)])
n5 = Button(Mafenetre,text="",command=lambda:[niv_selec(5)])
n6 = Button(Mafenetre,text="",command=lambda:[niv_selec(6)])
n7 = Button(Mafenetre,text="",command=lambda:[niv_selec(7)])
n8 = Button(Mafenetre,text="",command=lambda:[niv_selec(8)])
n9 = Button(Mafenetre,text="",command=lambda:[niv_selec(9)])
n10 = Button(Mafenetre,text="",command=lambda:[niv_selec(10)])
n11 = Button(Mafenetre,text="",command=lambda:[niv_selec(11)])
n12 = Button(Mafenetre,text="",command=lambda:[niv_selec(12)])
n13 = Button(Mafenetre,text="",command=lambda:[niv_selec(13)])
n14 = Button(Mafenetre,text="",command=lambda:[niv_selec(14)])
n15 = Button(Mafenetre,text="",command=lambda:[niv_selec(15)])
n16 = Button(Mafenetre,text="",command=lambda:[niv_selec(16)])
n17 = Button(Mafenetre,text="",command=lambda:[niv_selec(17)])
n18 = Button(Mafenetre,text="",command=lambda:[niv_selec(18)])
n19 = Button(Mafenetre,text="",command=lambda:[niv_selec(19)])
n20 = Button(Mafenetre,text="",command=lambda:[niv_selec(20)])
n21 = Button(Mafenetre,text="",command=lambda:[niv_selec(21)])
n22 = Button(Mafenetre,text="",command=lambda:[niv_selec(22)])
n23 = Button(Mafenetre,text="",command=lambda:[niv_selec(23)])
n24 = Button(Mafenetre,text="",command=lambda:[niv_selec(24)])
n25 = Button(Mafenetre,text="",command=lambda:[niv_selec(25)])
n26 = Button(Mafenetre,text="",command=lambda:[niv_selec(26)])
n27 = Button(Mafenetre,text="",command=lambda:[niv_selec(27)])
n28 = Button(Mafenetre,text="",command=lambda:[niv_selec(28)])
n29 = Button(Mafenetre,text="",command=lambda:[niv_selec(29)])
n30 = Button(Mafenetre,text="",command=lambda:[niv_selec(30)])

n1.config(image=img_n[0],width=34,height=35,bd=0)
n2.config(image=img_n[1],width=34,height=35,bd=0)
n3.config(image=img_n[2],width=34,height=35,bd=0)
n4.config(image=img_n[3],width=34,height=35,bd=0)
n5.config(image=img_n[4],width=34,height=35,bd=0)
n6.config(image=img_n[5],width=34,height=35,bd=0)
n7.config(image=img_n[6],width=34,height=35,bd=0)
n8.config(image=img_n[7],width=34,height=35,bd=0)
n9.config(image=img_n[8],width=34,height=35,bd=0)
n10.config(image=img_n[9],width=34,height=35,bd=0)
n11.config(image=img_n[10],width=34,height=35,bd=0)
n12.config(image=img_n[11],width=34,height=35,bd=0)
n13.config(image=img_n[12],width=34,height=35,bd=0)
n14.config(image=img_n[13],width=34,height=35,bd=0)
n15.config(image=img_n[14],width=34,height=35,bd=0)
n16.config(image=img_n[15],width=34,height=35,bd=0)
n17.config(image=img_n[16],width=34,height=35,bd=0)
n18.config(image=img_n[17],width=34,height=35,bd=0)
n19.config(image=img_n[18],width=34,height=35,bd=0)
n20.config(image=img_n[19],width=34,height=35,bd=0)
n21.config(image=img_n[20],width=34,height=35,bd=0)
n22.config(image=img_n[21],width=34,height=35,bd=0)
n23.config(image=img_n[22],width=34,height=35,bd=0)
n24.config(image=img_n[23],width=34,height=35,bd=0)
n25.config(image=img_n[24],width=34,height=35,bd=0)
n26.config(image=img_n[25],width=34,height=35,bd=0)
n27.config(image=img_n[26],width=34,height=35,bd=0)
n28.config(image=img_n[27],width=34,height=35,bd=0)
n29.config(image=img_n[28],width=34,height=35,bd=0)
n30.config(image=img_n[29],width=34,height=35,bd=0)

niv_but=Button(Mafenetre,text="OK",command=lambda:[lvlselect()])
niv_but.config(image=img_autre[7],width=180,height=91,bd=0)

ok=Button(Mafenetre,text="OK",command=lambda:[niv()])
ok.config(image=ok_img,width=48,height=48,bd=0)

bou9=Button(Mafenetre,text="Quitter",command=Mafenetre.destroy)
bou9.config(image=niveau_img,width=181,height=92,bd=0)

bou10=Button(Mafenetre,text="MENU",command=lambda:[menu()])
bou10.config(image=menu_but_img,width=181,height=92,bd=0)

jouer=Button(Mafenetre,text="JOUER",command=lambda:[quel_niv()])
jouer.config(image=jouer_img,width=183,height=94,bd=0)

comment_jouer=Button(Mafenetre,text="CJ",command=lambda:[cj1()])
comment_jouer.config(image=cjouer_img,width=183,height=94,bd=0)

size1=Button(Mafenetre,text="size",command=lambda:[size_fct(1)])
size2=Button(Mafenetre,text="size",command=lambda:[size_fct(2)])
size3=Button(Mafenetre,text="size",command=lambda:[size_fct(3)])
size1.config(image=img_autre[3],width=34,height=35,bd=0)
size2.config(image=img_autre[5],width=34,height=35,bd=0)
size3.config(image=img_autre[5],width=34,height=35,bd=0)

fleche=Button(Mafenetre,text="FLECHE1",command=lambda:[cj2()])
fleche.config(image=fleche_img,width=100,height=50,bd=0)
fleche2=Button(Mafenetre,text="FLECH2E",command=lambda:[menu()])
fleche2.config(image=fleche_img,width=100,height=50,bd=0)

b = [porte1,porte2,porte3,porte4,porte5,porte6,porte7,porte8]
autre = [bou9,jouer,comment_jouer,fleche,fleche2,bou10,ok,size1,size2,size3,niv_but]
n=[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22,n23,n24,n25,n26,n27,n28,n29,n30]
####################################################MAP

def menu():
    l[0]==True
    set_niv()
    ok.place_forget()
    bou10.place_forget()
    niv_but.place(x=685+offset,y=600)
    img_active.append(can1.create_image(213+offset,0, anchor = NW, image=img_lvl[0]))
    img_active.append(can1.create_image(0,350, anchor = NW, image=img_autre[4]))
    size1.place(x=20,y=368)
    size2.place(x=20,y=426)
    size3.place(x=20,y=484)
    bou9.place(x=435+offset,y=480)
    jouer.place(x=685+offset,y=480)
    comment_jouer.place(x=(930+offset),y=480)
    
    
def cj1():
    set_niv()
    ok.place_forget()
    bou10.place_forget()
    img_active.append(can1.create_image(213+offset,50+offset2, anchor = NW, image=img_autre[0]))

    fleche.place(x=1200+offset,y=600+offset2)
    
def cj2(): 
    set_niv()
    ok.place_forget()
    bou10.place_forget()
    img_active.append(can1.create_image(213+offset,50+offset2, anchor = NW, image=img_autre[1]))
    fleche2.place(x=1200+offset,y=600+offset2)

def lvl1():
    set_niv()
    img_active.append(can1.create_image(480+offset,140+offset2, anchor = NW, image=img_lvl[1])   )
    set_i(1)

    b[0].place(x=portes[0].co+offset,y=578+offset2)

def lvl2():
    set_niv()
    set_i(1)
    img_active.append(can1.create_image(479+offset,150+offset2, anchor = NW, image=img_lvl[2])   )
    
    b[0].place(x=portes[0].co+offset,y=578+offset2)
    
def lvl3():
    set_niv()
    set_i(1)
    img_active.append(can1.create_image(479+offset,150+offset2, anchor = NW, image=img_lvl[3])   )
    
    b[0].place(x=portes[0].co+offset,y=578+offset2)
    
def lvl4():
    set_niv()
    set_i(1)
    img_active.append(can1.create_image(479+offset,150+offset2, anchor = NW, image=img_lvl[4])   )
    
    b[0].place(x=portes[0].co+offset,y=578+offset2)
    
def lvl5():
    set_niv()
    set_i(1)
    img_active.append(can1.create_image(479+offset,150+offset2, anchor = NW, image=img_lvl[5])   )
    
    b[0].place(x=portes[0].co+offset,y=578+offset2)
   
def lvl6():
    set_niv()
    set_i(1)
    img_active.append(can1.create_image(479+offset,150+offset2, anchor = NW, image=img_lvl[6])   )
    
    b[0].place(x=portes[0].co+offset,y=578+offset2)

def lvl7():
    set_niv()
    set_i(2)
    img_active.append(can1.create_image(479+offset,150+offset2, anchor = NW, image=img_lvl[7])   )
    
    place(2)

def lvl8():
    set_niv()
    set_i(1)
    img_active.append(can1.create_image(479+offset,50+offset2, anchor = NW, image=img_lvl[8])   )
    
    b[0].place(x=portes[0].co+offset,y=578+offset2)

def lvl9():
    set_niv()
    set_i(1)
    img_active.append(can1.create_image(479+offset,50+offset2, anchor = NW, image=img_lvl[9])   )
    
    b[0].place(x=portes[0].co+offset,y=578+offset2)

def lvl10():
    set_niv()
    set_i(2)
    img_active.append(can1.create_image(479+offset,50+offset2, anchor = NW, image=img_lvl[10])   )
    
    place(2)


def lvl11():
    set_niv()
    set_i(4)
    img_active.append(can1.create_image(479+offset,50+offset2, anchor = NW, image=img_lvl[11])   )
    
    place(4)

def lvl12():
    set_niv()
    set_i(3)
    img_active.append(can1.create_image(479+offset,50+offset2, anchor = NW, image=img_lvl[12])   )
    
    place(3)
    
def lvl13():
    set_niv()
    set_i(3)
    img_active.append(can1.create_image(452+offset,50+offset2, anchor = NW, image=img_lvl[13])   )
    
    place(3)

def lvl14():
    set_niv()
    set_i(2)
    img_active.append(can1.create_image(498+offset,50+offset2, anchor = NW, image=img_lvl[14])   )
    
    place(2)
    
def lvl15():
    set_niv()
    set_i(3)
    img_active.append(can1.create_image(479+offset,50+offset2, anchor = NW, image=img_lvl[15])   )
     
    place(3)   
    
def lvl16():
    set_niv()
    set_i(2)
    img_active.append(can1.create_image(473+offset,50+offset2, anchor = NW, image=img_lvl[16])   )
     
    place(2)   
    
def lvl17():
    set_niv()
    set_i(3)
    img_active.append(can1.create_image(506+offset,50+offset2, anchor = NW, image=img_lvl[17])   )
     
    place(3)      
    
def lvl18():
    set_niv()
    set_i(4)
    img_active.append(can1.create_image(479+offset,50+offset2, anchor = NW, image=img_lvl[18])   )
     
    place(4)     
    
def lvl19():
    set_niv()
    set_i(3)
    img_active.append(can1.create_image(479+offset,50+offset2, anchor = NW, image=img_lvl[19])   )
     
    place(3)     
    
def lvl20():
    set_niv()
    set_i(2)
    img_active.append(can1.create_image(484+offset,50+offset2, anchor = NW, image=img_lvl[20])   )
     
    place(2)     
    
def lvl21():
    set_niv()
    set_i(2)
    img_active.append(can1.create_image(484+offset,50+offset2, anchor = NW, image=img_lvl[21])   )
     
    place(2)      
    
def lvl22():
    set_niv()
    set_i(2)
    img_active.append(can1.create_image(484+offset,50+offset2, anchor = NW, image=img_lvl[22])   )
     
    place(2)     
    
def lvl23():
    set_niv()
    set_i(3)
    img_active.append(can1.create_image(459+offset,50+offset2, anchor = NW, image=img_lvl[23])   )
     
    place(3)   
    
def lvl24():
    set_niv()
    set_i(4)
    img_active.append(can1.create_image(435+offset,50+offset2, anchor = NW, image=img_lvl[24])   )
     
    place(4)    
    
def lvl25():
    set_niv()
    set_i(4)
    img_active.append(can1.create_image(488+offset,50+offset2, anchor = NW, image=img_lvl[25])   )
     
    place(4)   
    
def lvl26():
    set_niv()
    set_i(6)
    img_active.append(can1.create_image(488+offset,50+offset2, anchor = NW, image=img_lvl[26])   )
     
    place(6)     
    
def lvl27():
    set_niv()
    set_i(5)
    img_active.append(can1.create_image(479+offset,50+offset2, anchor = NW, image=img_lvl[27])   )
     
    place(5)    
    
def lvl28():
    set_niv()
    set_i(5)
    img_active.append(can1.create_image(458+offset,40+offset2, anchor = NW, image=img_lvl[28])   )
     
    place(5)    
    
def lvl29():
    set_niv()
    set_i(5)
    img_active.append(can1.create_image(458+offset,40+offset2, anchor = NW, image=img_lvl[29])   )
     
    place(5)    
    
def lvl30():
    set_niv()
    set_i(5)
    img_active.append(can1.create_image(458+offset,40+offset2, anchor = NW, image=img_lvl[30])   )
     
    place(5)   
    
def lvlbonus():
    set_niv()
    set_i(8)
    img_active.append(can1.create_image(479+offset,59+offset2, anchor = NW, image=img_lvl[31])   )
     
    place(8)    
    
def lvlfin():
    set_niv()
    ok.place_forget()
    bou10.place(x=700+offset,y=650+offset2)
    img_active.append(can1.create_image(213+offset,40+offset2, anchor = NW, image=img_lvl[32])   )
     
def lvlselect():
    set_niv()
    niv_but.place_forget()
    ok.place_forget()
    bou10.place(x=700+offset,y=650+offset2)
    img_active.append(can1.create_image(213+offset,40+offset2, anchor = NW, image=img_autre[6])   )
    if offset==170:
        ax=390+offset
        ay=142
    elif offset==0:
        ax=560+offset
        ay=142
    elif offset==-100:
        ax=660+offset
        ay=142
    
    for i in range(len(n)):
        print("AAAAAAAAA",l)
        if l[i+1]==True:
            n[i].place(x=ax+offset,y=ay+offset2)
            if (i+1)%6==0 :
                ay+=83
                if offset==170:
                    ax=308+offset
                elif offset==0:
                    ax=478+offset
                elif offset==-100:
                    ax=578+offset
        ax+=82
    
####################################################NIVEAUX
print(l)
menu()
Mafenetre.attributes('-fullscreen', True)
Mafenetre.mainloop()
###################################################