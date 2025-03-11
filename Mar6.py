#Day 5, It was very fun to create this quiz and I learned so much, for example, adding .lower after the var mention can make it so even if the answer is Yes and not yes, it'll work either way.
# Not only that, it was amazing creating a quiz with so many different variables.

print("Fantasy Character Quiz")
print("----------------------")

magic_answer = input("Do you believe in magic?: ")
if magic_answer.lower() == "yes":
  print("You might be a wizard or magical creature!")
  wise_answer = input("Are you wise?: ")
  if wise_answer.lower() == "yes":
    print("You're Gandalf! A wise wizard!")
  else:
    playful_answer = input("Are you playful and mischievous?: ")
    if playful_answer.lower() == "yes":
      print("You're a house elf! Small but mighty with magic!")
    else:
      print("You're a witch or wizard in training. Keep doing those spells!")

