"""Lab#03 / Christian Gower / 01/17/2023 """

def golfScore(score, par):
  if ( 3 <= par <= 5 ):
    if score == 1:
        result = 'Hole in One!'
    elif score + 1 == par:
        result = 'Birdie!'
    elif score + 2 == par:
        result = 'Eagle!'
    elif score + 3 == par:
        result = 'Albatross!'
    elif score + 4 == par:
         result = 'Condor!'
    elif score == par:
        result = 'Par!'
    elif score - 1 == par:
         result = 'Bogey!'
    elif score - 2 == par:
        result = 'Double Bogey!'
    elif score - 3 == par:
        result = 'Triple Bogey!'
    elif score -4 >= par:
        result = 'Come On! You can do better than that!'
    return result
  else:
      result = 'Error'
      return result
i = 0
while (i < 5):
    print('Iteration:', i)
    score = int(input('Enter total strokes: '))
    par = int(input('Enter par: '))
    print('Two arguments are passed to the Function')
    print('Function returning the result')
    results = golfScore(score, par)
    print(results)
    i += 1
