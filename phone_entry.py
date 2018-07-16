class PhoneEntry:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        
    def display(self):
        print('{}={}'.format(self.name, self.number))
        
    @staticmethod
    def validateNumber(number):
        ans = False
        if(len(number) != 8):
            print('Error', 'Number length should be equal to 8')
        elif any(char not in '0123456789' for char in number):
            print('Error', 'Numbers should only contain digits 0-9')
        else:
            ans = True
        return ans
                
    @staticmethod
    def validateName(name):
        lowerCaseName = name.lower()
        ans = False
        if any(c not in 'abcdefghijklmnopqrstuvwxyz' for c in lowerCaseName):
            print('Error', 'Name should only containg English alphabet')
        else:
            ans = True
        return ans