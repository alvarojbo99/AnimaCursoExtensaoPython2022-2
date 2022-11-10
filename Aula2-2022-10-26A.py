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
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir.")  
else:
  print("Você ainda é jovem") 



  #E se eu quisessem perguntar o gênero (M = Masculino e F = Feminino)
#Mostre (...e você também precisa/precisou prestar o serviço militar obrigatório)

genero = input("Informe o gênero M+Masculino, F=Feminino, O=Outros: ")
if idade >= 18 and genero == "M": 
  print("... e você também precisa/precisou prestar o serviço militar obrigaótio") 




print("vai ser executadade qualquer jeito")


