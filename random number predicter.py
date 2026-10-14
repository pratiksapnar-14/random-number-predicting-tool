import random
n = random.randint(1,100)
a=-1
guesses = 0
while(a!=n):
    guesses +=1
    a=int(input("Guess a number : "))
    if(a>n):
        print("choose a lower number please")
    else:
        print("choose a greater number please")

print(f"you have guessed thee number in {guesses} attempts")                