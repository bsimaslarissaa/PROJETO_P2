import time
import random
from colorama import init, Fore, Back, Style # antes de rodar o código, instale o colorama: pip install colorama
init(autoreset=True)

maximo_xp = 20
xp_atual = 0

personagem = {
    "Nome": None,
    "Nível": 1,
    "HP": 10,
    "ATK": 2,
    "XP": 0,
    "Classe": 'Guerreiro'  
}

def escrever_texto(texto, cor ='', velocidade = 0.04):
    for letra in texto:
        print(cor + letra, end='', flush=True)
        time.sleep(velocidade)

def descricao(texto, cor ='', velocidade = 0.05):
    for letra in texto:
        print(cor + letra, end='', flush=True)
        time.sleep(velocidade)


def mostrar_status():
    escrever_texto("\nStatus do Personagem:\n", Fore.YELLOW, 0.009)
    escrever_texto(f"Nome: {personagem['Nome']}\n", Fore.YELLOW, 0.009)
    escrever_texto(f"Nível: {personagem['Nível']}\n", Fore.YELLOW, 0.009)
    escrever_texto(f"HP: {personagem['HP']}\n", Fore.YELLOW, 0.009)
    escrever_texto(f"ATK: {personagem['ATK']}\n", Fore.YELLOW, 0.009)
    escrever_texto(f"XP: {personagem['XP']}\n", Fore.YELLOW, 0.009)
    escrever_texto(f"Classe: {personagem['Classe']}\n", Fore.YELLOW, 0.009)

def criacao_personagem():
    escrever_texto(r"""   
  _____                          _                    _         _____
 / ____|                        | |                  | |       |  __ \
| |       __ _   ___   __ _   __| |  ___   _ __    __| |  ___  | |__) |  ___   ___   ___   _ __ ___   _ __    ___  _ __   ___   __ _  ___
| |      / _` | / __| / _` | / _` | / _ \ | '__|  / _` | / _ \ |  _  /  / _ \ / __| / _ \ | '_ ` _ \ | '_ \  / _ \| '_ \ / __| / _` |/ __|
| |____ | (_| || (__ | (_| || (_| || (_) || |    | (_| ||  __/ | | \ \ |  __/| (__ | (_) || | | | | || |_) ||  __/| | | |\__ \| (_| |\__ \
 \_____| \__,_| \___| \__,_| \__,_| \___/ |_|     \__,_| \___| |_|  \_\ \___| \___| \___/ |_| |_| |_|| .__/  \___||_| |_||___/ \__,_||___/
                 //                                                                                  | |
                                                                                                     |_|
        
""", Fore.BLUE, 0.001)
    escrever_texto("\nDigite o nome do seu personagem: ", Fore.RED)
    personagem["Nome"] = input('')

    escrever_texto("\nSeu personagem foi criado com sucesso!\n", Fore.RED, 0.05)
    mostrar_status()

    escrever_texto('\nATENÇÃO:\n \n')
    escrever_texto('texto VERDE = NARRAÇÃO DA HISTÓRIA\n', Fore.GREEN, 0.05)
    escrever_texto('texto AZUL = DIÁLOGOS\n', Fore.BLUE, 0.05)
    escrever_texto('texto VERMELHO = INTERAÇÃO\n', Fore.RED, 0.05)

    escrever_texto("\nPrepare-se para a aventura!\n\n", Fore.RED, 0.05)
    time.sleep(0.3)

  

    escrever_texto("Deseja ver a introdução do seu personagem? \n", Fore.RED, 0.05)
    escrever_texto("Digite 1 para ver a introdução ou 0 para pular para o início do jogo.\nSua escolha: ", Fore.RED, 0.03)
    escolha = input("")

    if escolha == "1":
        escrever_texto("\n--- Introdução do personagem ---\n", Fore.RED, 0.05)
        escrever_texto("\n-Narração: Você é um caçador de recompensas que viaja em busca de moedas de ouro e de itens raros.", Fore.GREEN)
        escrever_texto("\nDe vila em vila, aceita qualquer contrato, desde caçar bandidos até lidar com criaturas das sombras, contanto que o pagamento seja justo.", Fore.GREEN)
        escrever_texto("\nSeu passado é um mistério, mas seu objetivo é claro: juntar ouro suficiente para desaparecer do mapa e nunca mais depender de ninguém.", Fore.GREEN)
        escrever_texto("\nCerto dia, você entrou em um bar no centro da cidade, onde ouviu uma história sobre um tesouro secreto capaz de mudar sua vida para sempre.\n", Fore.GREEN)

    else:
        escrever_texto("\nvocê pulou a introdução\n", Fore.RED)

def ganhar_xp(quantidade):
        global maximo_xp
        personagem["XP"] += quantidade
        while personagem["XP"] >= maximo_xp:
              personagem["XP"] -= maximo_xp
              personagem["Nível"] += 1
              personagem["HP"] += 7  # Aumenta HP ao subir de nível
              personagem["ATK"] += 3  # Aumenta ATK ao subir de nível
              maximo_xp = int(maximo_xp * 1.5)  # XP necessário aumenta por nível
              if personagem["XP"] >= maximo_xp:
                 escrever_texto(f"\n*** PARABÉNS! {personagem['Nome']} subiu para o Nível {personagem['Nível']}! ***\n", Fore.YELLOW, 0.009)
                 escrever_texto(f"Novo HP: {personagem['HP']}\nNovo ATK: {personagem['ATK']}\nXP para próximo nível: {maximo_xp}\n", Fore.YELLOW, 0.009)
                 escrever_texto(f"\nXP Atual: {personagem['XP']}/{maximo_xp}\n",Fore.YELLOW, 0.009)
              else:
                  mostrar_status()



def interacao_balconista():


    escrever_texto("\n-Narração: Você entra num bar no meio da cidade. Ele está vazio e é um lugar meio largado e sujo, mas você ignora e segue em direção ao balcão para pegar uma bebida. \n", Fore.GREEN, 0.05)

    escrever_texto("\nEnquanto você aproveita sua bebiba em paz, o balconista começa a falar com você...\n", Fore.GREEN, 0.05)

    escrever_texto("\n-Balconista João: Ei, você aí! Quer ouvir uma história emocionante?\n", Fore.BLUE, 0.05)

    time.sleep(0.2)

    escrever_texto("\nDigite 1 para ouvir ou 0 para ignorar e continuar em silêncio. \nsua escolha: ", Fore.RED, 0.05)

    escolha = input("")

    if escolha == '1':
        escrever_texto("\n-Balconista João: Há uma caverna ao sul desta cidade, onde dizem que um dragão habita.\n", Fore.BLUE, 0.05)
       
        escrever_texto("\n-Balconista João: Dizem também que há tesouros inimagináveis escondidos lá dentro, esperando para serem descobertos.", Fore.BLUE, 0.05)
        escrever_texto(" - ao ouvir sobre os supostos tesouros, você fica com vontade de ir explorar essa tal caverna\n", Fore.GREEN, 0.05)
       
        escrever_texto("\n-Balconista João: Só de te olhar já deu pra ver que você seria capaz de encarar essa aventura.\n", Fore.BLUE, 0.05)
        
    else:
        escrever_texto("\n-Balconista João: Mesmo que você não queira ouvir, vou te contar...", Fore.BLUE, 0.05)

        escrever_texto(" (você encara o balconista com cara séria, mas ele começa a contar a história, ignorando seu desinteresse)", Fore.GREEN, 0.05)

        escrever_texto(" há uma caverna ao sul desta cidade, onde dizem que habita um dragão\n", Fore.BLUE, 0.05)
        
        escrever_texto("\n-Balconista João: Dizem também que há tesouros inimagináveis escondidos lá dentro, esperando para serem descobertos.", Fore.BLUE, 0.05)

        escrever_texto("- ao ouvir sobre os tesouros, voce começa a se interessar pela história\n", Fore.GREEN, 0.05)

        escrever_texto("\n-Balconista João: Só de te olhar já deu pra ver que você seria capaz de encarar essa aventura.\n", Fore.BLUE, 0.05)
    escrever_texto("\n-Balconista: Então, o que você me diz, caçador de recompensas? Tem coragem de entrar essa caverna?\n", Fore.BLUE, 0.05)
    escrever_texto("\nDigite 1 para aceitar o desafio ou 0 para ignorar e sair do bar.\nsua escolha: ", Fore.RED, 0.05)
    escolha = input("")

    if escolha == "1":
        escrever_texto("\nVocê aceita o desafio e sai do bar determinado.\n", Fore.GREEN, 0.05)
    else:
        escrever_texto("\nVocê ignora o balconista e sai do bar.\n", Fore.GREEN, 0.05)

        escrever_texto("\nmas está determinado a seguir nessa aventura\n", Fore.GREEN, 0.05)
    
    escrever_texto("\n\nVocê decide que precisa de equipamentos melhores para essa aventura...\n", Fore.GREEN, 0.05)

def cena_loja():
    escrever_texto("\nVocê entra na loja de equipamentos 'Armas & Armaduras' e é imediatamente abordado pelo vendedor.\n", Fore.GREEN, 0.05)
    
    imagem_loja = r""" 
                   
                       |\                     /)
                     /\_\\__               (_//
                    |   `>\-`     _._       //`)
                     \ /` \\  _.-`:::`-._  //
                      `    \|`    :::    `|/
                            |     :::     |
                            |.....:::.....|
                            |:::::::::::::|
                            |     :::     |
                            \     :::     /
                             \    :::    /
                              `-. ::: .-'
                               //`:::`\\
                              //   '   \\                                
                             |/         \| 
                   """ 
    escrever_texto(imagem_loja)  

    escrever_texto("\n-Vendedor: Parabéns, sortudo! Você é o nosso quadragésimo cliente do dia e ganhou um item grátis!\n", Fore.BLUE, 0.05)
    
    escrever_texto("\nEscolha seu item:\n\n", Fore.GREEN, 0.05)

    escrever_texto("1. Espada de Ferro (+3 ATK)\n", Fore.GREEN, 0.05)

    escrever_texto("0. Malha de Ferro (+10 HP) \n", Fore.GREEN, 0.05)

    escrever_texto("Sua escolha: (digite 1 para escolher a Espada ou 0 para escolher a Malha:  " , Fore.RED, 0.02)

    escolha = input(" ")

    if escolha == "1":
        personagem["ATK"] += 3
        print("\nVocê escolheu a Espada de Ferro! Seu ATK aumentou para", personagem["ATK"])
    elif escolha == "0":
        personagem["HP"] += 10
        print("\nVocê escolheu a Malha de Ferro! Seu HP aumentou para", personagem["HP"])
    
    mostrar_status()
    
    
    escrever_texto("\nAgora equipado, você está pronto para aventurar-se na caverna!", Fore.GREEN, 0.05)
    
    escrever_texto("\nVocê segue em direção ao sul, onde a caverna do tesouro supostamente está localizada...", Fore.GREEN, 0.05)
    time.sleep(0.4)
    

    combate_inicial()

def combate_inicial():
        escrever_texto("\nApós sair da loja, você segue para a entrada da caverna...\n", Fore.GREEN, 0.05)
        escrever_texto("No caminho, um lobo faminto aparece e bloqueia sua passagem!\n", Fore.GREEN, 0.05)

        inimigo = { "Nome": "Lobo Selvagem",
                     "HP": 8,
                     "ATK": 2,
                }
        while inimigo["HP"] > 0 and personagem["HP"] > 0:
              escrever_texto(f"\n{inimigo['Nome']} - HP: {inimigo['HP']}\n", Fore.RED, 0.05)
              escrever_texto(f"{personagem['Nome']} - HP: {personagem['HP']}\n", Fore.YELLOW, 0.05)           
              escrever_texto("\nDigite 1 para atacar ou 0 para fugir: ", Fore.RED, 0.05)         
          
              acao = input("")

              if acao == "1":
           
                 dano = personagem["ATK"] + random.randint(0, 2)
                 inimigo["HP"] -= dano
                 escrever_texto(f"\nVocê atacou e causou {dano} de dano!\n", Fore.GREEN, 0.05)

                 if inimigo["HP"] > 0:
                
                    dano_inimigo = inimigo["ATK"] + random.randint(0, 1)
                    personagem["HP"] -= dano_inimigo
                    escrever_texto(f"O {inimigo['Nome']} atacou e causou {dano_inimigo} de dano!\n", Fore.RED, 0.05) 

                    if personagem["HP"] <= 0:
                        escrever_texto("\nVocê foi derrotado pelo lobo...\nFIM DE JOGO!\n", Fore.RED, 0.05)
                        exit()
                 elif  inimigo["HP"] <= 0:                                                                 
                        escrever_texto("\nVocê derrotou o lobo e continua sua jornada!\n", Fore.GREEN, 0.05)   
                        ganhar_xp (10)
                        escrever_texto("\nApós algumas horas de caminhada, você avista a entrada sombria da caverna.\n", Fore.GREEN, 0.05)
                        escrever_texto("\npressione enter para entrar na caverna...", Fore.RED, 0.05)
                        input(" ")
                        entrada_caverna()
              else: 
                     escrever_texto("\nVocê fugiu do combate!\n", Fore.GREEN, 0.05)
                     entrada_caverna()

def entrada_caverna():

    escrever_texto("\n=== ENTRADA DA CAVERNA ===", Fore.RED, 0.05)
    
    #imagem_caverna =

    escrever_texto("\nVocê adentra a caverna úmida e escura. O ar é pesado e você sente que não está sozinho...", Fore.GREEN, 0.05)
 
    escrever_texto("\nDe repente, um Dragão salta da escuridão para atacá-lo!\n", Fore.GREEN, 0.05)

    imagem_dragao = r"""
    
                        _)                   (_
                         _) \ /\%/\ /\_/\ / (_
                         _) \\(0 0) (0 0)// (_
                        )_ -- \(oo) (oo)/ -- _(
                         )_ / /\\__,__//\ \ _(
                            )_ / --;-- \ _(
                          *. ( ( )) (( ) ) .*
                         '...(____)zz(____)...'
                                  / \
                                    """ 

    escrever_texto(imagem_dragao)

    dragao = {"HP": 10, "ATK": 3}
    
    while personagem["HP"] > 0 and dragao["HP"] > 0:
        escrever_texto("\n1. Atacar\n", Fore.RED, 0.01)
        escrever_texto("\n2. Tentar fugir\n ", Fore.RED, 0.01)
        escrever_texto("\no que você faz?", Fore.RED, 0.01)
        escolha = input(" ")
        
        if escolha == "1":
            dano = random.randint(1, personagem["ATK"])
            dragao["HP"] -= dano
            escrever_texto(f"\nVocê ataca o Dragão causando {dano} de dano!\n", Fore.RED, 0.03)
            
            if dragao["HP"] > 0:
                personagem["HP"] -= dragao["ATK"]
                escrever_texto(f"\nO Dragão contra-ataca causando {dragao['ATK']} de dano!\n", Fore.RED, 0.03)
                escrever_texto(f"\nSeu HP: {personagem['HP']}\n", Fore.RED, 0.03)
        elif escolha == "2":
            escrever_texto("\nVocê tenta fugir, mas o Dragão bloqueia sua saída!\n", Fore.RED, 0.03)
        else:
            escrever_texto("\nOpção inválida! O Dragão aproveita para atacar!\n", Fore.RED, 0.03)
            personagem["HP"] -= dragao["ATK"]
    
    if personagem["HP"] > 0:
        escrever_texto("\nVocê venceu o Dragão! e o tesouro secreto é todo seu!\n", Fore.RED, 0.03)
        ganhar_xp(25)  # Exemplo: dragão dá 25 de XP
        conquista_do_tesouro()
    else:
        escrever_texto("\nVocê foi derrotado pelo Dragão... Fim do jogo.", Fore.GREEN, 0.03)
        exit()

def conquista_do_tesouro():
    
    escrever_texto("\nApós vencer o dragão que habitava a caverna, você caminha mais adentro do território desconhecido, procurando o tesouro que veio encontrar.", Fore.GREEN, 0.03)

    escrever_texto("\nAo chegar nas partes mais profundas da caverna, você encontra uma área cheia de baús com grande fortuna dentro.", Fore.GREEN, 0.03)

    escrever_texto("\nCom tudo isso, seu objetivo principal está mais próximo do que nunca!", Fore.GREEN, 0.03)

    escrever_texto("\nNo seu caminho de volta, você repara sons estranhos vindo dos arbustos e das árvores.", Fore.GREEN, 0.03)

    escrever_texto("\nQuando você para de caminhar, esperando as presença te observando mostrar sua face, um homem aparece em sua frente.", Fore.GREEN, 0.03)

    
    escrever_texto("\nBandido: Quem diria. Conseguiu notar minha prensença. Estou impressionado.", Fore.BLUE, 0.05)

    time.sleep(0.2)

    escrever_texto("\nDigite 1 para perguntar quem ele é ou 0 para continuar em silêncio. \nsua escolha: ", Fore.RED, 0.05)

    escolha = input("")

    if escolha == '1':
        escrever_texto("\n-Bandido: Bem, já que você pediu com tanta educação...\n", Fore.BLUE, 0.05)
       
        escrever_texto("\n-Bandido Isaac: Me chamo Isaac. Eu recebi informação de que alguém foi enfrentar o dragão de uma caverna próxima.", Fore.BLUE, 0.05)
        
        escrever_texto(" - Imagine a minha surpresa quando eu vi o corpo morto do dragão perto da entrada. Quem não usarua tal oportunidade para pegar o tesouro das mãos do vitorioso quando ferido?\n", Fore.BLUE, 0.05)
       
        escrever_texto("\n-Bandido Isaac: Desculpa, cara. Não é nada pessoal. Eu simplemsmente não posso deixar essa oportunidade passar.\n", Fore.BLUE, 0.05)

    else:
        escrever_texto("\n-Bandido Isaac: Não é uma pessoa de muitas palavras, né? Bom, por mim, tudo bem. Eu só preciso do dinheiro, afinal.", Fore.BLUE, 0.05)

    Isaac = {"HP": 7, "ATK": 2}

    while personagem["HP"] > 0 and Isaac["HP"] > 0:
        escrever_texto("\n1. Atacar\n", Fore.RED, 0.01)
        escrever_texto("\n2. Tentar fugir\n ", Fore.RED, 0.01)
        escrever_texto("\no que você faz?", Fore.RED, 0.01)
        escolha = input(" ")
        
        if escolha == "1":
            dano = random.randint(1, personagem["ATK"])
            Isaac["HP"] -= dano
            escrever_texto(f"\nVocê encontra uma abertura e ataca o bandido, causando {dano} de dano!\n", Fore.RED, 0.03)

            if Isaac["HP"] > 0:
                personagem["HP"] -= Isaac["ATK"]
                escrever_texto(f"\nIsaac contra-ataca, causando {Isaac['ATK']} de dano!\n", Fore.RED, 0.03)
                escrever_texto(f"\nSeu HP: {personagem['HP']}\n", Fore.RED, 0.03)
        elif escolha == "2":
            escrever_texto("\nVocê tenta fugir, mas Isaac tê impede de  recuar!\n", Fore.RED, 0.03)
            
            escrever_texto("\n-Bandido Isaac: Como se eu fosse deixar você fugir.", Fore.BLUE, 0.05)
        else:
            escrever_texto("\nOpção inválida! Isaac se aproveita da abertura para atacar!\n", Fore.RED, 0.03)
            personagem["HP"] -= Isaac["ATK"]
    
    if personagem["HP"] > 0:
        escrever_texto("\nVocê derrotou Isaac! O tesouro continua em sua posse!\n", Fore.RED, 0.03)
        ganhar_xp(15) 
        escrever_texto("\nVocê Chegou ao Final do Jogo! Parabéns! ") 
        exit()
    else:
        escrever_texto("\nVocê foi derrotado por Isaac, e teve seu tesouro roubado... Fim do jogo.", Fore.GREEN, 0.03)
        exit() 

# Iniciar o jogo
criacao_personagem()
interacao_balconista()
cena_loja()
