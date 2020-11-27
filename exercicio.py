"""1. [ 7 pontos ] Crie um programa utilizando a linguagem de programaçãoPYTHON. Elabore uma estrutura (tipo de dado) para representar o Funcionário
(código, nome, salário) de uma empresa. As funções de cadastrar e mostrar devem conter passagem de parâmetro que será o vetor dos funcionários,
assim como foi abordado, explicado, apresentado em aula. As outras funções, verifique o que é necessário como parâmetro.
O programa deverá ter uma função para cada item do menu de opções:

...: PROGRAMA DE GERENCIAMENTO DE FUNCIONÁRIOS :...

Cadastrar no vetor e arquivo
Mostrar do vetor
Mostrar do arquivo
Excluir pelo código
Alterar nome e salário
Sair
Para a opção 1 ( 2 pontos ): deve-se desenvolver uma função para cadastrar cinco funcionários da empresa num vetor e também num arquivo funcionario.txt

Para a opção 2 ( 1 ponto ): deve-se desenvolver uma função para mostrar todos os dados dos funcionários da empresa na mesma linha, que estão no vetor

Para a opção 3 ( 1 ponto ): deve-se desenvolver uma função para mostrar todos os dados dos funcionários da empresa na mesma linha, que estão
armazenados no arquivo funcionario.txt

Para a opção 4 ( 1 ponto ): deve-se desenvolver uma função para, a partir de uma pesquisa realizada por um código,
a função deverá encontrar junto aos funcionários cadastrados e caso exista, exclua o funcionário do vetor

Para a opção 5 ( 1 ponto ): deve-se desenvolver uma função para, a partir de uma pesquisa realizada por um código,
a função deverá encontrar junto aos funcionários cadastrados e caso exista, permita que o usuário APENAS ALTERE o NOME e o SALÁRIO do funcionário do vetor

A construção como um todo do programa, receberá mais 1 ponto, caso esteja de acordo com o pedido do exercício."""
class Funcionario:
    codigo = 0
    nome = ""
    salario = 0.0
def menu():
 print("...: PROGRAMA DE GERENCIAMENTO DE FUNCIONÁRIOS :...")
 print("1.Cadastrar no vetor e arquivo digite 1")
 print("2.Mostrar do vetor digite 2")
 print("3.Mostrar do arquivo digite 3")
 print("4.Excluir pelo código digite 4")
 print("5.Alterar nome e salário digite 5")
 resposta = int(input("escolha uma das opções acima......"))
 return resposta;
def cadastrar(v):
    
    arquivo = open("funcinarios.txt", "w")
    for x in range(3):
        f = Funcionario()
        f.codigo = int(input("digite o código do funcionário ->"))
        f.nome = input("digite o nome do funcionário -> ")
        f.salario = float(input("digite o salário do funcionário ->"))
        v.append(f)
        arquivo.write('{} {} {:.2f}\n'.format(f.codigo, f.nome, f.salario))
    arquivo.close()
    input("digite algo para continuar.......")               
                   
    return build(v)
def mostrar(v):
   print("")  
   print("MOSTRAR DADOS DO VETOR")
   
    
   if len(v) == 0:
       print("Não ha dado no vetor")
       input("Digite algo para continuar...")
       return build(v)
   else:
     for x in range(len(v)):
         f = Funcionario()
         f.codigo = v[x].codigo
         f.nome = v[x].nome
         f.salario = v[x].salario
         print("")
         print("Código:",f.codigo,"Nome:",f.nome,"Salário;",f.salario)
     input("digite algo para continuar.......")
   
                   
   return build(v)
def mostrar_arquivo(v):
  arquivo = open("funcinarios.txt", "r")
  print("MOSTRAR DADOS DE ARQUIVO")
  for z in arquivo.readlines():
    print("-" * 120)
    f = Funcionario()
    f.codigo, f.nome, f.salario = z.strip().split(" ")
    print("Código do Funcionário: {}\t\tNome do Funcionário: {}\t\tSalário do Funcionário: {}".format(f.codigo,f.nome,f.salario))
  arquivo.close()
  input('Digite qualquer tecla para voltar ao menu...')
  return build(v)
def deletar(v):
    n_existe = True
    codigo = int(input("Digite o codigo do funcionário para excluir -> "))
    for r in range(len(v)):
       if codigo == v[r].codigo:
           v.pop(r)
           print("Funcionário excluido com sucesso!!!!")
           input("Volte ao Menu...............")
           n_existe = False
           
          
          
    if n_existe:
       print("Codigo não existe")
       input("Volte ao menu.....")
       return build(v)
    return build(v)
def alterar(v):
    n_existe = True
    codigo = int(input("Digite o codigo do funcionário para alterar -> "))
    for w in range(len(v)):
       if codigo == v[w].codigo:
           v[w].nome = input("Digite o nome do funcionário para alterar->")
           v[w].salario = float(input("Digite o salario do funcionário para alterar->"))
           
           input("Volte ao Menu...............")
           n_existe = False
           
          
          
    if n_existe:
       print("Codigo não existe")
       input("Volte ao menu.....")
       return build(v)
    return build(v)
   
    

def build(vetor):
   resposta = menu()
   if resposta == 1:
       cadastrar(vetor)
   elif resposta == 2:
       mostrar(vetor)
   elif resposta == 3:
       mostrar_arquivo(vetor)
   elif resposta == 4:
       deletar(vetor)
   elif resposta == 5:
       alterar(vetor)    
   else:
       print("Digite uma das opções acima")
       input("Volte ao menu.....")
       return build(vetor)
    
       
       

def main():
     vetor_funcionarios = [];
     build( vetor_funcionarios)
main()     
     
     
 
    
       
    


    
    
