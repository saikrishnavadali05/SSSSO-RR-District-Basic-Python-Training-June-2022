# appending lines to a file
# input lines for appending
lines = ["", "1. Steve Paul Jobs is regarded as a successful American businessman.",
         "2. He had attained success in different fields.",
         "3. He had a great contribution to the development of computers and mobiles.",
         "4. He is stated as the initiator of the personal computer revolution.",
         "5. He had served as the CEO of Apple Inc from 1997 to 2011."]
# opening file in a append mode
with open("Lines.txt", "a") as f:
    f.write("\n".join(lines))
