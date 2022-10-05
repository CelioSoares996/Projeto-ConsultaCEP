import PySimpleGUI as sg

def tela_inicial():
    sg.theme('Reddit')

    cep = [
        [sg.Text('Informe um CEP', font='Arial 12', pad=(0, 0))],
        [sg.Input(size=(20, 0), font='Arial 12', pad=(0, 0), key='cep')],
    ]

    coluna1 = [
        [sg.Text('LAGRADOURO:', font='Arial 12')],
        [sg.Text('BAIRRO:', font='Arial 12')],
        [sg.Text('LOCALIDADE:', font='Arila 12')],
        [sg.Text('UF:', font='Arial 12')],
        [sg.Text('IBGE:', font='Arial 12')],
        [sg.Text('DDD:')]
    ]

    coluna2 = [
        [sg.Input(font='Arial 12 bold', key='logradouro', size=(35, 1))],
        [sg.Input(font='Arial 12 bold', key='bairro', size=(35, 1))],
        [sg.Input(font='Arial 12 bold', key='localidade', size=(35, 1))],
        [sg.Input(font='Arial 12 bold', key='uf', size=(35, 1))],
        [sg.Input(font='Arial 12 bold', key='ibge', size=(35, 1))],
        [sg.Input(font='Arial 12 bold', key='ddd', size=(35, 1))]
    ]

    botoes = [
        [sg.Button('Consultar', font='Arial 12', size=(8, 1), pad=((0, 15), 0)),
         sg.CButton('Sair', font='Arial 12', size=(8, 1))]
    ]

    layout = [
        [sg.Text('ConsultaCEP', font='Arial 18 bold')],
        [sg.Column(cep, justification='center', element_justification='center')],
        [sg.Column(coluna1, pad=((0, 20), 0)),
        sg.Column(coluna2)],
        [sg.Column(botoes, justification='center')]
    ]

    janela_principal = sg.Window('ConsultaCEP', element_padding=(0, 10), layout=layout, size=(600, 500), finalize=True)
