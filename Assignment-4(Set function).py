# Creating and implementing Dictonary


My_Interests={
               "Studio Mappa":"Jujtsu kaisen",              #This is a simple example and syntax of Dictonary                        
               "Studio Ufotable":"Demon Slayer",            #Here that "Studios are keywords and the things after the semicollen are their values"  
               "Studio Bones":"My Hero Academia",
               "Anime Watched":80,                          #We can also add the integer value to the keyword
               "Rating":[8,9.5,9],                          #We can also add the list in the Dictonary
               "Another dictonary":{
                                     "Characters":"good",   #We can also add another dictonary into a dictonary
                                     "Plot":"Excellent"

               }                        
}
  
# print(My_Interests["Studio Mappa"])                       #This is how we print the value of a particular key inside the Dictonary 
# print(My_Interests["Another dictonary"]["Plot"])          #This is how we print the value inside the dictonary who is inside the main dictonary
# print(len(My_Interests))



# Me=My_Interests["Studio Mappa"]                          #Here we have given the value of "Studio Mappa" to some another external keyword Known as "Me". Now the value inside the dictonary is not lossed by this 
# print(Me)

# Me= My_Interests.get("Studio Mappa")                     #This is another method of assigning the value and this is mostly used by coders because using .get fuction reduces the throwing of erroes
# print(Me)

# print(My_Interests.keys)                                 #This is how we print all "Keys" inside the dictonaries

# MY=My_Interests.keys()                                   #This is how we can assign the "Keys" to some another variable 
# print(MY)                              

# My_Interests["Studio WIT"]=["Vivy"]                      #This is how we add a new "Key" and its "Value" in a Dictonary,But if we write the "key" which is already exisitng in the dictonary then the "Value" assigned to the "Key" will overwrite the "Value" existing the dictonary
# My_Interests["Studio Bones"]=["Mob Psyco 100"]           #This is how we can overwrite or change the "Value" inside a "Keys"
# My_Interests.update({"Studio Bones":"Mob Psyco 100"})    #This is another method of overwriting a "Key" or adding a new "Key" and "Value", This will never throw the error until and unless the name of the dictonary is wrong



# if "Anime Watched" in My_Interests:
#     print("Yes Anime Watched is present in the Dictonary") #This is how we can find whether the "Key" or a "Value" is present in a Dictonary or not


# My_Interests.pop("Studio Ufotable")                      #This is how we can pop out or remove a "Key" and its "Value" from a dictonary
# My_Interests.popitem()                                   #This will pop the last "Key" and its "Value" from the dictonary
# My_Interests.clear()                                     #This will clear all the "Key" and "Value" inside the dictonary but the dictonary will still exist ie some other "Keys" and their "Values" can be added to the existing dictonary
# del My_Interests                                         #This will delete the whole dictonary

print(My_Interests)