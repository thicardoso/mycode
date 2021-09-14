#!/usr/bin/env python3
# This Script will parse data from JSON file called trivia.json

import json #Importing json module to be able to work with JSON data

def main ():
    with open ("trivia.json", "r") as jsonfile: #Opens the file called trivia.json, reads its content and stores in jsonfile variable
        tri = json.load(jsonfile) #Load the content of jsonfile to variable tri
        for answer in tri:
            #tri.append(tri.rstrip("\n").split(' ')
            print( tri[0]['question'] ) #Print the value of Key 'question' which resided in list 0
            #tri.append(tri.rstrip("\n").split(' ')
            print( "Incorrect Answers are: ", tri[0]['incorrect_answers'] )
            #print( "Correct Answer is: ", tri[0]['correct_answer'] )

main()
