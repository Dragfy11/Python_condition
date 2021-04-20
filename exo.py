#place de cinéma

#récolter l'age de la personne "quel est votre age ?"
age = int(input("Quel est votre age?"))
#si la personne est mineur -> 7€
if age < 18:
    prix_total = 7
#si la personne est majeur -> 12€
else:
    prix_total = 12

# ternaire
#prix_total = (7, 12)[age < 18]

#souhaitez-vous du pop corn?
pop_corn = input('Souhaitez-vous du pop corn ?')
#si oui -> +5€
if pop_corn == "oui":
    prix_total += 5
#afficher ce prix total à payer
print("vous devez payer {} €".format(prix_total))