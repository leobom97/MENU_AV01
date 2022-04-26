'''Sistema para cadastrar e listar alunos'''
from lib.interface import *
from time import sleep
from lib.arquivo import *

arq = 'listaalunos.txt'

if not arquivoExiste(arq):
    print('O arquivo não existe por favor selecione a opção de criar o arquivo de registro')
elif arquivoExiste(arq):
    print('O arquivo de registro já existe.Não precisa criar outro!!!')

while True:
    resposta = menu(['Criar novo arquivo de registro','Cadastrar Alunos','Listar Alunos','Sair do Sistema'])
    if resposta == 1:
        #Criar novo arquivo para armazenar dados dos estudantes
        criarArquivo(arq)
    elif resposta == 2:
        #Cadastrar novo(a) aluno(a)
            cabeçalho('NOVO CADASTRO')
            nome = str(input('Nome: '))
            nota1 = float(input('Informe a primeira nota do Aluno: '))
            nota2 = float(input('Informe a segunda nota do Aluno: '))
            nota3 = float(input('Informe a terceira nota do Aluno: '))
            media = (nota1 + nota2 + nota3) / 3
            print(f'Media do aluno {media:.2f}')
            idade = leiaInt('Idade: ')
            cadastrar(arq, nome, idade, media)
    elif resposta == 3:
        #Opção de listar os alunos cadastrados
        lerArquivo(arq)
    elif resposta == 4:
        #Sair do sistema
        cabeçalho('Saindo do menu...Agradeçemos por usar nosso sistema :)')
        break
    else:
        cabeçalho('ERRO! Digite uma opção válida!')
    sleep(2)