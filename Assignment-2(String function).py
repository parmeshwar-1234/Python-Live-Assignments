#Implementing String


Para=("""JoJo's Bizarre Adventure is a Japanese manga series written and illustrated by Hirohiko Araki. 
         It was originally serialized in Shueisha's shōnen manga magazine Weekly Shōnen Jump from 1987 to 2004,
         and was transferred to the monthly seinen manga magazine Ultra Jump in 2005. 
         The series is divided into nine story arcs, each following a new protagonist bearing the "JoJo" nickname.
         JoJo's Bizarre Adventure is Shueisha's largest ongoing manga series by volume count,
         with its chapters collected in 130 tankōbon volumes as of May 2021.""")




# print(Para)                                      #This command is just to print Para

# print(Para[20])                                  #This command is to print the value at 3rd index

# print(Para[2:20])                                #This command is to print the value from 2nd index to 20th index but 20th index will be excluede

# print(Para[5:])                                  #This command is to print value from 5th index to the last index value

# print(Para[:64])                                 #This command is to print value from first index i.e. from 0th index to 64th index but 64th index will be excluded

# print(len(Para))                                 #This command is to print the length of string 

# print(Para.upper())                              #This command will print all strings in Para in a capital letters

# print(Para.lower())                              #This command will print all strings in Para in a small letters

# print(Para.capitalize())                         #This command will capitalise the first letter in the Para

# print(Para.replace("2004","2022"))               #This command will replace the older value with new value

summary= ("""\n \n \t Black Clover is a Japanese manga series written and illustrated by Yūki Tabata. 
         The story follows Asta, a young boy born without any magic power. 
        This is unknown to the world he lives in because seemingly everyone has some sort of magic power. 
        With his fellow mages from the Black Bulls, Asta plans to become the next Wizard King. 
        It has been serialized in Shueisha's Weekly Shōnen Jump magazine since February 2015, 
        with its chapters collected in 32 tankōbon volumes as of April 2022.""")

combine= Para+summary

# print(combine)                                  #This command will print the Para and summary together because of the opertaion done in line 41

