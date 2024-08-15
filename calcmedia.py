def calcular_media_semestre(notas_semestre):
    # Calcula a média das notas de um semestre
    return sum(notas_semestre) / len(notas_semestre)

def calcular_media_geral(notas_semestre1, notas_semestre2, notas_semestre3):
    # Calcula a média geral a partir das médias dos três semestres
    media_semestre1 = calcular_media_semestre(notas_semestre1)
    media_semestre2 = calcular_media_semestre(notas_semestre2)
    media_semestre3 = calcular_media_semestre(notas_semestre3)
    
    media_geral = (media_semestre1 + media_semestre2 + media_semestre3) / 3
    return media_geral

# Exemplo de uso da função
notas_semestre1 = [float(input(f"Digite a nota da matéria {i+1} do primeiro semestre: ")) for i in range(6)]
notas_semestre2 = [float(input(f"Digite a nota da matéria {i+1} do segundo semestre: ")) for i in range(7)]
notas_semestre3 = [float(input(f"Digite a nota da matéria {i+1} do terceiro semestre: ")) for i in range(6)]

media_final = calcular_media_geral(notas_semestre1, notas_semestre2, notas_semestre3)
print(f"A média final do aluno é: {media_final:.2f}")
