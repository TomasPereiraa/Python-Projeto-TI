#Import de bibliotecas
import sys
from time import strftime, gmtime
from msvcrt import kbhit, getch
import requests

#Função para obter data e hora
def datahora():
    return strftime("%d/%m/%Y %H:%M:%S")

#Função que permite enviar dados para a API
def send_to_api(dados):
    #dados =  {'nome': 'porta' , 'valor': valor_atuador, 'hora': datahora()}
    r = requests.post("http://127.0.0.1/ti/api/api.php", data = dados)

    if r.status_code==200: #Código Status HTTP --> OK (sucesso)
        print ("OK: POST realizado com sucesso")
        print (r.status_code)
    else:
        print ("ERRO: Não foi possível realizar o pedido")
        print (r.status_code)


try:
    #Legenda das opções
    print("Usage:\n[0]Fecha a porta\n[1]Abre a porta\n[CTRL+C]Terminar")
    while True:
        if kbhit():
            tecla = getch()[0]
            if tecla == 48: #48 é o ascii de 0
                dados = {'nome': 'porta' , 'valor': "Fechada", 'hora': datahora()}
                send_to_api(dados)
                print ( "\nPorta foi fechada" )
            elif tecla == 49: #49 é o ascii de 1
                dados = {'nome': 'porta' , 'valor': "Aberta", 'hora': datahora()}
                send_to_api(dados)
                print ( "\nPorta foi aberta" )
            else:
                print( "\nOpção inválida" + tecla)

except KeyboardInterrupt: # caso haja interrupção de teclado CTRL+C
     print( "Programa terminado pelo utilizador")

except : # caso haja um erro qualquer
     print( "Ocorreu um erro:", sys.exc_info() )

finally : # executa sempre, independentemente se ocorreu exception
     print( "Fim do programa") 