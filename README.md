[![CircleCI](https://circleci.com/gh/jumaxbrian/phone_book.svg?style=svg)](https://circleci.com/gh/jumaxbrian/phone_book)

## Phone Book App

1. ### About
    This program simulates a phone book application. Given n​ names and phone numbers, it assembles a phone book that maps friends' names to their respective phone numbers.

1. ### Installation  
    Clone this repository into your local machine. Ensure you have python3 installed as it is required by this application. Once you have cloned this repository locally. Move into the cloned directory e.g. `phone_book` and run `python3 phone_book_example.py `. 

1. ### Example usage
    1. Ensure you are in the directory that you cloned the repository into i.e. `phone_book` if you did not specify any.
    1. Type `python3 phone_book_example.py ` at the terminal. The program will run and wait for input from you.
    1. Enter the input given below
        ```
            3  
            sam 99912222 
            tom 11122227
            harry 12299933 
            Sam 
            Edward 
            harry
        ```
    1. Press `Ctrl+D` on the terminal to submit the input to the application.
    1. You will get the following response
        ```
        sam=99912222 
        Not found 
        harry=12299933
        ```
    1. The response for Edward is not found because he was not added to the phone book initially. Also, note that your inputs have to meet the following requirements
        1. The entries have to be equal to the number you input first i.e. if 3, then you must have 3 entries(name + space + number). You can have as many queries as you want i.e. only the names as shown above.
        1. You must use spaces to separate the names from the numbers

1. ### Running tests
    To run tests, type the codes below to test each of the two classes
    1. `python3 test_phone_entry.py ` for `PhoneEntry`
    1. `python3 test_phone_book.py ` for `PhoneBook`

1. ### Logged Errors
    While running the application, you may encounter errors anticipated by the application e.g. invalid input. You will find these in a file called `app.log` in the same directory as the main program.
