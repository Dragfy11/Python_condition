# exemple : Systeme de verification de mot de passe

password = input("Entrer votre mot de passe: ")
passeword_length= len(password)

#verifier si le mot de passe est inferieur à 8 caractères
if passeword_length <= 8:
    print("mot de passe trop court !")
elif 8 < passeword_length <= 12:
    print("mot de passe moyen !")
else:
    print("mot de passe parfait !")
print(passeword_length)