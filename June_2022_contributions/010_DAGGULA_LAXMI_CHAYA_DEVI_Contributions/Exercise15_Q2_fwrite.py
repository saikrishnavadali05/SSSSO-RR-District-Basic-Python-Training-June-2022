# script that write lines to the file
# providing list of lines to write in file
lines = ["1. Steve Jobs is a popular name in the world.",
         "2. He was the co-founder and chairman of Apple Inc.",
         "3. He is also referred to as an industrial designer, investor, and media tycoon.",
         "4. His full name was Steven Paul Jobs.",
         "5. He was born on 24 th February in the year 1955."]
# using fwrite
with open("Lines.txt", "w") as f:
    f.write("\n".join(lines))
