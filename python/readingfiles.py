from sys import argv
test, text.txt = argv

txt = open(text.txt)

print "Here's your file %r:" %text.txt
print txt.read()

print "Type the filename again:"
text.txt = raw_input("> ")

txt= open(text.txt)

print text.txt.read()

input() 