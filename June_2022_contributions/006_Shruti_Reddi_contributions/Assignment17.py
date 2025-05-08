def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
file_name=input("Enter the File Name : ")
n=int(input("Enter the number of lines to be read : "))
file_read_from_head(file_name,n)
