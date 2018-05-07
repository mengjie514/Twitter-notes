# File Objects 
f = open('pre-SCOvENG.json', 'r')
print(f.name)
print(f.mode)
f.close()

# Open file with context manager (small file)
with open('pre-SCOvENG.json', 'r') as f:
    print(f.read())

with open('pre-SCOvENG.json', 'r') as f:
    f_contents = f.read()
    print(f_contents)

# Open large file 
with open('pre-SCOvENG.json', 'r') as f:
    # grab the first line
    f_contents = f.readline()
    print(f_contents)

with open('pre-SCOvENG.json', 'r') as f:
    # simply iterate over the lines in file and read all
    for line in f:
        print(line)

with open('pre-SCOvENG.json', 'r') as f:
     # with f.read() to specify the amount of data want to read at a time
     # passing in a 100 and print out the first 100 characters of our file
     f_contents = f.read(100)
     print(f_contents)

with open('pre-SCOvENG.json', 'r') as f:
    size_to_read = 100
    f_contents = f.read(size_to_read)
    print(f_contents)

with open('pre-SCOvENG.json', 'r') as f:
    size_to_read = 100
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
    print(f_contents, end='')
    f_contents = f.read(size_to_read)