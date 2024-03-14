"""" Lab#04 / Christian Gower / 1.26.2023 """

print('Step 1:')
my_flower1 = input('My Flower 1:')
my_flower2 = input('My Flower 2:')
my_flower3 = input('My Flower 3:')
your_flower1 = input('Your Flower 1:')
your_flower2 = input('Your Flower 2:')
their_flower = input('Their Flower:')

my_list = [my_flower1,my_flower2, my_flower3]
print('Step 2:', my_list)
your_list = [your_flower1, your_flower2]
print('Step 3:', your_list)
our_list = my_list + your_list
print('Step 4:', our_list)
our_list.append(their_flower)
print('Step 5:', our_list)
our_list[1] = their_flower
print('Step 6:', our_list)
del our_list[1]
print('Step 7:', our_list)
del our_list[1]
print('Step 8:', our_list)

