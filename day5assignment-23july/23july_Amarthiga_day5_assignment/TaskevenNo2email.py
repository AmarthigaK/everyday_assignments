import smtplib as send 
even = []
for x in range(10):
    n1 = (int(input("Give any number")))
    if n1%2==0: 
        even.append(n1)

print(even)
print(type(even))
output = [str(a) for a in even]
print(output)
y = ",".join(output)
'''str_even = map(str, even)
print(list(str_even))'''

connection=send.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("amarproject2021@gmail.com", "remoteGIS24")
connection.sendmail("amarproject2021@gmail.com", "amarthiga@gmail.com", y)
print("Email has sent successfully")
connection.quit()
