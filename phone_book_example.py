#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 21:38:48 2018

@author: brian
"""

import sys

class PhoneEntry:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        
    def display(self):
        print(self.name,'=',self.number)
        
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
            
def processInput():
    phoneBook = PhoneBook()
    input = sys.stdin.readlines()
    n = int(input.pop(0))
    
    #process phone book entries
    for idx in range(n):
        entry = input[idx].rstrip()
        isEntryValid = PhoneBook.validateEntry(entry)
        if(isEntryValid):
            phoneBook.addEntry(entry)
        else:
            print("Invalid entry: ", entry)
            
    del input[:n] #delete phone book entries and remain with queries only
        
#    for line in input:
#        line = line.rstrip()
#        print(line)
#    del input[:n]
#    print(input)
        
    #process queries
    for idx in range(n):
        name = input[idx].rstrip()
        phoneBook.displayEntry(name)
    
   
        
        
if __name__ == '__main__':
    processInput()
            
        
   