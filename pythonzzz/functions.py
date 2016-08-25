import random
def happy_bday(name):
    print("Happy birthday to you")
    print("Happy birthday to you")
    print("Happy birthday dear "+ name)
    print("Happy birthday to you")
def main():
    name_one = input ("name one: ")
    name_two = input ("name two: ")
    happy_bday(name_one)
    happy_bday(name_two)
# i in range(10):
#    color = [4, 78, "hi", "string", "purple", 56]
#    colors_length = len(color)
#    random_number = random.randint(0,colors_length)
#    print(color[random_number])
for i in range(10):
    color = [4, 78, "hi", "string", "purple", 56]
    random_number = random.randint(0,len(color)-1)
    print(color[random_number])
