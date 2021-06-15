#Import de bibliotecas
import sys
import time
import requests
from playsound import playsound


try :
     print( "Prima CTRL+C para terminar")
     while True: # ciclo para o programa executar sem parar…
          r=requests.get('http://127.0.0.1/ti/api/api.php?nome=incendio') #Pedido GET para obter o valor do sensor de incendio
        
          if r.status_code==200: #sucesso no pedido
                valor_fogo=r.text
                print( "Estado de Incêndio: " + valor_fogo ) #Escrita do valor recebido
                if str(valor_fogo)== "Sensor Ativo":
                    print( "Estado de Incêndio: " + valor_fogo )
                    playsound("python/alarme.wav") #Comando que permite a reprodução do som de alarme
          else:
               print("O pedido HTTP não foi bem sucedido")
               
          time.sleep (2)

except KeyboardInterrupt: # caso haja interrupção de teclado CTRL+C
     print( "Programa terminado pelo utilizador")

except : # caso haja um erro qualquer
     print( "Ocorreu um erro:", sys.exc_info() )

finally : # executa sempre, independentemente se ocorreu exception
     print( "Fim do programa") 
