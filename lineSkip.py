

text_file = open("url.txt", "r")

text_file.close()

text_file = open("url.txt", "r")
print (text_file.read())
    
text_file.close()

text_file = open("url.txt", "r")

counter = 1
for counter in range(50):
    print(text_file.read(10))
    text_file.read(1)
    
text_file.close()




