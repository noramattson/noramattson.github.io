import random
menu_adjective = ["Yummy", "Fresh", "Chewy", "Crunchy","Spicy","Dry", "Honey"]
menu_style = ["roasted","steamed","boiled","stewed","pureed","sauteed","fried"]
menu_dish = ["chicken","peanut","salad","sandwich","yogurt","bread","string beans"]
list_length = len(menu_adjective)
for i in range(list_length):
    list_length = len(menu_adjective)
    random_number = random.randint(0,list_length-1)
    random_number2 = random.randint(0,list_length-1)
    random_number3 = random.randint(0,list_length-1)
    print(menu_adjective[random_number]+" "+menu_style[random_number2]+" "+menu_dish[random_number3])
    menu_adjective.pop(random_number)
    menu_style.pop(random_number2)
    menu_dish.pop(random_number3)
