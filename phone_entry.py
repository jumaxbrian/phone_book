import logging

#Setup for logging
logging.basicConfig(filename='app.log',
    format='%(asctime)s:%(levelname)s:%(message)s'
)

class PhoneEntry:
    '''
    Each contact is saved as a PhoneEntry in the PhoneBook where
    an entry has a name and a number
    '''
    def __init__(self, name, number):
        self.name = name
        self.number = number
        
    def display(self):
        print('{}={}'.format(self.name, self.number))
        
    @staticmethod
    def validateNumber(number):
        ans = False
        if(len(number) != 8):
            errorMsg = 'Number length should be equal to 8: ' + number
            logging.error(errorMsg)
        elif any(char not in '0123456789' for char in number):
            errorMsg = 'Numbers should only contain digits 0-9: ' + number
            logging.error(errorMsg)
        else:
            ans = True
        return ans
                
    @staticmethod
    def validateName(name):
        lowerCaseName = name.lower()
        ans = False
        if any(c not in 'abcdefghijklmnopqrstuvwxyz' for c in lowerCaseName):
            errorMsg = 'Name should only containg English alphabet: ' + lowerCaseName
            logging.error(errorMsg)
        else:
            ans = True
        return ans