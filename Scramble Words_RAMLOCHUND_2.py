# Assignment:Programming and Problem Solving
# Design a program to take as input a text file and scramble line by line by keeping 1st and 
# last letter of each word and output the scrambled text file
# Author : Ramlochund Gitendrajeet
# Date : 12/11/2019


import random
#Function to scramble line and combine each word back to line 
def scramble_line(line_str):
    word = line_str.split(' ')
    final_line = ' '.join(map(scramble_word, word))
    #' '.join((scramble_word)for scramble_word in word)
    return final_line
#Function to shuffle string
def shuffle_string(string):
    characters = list(string)
    random.shuffle(characters)
    shuffle_final=''.join(characters)
    return shuffle_final
#Function to scramble word 
def scramble_word(word_str):
    if len(word_str) <3:
        return word_str
    elif len(word_str)>=3:
    # Split word into first,last and middle letters
        first=word_str[0]
        middle=word_str[1:-1]
        last=word_str[-1]
        final_word=first + shuffle_string(middle) + last
    return final_word

#Function to open text file specified by user input
def open_read_file(file_name_str):
    with open(file_name_str, 'r') as filein:   
        for line_str in filein.readlines():
            view_scramble=scramble_line(line_str)
               
    with open((file_name_str + "_scrambled.txt" ),'a+') as fileout: 
        fileout.write(view_scramble)      
def main():
    file_name_str = raw_input("Enter input file name:") 
    open_read_file(file_name_str)
main()