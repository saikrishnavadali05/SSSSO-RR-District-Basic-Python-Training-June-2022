def LastNlines(fname, N):
    # opening file using with() method
    # so that file get closed
    # after completing work
    with open(fname) as file:
         
        # loop to read iterate
        # last n lines and print it
        for line in (file.readlines() [-N:]):
            print(line, end ='')
file_name=input("Enter the File Name : ")
n=int(input("Enter the number of lines to be read : "))
LastNlines(file_name,n) 