"""Lab#02 / Christian Gower / 01/17/2023 """

score = int(input('Enter total strokes: '))
par = int(input('Enter par: '))

def golfScore(score, par):
    if score == 1:
        print('Hole in One!')
    elif score + 1 == par:
        print('Birdie!')
    elif score + 2 == par:
        print('Eagle!')
    elif score + 3 == par:
        print('Albatross!')
    elif score + 4 == par:
         print('Condor!')
    elif score == par:
        print('Par!')
    elif score - 1 == par:
         print('Bogey!')
    elif score - 2 == par:
        print('Double Bogey!')
    elif score - 3 == par:
        print('Triple Bogey!')
    elif score -4 >= par:
        print('Come On! You can do better than that!')



if (par <= 5  and par >= 3):
    golfScore(score, par)
else:
    print('Error! Par must be between 3 and 5.')
