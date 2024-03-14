""" Lab#07 / Christian Gower / 3.2.2023 """
'''List = [2, 3, 4]
i = 0'''
'''if i in range(0, len(List)):
    i +=1
    print(List[i], end = '')
    print('\n')

List2D = [[2, 3, 4],
          [5, 6, 7],
          [8, 9, 10],
          [11, 12, 13]]

print('size of row', len(List2D))
print('size of column', len(List2D[0]))

for i in range(0, len(List2D)):
    print('rows', i, '', List2D[i])'''

'''for y in range(0, len(List2D)):  #row
    for x in range(0, len(List2D[0])): #col
        print(List2D[y][x], end=' ')
    print('\n')'''

List3D = [[[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],],

          [[10, 11, 12],
          [13, 14, 15],
          [16, 17, 18],],

          [[19, 20, 21],
          [22, 23, 24],
          [25, 26, 27],]]

'''
Q1
'''
print('Q1:')
print('Length of x: ==>', len(List3D[2][0]))
print('Length of y: ==>', len(List3D[0]))
print('Length of z: ==>', len(List3D))

'''
Q2
'''
print('Q2:')
for z in range(0, len(List3D)):
    print(List3D[z])

'''
Q3
'''
print('Q3:')
for z in range(0, len(List3D)):
    for y in range(0, len(List3D[0])):
        for x in range(0, len(List3D[2][0])):
            print(List3D[z][y][x], end = ' ')
    print('\n')


