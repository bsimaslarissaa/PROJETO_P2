# PROJETO_P2
## **Jogo de Text Adventure em Python**

**Alunos: Larissa Barbosa Simas - Matrícula: 202512476, Jhean Monteiro da Silva - Matrícula: 202512499, Cintia Mendes Bernardo - Matrícula:202512564 e Lorenzo Sampaio de Guadelupe - Matrícula - 202512519**

## Título: Caçador de Recompensas.

Você é um caçador de recompensas que viaja em busca de moedas e itens raros.
De vila em vila, aceita qualquer contrato, desde caçar bandidos até lidar com criaturas das sombras, contanto que o pagamento seja justo. Seu passado é um mistério, mas seu objetivo é claro: juntar ouro suficiente para desaparecer do mapa e nunca mais depender de ninguém.

Certo dia, você entrou em um bar no centro da cidade, onde ouviu uma história sobre um tesouro secreto capaz de mudar sua vida para sempre. a história era mais ou menos assim...

## Instruções detalhadas de instalação, incluindo requisitos e dependências:

O código não usa bancos de dados ou arquivos externos (todos os dados são armazenados em variáveis/dicionários).

Não há conexão com APIs ou redes.

Para executar o código, basta instalar o colorama (pip install colorama) e rodar em qualquer interpretador Python.

## Ferramentas e bibliotecas utilizadas: 
Time - Biblioteca padrão do Python usada para pausar a execução com time.sleep().

Random - Biblioteca padrão do Python usada para gerar números aleatórios (como em combates).

Colorama - Biblioteca externa usada para adicionar cores ao texto no terminal (instalada via pip install colorama).

Principais componentes usados:

Fore (para cores do texto)

Back (para cores de fundo)

Style (para estilos como negrito)

init(autoreset=True) (para redefinir automaticamente as cores após cada impressão).

Dicionários - Para armazenar os atributos do personagem (personagem), inimigos (inimigo, dragao, Isaac), etc.

Funções personalizadas - Como escrever_texto() e descricao() para imprimir texto com efeito de digitação.

Estruturas de controle - Loops (while) para combate e condicionais (if/else) para escolhas do jogador.

Input do usuário - Captura de escolhas via input().

## Descrição das principais funcionalidades implementadas: 

Sistema de XP e level-up - Implementado em ganhar_xp().

Combate por turnos - Lógica de ataque/fuga com dano aleatório.

Narrativa interativa - Escolhas que afetam o fluxo da história.

