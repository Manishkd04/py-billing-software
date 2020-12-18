from tkinter import *
import math, random, os
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman", 30, "bold"),pady=2).pack(fill=X)
        
        #=============Variables====================
        #=============Cosmetics====================
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()

        #=============Grocery========================
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

        #=============Cold Drinks====================
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

        #=============Total Product Price & Tax variable====================
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        #============Customer=========
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()

        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        
        self.search_bill=StringVar()

        #============Customer Detail Frame=========
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details", font=("times new roman",15,"bold"),fg="gold", bg=bg_color)
        F1.place(x=0, y=75, relwidth=1)

        cname_lbl=Label(F1, text="Customer Name",bg=bg_color,fg="white", font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=5)

        cphn_lbl=Label(F1, text="Phone No.",bg=bg_color,fg="white", font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=5)

        c_bill_lbl=Label(F1, text="Bill Number",bg=bg_color,fg="white", font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=5)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        #=============Cosmetic Frame===============
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetcis",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=175,width=325,height=380)

        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0, column=1,padx=10,pady=10)

        Face_cream_1b1=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1, column=1,padx=10,pady=10)

        Face_w_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2, column=1,padx=10,pady=10)

        Hair_s_lbl=Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3, column=1,padx=10,pady=10)

        Hair_g_lbl=Label(F2,text="Hair Gel",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_g_txt=Entry(F2,width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4, column=1,padx=10,pady=10)

        Body_lbl=Label(F2,text="Body Loshan",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Body_txt=Entry(F2,width=10,textvariable=self.loshan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5, column=1,padx=10,pady=10)

        #=============Grocery Frame===============
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=333,y=175,width=325,height=380)

        g1_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0, column=1,padx=10,pady=10)

        g2_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1, column=1,padx=10,pady=10)

        g3_lbl=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2, column=1,padx=10,pady=10)

        g4_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3, column=1,padx=10,pady=10)

        g5_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4, column=1,padx=10,pady=10)

        g6_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5, column=1,padx=10,pady=10)

        #=============Cold Drink Frame===============
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=663,y=175,width=325,height=380)

        c1_lbl=Label(F4,text="Maza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0, column=1,padx=10,pady=10)

        c2_lbl=Label(F4,text="Cock",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=10,textvariable=self.cock,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1, column=1,padx=10,pady=10)

        c3_lbl=Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2, column=1,padx=10,pady=10)

        c4_lbl=Label(F4,text="Thumbs Up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=10,textvariable=self.thumbsup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3, column=1,padx=10,pady=10)

        c5_lbl=Label(F4,text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4, column=1,padx=10,pady=10)

        c6_lbl=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5, column=1,padx=10,pady=10)
        
        #===========Bill Area==========================
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=993,y=180,width=300,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        
        #============Button Frame======================
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=555,relwidth=1,height=150)

        m1_lbl=Label(F6,text="Total Cosmetics Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Cold Drinks Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl=Label(F6,text="Cosmetics Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(F6,text="Cold Drinks Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=730,width=540,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total", bg="cadetblue",fg="white",bd=2,pady=23,width=7,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F,text="Genrate Bill",command=self.bill_area, bg="cadetblue",fg="white",bd=2,pady=23,width=11,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text="Clear",command=self.clear_data, bg="cadetblue",fg="white",bd=2,pady=23,width=8,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app, bg="cadetblue",fg="white",bd=2,pady=23,width=7,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):
        self.co_s_pr=self.soap.get()*40
        self.co_fac_pr=self.face_cream.get()*120
        self.co_faw_pr=self.face_wash.get()*60
        self.co_has_pr=self.spray.get()*180
        self.co_hag_pr=self.gell.get()*140
        self.co_bol_pr=self.loshan.get()*190

        self.total_cosmetic_price=float(self.co_s_pr+self.co_fac_pr+self.co_faw_pr+self.co_has_pr+self.co_hag_pr+self.co_bol_pr)
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))

        self.gr_ri_pr=self.rice.get()*50
        self.gr_fdo_pr=self.food_oil.get()*130
        self.gr_dl_pr=self.daal.get()*70
        self.gr_wht_pr=self.wheat.get()*190
        self.gr_sur_pr=self.sugar.get()*150
        self.gr_te_pr=self.tea.get()*200

        self.total_grocery_price=float(self.gr_ri_pr+self.gr_fdo_pr+self.gr_dl_pr+self.gr_wht_pr+self.gr_sur_pr+self.gr_te_pr)
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        self.dr_mz_pr=self.maza.get()*30
        self.dr_ck_pr=self.cock.get()*110
        self.dr_frt_pr=self.frooti.get()*50
        self.dr_thp_pr=self.thumbsup.get()*170
        self.dr_lmc_pr=self.limca.get()*130
        self.dr_spr_pr=self.sprite.get()*180

        self.total_drinks_price=float(self.dr_mz_pr+self.dr_ck_pr+self.dr_frt_pr+self.dr_thp_pr+self.dr_lmc_pr+self.dr_spr_pr)
        self.cold_drink_price.set("Rs. "+str(self.total_drinks_price))
        self.cd_tax=round((self.total_drinks_price*0.05),2)
        self.cold_drink_tax.set("Rs. "+str(self.cd_tax))

        self.Total_bill=float(self.total_cosmetic_price+self.total_grocery_price+self.total_drinks_price+self.c_tax+self.g_tax+self.cd_tax)

    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\tWelcome Famous Retail\n")
        self.textarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone no.: {self.c_phone.get()}")
        self.textarea.insert(END,f"\n ===============================")
        self.textarea.insert(END,f"\n Products\t\t QTY\t Price")
        self.textarea.insert(END,f"\n ===============================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer Details Should be Filled")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","Product Not Purchased")
        else:
            self.welcome_bill()
            #=====cosmetics=======
            if self.soap.get()!=0:
                self.textarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t{self.co_s_pr}")
            if self.face_cream.get()!=0:
                self.textarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t{self.co_fac_pr}")
            if self.face_wash.get()!=0:
                self.textarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t{self.co_faw_pr}")
            if self.spray.get()!=0:
                self.textarea.insert(END,f"\n Hair Spray\t\t{self.spray.get()}\t{self.co_has_pr}")
            if self.gell.get()!=0:
                self.textarea.insert(END,f"\n Hair Gel\t\t{self.gell.get()}\t{self.co_hag_pr}")
            if self.loshan.get()!=0:
                self.textarea.insert(END,f"\n Body Loshan\t\t{self.loshan.get()}\t{self.co_bol_pr}")

            #=====Grocery=======
            if self.rice.get()!=0:
                self.textarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t{self.gr_ri_pr}")
            if self.food_oil.get()!=0:
                self.textarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t{self.gr_fdo_pr}")
            if self.daal.get()!=0:
                self.textarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t{self.gr_dl_pr}")
            if self.wheat.get()!=0:
                self.textarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t{self.gr_wht_pr}")
            if self.sugar.get()!=0:
                self.textarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t{self.gr_sur_pr}")
            if self.tea.get()!=0:
                self.textarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t{self.gr_te_pr}")

            #=====Drinks=======
            if self.maza.get()!=0:
                self.textarea.insert(END,f"\n Maza\t\t{self.maza.get()}\t{self.dr_mz_pr}")
            if self.cock.get()!=0:
                self.textarea.insert(END,f"\n Cock\t\t{self.cock.get()}\t{self.dr_ck_pr}")
            if self.frooti.get()!=0:
                self.textarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t{self.dr_frt_pr}")
            if self.thumbsup.get()!=0:
                self.textarea.insert(END,f"\n Thumbs Up\t\t{self.thumbsup.get()}\t{self.dr_thp_pr}")
            if self.limca.get()!=0:
                self.textarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t{self.dr_lmc_pr}")
            if self.sprite.get()!=0:
                self.textarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t{self.dr_spr_pr}")

            self.textarea.insert(END,f"\n -------------------------------")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Cosmetic Tax\t\t {self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Grocery Tax\t\t {self.grocery_tax.get()}")
            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Cold drink Tax\t\t {self.cold_drink_tax.get()}")

            self.textarea.insert(END,f"\n Total Bill : \t\t Rs. {self.Total_bill}")
            self.textarea.insert(END,f"\n -------------------------------")
            self.save_bills()

    def save_bills(self):
        op=messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op>0:
            self.bill_data=self.textarea.get('1.0', END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. {self.bill_no.get} Saved Successfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")

    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to Clear Data?")
        if op>0:
            #=============Cosmetics====================
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)

            #=============Grocery========================
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            #=============Cold Drinks====================
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            #=============Total Product Price & Tax variable====================
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            #============Customer=========
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")

            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            
            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()


root=Tk()
obj = Bill_App(root)
root.mainloop()