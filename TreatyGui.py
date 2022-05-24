from tkinter import *
from tkinter.messagebox import showinfo

def makeWindows():

    TextChoice = False
    
    #making window
    window = Tk()
    window.title("Treaty: A Fun Way to treat your pet!")
    
    #entries
    Label(window,text="Enter your Pet's Name: ").pack()
    PetName = Entry(window).pack()
    Label(window,text="Enter your Phone Number: ").pack()
    PhoneNumber = Entry(window).pack()

    #Below could be made as sliders
    Label(window,text="Treats currently in treaty: ").pack()
    TreatAmount = Entry(window).pack()
    Label(window,text="Treats per dispense: ").pack()
    TreatPerDisp = Entry(window).pack()
    Label(window,text="How many hours per dispense: ").pack()
    HoursPerDisp = Entry(window).pack()

    #Buttons
    Txt= Button(window,text="Submit Information", command=lambda:handler(PetName,PhoneNumber, TreatAmount, TreatPerDisp,HoursPerDisp)).pack(side=RIGHT)

    #click to send text of time when treat dispensed
    #click to send end of the day log
    #click to send img of pet

def handler(PetName,PhoneNumber, TreatAmount, TreatPerDisp,HoursPerDisp):
    "handles the entry's data"
    PetName = PetName.get()
    PhoneNumber = PhoneNumber.get()
    TreatAmount = TreatAmount.get()
    TreatPerDisp = TreatPerDisp.get()
    HoursPerDisp = HoursPerDisp.get()
    return PetName,PhoneNumber, TreatAmount, TreatPerDisp,HoursPerDisp

window.mainloop()
