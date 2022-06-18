num= int(input("Enter number for factorial operation"))

#while loop

result= 1
count=num
while count:
    result *=count
    count -=1
    print(result)

    #for loop

result= 1
for i in range(1,num +1):
    result *=i
    print(result)