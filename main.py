from breezypythongui import EasyFrame
from tkinter.font import Font
import tkinter

class LabelDemo(EasyFrame):

    def __init__(self):

        # Create the main frame
        EasyFrame.__init__(self, width = 816, height = 624, title = "Null")
        self.setResizable(False);

        n47 = Font(size=47)

        # Create the nested frame for type of conversion
        typePanel = self.addPanel(row = 0, column = 0)

        # Create type of units drop-down
        CT = typePanel.addCombobox("Type of Conversion", ["Area", "Data Transfer Rate", "Digital Storage", "Energy", "Frequency", "Fuel Economy", "Length", "Mass", "Plane Angle", "Pressure", "Speed", "Temperature", "Time", "Volume"], column = 0, row = 0, columnspan = 2, sticky = tkinter.N+tkinter.W+tkinter.E)

        # Input panel creation
        inputPanel = self.addPanel(row = 1, column = 0, background = "purple")
                
        # Conversion input fields        
        inputPanel.addFloatField("1", row = 0, column = 0)
        inputPanel.addFloatField("Converted", row = 0, column = 1)

        #Conversion drop-down lists
        self.conver1 = inputPanel.addMenuBar(row = 1, column = 0)
        self.conver2 = inputPanel.addMenuBar(row = 1, column = 1)
        C1 = self.conver1.addMenu("Menu1")
        C2 = self.conver2.addMenu("Menu2")
        C1.addMenuItem("Test", command = print())        

def CVChanger(Ctype):
    ConverType = Ctype
    print(ConverType)

def ConverMenu():
    if CVType == "Area":
        C1.addMenuItem("Square kilometer")
        

def main():
    LabelDemo().mainloop()
    
if __name__ == "__main__":
    main()

