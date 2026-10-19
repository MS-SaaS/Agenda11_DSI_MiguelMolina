#Aqui no início, inicializei a biblioteca "Colorama" (Que serve para aplicar cores no texto do terminal) e defini usando o "init(autoreset=True)" que, sempre depois de uma linha colorida, o terminal volte para a cor padrão, assim eliminando a necessidade de resetar manualmente a cor após cada linha colorida.
from colorama import Fore, Style, init
init(autoreset=True)

#Aqui, tem a lista "niveis_agua" que contém todos os possíveis níveis de água do reservatório
niveis_agua = [
    "Nível 1 - Muito baixo (CRÍTICO)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (ALERTA)"
]
 
#Essa parte é uma pequena estrutura de repetição que percorre todos os níveis de água e, para cada nível, chama a função "definir_cor" para obter a cor correspondente.
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

#Essa parte final imprime os resultados baseados nos níveis de água, aplicando suas respectivas cores e finalizando reiniciando todas as cores usadas.
print("=== MONITORAMENTO DO RESERVATÓRIO ===\n")
for nivel in range(1, 6):
    cor = definir_cor(nivel)
    mensagem = niveis_agua[nivel - 1]
    print(cor + mensagem + Style.RESET_ALL)
