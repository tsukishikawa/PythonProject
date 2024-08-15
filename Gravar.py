#A função close() é muito importante para encerrar o arquivo após sua utilização.
#Atenção: Nunca abra o arquivo com a função open e depois o faça de novo, sem antes fechar a instância anterior.
#Sua síntaxe é:
#arquivo.close()
arquivo = open('arqText.txt', 'w')

arquivo.write('Curso Python \n')
arquivo.write('Aula Prática')
arquivo.close()

#leitura  do arquivo texto
leitura=open('arqText.txt', 'r')
print(leitura.read())
leitura.close()