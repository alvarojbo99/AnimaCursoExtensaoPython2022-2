# Meu primeiro projeto Python!!! 
#
# print() = comando de saida
print("Alo mundo!")

#Quando quiser guardar uma string! (frase)
nome = "Alvaro Jesus"
#Quando quiser guardar um numero inteiro!
idade = 23 

#Exibir meu nome (que esta dentro da variável nome) 
print(nome)

#Quando quiser exibir a frase "Minha idade é" completando com o conteúdo da variável idade 
#print ("minha idade é" +idade)
print("minha idade é " +str(idade))
print(f"Minha idade é {idade}\n")
print("Minha idade é {}".format(idade))

#Quando quiser exibir "Meu nome é ... e tenho ... 
#anos.." trocando pelas variáveis nome e idade
print("Meu nome é {} e tenho {} anos".format(nome, idade))


''' 
Comentario em bloco

'''



print("aula 2")

# comando input(): quero permitir que 
# o usuário digite algo...
nome = input( "Boa noite! Digite seu nome: ")

idade = int(input("Digite sua idade: "))

#comando de saída..exibir na tela
print(nome)
 
print("Sua idade é {} anos" .format(idade))

dobro = idade * 2

print("O dobro da idade informada é {} anos" .format(dobro)) 

#Estrutura condicional - o famoso "SE" (if)
#Se a pessoa for maior de idade, mostre "Você é maior de idade, ótimo! Já pode beber ou dirigir"
if idade >= 18:
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir")




