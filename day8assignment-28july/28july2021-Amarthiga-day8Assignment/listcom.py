Movies = ["Twilight", "Singam", "Dhoom", "Dangal", "soorarai potru", "Saina", "Uyare", "Sherlock Holmes", "Drishyam"]
#task1
New_Movie =[]
for n in Movies:
    if "a" in n:
        New_Movie.append(n)
print(New_Movie)

#task2
new_movie =[n for n in Movies if 's' in n]
print(new_movie)

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
new1 = [i.replace("noon","morning") for i in words]
print(new1)