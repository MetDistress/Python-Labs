""" Lab#06 / Christian Gower / 2.14.2023 """

class Hurricane:
    def __init__(self):
        self.name = ''
        self.speed = 0
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_speed(self):
        return self.speed
    def set_speed(self, speed):
        self.speed = speed

class Group(Hurricane):
    def __init__(self):
        Hurricane.__init__(self)
        self.category = ''
    def set_category(self, speed):
        if 74 <= speed <= 95:
            self.category = 1
        elif 96 <= speed <= 110:
            self.category = 2
        elif 111 <= speed <= 129:
            self.category = 3
        elif 130 <= speed <= 156:
            self.category = 4
        elif speed >= 157:
            self.category = 5
    def display_all(self):
        return self.name, self.speed, self.category

#Task 1
myWind = Hurricane()
myWind.set_name('IRS')
myWind.set_speed(100)
z = myWind.get_name()
z1 = myWind.get_speed()
print('Task 1')
print('Name:', z, 'Speed:', z1)

#Task 2
aGroup = Group()
aGroup.set_name('RIA')
aGroup.set_speed(120)
aGroup.set_category(120)
result = aGroup.display_all()
print('Task 2')
print(result)

#Challenge Activity
'''
bGroup = Group
bGroup.set_name('XYZ')
bGroup.set_speed(3000)
bGroup.set_cat(3000)
bGroup.display_all()

aList = []
aList.append(aGroup)
aList.append(bGroup)
'''
