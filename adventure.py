import time

maximo_xp = 10  # máximo de XP para subir de nível
xp_atual = 0  # XP atual do personagem

personagem = {
    "Nome": None,
    "Nível": 1,
    "HP": 10,
    "ATK": 2,
    "XP": f"{xp_atual}/{maximo_xp}",
    "Classe": "Guerreiro"
}

def criacao_personagem():
    print("Bem-vindo ao Text Adventure\n")
    personagem["Nome"] = input("Digite o nome do seu personagem: ")

    print("\nSeu personagem foi criado com sucesso!\n")
    print("Dados do Personagem:")
    print(f"Nome: {personagem['Nome']}")
    print(f"Nível: {personagem['Nível']}")
    print(f"HP: {personagem['HP']}")
    print(f"ATK: {personagem['ATK']}")
    print(f"XP: {personagem['XP']}")
    print(f"Classe: {personagem['Classe']}")
    print("\nPrepare-se para a aventura!\n")

    descricao = [
        "\nVocê é um caçador de recompensas que viaja em busca de moedas de ouro e de itens raros.",
        "\nDe vila em vila, aceita qualquer contrato, desde caçar bandidos até lidar com criaturas das sombras, contanto que o pagamento seja justo.",
        "\nSeu passado é um mistério, mas seu objetivo é claro: juntar ouro suficiente para desaparecer do mapa e nunca mais depender de ninguém.\n",
        "\n Certo dia, você entrou em um bar no centro da cidade, onde ouviu uma história sobre um tesouro secreto capaz de mudar sua vida para sempre. a história era mais ou menos assim:\n"
    ]

    print("Deseja ver a introdução do seu personagem?")
    print("Digite 1 para ver a introdução ou 0 para pular para o início do jogo.")
    escolha = input("Sua escolha: ")

    if escolha == '1':
        print("\n--- Introdução do personagem ---")
        for frase in descricao:
            print(frase)
            time.sleep(4.5)  # aguardar 2 segundos antes da próxima frase
    else:
        print("\nVocê pulou a introdução do personagem.")


def interacao_balconista():
    print("\nvocê entra num bar no meio da cidade. ele está vazio, e é também um ambiente meio largado e está muito sujo, mas você ignora isso e apenas segue em direção ao balcão para pedir uma bebida \n")
    time.sleep(6)
    print("\nenquanto você aproveita sua bebiba em paz, o balconista começa a falar com você...\n")
    time.sleep(3)
    print("\n-Balconista João: Ei, você aí! quer ouvir uma historia emocionante?\n")
    print("\ndigite 1 para ouvir ou 0 para ignorar e continuar em silencio.\n")
    escolha = input("sua escolha: ")

    if escolha == '1':
        print("\n-Balconista João: Então, ouça bem. há uma caverna ao sul desta cidade, onde dizem que um demônio habita\n")
        time.sleep(3)
        print("\n-Balconista João: Dizem também que há tesouros inimagináveis escondidos lá dentro, esperando para serem descobertos. - ao ouvir sobre os supostos tesouros, você fica com vontade de ir explorar essa tal caverna\n")
        time.sleep(3)
        print("\n-Balconista João: vejo que você tem bons equipamentos. certamente seria capaz de encarar essa aventura.\n")

    else:
        print("\n-Balconista João: Mesmo que você não queira ouvir, vou te contar. (você encara o balconista João com cara séria, mas ele começa a contar a história, ignorando seu desinteresse) - há uma caverna ao sul desta cidade, onde dizem que habita um demonio\n")
        time.sleep(9)
        print("\n-Balconista João: Dizem também que há tesouros inimagináveis escondidos lá dentro, esperando para serem descobertos. - ao ouvir sobre os tesouros, voce começa a se interessar pela história\n")
        time.sleep(3)
        print("\n-Balconista João: vejo que você tem bons equipamentos. certamente seria capaz de encarar essa aventura.\n")
    
    print("\n-Balconista: então, o que você me diz? tem coragem de ir explorar essa tal caverna\n")
    print("digite 1 para aceitar o desafio do balconista ou 0 para ignorar e se retirar do bar")

    escolha = input("sua escolha: ")

    if escolha == "1":
        print("você diz ao balconista que irá até essa caverna e pegará o tal tesouro. - em seguida, você se retira do bar.")

    elif escolha == "0":
        print("você apenas se levanta e sai do bar em silêncio")


criacao_personagem()
interacao_balconista()

#### TESTE LARISSA


