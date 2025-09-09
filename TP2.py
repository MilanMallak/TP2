#ce code
#Par Milan Mallak

import random
number = random.randint(0, 1000)

guess = int(input("Entre ta réponse"))
while guess != number :
    if guess >= number :
        if guess >= number + 100 :
            print("La réponse est moins que le chiffre que vous m'avez donné")
            guess = int(input("Entre ta réponse"))
        else :
            print("La réponse est moins que le chiffre que vous m'avez donné, mais vous êtes proche")
            guess = int(input("Entre ta réponse"))
    else :
        if guess <= number - 100 :
           print("La réponse est plus que le chiffre que vous m'avez donné")
           guess = int(input("Entre ta réponse"))
        else :
            print("La réponse est plus que le chiffre que vous m'avez donné,mais vous êtes proche")
            guess = int(input("Entre ta réponse"))
print(f"Bravo! la réponse, étais en effet {number}")