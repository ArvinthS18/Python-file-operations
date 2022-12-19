import time
import shutil
import csv
import re 

file_name = input("Enter a filename:")
fileE_names = file_name.split('.')
print("File Extension :", fileE_names[1])

f=open(file_name,"r")
log_lines = f.read().split('\n')
# print(log_lines)
f.close()

shutil.copyfile(file_name, 'example_copy.log')

check=input("Search the string in case sensitive (Y/N):" )
names=input("Enter a string to search: ")

new12= "Search string is" +names+ ".txt"
f2=open(new12,"w")

start=start = time.time()

arr=[]
w=0
Line_Count = 0
for line in log_lines:
    Line_Count +=1 
    if check=='Y':
        # if line.find(names) != -1:
        if names.upper() in line !=-1:
            w+=1
            case="uppercase"
            print(names, 'string exists in file','Line Number:', log_lines.index(line)) 
            # f2.write('string exists in file Line Number:'+str(log_lines.index(line)))
            print(line)
            arr.append(line)
            # f2.write(line)
    elif check =='N':
        if names.lower() in line !=-1:
            w+=1
            case="lowercase"
            print(names, 'string exists in file','Line Number:', log_lines.index(line)) 
            # f2.write('string exists in file Line Number:'+str(log_lines.index(line)))
            # f2.write('\n')
            print(line)
            # f2.write(line)
            arr.append(line)
            # f2.write('\n')


print("Seraching a word in: ",case)
print("Total word to ocuurence in the file is: ",names,w)  
print("Number of lines in the file : ",Line_Count-1)

#write a output in another file 
f2.write("------------------------------$$$ File Details $$$------------------------------"+'\n')
f2.write("File Name: "+str(file_name)+'\n')
f2.write("File Extension: " +str(fileE_names[1])+'\n')
f2.write("String to search: "+str(names)+'\n')
f2.write("Case type(Upper/Lower) "+str(case)+'\n')
f2.write("Total Number of line in the file is: " +str(Line_Count-1)+'\n')
f2.write("Total ocuurence in the file is: " +str(w)+'\n')
for lines in arr:  
    f2.write('string exists in file Line Number:'+str(log_lines.index(line)))
    f2.write('\n')
    f2.write(lines)
    f2.write('\n')
   


l1,l2,l3,l4=[],[],[],[]
for new_line in arr:
    l1.append((re.search('\d{4}[/\-](0?[1-9]|1[012])[/\-](0[1-9]|[2][0-9]|3[01])',new_line)).group())
    l2.append((re.search('\d{2}[:]\d{2}[:]\d{2}',new_line)).group())
    l3.append((re.search('\d{3}[-]\d{4}',new_line)).group())
    l4.append(new_line.split(" ",1)[1])

bad_words = [names]

cs=input("you want to remove a serching word in a file:(Y/N)")
if cs=='Y':
    with open('example_copy.log') as oldfile, open('newfile.log', 'w') as newf:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                newf.write(line)

elif cs=='N':
    #    for line in log_lines:
    #         with open('quotes.csv', 'w', newline='') as file:
    #             writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
    #             writer.writerows(log_lines)
    # csv_file = open('quotes.csv', "w")
    # writer = csv.writer(csv_file)
    # writer.writerows([new_line] for new_line in arr)
    # csv_file.close()
    
    d = {"key1": l1, 
         "key2": l2, 
         "key3": l3,
         "key4": l4}
    with open("test.csv", "w") as outfile:
        writerfile = csv.writer(outfile)
        writerfile.writerow(d.keys())
        writerfile.writerows(zip(*d.values()))


end = time.time()
print("The time of execution of above program is :",(end-start), "ms")