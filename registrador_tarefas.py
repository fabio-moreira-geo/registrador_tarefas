import PySimpleGUI as sg
import database_interface
import generate_csv
import contact_information_window
import create_database
import os.path
# Criando Layout


def criar_janela_inicial():
    sg.theme('DarkBrown4')
    linha = [
        [sg.Text('Seu nome:'), sg.Input('', size=10, key='-NAME-')],
        [sg.CalendarButton('Data', format="%d-%m"),
         sg.Input('', size=10, key='-DATE-')],
        [sg.Text('Tarefas:'),sg.Input(
            '', tooltip='O que você fez hoje?', key='-TASK-')]
    ]
    layout = [
        [sg.Frame('Tarefas', layout=linha, key='container')],
        [sg.Button('Resetar'), sg.Button(
            'Salvar'), sg.Button('Tabela'), sg.Button('CSV'), sg.Button('Sair')]
    ]
    return sg.Window('Registro de Atividades', layout=layout, finalize=True)
# Criar a janela


janela = criar_janela_inicial()

# Criar as regras dessa janela
while True:
    event, values = janela.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Salvar':
        database_interface.insert_contact(
            values['-NAME-'], values['-DATE-'], values['-TASK-'])
        sg.popup("Contact Information submitted!")
    elif event == 'CSV':
        generate_csv.create()
    elif event == 'Tabela':
        contact_information_window.create()
    elif event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()
    elif event == 'Sair':
        janela.close()
        