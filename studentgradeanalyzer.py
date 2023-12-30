n = int(input("Please enter the number of subjects: "))
mark = []
sum = 0
av = 0

for i in range(n):
    print("Enter the mark obtained in subject", i+1, ":")
    mark.append(int(input()))
    av = (av + mark[i]) / n
    sum = sum + mark[i]

def sort(mark):
    n = len(mark)
    for i in range(n-1):
        for j in range(n-i-1):
            if mark[j+1] < mark[j]:
                temp = mark[j+1]
                mark[j+1] = mark[j]
                mark[j] = temp

sort(mark)
print("-----------------------")
print("Total marks obtained:", sum)
print("Your average is:", av)
print("Your maximum mark obtained is:", mark[n-1])
print("Your minimum mark obtained is:", mark[0])
print("-----------------------")
print("Result status:")
for i in range(n):
    if(mark[i]>=35):
        print("PASS in subject ",i+1)
    else:
        print("FAIL in subject ",i+1)
if(av>=90):
    print("The overall Grade: A+")
elif(av>=80 and av<90):
    print("The overall Grade: A")
elif(av>=70 and av<80):
    print("The overall Grade: B+")
elif(av>=60 and av<70):
    print("The overall Grade: B")
elif(av>=50 and av<60):
    print("The overall Grade: C+")
elif(av>=35 and av<50):
    print("The overall Grade: C")
else:
    print("The overall Grade: F")
