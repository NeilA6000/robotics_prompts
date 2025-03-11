#This is my work for Day 6. I learned how to add 2 inputs with the AND thing which can help alot.
print("SECURE LOGIN")
username = input("Username > ")
password = input("Password > ")

if username == "mark" and password == "m123":
  print("Welcome Mark! Hope you're having a fantastic day.")
elif username == "suzanne" and password == "s456":
  print("Hey there Suzanne! Great to see you again!")
elif username == "alex" and password == "a789":
  print("Hi Alex! Your project updates look amazing.")
else:
  print("Invalid username or password. Access denied!")
