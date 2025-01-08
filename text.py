# with open("example.txt",'w+') as f:
#     f.write("mantu kumbar\n")
#     f.write("powerbi\n")
#     f.write("sql\n")
#     f.seek(0)
#     print(f.read())

# with open("file operations.txt",'w+') as f:
#     f.write("Rashmika mandanna\n")
#     f.write("Ashika Ranganath\n")
#     f.write("Rachita Ram\n")
#     f.write("Rukhmini Vasanth\n")


# try:
#     with open("file operations.txt",'r') as f:
#         for line in f:
#             print(line,end='')
# except FileNotFoundError:
#     print("file does not exist!!")

# file_name=input("enter the filename :")
# input=input("write a text to insert into the above file: ")
# try:
#     with open(file_name,'w') as f:
#         f.write(input)
# except FileNotFoundError:
#     print("File does not exist!!")

try:
    with open("file operations.txt",'r') as f:
        lines=f.readlines()
        print("the number of lines in a file is",len(lines))
except FileNotFoundError:
    print("File does not exist!!")




    



