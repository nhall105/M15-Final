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
                
        # Conversion input field/output text (Also labels)
        inputPanel.addLabel("Input", row = 0, column = 0, sticky = tkinter.E)
        inputPanel.addLabel("Output", row = 0, column = 1, sticky = tkinter.E)
        self.inNum = inputPanel.addFloatField(" ", row = 1, column = 0)
        self.outNum = inputPanel.addTextField(" ", row = 1, column = 1, state = 'readonly')

        # Conversion drop-down lists
        self.C1 = inputPanel.addCombobox("Units", ["Choose Unit"], column = 0, row = 2, command = self.typeGet)
        self.C2 = inputPanel.addCombobox("Units", ["Choose Unit"], column = 1, row = 2, command = self.typeGet)

        # Convert button because float fields can run commands smh
        self.conButton = inputPanel.addButton(text = "Convert", column = 0, row = 3, columnspan = 2, command = self.convert)

    # Function that grabs text in Unit Type drop-down and fills the Unit drop-downs accordingly    
    def typeGet(self):
        
        # Get text in Unit Type drop-down
        text = self.CT.getText()
        
        # Find matching text and fill Unit drop-downs accordingly
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
            self.C1["values"] = ["Joule", "Kilojoule", "Gram calorie", "Kilocalorie", "Watt hour", "Kilowatt hour", "Electronvolt", "British thermal unit", "US therm", "Foot-pound"]
            self.C2["values"] = ["Joule", "Kilojoule", "Gram calorie", "Kilocalorie", "Watt hour", "Kilowatt hour", "Electronvolt", "British thermal unit", "US therm", "Foot-pound"]
        elif text == "Frequency":
            self.C1["values"] = ["Hertz", "Kilohertz", "Megahertz", "Gigahertz"]
            self.C2["values"] = ["Hertz", "Kilohertz", "Megahertz", "Gigahertz"]
        elif text == "Fuel Economy":
            self.C1["values"] = ["Miles per gallon", "Miles per gallon (Imperial)", "Kilometer per liter", "Liter per 100 kilometers"]
            self.C2["values"] = ["Miles per gallon", "Miles per gallon (Imperial)", "Kilometer per liter", "Liter per 100 kilometers"]
        elif text == "Length":
            self.C1["values"] = ["Kilometer", "Meter", "Centimeter", "Millimeter", "Micrometer", "Nanometer", "Mile", "Yard", "Foot", "Inch", "Nautical mile"]
            self.C2["values"] = ["Kilometer", "Meter", "Centimeter", "Millimeter", "Micrometer", "Nanometer", "Mile", "Yard", "Foot", "Inch", "Nautical mile"]
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

    # Grabs the Unit drop-downs and number entered and convert, then outputs
    def convert(self):
        
        # Grab Units and number to convert
        unit1 = self.C1.getText()
        unit2 = self.C2.getText()
        num = float(self.inNum.getNumber())
        
        # Run drop-down text through function to get coresponding number
        unit1Num = units.unitValue(unit1)
        unit2Num = units.unitValue(unit2)
        
        #print(str(unit1Num)) #Testing purposes
        #print(str(unit2Num)) #Testing purposes
        #print(str(num)) #Testing purposes

        # Run numbers through conversion equation (uses a base unit for each meausurement so it takes current units, converts to base unit, then into final unit)
        convertNum = (num / unit1Num) * unit2Num
        
        # Tells how many decimal places based on number (turns into int if none)
        if float(convertNum).is_integer() == True:
            convertNum = int(convertNum)
        else:
            convertNum = max('{:.1f}'.format(convertNum),str(convertNum),key=len)

        #print(str(convertNum)) #Testing purposes

        # Put final number into text field
        self.outNum.setText(convertNum)

def main():
    UnitConverter().mainloop()
    
if __name__ == "__main__":
    main()

