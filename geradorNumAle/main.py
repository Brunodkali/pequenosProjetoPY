from random import randint;
import os;

numero_adivinhado = randint(1, 100);
numero_tentativas = 10;
seu_nome = input('Digite seu nome: ');
print(f'Ok! {seu_nome}, estou escolhendo um número de 1 até 100. Você consegue adivinhar?'); 

for tentativa in range(1, numero_tentativas +1):
    numero_escolhido = int(input('Escolha um número de 1 até 100: '));
    if numero_escolhido == numero_adivinhado:
        os.system('cls');
        print(f'Você acertou em {tentativa} tentativas!');
        break;
    elif numero_escolhido > numero_adivinhado:
        print('Escolha um número menor');
    else:
        print('Escolha um número maior');
print(f'O número era {numero_adivinhado}. Obrigado por jogar');