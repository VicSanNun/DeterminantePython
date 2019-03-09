#@author: Victor Nunes
#Estudante de Física e Engenharia
#Calcular Determinante de Matrizes básicas
#v.1.0 - 13/05/2018 00:20

#Definindo Funções para Calcular o Determinante

#Ordem 2
def ordem_2(a11, a12, a21, a22):
  det = ((a11*a22)-(a21*a12))
  return det
  
#Ordem 3
def ordem_3(a11, a12, a13, a21, a22, a23, a31, a32, a33):
  det = (((a11*a22*a33)+(a12*a23*a31)+(a13*a21*a32))-((a31*a22*a13)+(a32*a23*a11)+(a33*a21*a12)))
  return det

#Escolhendo a ordem da Matriz
ordem = int(input("Qual a ordem da Matriz ? 2 OU 3?"))

#Se ela for de Ordem 2
if (ordem == 2):
  linha1 = input("Insira os termos da primeira linha: ")
  
  #Conferindo a Quantidade de termos na linha
  if (linha1.count(" ") != 1):
    print("Dados Errados, Reinicie o Programa!");
  elif(linha1.count(" ") == 1):
    #Separando os Termos da Linha em Variáveis
    (a11, a12) = linha1.split(" ")
    #Convertendo para numero
    a11 = float(a11)
    a12 = float(a12)
  
  linha2 = input("Insira os termos da segunda linha: ")
  
  #Conferindo a Quantidade de termos na linha
  if(linha2.count(" ") != 1):
    print("Dados Errados, Reinicie o Programa!")
  elif(linha2.count(" ") == 1):
    #Separando os Termos da Linha em Variáveis
    (a21, a22) = linha2.split(" ")
    #Convertendo para numero
    a21 = float(a21)
    a22 = float(a22)
  
  determinante = ordem_2(a11, a12, a21, a22)
  print("\n","MATRIZ:")
  print("\n","|",a11, a12,"|")
  print("","|",a21, a22,"|")
  print("\n","Determinante =", determinante)
  
    
  
elif (ordem == 3):
  linha1 = input("Insira os termos da linha 1: ")
  
  #Conferindo Quantidade de Termos na MATRIZ
  if(linha1.count(" ") != 2):
    print("Dados Errados, Reinicie o Programa!")
  elif(linha1.count(" ") == 2):
    #Separando os Termos da Linha em Variáveis
    (a11, a12, a13) = linha1.split(" ")
    #Convertendo para numero
    a11 = float(a11)
    a12 = float(a12)
    a13 = float(a13)
    
  linha2 = input("Insira os termos da linha 2: ")
  
  #Conferindo Quantidade de Termos na MATRIZ
  if(linha2.count(" ") != 2):
    print("Dados Errados, Reinicie o Programa!")
  elif(linha2.count(" ") == 2):
    #Separando os Termos da Linha em Variáveis
    (a21, a22, a23) = linha2.split(" ")
    #Convertendo para numero
    a21 = float(a21)
    a22 = float(a22)
    a23 = float(a23)
    
  linha3 = input("Insira os termos da linha 3: ")
  
  #Conferindo Quantidade de Termos na MATRIZ
  if(linha3.count(" ") != 2):
    print("Dados Errados, Reinicie o Programa!")
  elif(linha3.count(" ") == 2):
    #Separando os Termos da Linha em Variáveis
    (a31, a32, a33) = linha3.split(" ")
    #Convertendo para numero
    a31 = float(a31)
    a32 = float(a32)
    a33 = float(a33)
    
  determinante = ordem_3(a11, a12, a13, a21, a22, a23, a31, a32, a33)
  print("\n","MATRIZ:")
  print("\n","|",a11, a12, a13,"|")
  print("","|",a21, a22, a23,"|")
  print("","|",a31, a32, a33,"|")
  print("\n","Determinante =", determinante)