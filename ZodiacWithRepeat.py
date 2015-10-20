
# coding: utf-8

# In[16]:

# In this version we want to be able to repeat the operation several times. To do so we will use function
# Here is a description of what we mean by Chinese Zodiac animal 
# and that is what we want to compute when the user gives us his/her birth year

"""
While taking a class on the culture of China, you have learned about the Chinese zodiac in which people fall into 1 of 12 categories, depending on the year of their birth. The categories, numbered 0 to 11, correspond to the following animals:

(0) monkey
(1) rooster
(2) dog
(3) pig
(4) rat
(5) ox
(6) tiger
(7) rabbit
(8) dragon
(9) snake
(10) horse
(11) goat

Those who believe in this zodiac think that the year of a person's birth influences both their personality and fortune in life.

Your task is to build a program that will ask a user for their birth year and tell them their zodiac sign.  If the user does not enter a number that can be interpreted as a year then an error message must be shown and the user given another chance.  If the user types "quit" then the program halts.

For extra credit: save each year that is input to a file and print a chart showing how many of each type or animal have been returned.

To find your zodiac sign, divide the year of your birth by 12. The remainder then determines your sign. For example: The remainder when we divide 1985 by 12, is 5; therefore, a person born in 1985 is an ox according to the Chinese zodiac.
"""

# Now we are going to plan the program

# Zodiacsetup will do all the opening, loading and closing of files/data
# It will return the ZodiacList and ZodiacDescList
def Zodiacsetup(): #it is an empty function so no input
    # Open the Zodiac description file ZodiacDescription.txt
    ZodiacText= open('zodiacDescriptions.txt','r') # open this file as a read only file
    
    # Read the file: We nned to make a list with each line of the file to return the right zodiac sign
    ZodiacList = [] # creating an empty list, so that Pyhton know the variable when we use it/complete it
    for line in ZodiacText:
        ZodiacList.append(line)
        

    # close the file, do it now because we don't need this anymore
    ZodiacText.close() #closing the file allow the computer to save it and put it in the memory instead of keeping it in the "buffer"
    
    return ZodiacList
def ZodiacDescSetup(): #it is an empty function so no input
    # Open the Zodiac description file ZodiacDescription.txt
    ZodiacDescText= open('zodiacDescriptions2.txt','r') # the description for each sign
    
    # Read the file: We nned to make a list with each line of the file to return the right zodiac sign
    ZodiacDescList= []
        
    for line in ZodiacDescText:
        ZodiacDescList.append(line)

    # close the file, do it now because we don't need this anymore
    ZodiacDescText.close()
    
    return ZodiacDescList
    
# zodiacCalc will collect the birthyear and determine the Chinese Zodiac animal and display it with its description
# it will return the birthYear for the next step
def ZodiacCalc():

    # Ask the user for input 
    # first start with a given number to built a working program 
    # and then when sure it works we change our given variable by the one the user gives us

    # need to build some back up in case the input is not an integer ==> error trapping
    #define birthYear before the try so that it returns something at the end
    birthYear=input("What year were you born? ")
    try:
        birthYear=int(birthYear)
        # because the memory keeps tabs on previous values of the parameters we need to put more content in the try
        ZodiacIndex=(birthYear+8)%12 #the list is wrongly indexed everyhting is shifted by +8 or -4 %12

        # Tell them the result
        print("Your Chinese Zodiac animal is "+ZodiacList[ZodiacIndex])
        print("Here is a description of your Chinese Zodiac animal:\n"+ ZodiacDescList[ZodiacIndex])

    except ValueError:  
        birthYear=input("You did not provide a year in the form of an integer, do you want to try again? Yes/No\n")
        if birthYear=='Yes':
            birthYear=0
        #birthYear="notgood"
    return birthYear
    
# repeat

ZodiacList=Zodiacsetup() 
ZodiacDescList=ZodiacDescSetup()
birthYear=0
# we want to run it as long as the user want to use it 
# then give the user a condition to spot the program and built the program accordingly
while type(birthYear) is int:
    birthYear= ZodiacCalc()


# In[ ]:



