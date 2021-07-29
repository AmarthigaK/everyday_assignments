for i in range(1,5):
    print(i)

#2
for i in range(1,11):
    if i==6:
        break
    else:
        print(i,end=" ")

#3
for i in range(1,11):
    if i==6:
        continue
    else:
        print(i,end=" ")

#4
for i in range(1,21):
    if i==6:
        pass        #nullifing effect
    print(i,end=" ")  # end=" " --> for horizontal line output

#5
for i in range(-11,11):
    if i==6:
        continue
    else:
        print(i,end=" ")
