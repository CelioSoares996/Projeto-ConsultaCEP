from interface_grafica import *
from consulta_cep import *
tela_inicial()
while True:
    windown, event, volues = sg.read_all_windows()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Consultar':
        try:
            logradouro = consulta(volues['cep'])['logradouro']
            bairro = consulta(volues['cep'])['bairro']
            localidade = consulta(volues['cep'])['localidade']
            uf = consulta(volues['cep'])[ 'uf']
            ibge = consulta(volues['cep'])['ibge']
            ddd = consulta(volues['cep'])['ddd']

            windown['logradouro'].update(logradouro)
            windown['bairro'].update(bairro)
            windown['localidade'].update(localidade)
            windown['uf'].update(uf)
            windown['ibge'].update(ibge)
            windown['ddd'].update(ddd)

        except:
            sg.popup('Virifique se o campo CEP foi preenchido corretamente\n'
                     'ou se esta conectado a internet', font='Arial 12', title='ERRO')
