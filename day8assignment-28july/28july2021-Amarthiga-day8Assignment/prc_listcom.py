Names = ["Abinaya", "Venkat", "Mekala", "Kowsalaya", "Aarthi", "Aasiha", "Mani", "David", "Godson"]
#task1
# New_Name =[]
# for n in Names:
#     if "a" in n:
#         New_Name.append(n)
# print(New_Name)

#task2
new_names =[n for n in Names if 's' in n]
print(new_names)

#task3
list =[24,23,21,56,3,9,12]
new=[x for x in list if x%2==0]
print(new)

#task Polyndrom
words = ["English","Tamil","civic","river","madam","example","running","mom", "malayalam","noon"]

polindrome =[i for i in words if i ==i[::-1]]
print(polindrome)

#task5
li = [i for i in range(2,12)]


#task6
x =[c for c in range(2,500) if c%2==1]
print(x)

#task7
words_new = [a.upper() for a in words]
print(words_new)

#task8
new1 = [i.replace("madam","sir") for i in words]
print(new1)