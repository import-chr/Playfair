import numpy as np
import math

class PlayFair:
    def __init__(self) -> None:
        self.alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    def verify(self, a, b):
        c = False
        for k in range(5):
            for l in range(5):
                if ord(a[k][l]) == ord(b):
                    c = True
        return c
    
    def position(self, a, b):
        pos = "00"

        for i in range(5):
            for j in range(5):
                if ord(a[i][j]) == ord(b):
                    pos = str(i) + "" + str(j)
        
        return pos
    
    def buildMtrx(self, charar, cipher_key):
        cont = 0
        cont2 = 0

        for i in range(5):
            for j in range(5):
                while True:
                    if cont < len(cipher_key):
                        if not self.verify(charar, cipher_key[cont]):
                            charar[i][j] = cipher_key[cont]
                            cont += 1
                            break
                        else:
                            cont += 1
                    else:
                        while True:
                            if cont2 < len(self.alphabet):
                                if not self.verify(charar, self.alphabet[cont2]):
                                    charar[i][j] = self.alphabet[cont2]
                                    cont2 += 1
                                    break
                                else:
                                    cont2 += 1
                        break
        
        return charar
    
    def showMtrx(self, charar):
        for i in range(5):
            for j in range(5):
                if charar[i][j] == b'I':
                    print('I/J', " ", end = '')
                else:
                    print(charar[i][j].decode(), "\t", end = '')
            print("")
        print("\n")
    
    def starMtrx(self):
        charar = np.chararray((5, 5))
        charar[:] = '*'
    
        return charar
    
    def pairChars(self):
        pairs = np.chararray(((math.ceil(len(Texto) / 2)) + 1, 2))
        pairs[:] = 'X'

        return pairs
    
    def cipher(self, txt, pairs, charar, cipher):
        cont = 0

        for i in range (math.ceil(len(txt) / 2) + 1):
            for j in range(2):
                if cont < len(txt):
                    pairs[i][j] = txt[cont]
                    cont += 1
                    if j == 1 and pairs[i][0] != b'X' and pairs[i][0] == pairs[i][1]:
                        pairs[i][1] = b'X'
                        cont -= 1

        self.showCipherResults(txt, pairs)

        X1 = 0
        X2 = 0
        Y1 = 0
        Y2 = 0

        for i in range(math.ceil(len(txt) / 2) + 1):
            for j in range(2):
                if (j == 0):
                    X1 = self.position(charar, pairs[i][j])[0]
                    X2 = self.position(charar, pairs[i][j])[1]
                else:
                    Y1 = self.position(charar, pairs[i][j])[0]
                    Y2 = self.position(charar, pairs[i][j])[1]

                X1 = int(X1)
                Y1 = int(Y1)
                X2 = int(X2)
                Y2 = int(Y2)

                W1 = X1
                W2 = Y2

                Z1 = Y1
                Z2 = X2

                if X2 == Y2:
                    W2 = X2
                    Z2 = Y2
                    W1 = X1 + 1
                    Z1 = Y1 + 1
                
                    if W1 == 5:
                        W1 = 0
                    
                    if Z1 == 5:
                        Z1 = 0

                if X1 == Y1:
                    W1 = X1
                    Z1 = Y1
                    W2 = X2 + 1
                    Z2 = Y2 + 1
                
                    if W2 == 5:
                        W2 = 0

                    if Z2 == 5:
                        Z2 = 0

                cipher[i][0] = charar[W1][W2]
                cipher[i][1] = charar[Z1][Z2]

        return cipher
    
    def decipher(self, txt, pairs, charar, decipher):
        cont = 0

        for i in range (math.ceil(len(txt) / 2)):
            for j in range(2):
                if cont < len(txt):
                    pairs[i][j] = txt[cont]
                    cont += 1

        self.showDecipherResults(txt, pairs)

        W1 = 0
        W2 = 0
        Z1 = 0
        Z2 = 0

        for i in range(math.ceil(len(txt) / 2)):
            for j in range(2):
                if (j == 0):
                    W1 = self.position(charar, pairs[i][j])[0]
                    W2 = self.position(charar, pairs[i][j])[1]
                else:
                    Z1 = self.position(charar, pairs[i][j])[0]
                    Z2 = self.position(charar, pairs[i][j])[1]

                W1 = int(W1)
                Z1 = int(Z1)
                W2 = int(W2)
                Z2 = int(Z2)

                X1 = W1
                X2 = Z2
                Y1 = Z1
                Y2 = W2

                if W2 == Z2:
                    X2 = W2
                    Y2 = Z2
                    X1 = W1 - 1
                    Y1 = Z1 - 1

                    if X1 == 5:
                        X1 = 0

                    if Y1 == 5:
                        Y1 = 0

                    if X1 == -1:
                        X1 = 4

                    if Y1 == -1:
                        Y1 = 4

                if W1 == Z1:
                    X1 = W1
                    Y1 = Z1
                    X2 = W2 - 1
                    Y2 = Z2 - 1

                    if X2 == 5:
                        X2 = 0

                    if Y2 == 5:
                        Y2 = 0

                    if X2 == -1:
                        X2 = 4

                    if Y2 == -1:
                        Y2 = 4

                decipher[i][0] = charar[X1][X2]
                decipher[i][1] = charar[Y1][Y2]
        
        return decipher
    
    def showCipherResults(self, original, cad):
        for i in range (math.ceil(len(original) / 2) + 1):
            for j in range(2):
                print(cad[i][j].decode(), "", end = '')
            print("\t", end = '')
        print("\n")
    
    def showDecipherResults(self, original, cad):
        for i in range (math.ceil(len(original) / 2)):
            for j in range(2):
                print(cad[i][j].decode(), "", end = '')
            print("\t", end = '')
        print("\n")

# ===================================
# >>------  INSTANCIA  ------<<
# ===================================
playfair = PlayFair()

while True:
    usr = int(input("[1] Cifrar\n[2] Descifrar\n[0] Salir\n[ ]"))

    if usr == 0:
        print("Saliendo...")
        break
    elif usr == 1:
        # ===================================
        # >>------  CIFRADO  ------<<
        # ===================================
        Texto = input("Cadena a cifrar: ")
        cipher_key = input("Llave de cifrado: ")

        Texto = Texto.upper().strip().replace(" ", "")
        Texto = Texto.replace("J", "I")

        cipher_key = cipher_key.upper().strip().replace(" ", "")
        cipher_key = cipher_key.replace("J", "I")

        charar = playfair.starMtrx()
        charar = playfair.buildMtrx(charar, cipher_key)

        playfair.showMtrx(charar)

        pairs = playfair.pairChars()
        ciphered = playfair.pairChars()

        finalCipher = playfair.cipher(Texto, pairs, charar, ciphered)

        playfair.showCipherResults(Texto, finalCipher)

        seguir = input("Volver al menu [s/n]: ")

        if seguir.lower() != 's':
            print("Saliendo...")
            break
    elif usr == 2:
        # ===================================
        # >>------  DESCIFRADO  ------<<
        # ===================================
        Texto = input("Cadena a descifrar: ")
        cipher_key = input("Llaver de cifrado: ")

        Texto = Texto.upper().strip().replace(" ", "")
        print(Texto)

        cipher_key = cipher_key.upper().strip().replace(" ", "")
        cipher_key = cipher_key.replace("J", "I")

        charar = playfair.starMtrx()
        charar = playfair.buildMtrx(charar, cipher_key)

        playfair.showMtrx(charar)

        pairs = playfair.pairChars()
        deciphered = playfair.pairChars()

        finalDecipher = playfair.decipher(Texto, pairs, charar, deciphered)

        playfair.showDecipherResults(Texto, finalDecipher)

        seguir = input("Volver al menu [s/n]: ")
        if seguir.lower() != 's':
            print("Saliendo...")
            break
