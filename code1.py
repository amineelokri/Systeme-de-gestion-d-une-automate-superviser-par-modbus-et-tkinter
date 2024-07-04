from tkinter import * 
from tkinter import messagebox
from pymodbus.client import ModbusTcpClient


class CustomMessageBox:
    def __init__(self, parent, title, message,d,modbus):
        self.modbus=modbus
        self.parent = parent
        self.title = title
        self.message = message
        self.d=d

        # Create a new Toplevel window
        self.top = Toplevel(parent)
        self.top.title(title)

        # Add a label to display the message
        self.spin_var = StringVar()
        self.spin_var.set("1000")  # Set default value

        self.s = Spinbox(self.top, from_=0, to=9000,textvariable=self.spin_var)
        self.s.grid(row=0,column=1,padx=20, pady=20)

        # Add a button to close the dialog
        self.confirme_button = Button(self.top, text="Confirmer", command=self.change_debit)
        self.close_button = Button(self.top, text="Annuler", command=self.close)
        self.close_button.grid(row=1,column=0,padx=20, pady=10)
        self.confirme_button.grid(row=1,column=2,padx=20, pady=10)

    def change_debit(self):
        valeur=int(self.s.get())
        adresse=10+self.d
        self.modbus.ecrireRegistre(adresse,valeur)
        self.close()


    def close(self):
        # Close the dialog window
        self.top.destroy()


class ModbusApp:
    def __init__(self,root,debit1,debit2,debit3,nv_sup,modbus):
        self.modbus=modbus
        self.root=root
        debit1=debit1+1
        self.debit1=debit1
        self.debit2=debit2
        self.debit3=debit3
        self.nv_sup=nv_sup
        self.nbrCycleRemplie=0
        self.nbrCycleVidange=0
        self.etat=False
        self.pred_etat=self.modbus.lireBit(300)
        self.pred_etat2=self.modbus.lireBit(301)






        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        taskbar_height = screen_height - self.root.winfo_toplevel().winfo_height()

        # Set window size to fill screen minus taskbar
        window_width = screen_width
        window_height = screen_height
        self.root.geometry(f"{window_width}x{window_height}")

        self.root.title('interface modbus pour controler une atomate')
        self.root['bg']='grey'

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        frame1 =LabelFrame(self.root, text="Première Trémie", padx=10, pady=10)
        frame1.grid(row=0, column=0, padx=10, pady=10,sticky="nsew")

        frame1.grid_rowconfigure(0, weight=1)
        frame1.grid_rowconfigure(1, weight=1)
        frame1.grid_columnconfigure(1, weight=1)

        ############################################################
        frame2 =LabelFrame(self.root, text="Deuxième Trémie", padx=10, pady=10)
        frame2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        frame2.grid_rowconfigure(0, weight=1)
        frame2.grid_rowconfigure(1, weight=1)
        frame2.grid_columnconfigure(1, weight=1)
        ##################################################################
        frame3 =LabelFrame(self.root, text="Troisième trémie", padx=10, pady=10)
        frame3.grid(row=1, column=1,padx=10,pady=10, sticky="nsew")
        self.frame3=frame3

        frame3.grid_rowconfigure(0, weight=1)
        frame3.grid_rowconfigure(1, weight=1)
        frame3.grid_columnconfigure(1, weight=1)

        ######################################################
        frame7 =LabelFrame(self.root, text="Barre de Contrôle ", padx=10, pady=10)
        frame7.grid(row=1, column=0,padx=10, pady=10, sticky="nsew")

        frame7.grid_rowconfigure(0, weight=1)
        frame7.grid_rowconfigure(1, weight=1)
        frame7.grid_columnconfigure(1, weight=1)


        ##############To add#######
        photo=PhotoImage(file="./assets/terimie1.png")
        canvas = Canvas(frame1,width=200, height=200)
        canvas.create_image(40,20,anchor=NW, image=photo)
        canvas.grid(row=0, column=1)
        canvas['bg']='white'

        frame4=LabelFrame(frame1, text="Paramètres", padx=10, pady=10)
        frame4.grid(row=0, column=0)

        self.t=Text(frame4,wrap="word",width=12,height=1)
        self.t.insert(END,self.debit1)
        self.t.grid(row=0,column=2,padx=5)
        #s = Spinbox(frame4, from_=0, to=9000,width=10)
        #s.grid(row=0,column=1,columnspan=2)

        l=Label(frame4,text="Débit")
        l.grid(row=0,column=0)

        b=Button(frame4,text='Modifier Le débit',command=self.callback1)
        b.grid(row=2,column=2,pady=10)



        # Ajouter des widgets à la deuxième frame (Register operations)
        photo2=PhotoImage(file="./assets/terimie2.png")
        canvas2 = Canvas(frame2,width=200, height=200)
        canvas2.create_image(40,20,anchor=NW, image=photo2)
        canvas2.grid(row=0, column=1)
        canvas2['bg']='white'

        frame5=LabelFrame(frame2, text="Paramètres", padx=10, pady=10)
        frame5.grid(row=0, column=0)

        self.t2=Text(frame5,wrap="word",width=12,height=1)
        self.t2.insert(END,self.debit2)
        self.t2.grid(row=0,column=2,padx=5)

        self.t2.delete("1.0",END)
        self.t2.insert(END,1100)
        #s = Spinbox(frame5, from_=0, to=9000,width=10)
        #s.grid(row=0,column=1,columnspan=2)

        l2=Label(frame5,text="Débit")
        l2.grid(row=0,column=0)

        b2=Button(frame5,text='Modifier Le débit',command=self.callback2)
        b2.grid(row=2,column=2,pady=10)



        # Ajouter des widgets à la troisième frame (Misc operations)
        self.photo3=PhotoImage(file="./assets/vide.png")
        self.canvas3 = Canvas(frame3,width=200, height=200)
        self.canvas3.create_image(40,20,anchor=NW, image=self.photo3)
        self.canvas3['bg']='white'

        frame6=LabelFrame(frame3, text="Paramètres", padx=10, pady=10)
        frame6.grid(row=0,column=0)
        self.canvas3.grid(row=0,column=1)


        self.t4=Text(frame6,wrap="word",width=12,height=1)
        self.t4.insert(END,self.nv_sup)
        self.t4.grid(row=0,column=2,pady=10)
        self.l4=Label(frame6,text="Niveau de remplissage")
        self.l4.grid(row=0,column=0,pady=10,padx=5)

        self.t3=Text(frame6,wrap="word",width=12,height=1)
        self.t3.insert(END,self.debit3)
        self.t3.grid(row=1,column=2)
        #s = Spinbox(frame6, from_=0, to=9000,width=10)
        #s.grid(row=0,column=1,columnspan=2)

        l3=Label(frame6,text="débit")
        l3.grid(row=1,column=0,padx=5)

        b3=Button(frame6,text='Modifier Le débit',command=self.callback3)
        b3.grid(row=3,column=2,pady=10)

        ###############################frame7####################


        frame8=LabelFrame(frame7, text="Nature de Cycle")
        frame8.grid(row=0,column=0)
        self.b6 = Button(frame8, text ="Remplissage",fg='green', relief=GROOVE)
        self.b7 = Button(frame8, text ="Vidange",fg='red',relief=SUNKEN)
        self.b6.grid(row=0,column=0,padx=10,pady=10)
        self.b7.grid(row=0,column=1,padx=10,pady=10)

        frame9=LabelFrame(frame7, text="État de l'automate")
        frame9.grid(row=0,column=1)


        t9=Text(frame9,wrap="word",width=12,height=1)
        t9.insert(END,"100 ms")

        t9.grid(row=0,column=1,pady=10,padx=5)
        l9=Label(frame9,text="Durée  de Cycle")
        l9.grid(row=0,column=0,pady=10,padx=5)

        self.t10=Text(frame9,wrap="word",width=12,height=1)
        self.t10.insert(END,100)
        self.t10.grid(row=1,column=1,pady=10,padx=5)
        l10=Label(frame9,text="Nombre de cycles de vidange")
        l10.grid(row=1,column=0,pady=10,padx=5)

        self.t12=Text(frame9,wrap="word",width=12,height=1)
        self.t12.insert(END,100)
        self.t12.grid(row=2,column=1,pady=10,padx=5)
        l12=Label(frame9,text="Nombre de cycles de remplissage")
        l12.grid(row=2,column=0,pady=10,padx=5)

        self.t11=Text(frame9,wrap="word",width=12,height=1)
        self.t11.insert(END,100)
        self.t11.grid(row=3,column=1,pady=10,padx=5)
        l11=Label(frame9,text="État convoyeur 1")
        l11.grid(row=3,column=0,pady=10,padx=5)

        icon1=PhotoImage(file="./assets/reset.png")

        button_Reset = Button(frame9,image=icon1, compound="left",width=30,height=30,padx=10,pady=10,command=self.reset)
        button_Reset['bg']="blue"
        button_Reset.grid(row=4,column=1,pady=10)
        

        self.icon_off=PhotoImage(file="./assets/off.png")
        self.icon_on=PhotoImage(file="./assets/on.png")

        self.button_OF = Button(frame7,image=self.icon_on, compound="left",width=30,height=30,command=self.marcher_arreter)
        self.button_OF['bg']="green"
        self.button_OF.grid(row=1,column=2,padx=20)
        self.update()
        root.mainloop()

    def calculerNbreCycle(self):
        nv_etat=self.modbus.lireBit(300)
        nv_etat2=self.modbus.lireBit(301)
        if(nv_etat!=self.pred_etat):
            self.nbrCycleRemplie=self.nbrCycleRemplie+1
            self.pred_etat=nv_etat

        if(nv_etat2!=self.pred_etat2):
            self.nbrCycleVidange=self.nbrCycleVidange+1
            self.pred_etat2=nv_etat2

    def up_etat_cycle(self,sup_rem):

        if(sup_rem):
            self.b6['fg']='green'
            self.b6.config(relief=GROOVE)
            self.b7['fg']='red'
            self.b7.config(relief=SUNKEN)
        else:
            self.b7['fg']='green'
            self.b7.config(relief=GROOVE)
            self.b6['fg']='red'
            self.b6.config(relief=SUNKEN)

    def update_image(self,sup_niv_c):
        taux=int(sup_niv_c)/10200
        img="./assets/vide.png"
        if(taux<0.1):
            img="./assets/vide.png"
        elif(taux<0.2):
            img="./assets/10%.png"
        elif(taux<0.3):
            img="./assets/20%.png"
        elif(taux<0.3):
            img="./assets/30%.png"
        elif(taux<0.5):
            img="./assets/40.png"
        elif(taux<0.6):
            img="./assets/50o.png"
        elif(taux<0.8):
            img="./assets/75%.png"
        elif(taux<0.91):
            img="./assets/90.png"
        else:
            img="./assets/100.png"

        self.canvas3.destroy()
        self.photo10=PhotoImage(file=img)
        self.canvas10 = Canvas(self.frame3,width=200, height=200)
        self.canvas10.create_image(40,20,anchor=NW, image=self.photo10)
        self.canvas10['bg']='white'
        self.canvas10.grid(row=0,column=1)




    def update(self):

        debit1=self.modbus.lireRegistre(automate.DEBIT_1)
        debit2=self.modbus.lireRegistre(automate.DEBIT_2)
        debit3=self.modbus.lireRegistre(automate.DEBIT_3)
        conv1=self.modbus.lireBit(automate.SUP_CONV1)
        sup_niv_c=self.modbus.lireRegistre(automate.SUP_NIV_C)
        sup_rem=self.modbus.lireBit(automate.SUP_CYCR)
        sup_vid=self.modbus.lireBit(automate.SUP_CYCV)
        
        self.update_image(sup_niv_c)
        self.up_etat_cycle(sup_rem)
        self.calculerNbreCycle()
        self.t10.delete("1.0",END)
        self.t10.insert(END,self.nbrCycleVidange//2)

        self.t12.delete("1.0",END)
        self.t12.insert(END,self.nbrCycleRemplie//2)


        self.t.delete("1.0",END)
        self.t.insert(END,debit1)

        self.t2.delete("1.0",END)
        self.t2.insert(END,debit2)

        self.t3.delete("1.0",END)
        self.t3.insert(END,debit3)

        self.t4.delete("1.0",END)
        self.t4.insert(END,sup_niv_c)

        self.t11.delete("1.0",END)
        self.t11.insert(END,conv1)
        
        self.root.after(350,self.update)

    def reset(self):
        self.nbrCycleRemplie=0
        self.nbrCycleVidange=0
    def marcher_arreter(self):

        if(self.etat):
            self.etat=False
            self.modbus.turnOff()
            self.button_OF.config(image=self.icon_on)
            self.button_OF['bg']="green"
        else:
            self.etat=True
            self.modbus.turnOn()
            self.button_OF.config(image=self.icon_off)
            self.button_OF['bg']="red"
    def callback1(self):
        CustomMessageBox(self.root, "Modifier le debit", "Choisissez une valeur",1,self.modbus)

    def callback2(self):
        CustomMessageBox(self.root, "Modifier le debit", "Choisissez une valeur",2,self.modbus)

    def callback3(self):
        CustomMessageBox(self.root, "Modifier le debit", "Choisissez une valeur",3,self.modbus)

class Automate:
    def __init__(self):
        self.FORC_MAR_add=201
        self.FORC_ARR_add=202
        self.SUP_CYCR=300
        self.SUP_CYCV=301
        self.SUP_CYCM=302
        self.SUP_CONV1=303
        self.SUP_CONV2=304
        self.SUP_CONV3=305
        self.SUP_DIST=306
        self.SUP_CONV2=304
        self.DEBIT_1=11
        self.DEBIT_2=12
        self.DEBIT_3=13
        self.SUP_NIV_C=30

class Modbus:

    def __init__(self, address='127.0.0.1', port=9502):
        # Constructeur par défaut qui initialise la communication Modbus
        self.client = ModbusTcpClient(address, port)
        self.client.connect()
    
    def ecrireBit(self,adresse,valeur):
        adresse = adresse - 1
        self.client.write_coils(adresse,valeur)
        
    def lireBit(self,adresse):
        adresse = adresse - 1
        resultat = self.client.read_coils(adresse,count=1)
        return resultat.getBit(0)
        
    def lireOctet(self,adresse):
        adresse = adresse - 1
        resultat = self.client.read_coils(adresse,count=8).bits
        puissance = 1
        res = 0
        for i in range(8):
            if resultat[i]:
                res = res + puissance
            puissance = puissance * 2
        return res
        
    def lireMot(self,adresse):
        adresse = adresse - 1
        resultat = self.client.read_coils(adresse,count=16).bits
        puissance = 1
        res = 0
        for i in range(16):
            if resultat[i]:
                res = res + puissance
            puissance = puissance * 2
        return res
        
    def ecrireRegistre(self,adresse,valeur):
        adresse = adresse - 1
        self.client.write_register(adresse,valeur)
        
    def lireRegistre(self,adresse):
        adresse = adresse - 1
        resultat = self.client.read_input_registers(adresse,count=1)
        return resultat.getRegister(0)
        
    def lireRegistreEntree(self,adresse):
        adresse = adresse - 1
        resultat = self.client.read_input_registers(adresse,count=1)
        return resultat.getRegister(0)
    def turnOn(self):
        arreter=self.ecrireBit(automate.FORC_ARR_add,0)
        arreter=self.ecrireBit(automate.FORC_MAR_add,1)
    def turnOff(self):

        arreter=self.ecrireBit(automate.FORC_MAR_add,0)
        arreter=self.ecrireBit(automate.FORC_ARR_add,1)

    def close(self):
        self.client.close()


    
if __name__ == "__main__":
    modbus = Modbus()
    automate=Automate()
    root=Tk()
    try:
        modbus.turnOff()
        debit1=modbus.lireRegistre(automate.DEBIT_1)
        debit2=modbus.lireRegistre(automate.DEBIT_2)
        debit3=modbus.lireRegistre(automate.DEBIT_3)
        sup_niv_c=modbus.lireRegistre(automate.SUP_NIV_C)
        app = ModbusApp(root,debit1,debit2,debit3,sup_niv_c,modbus)
        root.mainloop()




    finally:
        modbus.close()