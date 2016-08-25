count = 1
while count <= 100:
    if count % 15 == 0:
        print("fizzbuzz")
    if count % 5 == 0:
        print("buzz")
    if count % 3 == 0:
        print("fizz")
    count += 1
    print(count)
