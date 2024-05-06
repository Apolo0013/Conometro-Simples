from tkinter import *
from time import sleep


segundos = 0
minutos = 0
horas = 0

def iniciar():
    global segundos , minutos , horas , despausar
    despausar = False

    # botãoes que irar fica disponivel ao apertar o botao de iniciar
    if botao_pausar['text'] != 'Pausar':
        botao_pausar['text'] = 'Pausar'

    if botao_reniciar['state'] != 'disabled':
        botao_reniciar['state'] = 'normal'

    botao_pausar['state'] = 'normal' # botao de pausar o conometro
    botao_reniciar['state'] = 'normal' # botao de reniciar o conometro
    botao_iniciar['state'] = 'disabled'# botao de iniciar o conometro
    conometro()


def conometro():
    global segundos , minutos , horas , despausar

    while True:
        segundos += 1 # adicionar um segundo no conometro

        # se horas, minutos e segundo for baixo de 9
        if segundos <= 9 and  minutos <= 9 and horas <= 9:
            times['text'] = f'0{horas}:0{minutos}:0{segundos}'
        
        # se segundos for maior do que 9 e o outros nao:
        elif segundos > 9 and minutos <= 9 and horas <= 9:
            times['text'] = f'0{horas}:0{minutos}:{segundos}'

        # se minutos e segundo for maior doque 9
        elif minutos > 9 and segundos > 9 and horas <= 9:
            times['text'] = f'0{horas}:{minutos}:{segundos}'

        elif minutos > 9 and segundos > 9 and horas > 9:
            times['text'] = f'{horas}:{minutos}:{segundos}'

        elif horas > 9 and minutos < 9 and segundos < 9:
            times['text'] = f'{horas}:0{minutos}:0{segundos}'

        if segundos == 59:
            segundos = 0
            minutos += 1

        if minutos == 59:
            minutos = 0
            horas += 1

        times.update()
        janela.after(1000) # esperar 1 segundo
        if despausar:
            break


def pausa():
    global despausar
    botao_pausar['state'] = 'disabled'
    botao_reniciar['state'] = 'disabledQ'
    botao_iniciar['state'] = 'normal'
    if despausar == False:
        botao_pausar['text'] = 'Pausado'
        despausar = True
        
    elif despausar == True:
        despausar = False


def reniciar():
    global horas, minutos , segundos
    horas = 0 
    minutos = 0
    segundos = 0



botaoc = '#16B980'
cor_text = '#FFFFFF'
fonte = 'Arial 10 bold'


janela = Tk()
janela.title('Conometro')
janela.geometry('450x230')
janela.config(bg='#084530')
janela.iconphoto(False , PhotoImage(file = 'relogio.png'))

janela.resizable(width = False , height = False )

# Conometro
times = Label(janela , width = 7 , height = 0 , text = '00:00:00',  font = 'Times 70 bold' , fg = '#A8A8A8' , bg = '#084530', relief = 'flat')
times.place(x = 27 , y = 30)

#Botao de Iniciar
botao_iniciar = Button(janela, width = 15 , height = 3 , text = 'iniciar' , font = fonte , bg = botaoc , fg = cor_text , relief = 'flat' , anchor = CENTER , command = iniciar , state = 'normal')
botao_iniciar.place(x = 20 , y = 160)

# Botao de Pausar
botao_pausar = Button(janela , width = 15 , height = 3 , text = 'Pausar' , font = fonte , bg = botaoc , fg = cor_text , relief = 'flat', anchor = CENTER , command = pausa , state = 'disabled')
botao_pausar.place(x = 160 , y = 160)

# Botao de reniciar
botao_reniciar = Button(janela, width = 15 , height = 3 , text = 'Reniciar' , font = fonte , bg = botaoc , fg = cor_text  , relief = 'flat' , state = 'disabled' , command =reniciar)
botao_reniciar.place(x = 300, y = 160)

janela.mainloop()
