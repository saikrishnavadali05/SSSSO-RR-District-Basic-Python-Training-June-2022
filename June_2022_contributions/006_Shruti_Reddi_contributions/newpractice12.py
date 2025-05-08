 #Write a function in python to read the content 
 #from a text file "poem.txt" line by line and
 #display the same on screen. Solution

#file = open ("poem_txt.txt" , "r")

#for line in file:
       # print(line, end="")
    
#file.close()

#Write a function in python to count the number of lines from a text file "story.txt" which is not starting with an alphabet "T". 

#def line_count():
   # file = open("story.txt","r")
    ##for line in file:
        #if line[0] not in 'T':
          #  count+= 1
    #file.close()
    #print("No of lines not starting with 'T'=",count)

#line_count()

#def count_words():
   # file = open("story.txt","r")
    #count = 0
    #data = file.read()
    #words = data.split()
    #for word in words:
       # count += 1
    #print("Total words are",count)
   # file.close()

#count_words()

#def count_the():
   # file = open("story.txt","r")#
   # count = 0
    #data = file.read()
    #words = data.split()
    #for word in words:
     #   if word =="the" or word =="The":
        #    count += 1
   # print(count)

#    file.close()

#count_the()

#def display_words():
  # file = open("story.txt","r")
   #count = 0
   #data = file.read()
   #words = data.split()
   #for word in words:
   #  if len(word)<=4:
    #     print(word, end=" ")
   #print(count)

  # file.close()

#display_words()

#def count1_words():
   #file = open("story.txt","r")
   #count = 0
   #data = file.read()
   #words = data.split()
   #for word in words:
   #  if word=="this" or word=="This" or word=="these" or word=="These":
    #     count+=1
  # print(count)

  # file.close()

#count1_words()

#def end_words():
   #file = open("story.txt","r")
   #count = 0
   #data = file.read()
   #words = data.split()
   #for word in words:
     #if word[-1]=="e":
        # count+=1
   #print(count)

   #file.close()

#end_words()


#def word_uppercase():
  # file = open("story.txt","r")
   #count = 0
   #data = file.read()
   #for letter in data:
    # if letter.isupper():
       #  count+=1
   #print(count)

   #file.close()

#word_uppercase()

#def word_search():
 # file = open("matter.txt","r")
  #count = 0
  #data = file.read()
  #for letter in data:
     #   print(letter, end="#")

  #file.close()

#word_search()

#def JTOI():
  #file = open("words.txt","r+")
  #count = 0
  #data = file.read()
  #for letter in data:
       # if letter=="J":
            # print("I",end="")
        #else:
            #print(letter,end="")

  #file.close()

#JTOI()

def AMCount() :
  file = open("europe.txt","r")
  counta = 0
  countb=0
  data = file.read()
  for letter in data:
       if letter=="A"or letter=="a": 
            counta+=1
             
       elif letter=="M" or letter=="m":
            countb+=1
            
  file.close()
  print('A or a:',counta)
  print('M or m:',countb)

AMCount()
