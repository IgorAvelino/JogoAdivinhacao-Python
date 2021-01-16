from random import randint
import PySimpleGUI as sg

class JogoAdivinhacao():

    sg.theme('DarkGrey13')
    
    def __init__(self):
        self.tentar_denovo = True
        self.count = 1
    

    def iniciar(self):

        self.layout = [
            [sg.Text('================ JOGO DA ADIVINHAÇÃO!! ================')],
            [sg.Text('A máquina escolherá um número aleatório de acordo com a dificuldade\nDigite um valor para a dificuldade, e tente adivinhar o número escolhido...')],
            [sg.Text('Digite a Dificuldade: '), sg.Input(key='dificuldade')],
            [sg.Text('Digite seu Chute: '), sg.Input(key='chute')],
            [sg.Button('Chutar'), sg.Button('Sair')],
            [sg.Output(size=(50, 5))]
        ] 

        self.janela = sg.Window("JOGO DA ADIVINHAÇÃO", layout=self.layout)
        self.GerarNumAleatorio()

        while True:

            self.eventos, self.valores = self.janela.Read()
            if self.eventos == 'Sair':
                break

            if self.eventos == 'Chutar':
                self.chute = int(self.valores['chute'])

                while self.tentar_denovo == True:

                    if self.chute > self.num:
                        print('Muito Alto')
                        self.count += 1
                        break
                        
                    elif self.chute < self.num:
                        print('Muito Baixo')
                        self.count += 1
                        break

                    elif self.chute == self.num:
                        self.tentar_denovo = False
                        print()
                        print('PARABÉNS')
                        print('Você venceu!!!')
                        print(f'Número de Tentativas: {self.count}')

                        if self.count == 1:
                            print(' ========= NA PRIMEIRA TENTATIVA !!! =========')

                        break
    
    def GerarNumAleatorio(self):
        self.eventos, self.valores = self.janela.Read()
        self.dificuldade = self.valores['dificuldade']
        self.num = randint(1, int(self.dificuldade))
            

# PROGRAMA
adivinhacao = JogoAdivinhacao()
adivinhacao.iniciar()
