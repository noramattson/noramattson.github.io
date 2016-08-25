import random
#apple = ["a","p","p","l","e"]
#orange = ["o","r","a","n","g","e"]
word1 = input("input word: ")
word2 = input("input word: ")
apple = list(word1)
orange = list(word2)
fruits = apple + orange
new_word = []
for i in range(len(fruits)):
    lengthfruits = len(fruits)-1
    randomnumber = random.randint(0,lengthfruits)
    new_word.append(fruits[randomnumber])
    fruits.pop(randomnumber)
print("".join(new_word))

class Student():
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("Hi")
    def returnname(self):
        return self.name
nora = Student("Nora")
print(nora.name)
nora.greet()
