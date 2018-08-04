'''
+++ READING FILES +++
Involves two files, ex15.py that runs and ex15_sample.txt plain text file to read from the script.
Open the .txt and print it out. Do not hard code it.
'''

from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file %r:" % filename)
print(txt.read())

print("I'll also ask you to type it again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

