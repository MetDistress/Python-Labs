""" Lab#09 / Christian Gower / 3.30.2023 """

loc = "C:\\Users\\cg19198\\Documents\\alice.txt"
aFile = open(loc,'r')
Lines = aFile.readlines()
count = len(Lines)
print('Number of Lines:', count)
print('Name of File:', aFile.name)
print('Open Mode:', aFile.mode)
print('Open or Closed:', aFile.closed)
print('Content of the Last 5 Lines (Even Number):')

counter = 0
for i in Lines: #everything
    counter = counter + 1
    if counter > count - 10:
        if counter % 2 == 0:
            print('(', counter, ')', i)

aFile.close()
print('Open or Closed:', aFile.closed)
