import csv
  
l1=['a','b','c']
l2=['d','2','s']
l3=[1,2,3]
# dictionary of list
d = {"key1": l1, 
     "key2": l2, 
     "key3": l3}
  
# writing to csv file
with open("test.csv", "w") as outfile:
    
    # creating a csv writer object
    writerfile = csv.writer(outfile)
      
    # writing dictionary keys as headings of csv
    writerfile.writerow(d.keys())

    # writing list of dictionary
    writerfile.writerows(zip(*d.values()))

# import re
# import re

# #Check if the string starts with "The" and ends with "Spain":

# txt = " 1212121212121212 rain The in Spain"
# x = re.search("r[0-9]^The", txt)
# if x:
# 	print(txt)

# import re

# #original string
# string1 = "Hello!James12,India2020"

# pattern = r'[0-9]'

# # Match all digits in the string and replace them with an empty string
# new_string = re.sub(pattern, '', string1)

# print(new_string)


string1 = "238 NEO Sports"
print (string1.split(' ', 1))