# Creating list and implementing it

My_List= ["Anime","Webtoon","Manga","K-Pop","AMV"]    #List can be a collection of strings
My_List_2= [35,63,43,745,3]                           #List can also be collection of integers and floats
My_List_3= [70.43,522,"Tatakae",]                     #List can also be collection of all datatypes available

# Now I will implement the My_List and comment out all implementation so the front user can test every implementation once at a time


# print(My_List[2])                     #Here value at index 2 will be printed
# print(My_List[1:4])                   #Here everything will be printed from index 1 to 4 but index 4 will be excluded 
# print(My_List[-4:-1])                 #Here will also last index will be excluded 
# print(My_List[:4])                    #Here form 0 to 4th index will be printed but 4th index will be excluded
# print(My_List[0:])                    #Here also form 0 to 4th index will be printed but this time here 4th index will be included


# My_List[4]= "OST"                     #Here my 4th index will be replaced by new word implemented by me
# My_List[2:4]= ["OST , Webseries"]     #Here by this we can replace multiple values inside the list
# My_List[0:4]= ["OST , Webseries"]     #Here we have replaced more than two lists with the two lists (i.e. replaced more lists with less lists)
# My_List[1:2]= ["OST , Webseries"]     #Here we have replaced less than two lists with the two lists (i.e. replaced less lists with more lists)

# My_List.append("Web novel")           #Here the new word will be added at the end of the list
# My_List.insert(3,"Web novel")         #Here the new word will be inserted at the third index
# My_List.extend(My_List_2)             #Here my first list will be merged with second list  

# My_List.pop(3)                        #Here I have popped up the value at index 3
# My_List.pop()                         #Here this will pop the value present at the last of the index
# My_List.remove ("Webtoon")            #Here I have removed the word "Webtoon" without using the index
# My_List.clear()                       #Here this will clear my list But my list will still be there
# del My_List [3]                       #Here value at the index 3 is been deleted (writing syntax of this command is different remember)
# del My_List                           #Here this command will delete My_List 

# My_List.sort()                        #Here this will sort My_List in alplabetical order
# My_List.sort(reverse=True)            #Here this will sort My_List in reverse alplabetical order            

print(My_List)