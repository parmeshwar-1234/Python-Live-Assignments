# Here we will see the declaration and implementation of the print and input function 

print("Enter you name \n")
Your_Name=input()                                              # This is how we usually declare the print and input function

# But whatever is entered in the "input" function is a string in order to convert it to an integer we shall do some extra work

Your_Age=int(input())                                          # This is how we convert the string into the integer, same goes to float

print("Hey","how","are","you,","watcha","doin?",sep=" - ")     # That sep function will put that hignfen between every individual string
print("Hey","how areyou watcha doin?",end=" ----> ")           # That end function will put that symbol at the end this function is usually used in loops to repeat some format at the end 

