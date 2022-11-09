import random
def scramble_line(line_str):
    word = line_str.split(' ')
    final_line = ' '.join(map(scramble_word, word))
    return final_line

def shuffle_string(string):
    characters = list(string)
    random.shuffle(characters)
    return ''.join(characters)

def scramble_word(word_str):
    # No operation needed on sufficiently small words
    # (Also, main algorithm requires word length >= 2)
    if len(word_str) <3:
        return word_str

    # Split word into first & last letter, and middle letters
    first=word_str[0]
    middle=word_str[1:-1]
    last=word_str[-1]
    final_word=first + shuffle_string(middle) + last
    return final_word

def open_read_file(file_name_str):
    with open(file_name_str, 'r') as filein: 
        
        for line_str in filein.readlines():
            view_scramble=scramble_line(line_str)
            print(view_scramble)    
            
    with open((file_name_str + "_output.txt" ),'a+') as fileout: 
        fileout.write(view_scramble)     
    
def main():
    file_name_str = raw_input("Enter input file name:") 
    open_read_file(file_name_str)

main()