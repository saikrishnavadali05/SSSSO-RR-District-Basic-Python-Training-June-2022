number_of_words = 0
with open('Assignment-2question19_Input.txt','r') as File_input:
    data = File_input.read()
lines = data.split()
number_of_words += len(lines)
print(number_of_words)

with open('Assignment-2question19_Input.txt','r') as File_input:
    print(File_input.read())