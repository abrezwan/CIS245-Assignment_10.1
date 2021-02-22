Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
def main():
directory = input ("Enter the directory you want to save the file to : ")
filename = input ("Enter the file name : ")
name = input ("Enter your name : ")
address = input ("Enter your address : ")
phone_number = input ("Enter your phone number : ")

if os.path.isdir (directory):
writeFile = open (os.path.join(directory,filename),'w')
writeFile.write (name+','+address+','+phone_number+'\n')
writeFile.close()
print ("File contents:")
readFile = open(os.path.join(directory,filename),'r')
for line in readFile:
print(line)
readFile.close()
else:
print ("The directory you are looking for does not exist")
main()
