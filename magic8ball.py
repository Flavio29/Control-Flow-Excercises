import random

name = "Jose"
question = "Will I win the lottery?"
answer = ""

random_number = random.randint(1, 12)
# print(random_number)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "Why you asking me?"
elif random_number == 11:
  answer = "Check the weather app."
elif random_number ==12:
  answer = "I think so..."      
else:
  answer = "Error"

if name == "":
  print ("Question: " + question)
else:
  print(name + " asks: " + question)

if question == "":
  print("Where is your question?")
else:  
   print("Magic 8-Ball's answer: " + answer)