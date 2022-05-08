# In this lets initialize and implement a set function

#Record= {1,2,45,735}                         # This is a one way of setting a set function
Record_2= set(2,356,34,845)                   # This is another way of setting a set function but this is more efficient way of declaring the set
#Mix= set(523,"Apple Juice",True)             # Set can carry any data type 

# Record_3= set(24,26,62,64,82,82)            # Duplicate values are not allowed in the set 
# print(Record_3)

#print(len(Record_2))                         # This is how we can print the length of a set

#for x in Record_2:                           # This is how we can printout the whole set
#   print(x)

#if (356 in Record_2):                        # This is how we check whether the value is present in the set or not
#   print("Yes your entered value is present in the set")

#Record_2.add(500)                           # This is how we add a new value in the set
#Record_2.update(Mix)                        # This is how we add an another set in a previous set

#Record_2.remove(2)                          # This is how we remove a value from a set
#Record_2.pop()                              # This is how we pop out the value from the set but as set is unordered we don't know that what value will be pop out
#Record_2.clear()                            # This is how we clear all the variables or the values stored inside the set
#del Record_2                                # This is how we delete a whole set


print(Record_2)