#try and exception program

"""try:
    age=int(input("Enter your age: "))
    print("No problem.")
except ValueError:
    print("There is a Value Error! Please enter number only.")"""

#file program

#create file and writing in it
f=open("file1","w")
f.write("Hello World\n")
f.write("Good Morning\n")
f.close()
f=open("file1","r")

#read from file
f=open("file1","r")
print(f.read())
f.close()

#appending in file 1
f=open("file1","a+")
f.write("Good Afternoon")
f.close()
f=open("file1","r")

#recreate new file
f1=open("file2","w")
for data in f:
    f1.write(data)
f.close()
f1.close()

#appending in file 2
f1=open("file2","a+")
f1.write("\nFile copied")
f1.close()
f1=open("file2","r")



