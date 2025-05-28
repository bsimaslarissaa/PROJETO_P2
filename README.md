# PROJETO_P2
## Jogo de Text Adventure em Python 🎮 

## Alunos: 👩‍🎓👨‍🎓👩‍🎓👨‍🎓

Larissa Barbosa Simas - Matrícula: 202512476

Jhean Monteiro da Silva - Matrícula: 202512499

Cintia Mendes Bernardo - Matrícula: 202512564

Lorenzo Sampaio de Guadelupe - Matrícula: 202512519

## Professor: 👨‍🏫❤️

João Batista Coelho Junior

## Título: Caçador de Recompensas.

Você é um caçador de recompensas que viaja em busca de moedas e itens raros.
De vila em vila, aceita qualquer contrato, desde caçar bandidos até lidar com criaturas das sombras, contanto que o pagamento seja justo. Seu passado é um mistério, mas seu objetivo é claro: juntar ouro suficiente para desaparecer do mapa e nunca mais depender de ninguém.

Certo dia, você entrou em um bar no centro da cidade, onde ouviu uma história sobre um tesouro secreto capaz de mudar sua vida para sempre. a história era mais ou menos assim...

## 📜 Manual de como jogar, incluindo comandos disponíveis:

🎮 COMO JOGAR:

Você controla um caçador de recompensas em busca de tesouros e fama.

Tome decisões digitando "1" ou "0" quando solicitado.

Em combates, escolha entre atacar (1) ou fugir (0).

Ganhe XP derrotando inimigos para subir de nível e ficar mais forte.

🎮 Comandos principais:

📜 Menu de interação:

1 = Aceitar / Confirmar / Atacar

0 = Recusar / Fugir / Ignorar

⚔️ Combate:

1 = Atacar (causa dano ao inimigo)

0 = Tentar fugir (nem sempre funciona)

📊 Status do personagem: 

HP (Vida): Se chegar a 0, você morre e o jogo acaba.

ATK (Ataque): Define o dano que você causa.

XP (Experiência): Acumule para subir de nível.

Nível: Quanto maior, mais forte você fica.

🌟 Dicas: 

✅ Escolha equipamentos sabiamente (Espada aumenta ATK, Armadura aumenta HP).

✅ Cuidado com inimigos – mesmo os mais fracos podem ser perigosos.

✅ Subir de nível aumenta seu HP máximo e ATK.

✅ Sempre verifique seu status antes de combates difíceis.

🎯 Objetivo: 

Derrote o Dragão da Caverna e encontre o tesouro escondido.

Sobreviva aos perigos e complete sua missão!

Boa sorte, caçador! 🏆⚔️

## 📜 Instruções detalhadas de instalação, incluindo requisitos e dependências: 

O código não usa bancos de dados ou arquivos externos (todos os dados são armazenados em variáveis/dicionários).

Não há conexão com APIs ou redes.

Para executar o código, basta instalar o colorama (pip install colorama) e rodar em qualquer interpretador Python.

## 📜 Ferramentas e bibliotecas utilizadas: 
Time - Biblioteca padrão do Python usada para pausar a execução com time.sleep().

Random - Biblioteca padrão do Python usada para gerar números aleatórios (como em combates).

Colorama - Biblioteca externa usada para adicionar cores ao texto no terminal (instalada via pip install colorama).

Principais componentes usados:

Fore (para cores do texto)

Back (para cores de fundo)

Style (para estilos como negrito)

init(autoreset=True) (para redefinir automaticamente as cores após cada impressão).

Dicionários - Para armazenar os atributos do personagem (personagem), inimigos (dragao/Isaac), etc.

Funções personalizadas - Como escrever_texto() e descricao() para imprimir texto com efeito de digitação.

Estruturas de controle - Loops (while) para combate e condicionais (if/else) para escolhas do jogador.

Input do usuário - Captura de escolhas via input().

## 📜 Descrição das principais funcionalidades implementadas: 
Sistema de XP e level-up - Implementado em ganhar_xp().

Combate por turnos - Lógica de ataque/fuga com dano aleatório.

Narrativa interativa - Escolhas que afetam o fluxo da história.


## 📜 Divisão de tarefas entre os membros do grupo:

Todos os membros contribuiram de forma positiva com o trabalho. 

Larissa Barbosa:

 1. Contribuiu com a criação do repositório do GitHub e compartilhamento entre os colegas e o professor. 

 2. Realizou também as ediçoes no arquivo README.md com as instruções e informações sobre o jogo.

 3. Em relação ao código, acrescentou a parte da ''Caverna e Combate com o Dragão'' .

Jhean Monteiro:

1. Criou a introdução do personagem.
   
2. Realizou a primeira versão do código, atribuindo status ao personagem e adicionado a cena do bar.
   
3. Adicionou a cena da loja.
   
4. Colocou cores nos textos pra diferenciar as falas.
   
4. Inseriu ASCII arts ( com participação, da Cintia ).

Lorenzo: 

1. Contribiu no código adicionando o combate contra o bandido.

Cintia Mendes: 

1. Contribiu com o combate contra o lobo.

2. Inseriu ASCII arts ( com participação, do Jhean ).


## 📜 Screenshots do jogo em funcionamento (com explicações):

1. Tela de criação do personagem:
 
O jogo pede o nome do personagem.

Mostra status iniciais (HP: 10, ATK: 2, Nível: 1).

Oferece opção de ver a introdução ou pular.
   
   ![personagem](https://github.com/user-attachments/assets/7b2e670d-6041-4bab-bd55-2de77a724901)


2. Cena do Bar:
   
Balconista João conta sobre a caverna do tesouro.

Opções:

1 para ouvir a história.

0 para ignorar (mas a história é contada de qualquer forma).
   
![bar](https://github.com/user-attachments/assets/8e14b4f2-823c-4b7c-adf6-cb5d8643162c)

3. Loja de Equipamentos:
    
Escolha:

Espada de Ferro (+3 ATK) ou Malha de Ferro (+10 HP).

Efeito:

Atualiza os status do personagem.

![loja](https://github.com/user-attachments/assets/8caa2aa1-afce-4b7e-a457-ae9214847541)



