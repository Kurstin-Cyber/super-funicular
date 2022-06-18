for i in range(2000,3201):
    if i%7 == 0 and i%5!=0:
        print (i, end= " ")

        #or

for i in range (2000,3201):
    if not i%7 == 0 and i%5:
        print (i, end = ",")

    print ("\b")