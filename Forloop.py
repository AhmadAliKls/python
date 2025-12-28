firstnum = int(input("Enter the first number: "))
lastnum = int(input("Enter the last number: "))

if firstnum == lastnum:
    print("Both numbers are equal:", firstnum)
elif firstnum < lastnum:
    for i in range(firstnum, lastnum + 1):
        print(i)
else:
    for i in range(firstnum, lastnum - 1, -1):
        print(i)

print("Done")
