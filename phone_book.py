from phone_entry import PhoneEntry

class PhoneBook:
    def __init__(self):
        self.entries = dict()
        
    @staticmethod
    def validateEntry(entry):
        ans = False
        name, number = entry.split()
        isNameValid = PhoneEntry.validateName(name)
        if(isNameValid):
            isNumValid = PhoneEntry.validateNumber(number)
            if(isNumValid):
                ans = True
                
        return ans
        
    def addEntry(self, entry):
        name, number = entry.split()
        name = name.lower()
        self.entries[name] = PhoneEntry(name, number)
        
    def displayEntry(self, name):
        lowerCaseName = name.lower()
        if lowerCaseName in self.entries:
            self.entries[lowerCaseName].display()
        else:
            print("Not found")