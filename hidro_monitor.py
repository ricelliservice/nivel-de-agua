from random import randint
from time import sleep
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

# Lista de dicionários com os dados do reservatório
NIVEIS_RESERVATORIO = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)", "cor": Fore.RED},
    {"nivel": 2, "situacao": "Baixo", "cor": Fore.YELLOW},
    {"nivel": 3, "situacao": "Médio", "cor": Fore.GREEN},
    {"nivel": 4, "situacao": "Alto", "cor": Fore.CYAN},
    {"nivel": 5, "situacao": "Muito alto (alerta)", "cor": Fore.BLUE},
]


def exibir_cabecalho():
    """Exibe o título do programa dentro de uma caixa azul no terminal."""
    cor_caixa = Fore.BLUE
    print(
        f"{cor_caixa}┌──────────────────────────────────────────────────┐{Style.RESET_ALL}"
    )
    print(
        f"{cor_caixa}│         SISTEMA DE MONITORAMENTO HÍDRICO         │{Style.RESET_ALL}"
    )
    print(
        f"{cor_caixa}│               -- Hidro Monitor --                │{Style.RESET_ALL}"
    )
    print(
        f"{cor_caixa}└──────────────────────────────────────────────────┘{Style.RESET_ALL}\n"
    )


def animar_leitura():
    """Simula o processo de leitura do nível com uma animação de setas."""
    print("Lendo Nível do reservatório", end="", flush=True)
    for _ in range(6):
        sleep(0.3)
        print(" >", end="", flush=True)
    print("\n")


def obter_cor_e_situacao(nivel_informado):
    """Retorna o dicionário de dados correspondente ao nível informado."""
    for item in NIVEIS_RESERVATORIO:
        if item["nivel"] == nivel_informado:
            return item
    return None


def monitorar_reservatorio():
    """Executa a simulação completa de leitura e exibição do nível."""
    # Sorteia o nível do reservatório entre 1 e 5
    nivel_atual = randint(1, 5)

    # Executa a animação de leitura
    animar_leitura()

    # Pausa de 1.5 segundos antes de exibir o resultado final
    sleep(1.5)

    # Busca a cor e a situação correspondentes
    dados = obter_cor_e_situacao(nivel_atual)

    if dados:
        cor_caixa_resposta = Fore.MAGENTA
        # Formata o texto do resultado com cor própria do nível e efeito de negrito (Style.BRIGHT)
        texto_resultado = f"Nível {dados['nivel']}: {dados['situacao']}"
        conteudo_formatado = (
            f"{Style.BRIGHT}{dados['cor']}{texto_resultado:<48}{Style.RESET_ALL}"
        )

        print(
            f"{cor_caixa_resposta}┌──────────────────────────────────────────────────┐{Style.RESET_ALL}"
        )
        print(
            f"{cor_caixa_resposta}│{Style.RESET_ALL} {conteudo_formatado} {cor_caixa_resposta}│{Style.RESET_ALL}"
        )
        print(
            f"{cor_caixa_resposta}└──────────────────────────────────────────────────┘{Style.RESET_ALL}\n"
        )


# === FLUXO PRINCIPAL DO PROGRAMA ===
exibir_cabecalho()

# Pergunta inicial para dar a largada no sistema
while True:
    inicio = input("Deseja iniciar o monitoramento? (S/N): ").strip().upper()
    print()

    if inicio == "S":
        monitorar_reservatorio()

        # Segundo laço responsável pelas repetições subsequentes
        while True:
            repetir = (
                input("Deseja fazer a leitura novamente? (S/N): ")
                .strip() #Remove espaços em branco no início e no final da string
                .upper() #Converte a string para maiúsculas
            )
            print()

            if repetir == "S":
                monitorar_reservatorio()
            elif repetir == "N":
                print(
                    f"{Fore.GREEN}Encerrando o sistema de monitoramento...{Style.RESET_ALL}"
                )
                sleep(1)  # Pausa de 1 segundo entre as mensagens
                print(f"{Fore.GREEN}Até logo!{Style.RESET_ALL}")
                break
            else:
                print(
                    f"{Fore.RED}Opção inválida! Por favor, digite 'S' para Sim ou 'N' para Não.{Style.RESET_ALL}\n"
                )

        # Encerra o laço principal após a saída do laço de repetição
        break

    elif inicio == "N":
        print(
            f"{Fore.GREEN}Sistema finalizado sem executar medições.{Style.RESET_ALL}"
        )
        sleep(1)  # Pausa de 1 segundo entre as mensagens
        print(f"{Fore.GREEN}Até logo!{Style.RESET_ALL}")
        break
    else:
        print(
            f"{Fore.RED}Opção inválida! Por favor, digite 'S' para Sim ou 'N' para Não.{Style.RESET_ALL}\n"
        )