import random
class Ada():
    courage = "high"
    def __init__(self,name,age,superpower):
        self.name = name
        self.age = age
        self.superpower = superpower
    def code(self, quality):
        if self.quality > 5:
            self.superpower = "rockstar"
        else:
            self.superpower = "patient"
    def question(self,confusion_level):
        if self.confusion_level >= 10:
            print("Ask a question")
        else:
            print("go help someone else")
list_students = []
for i in range(100):
    list_students.append(Ada("Nora",random.randint(10,30),"nice gal"))
for i in list_students:
    print(i.age)
