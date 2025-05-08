#to print vowels in a sentence
dataString = input("Enter a sentence :")
print("Input String : ", dataString)
for i in dataString:
    if i.lower() in ['a','e','i','o','u']:
        print(i)