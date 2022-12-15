"""
file1=input("Enter the name of file1 with location: ")
file2=input("Enter the name of file2 with location: ")
try:
    file_1=open(file1,"r")
    file_2=open(file2,"a")
    nxt=file_1.readline()
    while nxt!="":
        file_1.write(nxt)
        nxt=file_2.readline()
    file_1.close()
    file_2.close()
    print("done")

except:
    print("File not found")
"""

old=input("Enter the name of  old file with location: ")
new=input("Enter the name of new file with location: ")
try:
    file_old=open(old,"r")
    file_new=open(new,"a")
    nxt=file_old.readline()
    while nxt!="":
        file_new.write(nxt)
        nxt=file_old.readline()
    file_old.close()
    file_new.close()
    print("done")
    

except:
    print("File not found")
   

