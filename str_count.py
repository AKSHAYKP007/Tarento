#question?????
#Program to count the number of words ,alphabets, number of digits in a string.

#prgram



txt=input('Enter the string').strip()  # read the text from the input
word_count=0       # initialise all the variables to zero
alpha_count=0
digit_count=0
for i in txt:  # ierate through the characters in the string
   if(i==' '):   # if it is a space
        word_count+=1  #then increment the word_count by 1
   elif ((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122)): #else if it is alphabet increment the 
        alpha_count+=1     #alphabet count by 1. here ord() is a built in function in python to return the ASCII.
   else:
        digit_count+=1   #else increment digit count
#printing the results
print('Total words - {}\nalphabets - {} \nNumbers - {}'.format(word_count+1,alpha_count,digit_count))            

