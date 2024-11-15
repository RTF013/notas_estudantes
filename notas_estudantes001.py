nota_otima = 10
nota_boa = 8
nota_regular = 7
nota_razoavel = 6
nota_ruim = 5
qual_sua_nota = int(input("Digite nota do Aluno: "))

if qual_sua_nota == 10 or qual_sua_nota == 9:
    print('OTIMA')
elif qual_sua_nota == 8:
    print('Muito bem, BOA')
elif qual_sua_nota == 7:
    print('Aluno nota REGULAR')
elif qual_sua_nota == 6:
    print('Aluno RAZOAVEL')
elif qual_sua_nota == 5:
    print('Não foi dessa vez, RUIM')
else:
    print('Vixi está reprovado direto!')
