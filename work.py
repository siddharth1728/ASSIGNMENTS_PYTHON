a = ["cat", "dog", "monkey", "cow"]

for i in range(len(a)):
    print(a[i] + a[(i + 1) % len(a)], end=", ")