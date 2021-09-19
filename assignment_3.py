
a = input()
upper_char = 0
lower_char = 0
for i in a:
    if ord(i) <=ord('z') and ord(i) >= ord('a'):
        lower_char +=1

    elif ord(i) <= ord('Z') and ord(i) >= ord('A'):
        upper_char += 1
print("No. of Upper case characters : ",upper_char)

print("No. of Lower case Characters : ",lower_char)
        