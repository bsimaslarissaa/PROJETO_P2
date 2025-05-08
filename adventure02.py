import time
import random

maximo_xp = 20
xp_atual = 0

personagem = {
    "Nome": None,
    "Nível": 1,
    "HP": 10,
    "ATK": 2,
    "XP": f"{xp_atual}/{maximo_xp}",
    "Classe": "Guerreiro"
}

def mostrar_status():
    print("\nStatus do Personagem:")
    print(f"Nome: {personagem['Nome']}")
    print(f"Nível: {personagem['Nível']}")
    print(f"HP: {personagem['HP']}")
    print(f"ATK: {personagem['ATK']}")
    print(f"XP: {personagem['XP']}")
    print(f"Classe: {personagem['Classe']}\n")

def criacao_personagem():
    print("Bem-vindo ao Text Adventure\n")
    personagem["Nome"] = input("Digite o nome do seu personagem: ")

    print("\nSeu personagem foi criado com sucesso!\n")
    mostrar_status()
    print("\nPrepare-se para a aventura!\n")

    descricao = [
        "\nVocê é um caçador de recompensas que viaja em busca de moedas de ouro e de itens raros.",
        "\nDe vila em vila, aceita qualquer contrato, desde caçar bandidos até lidar com criaturas das sombras, contanto que o pagamento seja justo.",
        "\nSeu passado é um mistério, mas seu objetivo é claro: juntar ouro suficiente para desaparecer do mapa e nunca mais depender de ninguém.",
        "\nCerto dia, você entrou em um bar no centro da cidade, onde ouviu uma história sobre um tesouro secreto capaz de mudar sua vida para sempre."
    ]

    print("Deseja ver a introdução do seu personagem?")
    print("Digite 1 para ver a introdução ou 0 para pular para o início do jogo.")
    escolha = input("Sua escolha: ")

    if escolha == '1':
        print("\n--- Introdução do personagem ---")
        for frase in descricao:
            print(frase)
            time.sleep(2)
    else:
        print("\nVocê pulou a introdução do personagem.")

def interacao_balconista():
    print("\nVocê entra num bar no meio da cidade. Ele está vazio e é um ambiente meio largado e sujo, mas você ignora e segue em direção ao balcão para pegar uma bebida. \n")
    input("\nAperte Enter para avançar o diálogo... \n")
    print("\nEnquanto você aproveita sua bebiba em paz, o balconista começa a falar com você...\n")
    time.sleep(3)
    print("\n-Balconista João: Ei, você aí! Quer ouvir uma história emocionante?")
    time.sleep(3)
    print("\nDigite 1 para ouvir ou 0 para ignorar e continuar em silêncio.")
    time.sleep(3)
    escolha = input("Sua escolha: ")

    if escolha == '1':
        print("\n-Balconista João: Há uma caverna ao sul desta cidade, onde dizem que um demônio habita.")
        time.sleep(3)
        print("\n-Balconista João: Dizem também que há tesouros inimagináveis escondidos lá dentro, esperando para serem descobertos. - ao ouvir sobre os supostos tesouros, você fica com vontade de ir explorar essa tal caverna\n")
        time.sleep(6)
        print("\n-Balconista João: vejo que você tem bons equipamentos. certamente seria capaz de encarar essa aventura.\n")
        time.sleep(3)
    else:
        print("\n-Balconista João: Mesmo que você não queira ouvir, vou te contar...(você encara o balconista João com cara séria, mas ele começa a contar a história, ignorando seu desinteresse) - há uma caverna ao sul desta cidade, onde dizem que habita um demonio\n")
        time.sleep(9)
        print("\n-Balconista João: Dizem também que há tesouros inimagináveis escondidos lá dentro, esperando para serem descobertos. - ao ouvir sobre os tesouros, voce começa a se interessar pela história\n")
        time.sleep(6)
        print("\n-Balconista João: vejo que você tem bons equipamentos. certamente seria capaz de encarar essa aventura.\n")
        time.sleep(5)
    print("\n-Balconista: Então, o que você me diz? Tem coragem de ir explorar essa caverna?")
    print("Digite 1 para aceitar o desafio ou 0 para ignorar e sair do bar.")
    escolha = input("Sua escolha: ")

    if escolha == "1":
        print("\nVocê aceita o desafio e sai do bar determinado.")
    else:
        print("\nVocê ignora o balconista e sai do bar.")
    
    print("\nVocê decide que precisa de equipamentos melhores para essa aventura...")

def cena_loja():
    print("\nVocê entra na loja de equipamentos 'Armas & Armaduras'.")
    time.sleep(2)
    print("\nVendedor: Parabéns, sortudo! Você é o nosso quadragésimo cliente do dia e ganhou um item grátis!")
    time.sleep(2)
    print("\nEscolha seu presente:")
    print("1. Espada de Ferro (+3 ATK)")
    print("0. Malha de Ferro (+10 HP)")
    escolha = input("Sua escolha (digite 1 para escolher a Espada ou 0 para escolher a Malha) : \n ")

    if escolha == "1":
        personagem["ATK"] += 3
        print("\nVocê escolheu a Espada de Ferro! Seu ATK aumentou para", personagem["ATK"])
    elif escolha == "0":
        personagem["HP"] += 10
        print("\nVocê escolheu a Malha de Ferro! Seu HP aumentou para", personagem["HP"])
    
    mostrar_status()
    
    # Nova parte adicionada para continuar o jogo
    print("\nAgora equipado, você está pronto para aventurar-se na caverna!")
    time.sleep(2)
    print("\nVocê segue em direção ao sul, onde a caverna do tesouro supostamente está localizada...")
    time.sleep(3)
    print("\nApós algumas horas de caminhada, você avista a entrada sombria da caverna.")
    input("\nPressione Enter para entrar na caverna...")
    
    # Próxima cena do jogo entrando na caverna 
    entrada_caverna()

def entrada_caverna():
    print("\n=== ENTRADA DA CAVERNA ===")
    print("\nVocê adentra a caverna úmida e escura. O ar é pesado e você sente que não está sozinho...")
    time.sleep(3)
    print("\nDe repente, um Dragão salta da escuridão para atacá-lo!")
    time.sleep(2)
    
    # Batalha com o Dragrao
    dragao = {"HP": 10, "ATK": 3}
    
    while personagem["HP"] > 0 and dragao["HP"] > 0:
        print("\n1. Atacar")
        print("2. Tentar fugir")
        escolha = input("O que você faz? ")
        
        if escolha == "1":
            dano = random.randint(1, personagem["ATK"])
            dragao["HP"] -= dano
            print(f"\nVocê ataca o Dragão causando {dano} de dano!")
            
            if dragao["HP"] > 0:
                personagem["HP"] -= dragao["ATK"]
                print(f"O Dragão contra-ataca causando {dragao['ATK']} de dano!")
                print(f"Seu HP: {personagem['HP']}")
        elif escolha == "2":
            print("\nVocê tenta fugir, mas o Dragão bloqueia sua saída!")
        else:
            print("\nOpção inválida! O Dragão aproveita para atacar!")
            personagem["HP"] -= dragao["ATK"]
    
    if personagem["HP"] > 0:
        print("\nVocê derrotou o Dragão! E o tesouro secreto é todo seu!")
        
    else:
        print("\nVocê foi derrotado pelo Dragão... Fim do jogo.")
        exit()

# Iniciar o jogo
criacao_personagem()
interacao_balconista()
cena_loja()
