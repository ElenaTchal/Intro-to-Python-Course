# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    Print("File cannot be opened")
    quit()
fhread = fh.read()
fstrip = fhread.rstrip()
fcap = fstrip.upper()
print(fcap)
