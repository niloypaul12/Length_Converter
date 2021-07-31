from tkinter import * #* means everything. so we are importing everything from tkinter.

App = Tk()
App.title('Length Converter') #title of the app
App.geometry('350x150') #size ratio width* length
scales = ['Meters', 'Inches', 'Foot','Cm','Km',] #all the units that we want to measure. can add more.

_from = StringVar()
from_menu = OptionMenu(App, _from, *scales)
from_menu.grid(row=0,column=0, pady = 5)

lbl = Label(App, text = 'Convert to ')
lbl.grid(row =0, column =1, pady = 5)

to_ = StringVar()
to_menu = OptionMenu(App, to_, *scales)
to_menu.grid(row=0,column=2, pady = 5)

enterL= Label(App, text='Length Here ')
enterL.grid(row=1, column=0, columnspan = 1, pady = 5)

numE = Entry(App)
numE.grid(row=1, column=1, columnspan= 2, pady=5)

def converter():
    From = _from.get()
    To= to_.get()
    num = float(numE.get())

    if From == 'Meters' and To== 'Inches':
        conv_num = num * 39.37
    elif From == 'Meters' and To == 'Foot':
        conv_num = num * 3.28
    elif From == 'Meters' and To == 'Cm':
        conv_num = num * 100
    elif From == 'Cm' and To == 'Meters':
        conv_num = num /100
    elif From == 'Km' and To == 'Meters':
        conv_num = num * 1000
    elif From == 'Meters' and To == 'Km':
        conv_num = num / 1000
    elif From == 'Inches' and To == 'Meters':
        conv_num = num / 39.37
    elif From == 'Foot' and To == 'Meters':
        conv_num = num / 3.28
    elif From == 'Inches' and To == 'Foot':
        conv_num = num / 12
    elif From == 'Foot' and To == 'Inches':
        conv_num = num * 12
    elif From == 'Foot' and To == 'Cm':
        conv_num = num * 30.48
    elif From == 'Cm' and To == 'Foot':
        conv_num = num / 30.48
    elif From == 'Km' and To == 'Foot':
        conv_num = num * 3280.839895
    elif From == 'Foot' and To == 'Km':
        conv_num = num / 3280.839895
    elif From == 'Km' and To == 'Cm':
        conv_num = num * 100000
    elif From == 'Cm' and To == 'Km':
        conv_num = num /100000
    elif From == 'Inches' and To == 'Cm':
        conv_num = num * 2.54
    elif From == 'Cm' and To == 'Inches':
        conv_num = num / 2.54
    elif From == 'Km' and To == 'Inches':
        conv_num = num * 39370.07874
    elif From == 'Inches' and To == 'Km':
        conv_num = num / 39370.07874
    else:
        conv_num = num

    numL = Label(App, text = round(conv_num, 2), width = 10)
    numL.grid(row= 1, column =4, pady = 5)


conB = Button(App, text = 'Convert', command = converter)
conB.grid(row = 2, column = 0, pady = 5)

App.mainloop()


