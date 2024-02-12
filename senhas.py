import PySimpleGUI as sg
import random as rd
import string as st
import pyperclip

# Variável global para armazenar a senha gerada
senha_gerada = ''

# Função para gerar a senha com base nas escolhas do usuário
def gerar_senha(quantidade, incluir_numero, incluir_maiuscula, incluir_minuscula, incluir_simbolo):
    global senha_gerada
    caracters = ''

    if incluir_numero:
        caracters += st.digits
    if incluir_maiuscula:
        caracters += st.ascii_uppercase
    if incluir_minuscula:
        caracters += st.ascii_lowercase
    if incluir_simbolo:
        caracters += st.punctuation
    if not caracters:
        sg.popup_error('Selecione pelo menos um tipo de caracter para gerar sua senha.')
        return
    
    senha_gerada = ''.join(rd.choice(caracters) for _ in range(int(quantidade)))

# Fazer a interface
def tela_inicial():
    layout = [
        [sg.Text('Digite a quantidade numérica para o tamanho da sua senha')],
        [sg.Input(key='quantidade')],
        [sg.Text('Deseja Incluir números na sua senha?')],
        [sg.Radio('Sim', 'opcao_numero', key='sim_numero', default=False), sg.Radio('Não', 'opcao_numero', key='nao_numero')],
        [sg.Text('Deseje Incluir letras Maiúsculas')],
        [sg.Radio('Sim', 'opcao_maiuscula', key='maiuscula', default=False), sg.Radio('Não', 'opcao_maiuscula', key='nao_maiuscula')],
        [sg.Text('Deseje Incluir letras Minúsculas')],
        [sg.Radio('Sim', 'opcao_minuscula', key='minuscula', default=False), sg.Radio('Não', 'opcao_minuscula', key='nao_minuscula')],
        [sg.Text('Deseje Incluir letras Símbolos')],
        [sg.Radio('Sim', 'opcao_simbolo', key='simbolo', default=False), sg.Radio('Não', 'opcao_simbolo', key='nao_simbolo')],
        [sg.Button('Criar Senha')],
    ] 

    window = sg.Window('Gerador de Senhas', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Criar Senha':
            quantidade = values['quantidade']
            incluir_numero = values['sim_numero']
            incluir_maiuscula = values['maiuscula']
            incluir_minuscula = values['minuscula']
            incluir_simbolo = values['simbolo']

            gerar_senha(quantidade, incluir_numero, incluir_maiuscula, incluir_minuscula, incluir_simbolo)

            if senha_gerada:
                layout_copiar = [
                    [sg.Text('Senha Gerada:')],
                    [sg.Text(senha_gerada, key='senha_gerada')],
                    [sg.Button('Copiar Senha')]
                ]
                
                window_copiar = sg.Window('Copiar Senha', layout_copiar)

                while True:
                    event_copiar, values_copiar = window_copiar.read()

                    if event_copiar == sg.WIN_CLOSED:
                        break
                    elif event_copiar == 'Copiar Senha':
                        pyperclip.copy(senha_gerada)
                        sg.popup('Senha copiada para a área de transferência!', title='Cópia Concluída')
                        break

                window_copiar.close()

    window.close()

# Tela com senha gerada
tela_inicial()
