from Tkinter import *
from tkMessageBox import *
import sqlite3
root5=Tk()
con=sqlite3.Connection('record')
cur=con.cursor()
root5.geometry('380x200')
ee6=0
Label(root5,text='         ').grid(row=0,column=0)
Label(root5,text='         ').grid(row=0,column=1)
Label(root5,text='WELCOME TO ATUL MOTORS',font='100',bg='orange').grid(row=0,column=2)
Label(root5,text=' ').grid(row=1,column=2)
def close():
    cl=askyesno('EXIT','ARE YOU SURE ?')
    if(cl==True):
        root5.destroy()
Label(root5,text=' ',).grid(row=5,column=2)
Button(root5,text='Exit',command=close,width='30',bg='light blue').grid(row=6,column=2)
def imp():
    v4=IntVar()
    v5=IntVar()
    v6=IntVar()
    v7= IntVar()
    v8=IntVar()
    v9=IntVar()
    v10=IntVar()
    v11=IntVar()
    v12=IntVar()
    v13=IntVar()
    v14=IntVar()
    v15=IntVar()
    v16=IntVar()
    v17=IntVar()
    v18=IntVar()
    v19=IntVar()
    v20=IntVar()
    v21=IntVar()
    v22=IntVar()
    v23=IntVar()
    v24=IntVar()
    v25=IntVar()
    v26=IntVar()
    v27=IntVar()
    global va
    global c23
    global c24
    global c25 
    global c
    global c1
    global c2
    global c3
    global c4
    global c5
    global c6
    global c7
    global c8
    global c9
    global c10
    global c11
    global c12
    global c13
    global c14
    global c15
    global c16
    global c17
    global c18
    global c19
    global c20
    global c21
    global c22
    root=Toplevel()
    cur.execute("create table if not exists cdb(name varchar(25) NOT NULL,address varchar(30) NOT NULL,contact_no number(12) NOT NULL,rno varchar(10) Primary key,tov varchar(10) NOT NULL,comp varchar(10) NOT NULL,model varchar(10) NOT NULL,d date NOT NULL,dt varchar(20) NOT NULL,mop varchar(10))")
    cur.execute("create table if not exists card(cno number(14),cvv number(4))")
    cur.execute("create table if not exists cdb2(rno varchar2(10) Primary key,s1 varchar(10),s2 varchar(10),s3 varchar(10),s4 varchar(10),s5 varchar(10),s6 varchar(10),s7 varchar(10),s8 varchar(10))")
    cur.execute("create table if not exists cdb1(rno varchar2(10) Primary key,inter varchar(10),exter varchar(10),s1 varchar(10),s2 varchar(10),s3 varchar(10),s4 varchar(10),s5 varchar(10),s6 varchar(10),s7 varchar(10),s8 varchar(10),s9 varchar(10),s10 varchar(10),s11 varchar(10),s12 varchar(10),s13 varchar(10),s14 varchar(10),s15 varchar(10),s16 varchar(10),s17 varchar(10),s18 varchar(10),s19 varchar(10),s20 varchar(10),s21 varchar(10),s22 varchar(10),s23 varchar(10),s24 varchar(10))")
    cur.execute("create table if not exists entry(ent number(10),rno varchar2(10) Primary key)")
    root.title('SUVANSH AGRAWAL')
    Label(root,text='SERVICE CENTER',font='70',bg='green').grid(row=1,column=1)
    Label(root,text='').grid(row=3,column=0)
    Label(root,text='').grid(row=4,column=0)
    Label(root,text='  NAME   ',relief=GROOVE).grid(row=5,column=0,sticky=N+S+E+W)
    e=Entry(root,width='30')
    e.grid(row=5,column=1,columnspan=10)
    Label(root,text='ADDRESS',relief=GROOVE).grid(row=6,column=0,sticky=N+S+E+W)
    e1=Entry(root,width='30')
    e1.grid(row=6,column=1,columnspan=10)
    Label(root,text='CONTACT NO',relief=GROOVE).grid(row=7,column=0,sticky=N+S+E+W)
    e2=Entry(root,width='30')
    e2.grid(row=7,column=1,columnspan=10)
    Label(root,text='R No:',relief=GROOVE).grid(row=8,column=0,sticky=N+S+E+W)
    e3=Entry(root,width='30')
    e3.grid(row=8,column=1,columnspan=10)
    Label(root,text="type of Vehicle: " ,relief=GROOVE).grid(row=9,column=0,sticky=N+S+E+W)
    variable=StringVar(root)
    variable.set("select")
    w=OptionMenu(root,variable,"LMV","MUV","HEAVY")
    w.grid(row=9,column=1,columnspan=10)
    Label(root,text='CAR',relief=GROOVE).grid(row=10,column=0,sticky=N+S+W)
    Label(root,text='Company',relief=GROOVE).grid(row=10,column=0,sticky=N+S+E)
    e4=Entry(root,width='15')
    e4.grid(row=10,column=1,columnspan=10)
    Label(root,text='  Model  ',relief=GROOVE).grid(row=11,column=0,sticky=N+S+E)
    e5=Entry(root,width='15')
    e5.grid(row=11,column=1,columnspan=10)
    Label(root,text='DATE',relief=GROOVE).grid(row=12,column=0,sticky=N+S+E+W)
    variable1=StringVar(root)
    variable1.set("D")
    w1=OptionMenu(root,variable1,"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
    w1.grid(row=12,column=1,sticky=N+S+E)
    variable2=StringVar(root)
    variable2.set("M")
    w2=OptionMenu(root,variable2,"JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC")
    w2.grid(row=12,column=2,sticky=N+S+E+W)
    variable3=StringVar(root)
    variable3.set("Y")
    w3=OptionMenu(root,variable3,"2018","2019","2020","2021","2022")
    w3.grid(row=12,column=3,sticky=W+N+S)
    Label(root,text='Damage Type ',relief=GROOVE).grid(row=13,column=0,sticky=N+E+W+S)
    v1=IntVar(root)
    Radiobutton(root,text='Accidental Damage',variable=v1,value=1).grid(row=13,column=1,sticky=N+E+W+S)
    Radiobutton(root,text='Major Damage',variable=v1,value=2).grid(row=13,column=2,sticky=N+S+W)
    Radiobutton(root,text='Quick Repair And Service',variable=v1,value=3).grid(row=13,column=3,sticky=N+S+W)
    def c():
        d=variable1.get()+'-'+variable2.get()+'-'+variable3.get()
        def error():
            global tod
            if(v1.get()==1):
                tod="Accidental Damage"
            if(v1.get()==2):
                tod="Major Damage"
            if(v1.get()==3):
                tod="Quick Repair And Service"
            v30=StringVar(root)
            if not e.get():
                showerror("ERROR","NAME NOT MENTIONED")
            if not e1.get():
                showerror("ERROR","ADDRESS NOT MENTIONED")
            if not e2.get() or len(e2.get())>10 or len(e2.get())<10:
                showerror("ERROR","CONTACT NO NOT MENTIONED")
            if not e3.get():
                showerror("ERROR","R NO NOT MENTIONED")
            if not e4.get():
                showerror("ERROR","COMPANY NOT MENTIONED")
            if not e5.get():
                showerror("ERROR","MODEL NOT MENTIONED")
            if variable.get()=='select':
                showerror("ERROR","TYPE OF VEHICLE NOT SELECTED")
            if variable1.get()=='D':
                showerror("ERROR","DATE NOT SELECTED")
            if variable2.get()=='M':
                showerror("ERROR","MONTH NOT SELECTED")
            if variable3.get()=='Y':
                showerror("ERROR","YEAR NOT SELECTED")
            else:
                cl=askyesno('Are you done','Sure youre done ?')
                if(cl==True):
                    cur.execute("insert into cdb values(?,?,?,?,?,?,?,?,?,?)",(e.get(),e1.get(),e2.get(),e3.get(),variable.get(),e4.get(),e5.get(),d,tod,mop))
                    con.commit()
                    showinfo("successful","ENTRY SUCCESSFUL")
                    root.destroy()
        if(v1.get()==1):
            Label(root,text='Mode of payment',relief=GROOVE).grid(row=18,column=0,sticky=N+E+W+S)
            v30=IntVar(root)
            Radiobutton(root,text='CASH',variable=v30,value=1).grid(row=18,column=1,sticky=N+E+W+S)
            Radiobutton(root,text='CARD',variable=v30,value=2).grid(row=18,column=2,sticky=N+E+W+S)
            def y1():
                global mop
                if(v30.get()==1):
                    mop="CASH"
                if(v30.get()==2):
                    mop="CARD"   
                if(v30.get()==1):
                    Button(root,text="SUBMIT",command=error).grid(row=20,column=2)
                if(v30.get()==2):
                    root3=Toplevel()
                    Label(root3,text='CARD GATEWAY',font='50',bg='blue').grid(row=0,column=2)
                    Label(root3,text='CARD NUMBER').grid(row=1,column=0)
                    Label(root3,text=' ').grid(row=1,column=1)
                    e11=Entry(root3)
                    e11.grid(row=1,column=2)
                    Label(root3,text='CVV NO').grid(row=2,column=0)
                    Label(root3,text=' ').grid(row=2,column=1)
                    e12=Entry(root3)
                    e12.grid(row=2,column=2)
                    def y3():
                        cl=askyesno('Are you done','Sure youre done ?')
                        if(cl==True):
                            cur.execute("insert into card values(?,?)",(e11.get(),e12.get()))
                            con.commit()
                            root3.destroy()
                        Button(root,text="SUBMIT",command=error).grid(row=20,column=2)
                    Button(root3,text='OKAY',command=y3).grid(row=3,column=2)
            Button(root,text='SELECT',command=y1).grid(row=19,column=3)
        if(v1.get()==3):
            Label(root,text='Service No',relief=GROOVE).grid(row=16,column=0)
            e6=Entry(root,width='3')
            e6.grid(row=16,column=1,columnspan=10)
            
            def g():
                cur.execute("insert into entry values(?,?)",(e6.get(),e3.get()))
                if(int(e6.get())>3):
                    Label(root,text='free service over').grid(row=17,column=1)
                    def g1():
                        root2=Toplevel()
                        Label(root2,text='SELECT',font='40').grid(row=0,column=0)
                        v7=IntVar()
                        v8=IntVar()
                        v9=IntVar()
                        v10=IntVar()
                        v11=IntVar()
                        v12=IntVar()
                        v13=IntVar()
                        v14=IntVar()
                        Checkbutton(root2,text='AC',variable=v7,onvalue=1).grid(row=1,column=0,sticky=N+S+W)
                        Checkbutton(root2,text='ENGINE CHECK',variable=v8,onvalue=1).grid(row=1,column=1,sticky=N+S+W)
                        Checkbutton(root2,text='BRAKE PADS',variable=v9,onvalue=1).grid(row=2,column=0,sticky=N+S+W)
                        Checkbutton(root2,text='ECG',variable=v10,onvalue=1).grid(row=2,column=1,sticky=N+S+W)
                        Checkbutton(root2,text='ELECTRIC',variable=v11,onvalue=1).grid(row=3,column=0,sticky=N+S+W)
                        Checkbutton(root2,text='GEAR BOX',variable=v12,onvalue=1).grid(row=3,column=1,sticky=N+S+W)
                        Checkbutton(root2,text='GEAR LEVER',variable=v13,onvalue=1).grid(row=4,column=0,sticky=N+S+W)
                        Checkbutton(root2,text='NOT MENTIONED',variable=v14,onvalue=1).grid(row=4,column=1,sticky=N+S+W)
                        def y():
                            if(v7.get()==1):
                                c="AC"
                            else:
                                c=" "
                            if(v8.get()==1):
                                c1="ENGINE CHECK"
                            else:
                                c1=" "
                            if(v9.get()==1):
                                c2="BRAKE PADS"
                            else:
                                c2=" "
                            if(v10.get()==1):
                                c3="ECG"
                            else:
                                c3=" "
                            if(v11.get()==1):
                                c4="ELECTRIC"
                            else:
                                c4=" "
                            if(v12.get()==1):
                                c5="GEAR BOX"
                            else:
                                c5=" "
                            if(v13.get()==1):
                                c6="GEAR LEVER"
                            else:
                                c6=" "
                            if(v14.get()==1):
                                c7="NOT MENTIONED"
                            else:
                                c7=" "
                            cl=askyesno('Are you done','Sure youre done ?')
                            if(cl==True):
                                cur.execute("insert into cdb2 values(?,?,?,?,?,?,?,?,?)",(e3.get(),c,c1,c2,c3,c4,c5,c6,c7))
                                con.commit()
                                root2.destroy()
                            print v9.get()
                            Label(root,text='Mode of payment',relief=GROOVE).grid(row=18,column=0,sticky=N+E+W+S)
                            v30=IntVar(root)
                            Radiobutton(root,text='CASH',variable=v30,value=1).grid(row=18,column=1,sticky=N+E+W+S)
                            Radiobutton(root,text='CARD',variable=v30,value=2).grid(row=18,column=2,sticky=N+E+W+S)
                            Radiobutton(root,text='FREE',variable=v30,value=3).grid(row=18,column=3,sticky=N+E+W+S)
                            def y1():
                                global mop
                                if(v30.get()==1):
                                    mop="CASH"
                                if(v30.get()==2):
                                    mop="CARD"
                                if(v30.get()==3):
                                    mop="FREE"
                                if(v30.get()==1):
                                    Button(root,text="SUBMIT",command=error).grid(row=20,column=2)
                                if(v30.get()==2):
                                    root3=Toplevel()
                                    Label(root3,text='CARD GATEWAY',font='50',bg='blue').grid(row=0,column=1)
                                    Label(root3,text='CARD NUMBER').grid(row=1,column=0)
                                    Label(root3,text=' ').grid(row=1,column=1)
                                    e11=Entry(root3)
                                    e11.grid(row=1,column=2)
                                    Label(root3,text='CVV NO').grid(row=2,column=0)
                                    Label(root3,text=' ').grid(row=2,column=1)
                                    e12=Entry(root3)
                                    e12.grid(row=2,column=2)
                                    def y3():
                                        cl=askyesno('Are you done','Sure youre done ?')
                                        if(cl==True):
                                            cur.execute("insert into card values(?,?)",(e11.get(),e12.get()))
                                            con.commit()
                                            root3.destroy()
                                        Button(root,text="SUBMIT",command=error).grid(row=20,column=2)
                                    Button(root3,text='OKAY',command=y3).grid(row=3,column=2)
                            Button(root,text='SELECT',command=y1).grid(row=19,column=3)
                        Button(root2,text="Done",command=y).grid(row=5,column=2)
                    Button(root,text='Continue',command=g1).grid(row=17,column=2)
                else:
                    Label(root,text="you're in for free servicing ").grid(row=17,column=1)
                    Label(root,text='Mode of payment',relief=GROOVE).grid(row=18,column=0,sticky=N+E+W+S)
                    v30=IntVar(root)
                    Radiobutton(root,text='CASH',variable=v30,value=1).grid(row=18,column=1,sticky=N+E+W+S)
                    Radiobutton(root,text='CARD',variable=v30,value=2).grid(row=18,column=2,sticky=N+E+W+S)
                    Radiobutton(root,text='FREE',variable=v30,value=3).grid(row=18,column=3,sticky=N+E+W+S)
                    def y3():
                        Button(root,text="SUBMIT",command=error).grid(row=20,column=2)        
                    Button(root,text='SELECT',command=y3).grid(row=19,column=3)        
            Button(root,text='OK',command=g).grid(row=16,column=3)
        if(v1.get()==2):
            va="Major Damage"
            v2=IntVar()
            v3=IntVar()    
            root1=Toplevel()
            Label(root1,text="MAJOR DAMAGE").grid(row=0,column=0,columnspan=10)
            Label(root1,text="COMPLAINS",relief=GROOVE,width='15').grid(row=1,column=0)
            def y():
                if(v7.get()==1):
                    c="AC"
                else:
                    c=" "
                if(v8.get()==1):
                    c1="STEERING"
                else:
                    c1=" "
                if(v9.get()==1):
                    c2="SEAT"
                else:
                    c2=" "
                if(v10.get()==1):
                    c3="MUSIC SYSTEM"
                else:
                    c3=" "
                if(v11.get()==1):
                    c4="CLUTCH"
                else:
                    c4=" "
                if(v12.get()==1):
                    c5="NOT MENTIONED"
                else:
                    c5=" "
                if(v13.get()==1):
                    c6="OIL PROBLEM"
                else:
                    c6=" "
                if(v14.get()==1):
                    c7="HEATING"
                else:
                    c7=" "
                if(v15.get()==1):
                    c8="SPARK PLUG"
                else:
                    c8=" "
                if(v16.get()==1):
                    c9="SENSOR PROBLEM"
                else:
                    c9=" "
                if(v17.get()==1):
                    c10="NOT MENTIONED"
                else:
                    c10=" "
                if(v18.get()==1):
                    c11="BUMPER"
                else:
                    c11=" "
                if(v19.get()==1):
                    c12="BONNET"
                else:
                    c12=" "
                if(v20.get()==1):
                    c13="FENDER"
                else:
                    c13=" "
                if(v21.get()==1):
                    c14="FASCIA"
                else:
                    c14=" "
                if(v22.get()==1):
                    c15="DECKLID"
                else:
                    c15=" "
                if(v23.get()==1):
                    c16="ROOF"
                else:
                    c16=" "
                if(v24.get()==1):
                    c17="RIM"
                else:
                    c17=" "
                if(v25.get()==1):
                    c18="SPOILER"
                else:
                    c18=" "
                if(v26.get()==1):
                    c19="QUATER PANEL"
                else:
                    c19=" "
                if(v27.get()==1):
                    c20="NOT MENTIONED"
                else:
                    c20=" "
                if(v4.get()==1):
                    c23="CABIN"
                else:
                    c23=" "
                if(v5.get()==1):
                    c24="ENGINE"
                else:
                    c24=" "
                if(v6.get()==1):
                    c25="BODY"
                else:
                    c25=" "
                if(v2.get()==1):
                    c21="INTERIOR"
                else:
                    c21=" "
                if(v3.get()==1):
                    c22="EXTERIOR"
                else:
                    c22=" "
                cl=askyesno('Are you done','Sure youre done ?')
                if(cl==True):
                    cur.execute("insert into cdb1 values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(e3.get(),c21,c22,c23,c24,c25,c,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20))
                    con.commit()
                    root1.destroy()
                Label(root,text='Mode of payment',relief=GROOVE).grid(row=18,column=0,sticky=N+E+W+S)
                v30=IntVar(root)
                Radiobutton(root,text='CASH',variable=v30,value=1).grid(row=18,column=1,sticky=N+E+W+S)
                Radiobutton(root,text='CARD',variable=v30,value=2).grid(row=18,column=2,sticky=N+E+W+S)
                def y1():
                    global mop
                    if(v30.get()==1):
                        mop="CASH"
                    if(v30.get()==2):
                        mop="CARD"   
                    if(v30.get()==1):
                        Button(root,text="SUBMIT",command=error).grid(row=20,column=2)
                    if(v30.get()==2):
                        root3=Toplevel()
                        Label(root3,text='CARD GATEWAY',font='50',bg='blue').grid(row=0,column=2)
                        Label(root3,text='CARD NUMBER').grid(row=1,column=0)
                        Label(root3,text=' ').grid(row=1,column=1)
                        e11=Entry(root3)
                        e11.grid(row=1,column=2)
                        Label(root3,text='CVV NO').grid(row=2,column=0)
                        Label(root3,text='').grid(row=2,column=1)
                        e12=Entry(root3)
                        e12.grid(row=2,column=2)
                        def y3():
                            cl=askyesno('Are you done','Sure youre done ?')
                            if(cl==True):
                                cur.execute("insert into card values(?,?)",(e11.get(),e12.get()))
                                con.commit()
                                root3.destroy()
                            Button(root,text="SUBMIT",command=error).grid(row=20,column=2)
                        Button(root3,text="OKAY",command=y3).grid(row=3,column=2)
                Button(root,text='SELECT',command=y1).grid(row=19,column=3)
            def de():
                Button(root1,text='Done',command=y).grid(row=13,column=3)
                global c23
                global c24
                global c25 
                global c
                global c1
                global c2
                global c3
                global c4
                global c5
                global c6
                global c7
                global c8
                global c9
                global c10
                global c11
                global c12
                global c13
                global c14
                global c15
                global c16
                global c17
                global c18
                global c19
                global c20
                global c21
                global c22
                def h():
                    if(v7.get()==1 or v8.get()==1 or v9.get()==1 or v10.get()==1 or v11.get()==1 or v12.get()==1 or v13.get()==1 or v14.get()==1 or v15.get()==1 or v16.get()==1 or v17.get()==1 or v18.get()==1 or v19.get()==1 or v20.get()==1 or v21.get()==1 or v22.get()==1 or v23.get()==1 or v24.get()==1 or v25.get()==1 or v26.get()==1 or v27.get()==1):
                        c=askquestion('WARRANTY','Product is in warranty ?')
                    
                def e():
                        if(v4.get()==1):
                            Checkbutton(root1,text='AC',command=h,variable=v7,onvalue=1).grid(row=3,column=0,sticky=N+S+W,columnspan=8)
                            Checkbutton(root1,text='STEERING',command=h,variable=v8,onvalue=1).grid(row=4,column=0,sticky=N+S+W,columnspan=8)
                            Checkbutton(root1,text='SEAT',command=h,variable=v9,onvalue=1).grid(row=5,column=0,sticky=N+S+W,columnspan=8)
                            Checkbutton(root1,text='MUSIC SYSTEM',command=h,variable=v10,onvalue=1).grid(row=6,column=0,sticky=N+S+W,columnspan=8)
                            Checkbutton(root1,text='CLUTCH PLATES',command=h,variable=v11,onvalue=1).grid(row=7,column=0,sticky=N+S+W,columnspan=8)
                            Checkbutton(root1,text='NOT MENTION',variable=v12,onvalue=1).grid(row=8,column=0,sticky=N+S+W,columnspan=8)
                def f():
                        if(v5.get()==1):
                            Checkbutton(root1,text='OIL PROBLEM',command=h,variable=v13,onvalue=1,).grid(row=3,column=1,sticky=N+S+W,columnspan=20)
                            Checkbutton(root1,text='HEATING',command=h,variable=v14,onvalue=1).grid(row=4,column=1,sticky=N+S+W,columnspan=20)
                            Checkbutton(root1,text='SPARK PLUG',command=h,variable=v15,onvalue=1).grid(row=5,column=1,sticky=N+S+W,columnspan=20)
                            Checkbutton(root1,text='SENSOR PROBLEM',command=h,variable=v16,onvalue=1).grid(row=6,column=1,sticky=N+S+W,columnspan=20)
                            Checkbutton(root1,text='NOT MENTION',variable=v17,onvalue=1).grid(row=7,column=1,sticky=N+S+W,columnspan=20)
                def g():
                        if(v6.get()==1):
                            Checkbutton(root1,text='BUMPER',command=h,variable=v18,onvalue=1,).grid(row=3,column=2,sticky=N+S+W)
                            Checkbutton(root1,text='BONNET',command=h,variable=v19,onvalue=1).grid(row=4,column=2,sticky=N+S+W)
                            Checkbutton(root1,text='FENDER',command=h,variable=v20,onvalue=1).grid(row=5,column=2,sticky=N+S+W)
                            Checkbutton(root1,text='FASCIA',command=h,variable=v21,onvalue=1).grid(row=6,column=2,sticky=N+S+W)
                            Checkbutton(root1,text='DECKLID',command=h,variable=v22,onvalue=1).grid(row=7,column=2,sticky=N+S+W)
                            Checkbutton(root1,text='ROOF',command=h,variable=v23,onvalue=1).grid(row=8,column=2,sticky=N+S+W)
                            Checkbutton(root1,text='RIM',command=h,variable=v24,onvalue=1).grid(row=9,column=2,sticky=N+S+W)
                            Checkbutton(root1,text='SPOILER',command=h,variable=v25,onvalue=1).grid(row=10,column=2,sticky=N+S+W)
                            Checkbutton(root1,text='QUATER PANEL',command=h,variable=v26,onvalue=1).grid(row=11,column=2,sticky=N+S+W)
                            Checkbutton(root1,text='NOT MENTIONED',command=h,variable=v27,onvalue=1).grid(row=12,column=2,sticky=N+S+W)

                if(v2.get()==1):
                    Checkbutton(root1,text='cabin',command=e,variable=v4,onvalue=1).grid(row=2,column=0,sticky=N+W+S,columnspan=8)
                    Checkbutton(root1,text='Engine',command=f,variable=v5,onvalue=1).grid(row=2,column=1)
                if(v3.get()==1):
                    Checkbutton(root1,text='Body',command=g,variable=v6,onvalue=1).grid(row=2,column=2)
            Checkbutton(root1,text='Interior',variable=v2,command=de,onvalue=1,width='15').grid(row=1,column=1)
            Checkbutton(root1,text='Exterior',variable=v3,command=de,onvalue=1).grid(row=1,column=2)
            
    Button(root,text='OK',command=c).grid(row=15,column=2)
    root.mainloop()
def search():
    root6=Toplevel()
    root6.geometry('260x120')
    Label(root6,text='SEARCH WINDOW',font='100',bg='purple').grid(row=0,column=2,columnspan=40)
    Label(root6,text='         ').grid(row=1,column=1)
    Label(root6,text='         ').grid(row=2,column=1)
    Label(root6,text='         ').grid(row=3,column=0)
    Label(root6,text='R NO',relief=GROOVE).grid(row=3,column=1,sticky=N+W+S)
    q1=Entry(root6)
    q1.grid(row=3,column=3)
    def go():
        root7=Toplevel()
        sqlText="select * from cdb where rno = '"+q1.get()+"'"
        cur.execute(sqlText)
        a=cur.fetchall()
        print a
        name=a[0][0]
        addr=a[0][1]
        cont=a[0][2]
        regn=a[0][3]
        typ=a[0][4]
        comp=a[0][5]
        mode=a[0][6]
        date=a[0][7]
        tod=a[0][8]
        mop=a[0][9]
        Label(root7,text='NAME',relief=RIDGE).grid(row=0,column=0,sticky=N+E+W+S)
        Label(root7,text=name).grid(row=0,column=2,sticky=N+E+W+S)
        Label(root7,text=' ').grid(row=0,column=1)
        Label(root7,text=' ').grid(row=1,column=0)
        Label(root7,text='Address',relief=RIDGE).grid(row=2,column=0,sticky=N+E+W+S)
        Label(root7,text=addr).grid(row=2,column=2,sticky=N+E+W+S)
        Label(root7,text=' ').grid(row=2,column=1)
        Label(root7,text=' ').grid(row=3,column=0)
        Label(root7,text='Contact NO',relief=RIDGE).grid(row=4,column=0,sticky=N+E+W+S)
        Label(root7,text=cont).grid(row=4,column=2,sticky=N+E+W+S)
        Label(root7,text=' ').grid(row=4,column=1)
        Label(root7,text=' ').grid(row=5,column=0)
        Label(root7,text='Registration No',relief=RIDGE).grid(row=6,column=0,sticky=N+E+W+S)
        Label(root7,text=regn).grid(row=6,column=2,sticky=N+E+W+S)
        Label(root7,text=' ').grid(row=6,column=1)
        Label(root7,text=' ').grid(row=7,column=0)
        Label(root7,text='Type of Vehicle',relief=RIDGE).grid(row=8,column=0,sticky=N+E+W+S)
        Label(root7,text=typ).grid(row=8,column=2,sticky=N+E+W+S)
        Label(root7,text=' ').grid(row=8,column=1)
        Label(root7,text=' ').grid(row=9,column=0)
        Label(root7,text='Company',relief=RIDGE).grid(row=10,column=0,sticky=N+E+W+S)
        Label(root7,text=comp).grid(row=10,column=2,sticky=N+E+W+S)
        Label(root7,text=' ').grid(row=10,column=1)
        Label(root7,text=' ').grid(row=11,column=0)
        Label(root7,text='Model',relief=RIDGE).grid(row=12,column=0,sticky=N+E+W+S)
        Label(root7,text=mode).grid(row=12,column=2,sticky=N+E+W+S)
        Label(root7,text=' ').grid(row=12,column=1)
        Label(root7,text=' ').grid(row=13,column=0)
        Label(root7,text='Date',relief=RIDGE).grid(row=14,column=0,sticky=N+E+W+S)
        Label(root7,text=date).grid(row=14,column=2,sticky=N+E+W+S)
        Label(root7,text=' ').grid(row=14,column=1)
        Label(root7,text=' ').grid(row=15,column=0)
        Label(root7,text='Type of Damage',relief=RIDGE).grid(row=16,column=0,sticky=N+E+W+S)
        Label(root7,text=tod).grid(row=16,column=2,sticky=N+E+W+S)
        Label(root7,text=' ').grid(row=16,column=1)
        Label(root7,text=' ').grid(row=17,column=0)
        Label(root7,text='Mode of Payment',relief=RIDGE).grid(row=18,column=0,sticky=N+E+W+S)
        Label(root7,text=mop).grid(row=18,column=2,sticky=N+E+W+S)
        Label(root7,text=' ').grid(row=18,column=1)
        Label(root7,text=' ').grid(row=19,column=0)
        sqlText2="select ent from entry where rno = '"+q1.get()+"'"
        cur.execute(sqlText2)
        a1=cur.fetchall()
        if(a1!=[]):
            xy=a1[0][0]
            if(xy>3):
                Label(root7,text='Parts',relief=RIDGE).grid(row=20,column=0,sticky=N+E+W+S)
                Label(root7,text="  ").grid(row=21,column=0)
                Label(root7,text="  ").grid(row=21,column=1)
                sqlText1="select * from cdb2 where rno = '"+q1.get()+"'"
                cur.execute(sqlText1)
                b=cur.fetchall()
                rno=b[0][0]
                s=b[0][1]
                s1=b[0][2]
                s2=b[0][3]
                s3=b[0][4]
                s4=b[0][5]
                s5=b[0][6]
                s6=b[0][7]
                s7=b[0][8]
                j=20
                if(s==" "):
                    print s
                else:
                    Label(root7,text=b[0][1]).grid(row=j,column=2)
                    j=j+1
                if(s1==" "):
                    print s1
                else:
                    Label(root7,text=b[0][2]).grid(row=j,column=2)
                    j=j+1
                if(s2==" "):
                    print s2
                else:
                    Label(root7,text=b[0][3]).grid(row=j,column=2)
                    j=j+1
                if(s3==" "):
                    print s3
                else:
                    Label(root7,text=b[0][4]).grid(row=j,column=2)
                    j=j+1
                if(s4==" "):
                    print s4
                else:
                    Label(root7,text=b[0][5]).grid(row=j,column=2)
                    j=j+1
                if(s5==" "):
                    print s5
                else:
                    Label(root7,text=b[0][6]).grid(row=j,column=2)
                    j=j+1
                if(s6==" "):
                    print s6
                else:
                    Label(root7,text=b[0][7]).grid(row=j,column=2)
                    j=j+1
                if(7==" "):
                    print s7
                else:
                    Label(root7,text=b[0][8]).grid(row=j,column=2)
                    j=j+1
        sqlText4="select * from cdb1 where rno = '"+q1.get()+"'"
        cur.execute(sqlText4)
        ch=cur.fetchall()
        Label(root7,text=' ').grid(row=20,column=3)
        print ch
        if(ch!=[]):
            Label(root7,text="PARTS",relief=RIDGE).grid(row=20,column=0,sticky=N+E+W+S)
            j=20
            if(ch[0][1]==" "):
                print ch[0][1]
            else:
                Label(root7,text=ch[0][1],relief=RAISED).grid(row=20,column=2)
                j=j+1
                if(ch[0][3]==" "):
                    print ch[0][3]
                else:
                    Label(root7,text=ch[0][3],relief=RAISED).grid(row=21,column=2)
                    j=22
                    if(ch[0][6]==" "):
                        print ch[0][6]
                    else:
                        Label(root7,text=ch[0][6]).grid(row=j,column=2)
                        j=j+1
                    if(ch[0][7]==" "):
                        print ch[0][7]
                    else:
                        Label(root7,text=ch[0][7]).grid(row=j,column=2)
                        j=j+1
                    if(ch[0][8]==" "):
                        print ch[0][8]
                    else:
                        Label(root7,text=ch[0][8]).grid(row=j,column=2)
                        j=j+1
                    if(ch[0][9]==" "):
                        print ch[0][9]
                    else:
                        Label(root7,text=ch[0][9]).grid(row=j,column=2)
                        j=j+1
                    if(ch[0][10]==" "):
                        print ch[0][10]
                    else:
                        Label(root7,text=ch[0][10]).grid(row=j,column=2)
                        j=j+1
                    if(ch[0][11]==" "):
                        print ch[0][11]
                    else:
                        Label(root7,text=ch[0][11]).grid(row=j,column=2)
                        j=j+1
                if(ch[0][4]==" "):
                    print ch[0][4]
                else:
                    Label(root7,text=ch[0][4],relief=RAISED).grid(row=21,column=3)
                    j=22
                    if(ch[0][12]==" "):
                        print ch[0][12]
                    else:
                        Label(root7,text=ch[0][12]).grid(row=j,column=3)
                        j=j+1
                    if(ch[0][13]==" "):
                        print ch[0][13]
                    else:
                        Label(root7,text=ch[0][13]).grid(row=j,column=3)
                        j=j+1
                    if(ch[0][14]==" "):
                        print ch[0][14]
                    else:
                        Label(root7,text=ch[0][14]).grid(row=j,column=3)
                        j=j+1
                    if(ch[0][15]==" "):
                        print ch[0][15]
                    else:
                        Label(root7,text=ch[0][15]).grid(row=j,column=3)
                        j=j+1
                    if(ch[0][16]==" "):
                        print ch[0][16]
                    else:
                        Label(root7,text=ch[0][16]).grid(row=j,column=3)
                        j=j+1
            if(ch[0][2]==" "):
                print ch[0][2]
            else:
                Label(root7,text=ch[0][2],relief=RAISED).grid(row=20,column=4)
                j=j+1
                if(ch[0][5]==" "):
                    print ch[0][5]
                else:
                    Label(root7,text=ch[0][5],relief=RAISED).grid(row=21,column=4)
                    j=22
                    if(ch[0][17]==" "):
                        print ch[0][17]
                    else:
                        Label(root7,text=ch[0][17]).grid(row=j,column=4)
                        j=j+1
                    if(ch[0][18]==" "):
                        print ch[0][18]
                    else:
                        Label(root7,text=ch[0][18]).grid(row=j,column=4)
                        j=j+1
                    if(ch[0][19]==" "):
                        print ch[0][19]
                    else:
                        Label(root7,text=ch[0][9]).grid(row=j,column=4)
                        j=j+1
                    if(ch[0][20]==" "):
                        print ch[0][20]
                    else:
                        Label(root7,text=ch[0][20]).grid(row=j,column=4)
                        j=j+1
                    if(ch[0][21]==" "):
                        print ch[0][21]
                    else:
                        Label(root7,text=ch[0][21]).grid(row=j,column=4)
                        j=j+1
                    if(ch[0][22]==" "):
                        print ch[0][22]
                    else:
                        Label(root7,text=ch[0][22]).grid(row=j,column=4)
                        j=j+1
                    if(ch[0][23]==" "):
                        print ch[0][23]
                    else:
                        Label(root7,text=ch[0][23]).grid(row=j,column=4)
                        j=j+1
                    if(ch[0][24]==" "):
                        print ch[0][24]
                    else:
                        Label(root7,text=ch[0][24]).grid(row=j,column=4)
                        j=j+1
                    if(ch[0][25]==" "):
                        print ch[0][25]
                    else:
                        Label(root7,text=ch[0][25]).grid(row=j,column=4)
                        j=j+1
                    if(ch[0][26]==" "):
                        print ch[0][26]
                    else:
                        Label(root7,text=ch[0][26]).grid(row=j,column=4)
                        j=j+1
            
    Button(root6,text='GO',command=go).grid(row=3,column=4)
Button(root5,text='SEARCH',command=search,width='30',bg='light blue').grid(row=2,column=2)
Label(root5,text=' ').grid(row=3,column=2)
Button(root5,text='ADD NEW',command=imp,width='30',bg='light blue').grid(row=4,column=2)
root5.mainloop()
