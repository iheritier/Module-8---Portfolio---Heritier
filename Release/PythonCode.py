#Ian Heritier
#Module Seven Assignment

import re
import string

def DoubleValue(v):
    return v * 2 #simple method, just sends back twice the received value

def MultiplicationTable(v):
    #use for loop to print v's multiplication table
    for multiplier in range(1, 11): #1-10
        print("" + str(v) + " X " + str(multiplier) + " = " + str(v * multiplier))
    return 0 #I want a return value here so the program doesn't end.

def Frequency(): #print frequency of each element in the list

    print("\nFrequency of words in list:")
    file = open("CS210_Project_Three_Input_File.txt") #open file for reading
    
    lines = [] #keep track of all entries (without escape sequence)
    individualWords = [] #start a list of individual words

    #for x in range(len(listOfWords)):
       #if not(listOfWords[x] in individualWords): #if not already in list of unique words, add it
            #individualWords.append(listOfWords[x])
    
    rawlines = file.readlines() #read in all lines as a list
 
    for line in rawlines:
        lines.append("{}".format(line.strip())) #get all the lines w/o endlines

    for x in range(len(lines)):
        if not(lines[x] in individualWords): #if not already in list of unique words, add it
            individualWords.append(lines[x])

    for i in range(len(individualWords)): #for each individual word
        count = 0
        for j in range(len(lines)): #check for instances of the word in the list
            if lines[j] == individualWords[i]:
                count += 1 #add to count for each instance
        print(individualWords[i] + ": " + str(count)) #print results for this word

def ItemCheck(item): #check number of times a certain string appears
    file = open("CS210_Project_Three_Input_File.txt") #open file for reading
    
    lines = [] #keep track of all entries (without escape sequence)
    individualWords = [] #start a list of individual words

    #for x in range(len(listOfWords)):
       #if not(listOfWords[x] in individualWords): #if not already in list of unique words, add it
            #individualWords.append(listOfWords[x])
    
    rawlines = file.readlines() #read in all lines as a list
 
    for line in rawlines:
        lines.append("{}".format(line.strip())) #get all the lines w/o endlines

    count = 0 #track # of occurrences of the given word
    for line in lines:
        if line == item:
            count += 1

    return count

def Histogram():
    print("\nVisual histogram of words in list:")
    file = open("CS210_Project_Three_Input_File.txt") #open file for reading
    fileout = open("frequency.dat", 'w') #open file for writing
    
    lines = [] #keep track of all entries (without escape sequence)
    individualWords = [] #start a list of individual words
    
    rawlines = file.readlines() #read in all lines as a list
 
    for line in rawlines:
        lines.append("{}".format(line.strip())) #get all the lines w/o endlines

    for x in range(len(lines)):
        if not(lines[x] in individualWords): #if not already in list of unique words, add it
            individualWords.append(lines[x])

    for i in range(len(individualWords)): #for each individual word
        count = 0
        for j in range(len(lines)): #check for instances of the word in the list
            if lines[j] == individualWords[i]:
                count += 1 #add to count for each instance
        fileout.write(individualWords[i] + " " + str(count) + "\n") #print results for this word to fileout
    
    fileout.close() #conclude writing to fileout

    #open and read in frequency.dat that was created above
    file = open("frequency.dat")
    rawlines = file.readlines()
    lines = []
    for line in rawlines:
        lines.append("{}".format(line.strip())) #get all the lines back from the file w/o endlines

    for line in lines:
        word = line.split(' ')[0] #word is first thing in the line
        freq = line.split(' ')[1] #frequency is second thing in the line
        stars = "" #string to store the asterisks representing frequency
        for x in range(int(freq)):
            stars += "*"
        print(word + " " + stars) #final printout for this word
        
        


