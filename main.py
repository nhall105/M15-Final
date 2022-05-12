from breezypythongui import EasyFrame
from tkinter.font import Font
import tkinter
import units
import temp

class UnitConverter(EasyFrame):

    def __init__(self):

        # Create the main frame
        EasyFrame.__init__(self, title = "Unit Converter")

        # Create type of units drop-down
        self.CT = self.addCombobox("Type of Conversion", ["Area", "Data Transfer Rate", "Digital Storage", "Energy", "Frequency", "Fuel Economy", "Length", "Mass", "Plane Angle", "Pressure", "Speed", "Temperature", "Time", "Volume"], column = 0, row = 0, columnspan = 2, sticky = tkinter.N+tkinter.W+tkinter.E)

        # Input panel creation
        inputPanel = self.addPanel(row = 1, column = 0, background = "purple")
                
        # Conversion input field/output text (Also labels)
        inputPanel.addLabel("Input", row = 0, column = 0, sticky = tkinter.S+tkinter.E+tkinter.W)
        inputPanel.addLabel("Output", row = 0, column = 1, sticky = tkinter.S+tkinter.E+tkinter.W)
        self.inNum = inputPanel.addFloatField(" ", row = 1, column = 0, sticky = tkinter.E+tkinter.W)
        self.outNum = inputPanel.addTextField(" ", row = 1, column = 1, state = 'readonly', sticky = tkinter.E+tkinter.W)

        # Conversion drop-down lists
        self.C1 = inputPanel.addCombobox("Units", ["Choose Unit"], column = 0, row = 2, command = self.typeGet, sticky = tkinter.N+tkinter.E+tkinter.W)
        self.C2 = inputPanel.addCombobox("Units", ["Choose Unit"], column = 1, row = 2, command = self.typeGet, sticky = tkinter.N+tkinter.E+tkinter.W)

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
            self.C1["values"] = ["Metric ton", "Kilogram", "Gram", "Milligram", "Microgram", "Imperial ton", "US ton", "Stone", "Pound", "Ounce"]
            self.C2["values"] = ["Metric ton", "Kilogram", "Gram", "Milligram", "Microgram", "Imperial ton", "US ton", "Stone", "Pound", "Ounce"]
        elif text == "Plane Angle":
            self.C1["values"] = ["Degree", "Gradian", "Milliradian", "Minute of arc", "Radian", "Second of arc"]
            self.C2["values"] = ["Degree", "Gradian", "Milliradian", "Minute of arc", "Radian", "Second of arc"]
        elif text == "Pressure":
            self.C1["values"] = ["Bar", "Pascal", "Pound-force per square inch", "Standard atmosphere", "Torr"]
            self.C2["values"] = ["Bar", "Pascal", "Pound-force per square inch", "Standard atmosphere", "Torr"]
        elif text == "Speed":
            self.C1["values"] = ["Miles per hour", "Foot per second", "Meter per second", "Kilometer per hour", "Knot"]
            self.C2["values"] = ["Miles per hour", "Foot per second", "Meter per second", "Kilometer per hour", "Knot"]
        elif text == "Temperature":
            self.C1["values"] = ["Celsius", "Fahrenheit", "Kelvin"]
            self.C2["values"] = ["Celsius", "Fahrenheit", "Kelvin"]
        elif text == "Time":
            self.C1["values"] = ["Nanosecond", "Microsecond", "Millisecond", "Second", "Minute", "Hour", "Day", "Week", "Month", "Calendar year", "Decade", "Century"]
            self.C2["values"] = ["Nanosecond", "Microsecond", "Millisecond", "Second", "Minute", "Hour", "Day", "Week", "Month", "Calendar year", "Decade", "Century"]
        elif text == "Volume":
            self.C1["values"] = ["US liquid gallon", "US liquid quart", "US liquid pint", "US legal cup", "US fluid ounce", "US tablespoon", "US teaspoon", "Cubic meter", "Liter", "Milliliter", "Imperial gallon", "Imperial quart", "Imperial pint", "Imperial cup", "Imperial fluid ounce", "Imperial tablespoon", "Imperial Teaspoon", "Cubic foot", "Cubic inch"]
            self.C2["values"] = ["US liquid gallon", "US liquid quart", "US liquid pint", "US legal cup", "US fluid ounce", "US tablespoon", "US teaspoon", "Cubic meter", "Liter", "Milliliter", "Imperial gallon", "Imperial quart", "Imperial pint", "Imperial cup", "Imperial fluid ounce", "Imperial tablespoon", "Imperial Teaspoon", "Cubic foot", "Cubic inch"]

    # Grabs the Unit drop-downs and number entered and convert, then outputs
    def convert(self):
        
        # Grab Units and number to convert
        unit1 = self.C1.getText()
        unit2 = self.C2.getText()
        num = float(self.inNum.getNumber())
        
        # Run drop-down text through function to get coresponding number
        if self.CT.getText() != "Temperature":
            unit1Num = units.unitValue(unit1)
            unit2Num = units.unitValue(unit2)
        
        #print(str(unit1Num)) #Testing purposes
        #print(str(unit2Num)) #Testing purposes
        #print(str(num)) #Testing purposes

        # Run numbers through conversion equation (uses a base unit for each meausurement so it takes current units, converts to base unit, then into final unit)
        if self.CT.getText() == "Temperature":
            convertNum = temp.tempConv(unit1, unit2, num)
        else:
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

