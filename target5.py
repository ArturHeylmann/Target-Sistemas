
a = input("Escreva uma palavra: ")

reverse = []
print(len(a))
for i in reversed(range(len(a))):
    reverse.append(a[i])

reverseString = ''.join(reverse)
print(reverseString)


