from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from data import *
#---------------------------------
db_voter=voter('voter')
db_candidate=voter('candidate')
Id=Camra()
#---------------------------------
windo=Tk()
windo.geometry("300x250+500+150")
windo.title("انتخاب")
stel=ttk.Style()
stel.theme_use('classic')
windo.resizable(width=False,height=False)
#--------------------------------
# p=ImageTk.PhotoImage(Image.open("tt.png"))
# p=ImageTk.PhotoImage(Image.open("t.png"))
# p=ImageTk.PhotoImage(Image.open("t.png"))
# p=ImageTk.PhotoImage(Image.open("t.png"))
neam_font='Times New Roman'
bg="#aafff0"
bg_B="#27d1b2"
fg="#241782"
e_n=StringVar()
#--------------------------------
def statistics():
    frim4=Frame(windo,bg=bg)
    frim4.place(x=0,y=0,width=300,height=500)
    windo.geometry("300x500+500+150")
    Label(frim4,text="عدد الاصوات",font=(neam_font,15),bg=bg,fg=fg).place(x=20,y=20)
    Label(frim4,text="الاسم",font=(neam_font,15),bg=bg,fg=fg).place(x=250,y=20)
    y=60
    for name,voter in db_candidate.serch_alll():
        Label(frim4,text=name,font=(neam_font,15),bg=bg,fg=fg).place(x=220,y=y,width=80,height=30)
        Label(frim4,text=voter,font=(neam_font,15),bg=bg,fg=fg).place(x=50,y=y)
        y+=40
        
    Button(frim4,text="رجوع",command=frim_def_1,bd=3,fg=fg,bg=bg_B).place(x=100,y=400,width=100,height=50)
def frim_def_1():
    e_n.set("")
    windo.geometry("300x250+500+150")
    frim1=Frame(windo,bg=bg)
    frim1.place(x=0,y=0,width=300,height=250)
    #--------------------button-------------------
    button_election=Button(frim1,text="انتخاب",command=frim_def_2,bd=3,fg=fg,bg=bg_B)
    button_election.place(x=20,y=50,width=100,height=50)
    button_counters=Button(frim1,text="احصائيات",bd=3,fg=fg,bg=bg_B,command=statistics)
    button_counters.place(x=180,y=50,width=100,height=50)
    button_exit=Button(frim1,text="خروج",command=windo.quit,bd=3,fg=fg,bg=bg_B)
    button_exit.place(x=100,y=150,width=100,height=50)
#-------------------------------------
def frim_def_2():
    windo.geometry("300x250+500+150")
    frim2=Frame(windo,bg=bg)
    frim2.place(x=0,y=0,width=300,height=300)
    e_i=StringVar()
    lest_name=[]
    for x in db_voter.serch("name"):
        lest_name.append(x[0])
    def get_id(event):
        idd=Id.camra_get().split("-")[0].strip()
        t=db_voter.serch_all("name","id",idd)
        print(t[0])
        e_n.set(" ")
        e_i.set(idd)
    def check():
        if e_n.get() in lest_name:
            if db_voter.serch_all("voter_t","name",e_n.get())[0]=="0":
                if e_i.get() == db_voter.serch_all("id","name",e_n.get())[0]:
                    frim_def_3()
                else:
                    messagebox.showinfo("info","رقم الهوية خطأ")
            else:
                messagebox.showinfo("info","الناخب قام بالانتخاب ")
        else:
            messagebox.showinfo("info","الاسم خطأ")
    #--------------------------------------------
    def focs(x):
        entry_Id_Number.focus()
    #--------------------label-------------------
    label_name=Label(frim2,text="اسم الناخب",font=(neam_font,15),bg=bg,fg=fg)
    label_name.place(x=200,y=20,width=100,height=50)
    label_Id_Number=Label(frim2,text="رقم الهويه",font=(neam_font,15),bg=bg,fg=fg)
    label_Id_Number.place(x=200,y=90,width=100,height=50)
    #--------------------entry-------------------
    entry_name=Entry(frim2,font=(neam_font,16),borderwidth=2,textvariable=e_n,justify="right")
    entry_name.place(x=90,y=60,width=200,height=30)
    entry_name.bind("<Return>",focs)
    entry_Id_Number=Entry(frim2,font=(neam_font,16),borderwidth=2,textvariable=e_i,justify="right")
    entry_Id_Number.place(x=90,y=130,width=200,height=30)
    #--------------------button-------------------
    button_next=Button(frim2,text="التالي",bg=bg_B,fg=fg,command=check)
    button_next.place(x=180,y=180,width=100,height=50)
    button_back=Button(frim2,text="رجوع",bg=bg_B,fg=fg,command=frim_def_1)
    button_back.place(x=20,y=180,width=100,height=50)
    windo.bind('<a>',get_id)
#----------------------------------------------
def frim_def_3():
    frim3=Frame(windo,bg=bg)
    frim3.place(x=0,y=0,width=300,height=500)
    windo.geometry("300x500+500+150")
    #----------------------------------
    rd=StringVar()
    i=0
    #-----------------def--------------
    def radio(x):
        yes_no=messagebox.askyesno("info","هل تريد انتخاب "+x)
        if yes_no:
            n_votes=int(db_candidate.serch_all("number","name",rd.get())[0])
            db_candidate.updet(str(n_votes+1),x)
            db_voter.updet_v("1",e_n.get())
            messagebox.showinfo("info","قمت بالانتخاب بنجاح")
            frim_def_1()
        else:
            return
    #----------------------------------
    for name in db_candidate.serch("name"):
        Radiobutton(frim3,text=name,font=(neam_font,20),
                    bg=bg,fg=fg,selectcolor="#12fff1",
                    variable=rd,value=name,
                    compound="left",indicatoron=0,
                    padx=100,).place(x=0,y=i,width=300,height=53)
        i+=53
    #------------------------------------
    button_election=Button(frim3,text="انتخاب",bg=bg_B,fg=fg,command=lambda:radio(rd.get()))
    button_election.place(x=180,y=400,width=100,height=50)
    button_back=Button(frim3,text="رجوع",bg=bg_B,fg=fg,command=frim_def_2)
    button_back.place(x=20,y=400,width=100,height=50)
frim_def_1()
windo.mainloop()