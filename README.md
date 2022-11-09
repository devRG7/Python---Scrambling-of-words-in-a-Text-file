# Python---Scrambling-of-words-in-a-Text-file
This assignment which was given for the Programming and Problem solving concept was really very challenging and tough. But after analyzing and understanding each function and what it required as parameters, it was then possible to design and make it.
Still the main function scramble_word(word_str) was not successful as expected since I was not able to include punctuation inside the function.
Time was very limited taking into consideration that as a working person in a much demanded company where my presence is utmost important for urgent problematic solving and analysis. But still I was able to present a program instead of nothing.
The program required several python chapters understandings where the acquired knowledge was very important to be applied. Overall I am very pleased with the programing since I am at a very beginner level and I was able to present this program and its source code together with this document.

There is a need to design and code a python program that will take as input a text file having readable characters inside it and scramble the lines along with the words but keeping the original position of the start letter and ending letter of each word.

An Example of the input: 
The purpose of the program is to shuffle only the middle letters of each word in a sentence, leaving it still readable like this

An Example of the output: 
The psrpoue of the paogrrm is to sufhlfe only the mddlie lrettes of ecah wrod in a snceente, lianveg it sitll rbdlaeae like this

The programs should be coded by making use of: random, string, lists and files in python.

Program Design

![image](https://user-images.githubusercontent.com/61977663/200772507-ecde0356-525c-4f9a-8dcb-03adbfc3f116.png)

PseudoCode

![image](https://user-images.githubusercontent.com/61977663/200773121-2a21d590-878c-4782-8104-3a411b3fcc4a.png)

FlowCharts

![image](https://user-images.githubusercontent.com/61977663/200773279-f10717dd-53f8-4cc1-abf0-f6892fff9c05.png)
![image](https://user-images.githubusercontent.com/61977663/200773386-fdf208b8-43c4-46c0-83d6-113409e44e4f.png)

Description of Each Function

![image](https://user-images.githubusercontent.com/61977663/200773498-89c9edff-e1ac-4c70-9537-4d1b7222094f.png)
![image](https://user-images.githubusercontent.com/61977663/200773596-bdcdff0f-70f5-4677-9f0a-eda0608906df.png)

Critical Appraisal

The main functions of the program was as follows:

 Take each line from a text

 Convert it into a list

 Take each word from the list

 If word<3 ignore the words else take the word and keep 1st and last alphabet from word unchanged

 From the remaining of the word, the middle part of it, a function implemented to shuffle the middle string and return back the shuffle string.

 From each shuffle string, join back the word with the 1st and last alphabet to re construct the word and assigned it to a list

 Word from list Is then joined to make the sentence back

 Same is written into an output text with the scrambled words in the sentences

![image](https://user-images.githubusercontent.com/61977663/200774141-a43cbf6f-f90a-4791-859e-d5306323106a.png)

