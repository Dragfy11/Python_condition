wallet = 5000
computer_price = 1000

# le prix de l'ordinateur est inférieur à 1000 €
if computer_price <= wallet or computer_price > 1000:
    print("l'achat est possible")
    wallet -= computer_price

else:
    print("l'achat est impossible, vous n'avez que {} €".format(wallet))

#condition ternaire
text=("L'achat est possible", "l'achat est impossible")[computer_price <= 1000]
print(text)

print(wallet)