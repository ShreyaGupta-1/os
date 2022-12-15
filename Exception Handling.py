f1 = input("Enter first file name: ")
data1 = input("Enter data for first file: ")
f1 = open(f1, "w")
f1.write(data1)

f2 = input("Enter second file name: ")
data2 = input("Enter data for second file: ")
f2 = open(f2, "w")
f2.write(data2)

for i in f1:
    f2.write(i)
    f2.write("\n")
f2.close()
f1.close()
f3 = open("C:/Users/91945/Desktop/Phil.txt","r" )
print("The new file is for second file.")
print(f3.read())
