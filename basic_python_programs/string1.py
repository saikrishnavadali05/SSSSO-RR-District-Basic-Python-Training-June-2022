"""
Write a program to find how many times substring “sai” appears in the 
given string. write script Using string method and also without it
"""






#solution1

str_x = "sai is good developer. sai is a writer"
# use count method of a str class
cnt = str_x.count("sai")
print(cnt)

#solution 2

def count_emma(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + 4] == 'sai'
    return count

count = count_emma("sai is good developer. sai is a writer")
print("sai appeared ", count, "times")