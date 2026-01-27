alunos = []
cadastro_novo_aluno = 'sim'

while cadastro_novo_aluno == 'sim':
    nome = input('Digite o nome do aluno: ')
    nota_1 = input('Digite a nota da prova 1:  ')
    nota_2 = input('Digite a nota da prova 2:  ')
    nota_3 = input('Digite a nota da prova 3:  ')
    
    int_nota_1 = int(nota_1)
    int_nota_2 = int(nota_2)
    int_nota_3 = int(nota_3)
    notas = (int_nota_1, int_nota_2, int_nota_3)
    media = ( (int_nota_1 + int_nota_2 + int_nota_3) / 3)
    
    aluno = ('Nome: ',nome,'Notas: ',notas ,'Média:', media)
    alunos.append(aluno)
    
    cadastro_novo_aluno = input('Deseja cadastrar outro aluno? digite [sim] ou [nao]')
    
    if cadastro_novo_aluno == 'nao':
     print(f'Os alunos cadastrados são: {alunos}')

print(f'Temos ao total {len(alunos)} Alunos cadastrados.')