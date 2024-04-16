print("Welcome to my comp quiz")

playing = input("Do you want to play? ")
if playing != "yes":
    quit()

print("Okay lets play:)")
score = 0

answer = input("What does CPU stand for?")
if answer == "Central Processing Unit":
    print ('Correct')
    score += 1
else:
    print('Incorrect')

answer = input("What does RAM stand for?")
if answer == "Randon Acess Memory":
    print ('Correct')
    score += 1
else:
    print('Incorrect')
answer = input("What does PSU stand for?")
if answer == "Power Supply":
    print ('Correct')
    score += 1
else:
    print('Incorrect')

answer = input("What does GPU stand for?")
if answer == "Graphics Processing Unit":
    print ('Correct')
    score += 1
else:
    print('Incorrect')

print("You got " + str(score) + "questions correct!")
print("You got " + str(score / 4 * 100) + " % ")
