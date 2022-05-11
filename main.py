from breezypythongui import EasyFrame
from tkinter.font import Font
import tkinter
import units

class UnitConverter(EasyFrame):

    def __init__(self):

        # Create the main frame
        EasyFrame.__init__(self, width = 816, height = 624, title = "Unit Converter")

        # Create type of units drop-down
        self.CT = self.addCombobox("Type of Conversion", ["Area", "Data Transfer Rate", "Digital Storage", "Energy", "Frequency", "Fuel Economy", "Length", "Mass", "Plane Angle", "Pressure", "Speed", "Temperature", "Time", "Volume"], column = 0, row = 0, columnspan = 2, sticky = tkinter.N+tkinter.W+tkinter.E)

        # Input panel creation
        inputPanel = self.addPanel(row = 1, column = 0, background = "purple")
                
        # Conversion input/output fields
        inputPanel.addLabel("Input", row = 0, column = 0, sticky = tkinter.E)
        inputPanel.addLabel("Output", row = 0, column = 1, sticky = tkinter.E)
        self.inNum = inputPanel.addFloatField(" ", row = 1, column = 0)
        self.outNum = inputPanel.addTextField(" ", row = 1, column = 1, state = 'readonly')

        # Conversion drop-down lists
        self.C1 = inputPanel.addCombobox("Units", ["Choose Unit"], column = 0, row = 2, command = self.typeGet)
        self.C2 = inputPanel.addCombobox("Units", ["Choose Unit"], column = 1, row = 2, command = self.typeGet)

        # Convert button because float fields can run commands smh
        self.conButton = inputPanel.addButton(text = "Convert", column = 0, row = 3, columnspan = 2, command = self.convert)
        
    def typeGet(self):
        text = self.CT.getText()
        if text == "Area":
            self.C1["values"] = ["Square kilometer", "Square meter", "Square mile", "Square yard", "Square foot", "Square inch", "Hectare", "Acre"]
            self.C2["values"] = ["Square kilometer", "Square meter", "Square mile", "Square yard", "Square foot", "Square inch", "Hectare", "Acre"]
        elif text == "Data Transfer Rate":
            self.C1["values"] = ["Bit per second", "Kilobit per second", "Kilobyte per second", "Kibibit per second", "Megabit per second", "Megabyte per second", "Mebibit per second", "Gigabit per second", "Gigabyte per second", "Gibibit per second", "Terabit per second", "Terabyte per second", "Tebibit per second"]
            self.C2["values"] = ["Bit per second", "Kilobit per second", "Kilobyte per second", "Kibibit per second", "Megabit per second", "Megabyte per second", "Mebibit per second", "Gigabit per second", "Gigabyte per second", "Gibibit per second", "Terabit per second", "Terabyte per second", "Tebibit per second"]
        elif text == "Digital Storage":
            self.C1["values"] = ["Bit", "Kilobit", "Kibibit", "Megabit", "Mebibit", "Gigabit", "Gibibit", "Terabit", "Tebibit", "Petabit", "Pebibit", "Byte", "Kilobyte", "Kibibyte", "Megabyte", "Mebibyte", "Gigabyte", "Gibibyte", "Terabyte", "Tebibyte", "Petabyte", "Pebibyte"]
            self.C2["values"] = ["Bit", "Kilobit", "Kibibit", "Megabit", "Mebibit", "Gigabit", "Gibibit", "Terabit", "Tebibit", "Petabit", "Pebibit", "Byte", "Kilobyte", "Kibibyte", "Megabyte", "Mebibyte", "Gigabyte", "Gibibyte", "Terabyte", "Tebibyte", "Petabyte", "Pebibyte"]
        elif text == "Energy":
            self.C1["values"] = ["DS 1"]
            self.C2["values"] = ["DS 2"]
        elif text == "Frequency":
            self.C1["values"] = ["DS 1"]
            self.C2["values"] = ["DS 2"]
        elif text == "Fuel Economy":
            self.C1["values"] = ["DS 1"]
            self.C2["values"] = ["DS 2"]
        elif text == "Length":
            self.C1["values"] = ["DS 1"]
            self.C2["values"] = ["DS 2"]
        elif text == "Mass":
            self.C1["values"] = ["DS 1"]
            self.C2["values"] = ["DS 2"]
        elif text == "Plane Angle":
            self.C1["values"] = ["DS 1"]
            self.C2["values"] = ["DS 2"]
        elif text == "Pressure":
            self.C1["values"] = ["DS 1"]
            self.C2["values"] = ["DS 2"]
        elif text == "Speed":
            self.C1["values"] = ["DS 1"]
            self.C2["values"] = ["DS 2"]
        elif text == "Temperature":
            self.C1["values"] = ["DS 1"]
            self.C2["values"] = ["DS 2"]
        elif text == "Time":
            self.C1["values"] = ["DS 1"]
            self.C2["values"] = ["DS 2"]
        elif text == "Volume":
            self.C1["values"] = ["DS 1"]
            self.C2["values"] = ["DS 2"]

    def convert(self):
        unit1 = self.C1.getText()
        unit2 = self.C2.getText()
        num = float(self.inNum.getNumber())
        unit1Num = units.unitValue(unit1)
        unit2Num = units.unitValue(unit2)
        print(str(unit1Num))
        print(str(unit2Num))
        print(str(num))
        convertNum = (num / unit1Num) * unit2Num
        if float(convertNum).is_integer() == True:
            convertNum = int(convertNum)
        else:
            convertNum = max('{:.1f}'.format(convertNum),str(convertNum),key=len)
        print(str(convertNum))
        self.outNum.setText(convertNum)

def main():
    UnitConverter().mainloop()
    
if __name__ == "__main__":
    main()

