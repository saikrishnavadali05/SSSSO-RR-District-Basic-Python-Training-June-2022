with open("input_name.txt", "r") as f:
    line = f.readline()
# split line in to words and storing in list

data = line.split()
# printing lastname firstname middlename
print(data[-1], data[0], data[1])

# saving lastname in last_name.txt file
with open(" last_name.txt", "w") as f:
    f.write(data[-1])

# saving firstname in first_name.txt file
with open("first_name.txt", "w") as f:
    f.write(data[0])

# saving middlename in middle_name.txt file
with open("middle_name.txt", "w") as f:
    f.write(data[1])
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
