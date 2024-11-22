def dechiffrement_cesar(message, clef):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    resultat = ''

    for lettre in message.upper():  
        if lettre in alphabet:  
            index = (alphabet.index(lettre) - clef) % 26
            resultat += alphabet[index]
        else:
            resultat += lettre  

    return resultat


texte_chiffre = input("Entrez un message à déchiffrer : ")
decalage = int(input("Entrez la clé utilisée pour le chiffrement : "))
print("Message déchiffré :", dechiffrement_cesar(texte_chiffre, decalage))

