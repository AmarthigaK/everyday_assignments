import smtplib
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("amarproject2021@gmail.com", "remoteGIS24")
message= "Hi, I am sending a email by my python code.:) Happy Learning"
connection.sendmail("amarproject2021@gmail.com","amarthiga.k@gmail.com",message)
print("Email has sent successfully")
connection.quit()

