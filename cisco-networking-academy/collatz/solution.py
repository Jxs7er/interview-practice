while True:
    try:
        c0 = int(input("Insert a number: "))
        if c0 > 0:
            break
    except ValueError:
        continue

counter = 0

while c0 != 1:
    c0 = c0 // 2 if c0 % 2 == 0 else 3 * c0 + 1
    print(c0)
    counter += 1
else: 
    print(f"pasos = {counter}")