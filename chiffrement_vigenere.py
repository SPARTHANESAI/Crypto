def chiffrement_polyalphabetique(texte, cle):
    texte_chiffre = ""
    index_cle = 0

    for char in texte:
        if char.isalpha():
            if char.isupper():
                decalage = ord(cle[index_cle % len(cle)].upper()) - ord('A')
                texte_chiffre += chr((ord(char) + decalage - ord('A')) % 26 + ord('A'))
            else:
                decalage = ord(cle[index_cle % len(cle)].lower()) - ord('a')
                texte_chiffre += chr((ord(char) + decalage - ord('a')) % 26 + ord('a'))
            index_cle += 1
        else:
            texte_chiffre += char

    return texte_chiffre

def dechiffrement_polyalphabetique(texte_chiffre, cle):
    texte_dechiffre = ""
    index_cle = 0

    for char in texte_chiffre:
        if char.isalpha():
            if char.isupper():
                decalage = ord(cle[index_cle % len(cle)].upper()) - ord('A')
                texte_dechiffre += chr((ord(char) - decalage - ord('A')) % 26 + ord('A'))
            else:
                decalage = ord(cle[index_cle % len(cle)].lower()) - ord('a')
                texte_dechiffre += chr((ord(char) - decalage - ord('a')) % 26 + ord('a'))
            index_cle += 1
        else:
            texte_dechiffre += char

    return texte_dechiffre

# Exemple d'utilisation
message_chiffre = "Iplvsw lw oswecw"
cle_poly = "FEU"

message_dechiffre = dechiffrement_polyalphabetique(message_chiffre, cle_poly)

print("Message chiffré:", message_chiffre)
print("Message déchiffré:", message_dechiffre)


# Exemple d'utilisation
message_clair = "Bonjour le monde"
cle_poly = "FEU"

message_chiffre = chiffrement_polyalphabetique(message_clair, cle_poly)

print("Message clair:", message_clair)
print("Message chiffré:", message_chiffre)
