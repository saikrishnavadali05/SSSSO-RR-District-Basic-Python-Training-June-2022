"""
How to keep old content when Writing to Files in Python?
"""




#solution

# Python program to keep the old content of the file
# when using write.

# Opening the file with append mode
file = open("1.txt", "a")

# Content to be added
content = "\n\n# This Content is added through the program #"

# Writing the file
file.write(content)

# Closing the opened file
file.close()
