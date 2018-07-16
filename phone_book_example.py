#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 21:38:48 2018

@author: brian
"""

import sys
import logging         

from phone_book import PhoneBook
            
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
            errorMsg = "Invalid entry: " + entry
            logging.error(errorMsg)
            
    del input[:n] #delete phone book entries and remain with queries only
        
    #process queries
    for idx in range(n):
        name = input[idx].rstrip()
        phoneBook.displayEntry(name)
    
   
        
        
if __name__ == '__main__':
    processInput()
            
        
   