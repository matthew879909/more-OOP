class IOString():
    def __init__(self):
        self.str1 = ""
    def get_String(self):
        self.atr1 = input("Enetr String : ")
    def print_String(self):        
        print(self.atr1.upper())
str1 = IOString()
str1.get_String()
str1.print_String()         