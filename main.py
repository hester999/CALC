from tkinter import *
from tkinter import ttk



class Calc():

    def __init__(self):


        self.form1 = Tk()
        self.style = ttk.Style()

        self.form1.geometry("500x500")

        self.form1['bg'] = '#2B2B2B'

        self.form1.title("Calc")


        try:
            self.form1.iconphoto(False,PhotoImage(file = "./fav/app_pic.png"))

        except:
            self.form1.iconbitmap()



        self.frame1 = Frame(self.form1, background='#2B2B2B')



        self.input_form = ttk.Entry(self.frame1)

        self.input_form.grid(row =0 ,column=0, columnspan= 6,ipady=50, ipadx=0,padx=0,sticky="NWES")


        self.Button_percent = ttk.Button(self.frame1, text="%").grid(row =1,column=0,sticky="NWES")
        self.Button_CE = ttk.Button(self.frame1, text="CE").grid(row =1,column=1,sticky="NWES")
        self.Button_C = ttk.Button(self.frame1, text="C").grid(row =1,column=2,sticky="NWES")
        self.Button_Del = ttk.Button(self.frame1, text="DEL").grid(row =1,column=3,sticky="NWES")

        self.Button_Unknow = ttk.Button(self.frame1, text = "1/x").grid(row =2, column=0, sticky="NWES")
        self.Button_POW = ttk.Button(self.frame1, text = "x^2").grid(row =2, column=1, sticky="NWES")
        self.Button_SQRT = ttk.Button(self.frame1, text = '\u221a').grid(row =2, column=2, sticky="NWES")





        self.Button_1 = ttk.Button(self.frame1,text = "7").grid(row =3,column=0,sticky="NWES")
        self.Button_2 = ttk.Button(self.frame1,text = "8").grid(row =3,column=1,sticky="NWES")
        self.Button_3 = ttk.Button(self.frame1,text = "9").grid(row =3,column=2,sticky="NWES")
        self.Button_4 = ttk.Button(self.frame1,text = "4").grid(row =4,column=0,sticky="NWES")
        self.Button_5 = ttk.Button(self.frame1,text = "5").grid(row =4,column=1,sticky="NWES")
        self.Button_6 = ttk.Button(self.frame1,text = "6").grid(row =4,column=2,sticky="NWES")
        self.Button_7 = ttk.Button(self.frame1,text = "1").grid(row =5,column=0,sticky="NWES")
        self.Button_8 = ttk.Button(self.frame1,text = "2").grid(row =5,column=1,sticky="NWES")
        self.Button_9 = ttk.Button(self.frame1,text = "3").grid(row =5,column=2,sticky="NWES")


        self.Button_Div = ttk.Button(self.frame1, text="/").grid(row=2, column=3, sticky="NWES")
        self.Button_Multiply = ttk.Button(self.frame1, text="X").grid(row=3, column=3, sticky="NWES")
        self.Button_Minus = ttk.Button(self.frame1, text="-").grid(row=4, column=3, sticky="NWES")
        self.Button_Plus = ttk.Button(self.frame1, text="+").grid(row = 5, column=3,sticky="NWES")

        self.Button_Negate = ttk.Button(self.frame1,text = "+/-").grid(row =6,column=0,sticky="NWES")
        self.Button_0 = ttk.Button(self.frame1, text="0").grid(row=6, column=1, sticky="NWES")
        self.Button_float = ttk.Button(self.frame1, text= ",").grid(row = 6,column=2,sticky="NWES")
        self.Button_Equal = ttk.Button(self.frame1, text= "=").grid(row = 6, column=3,sticky="NWES")

        # self.style.configure("TButton",foreground = "black")


        # Конфигурвтор колонки
        self.frame1.columnconfigure(0, minsize=60)
        self.frame1.columnconfigure(1, minsize=60)
        self.frame1.columnconfigure(2, minsize=60)
        self.frame1.columnconfigure(3, minsize=60)


        # Конфигурвтор ряда
        self.frame1.rowconfigure(1, minsize=60)
        self.frame1.rowconfigure(2, minsize=60)
        self.frame1.rowconfigure(3, minsize=60)
        self.frame1.rowconfigure(4, minsize=60)
        self.frame1.rowconfigure(5, minsize=60)
        self.frame1.rowconfigure(6, minsize=60)




        self.frame1.grid(padx=193.5,pady=5)


        self.form1.mainloop()





if __name__ == '__main__':

    Calc()

