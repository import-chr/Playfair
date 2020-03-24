import numpy as np;
import math;
def verifica(a,b):
    c=False;
    for k in range(5):
        for l in range(5):
            if ord(a[k][l]) == ord(b):
                c = True;
            #else:
                #print(a[k][l], " != ", b)
    return c;

def posicion(a,b):
    pos="00";
    for i in range(5):
        for j in range(5):
            if ord(a[i][j])==ord(b):
                pos=str(i)+""+str(j);
    return pos;
def construir_matriz(charar,Clave):
    Abecedario = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
    # Generar Matriz
    cont = 0
    cont2 = 0
    print("La clave es: ", Clave)
    for i in range(5):
        for j in range(5):
            while True:
                if cont < len(Clave):
                    if not verifica(charar, Clave[cont]):
                        charar[i][j] = Clave[cont];
                        cont = cont + 1;
                        break
                    else:
                        cont = cont + 1;
                else:
                    while True:
                        if cont2 < len(Abecedario):
                            if not verifica(charar, Abecedario[cont2]):
                                charar[i][j] = Abecedario[cont2];
                                cont2 = cont2 + 1;
                                break
                            else:
                                cont2 = cont2 + 1;
                    break;

    print("Resultado de Matriz");
    for i in range(5):
        for j in range(5):
            if charar[i][j] == b'I':
                print('I/J', " ", end='')
            else:
                print(charar[i][j].decode(), "\t", end='')
        print("");

    print("\n")
    return charar

Rta=int(input("Bienvenido\n\n1. Cifrar\n2. Descifrar\n\nRta: "))
if Rta==1:
    #Solicitar Datos
    Texto = input("Por favor introduzca el texto a cifrar: ");
    Clave = input("Por favor introduzca la clave: ");
    #Texto = "THIS SECRET MESSAGE IS ENCRYPTED";
    Texto = Texto.upper().strip().replace(" ", "");
    Texto = Texto.replace("J", "I");
    #Clave = "Yoan Pinzon";
    Clave = Clave.upper().strip().replace(" ", "");
    Clave = Clave.replace("J", "I");

    charar = np.chararray((5, 5));
    charar[:] = '*';
    charar=construir_matriz(charar,Clave)

    pares=np.chararray(((math.ceil(len(Texto)/2))+1,2));
    pares[:]='X';

    cifrado = np.chararray(((math.ceil(len(Texto) / 2)) + 1, 2));
    cifrado[:] = 'X';

    cont=0;
    for i in range (math.ceil(len(Texto)/2)+1):
        for j in range(2):
            if cont<len(Texto):
                pares[i][j] = Texto[cont]
                cont+=1;
                if (j==1 and pares[i][0] != b'X' and pares[i][0]==pares[i][1]):
                    pares[i][1]=b'X'
                    cont-=1


    for i in range (math.ceil(len(Texto)/2)+1):
        for j in range(2):
            print(pares[i][j].decode(), "", end='')
        print("\t", end='');

    print("\n")

    #Posiciones primera letra
    X1=0;
    X2=0
    #Posiciones segunda letra
    Y1=0
    Y2=0

    for i in range(math.ceil(len(Texto) / 2) + 1):
        for j in range(2):
            if (j == 0):
                X1 = posicion(charar,pares[i][j])[0]
                X2 = posicion(charar,pares[i][j])[1]
            else:
                Y1 = posicion(charar,pares[i][j])[0]
                Y2 = posicion(charar,pares[i][j])[1]
            #Caso 1
            X1 = int(X1)
            Y1 = int(Y1)
            X2 = int(X2)
            Y2 = int(Y2)

            #Caso 1
            W1=X1;
            W2=Y2;

            Z1=Y1;
            Z2=X2;
            #Caso 2
            if X2 == Y2:
                W2=X2
                Z2=Y2
                W1=X1+1
                Z1=Y1+1
                if W1==5:
                    W1=0
                if Z1==5:
                    Z1=0

            # Caso 3
            if X1 == Y1:
                W1 = X1
                Z1 = Y1
                W2 = X2 + 1
                Z2 = Y2 + 1
                if W2 == 5:
                    W2 = 0
                if Z2 == 5:
                    Z2 = 0

            cifrado[i][0] = charar[W1][W2]
            cifrado[i][1] = charar[Z1][Z2]

    for i in range (math.ceil(len(Texto)/2)+1):
        for j in range(2):
            print(cifrado[i][j].decode(), "", end='')
        print("\t", end='');

    print("\n")
else:
    #Descifrar
    # Solicitar Datos
    Texto = input("Por favor introduzca el texto a descifrar: ");
    Clave = input("Por favor introduzca la clave: ");
    #Texto = "WE DL LK HW LY LF XP QP HF DL HY HW OY YL KP";
    Texto = Texto.upper().strip().replace(" ", "");
    print(Texto)
    #Texto = Texto.replace("J", "I");
    #Clave = "Yoan Pinzon";
    Clave = Clave.upper().strip().replace(" ", "");
    Clave = Clave.replace("J", "I");

    charar = np.chararray((5, 5));
    charar[:] = '*';
    charar = construir_matriz(charar, Clave)

    pares=np.chararray(((math.ceil(len(Texto)/2))+1,2));
    pares[:]='X';

    descifrado = np.chararray(((math.ceil(len(Texto) / 2)) + 1, 2));
    descifrado[:] = 'X';

    cont=0;
    for i in range (math.ceil(len(Texto)/2)):
        for j in range(2):
            if cont<len(Texto):
                pares[i][j] = Texto[cont]
                cont+=1;
                """if (j==1 and pares[i][0] != b'X' and pares[i][0]==pares[i][1]):
                    pares[i][1]=b'X'
                    cont-=1"""


    for i in range (math.ceil(len(Texto)/2)):
        for j in range(2):
            print(pares[i][j].decode(), "", end='')
        print("\t", end='');

    print("\n")


    #Posiciones primera letra
    W1=0;
    W2=0
    #Posiciones segunda letra
    Z1=0
    Z2=0

    for i in range(math.ceil(len(Texto) / 2)):
        for j in range(2):
            if (j == 0):
                W1 = posicion(charar,pares[i][j])[0]
                W2 = posicion(charar,pares[i][j])[1]
            else:
                Z1 = posicion(charar,pares[i][j])[0]
                Z2 = posicion(charar,pares[i][j])[1]
            #Caso 1
            W1 = int(W1)
            Z1 = int(Z1)
            W2 = int(W2)
            Z2 = int(Z2)

            #Caso 1
            X1=W1;
            X2=Z2;

            Y1=Z1;
            Y2=W2;
            #Caso 2
            if W2 == Z2:
                X2=W2
                Y2=Z2
                X1=W1-1
                Y1=Z1-1
                if X1==5:
                    X1=0
                if Y1==5:
                    Y1=0
                if X1 == -1:
                    X1 = 4
                if Y1 == -1:
                    Y1 = 4

            # Caso 3
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

            descifrado[i][0] = charar[X1][X2]
            descifrado[i][1] = charar[Y1][Y2]

    for i in range (math.ceil(len(Texto)/2)):
        for j in range(2):
            print(descifrado[i][j].decode(), "", end='')
        print("\t", end='');

    print("\n")

#ZO MH LC HY ZK MN SO NQ DL KT OQ CY KI EC LK SO YI EQ PQ RX EY KR WM NS DL GY LD GF AB YA QN YE AP GN IX PG HY YS NB HT EC TL KF VN RP YT PU PF CY EB YA WM KI MP LF UZ LH TC YH NP CK KL LY YT KI GB DH CY EC RD GN CL GO IH YE TY KI XO UY VN SC LX KF MX PW
#WE DL LK HW LY LF XP QP HF DL HY HW OY YL KP