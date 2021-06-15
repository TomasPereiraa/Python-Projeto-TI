#Import de bibliotecas
import cv2
import requests
import _thread
from time import strftime

#Criação de um objeto que permite captar a foto
cam = cv2.VideoCapture(0)
ret, image = cam.read()

#função para obter a data e hora
def datahora():
    return strftime("%d/%m/%Y %H:%M:%S")

#Função que permite enviar dados para API
def send_to_api(dados):
    #dados =  {'nome': 'webcam' ,'valor:valor,'hora': datahora()}
    r = requests.post("http://127.0.0.1/ti/api/api.php", data = dados)

    if r.status_code==200: #Código Status HTTP --> OK (Sucesso)
        print ("OK: POST realizado com sucesso")
        print (r.status_code)
    else:
        print ("ERRO: Não foi possível realizar o pedido")
        print (r.status_code)

#Função que envia a foto 
def send_file(files):
    url = 'http://127.0.0.1/ti/upload.php'
    
    r = requests.post(url, files=files)
    print(str(r.status_code) + " " + r.text)

#Código que permite a tiragem da foto
try:
    cv2.imwrite('webcam.jpg',image)

    #colocação de dados e da foto em arrays
    files = {'imagem': open('webcam.jpg', 'rb')}
    dados = {'nome': 'webcam','valor':" " ,'hora': datahora()}

    _thread.start_new_thread(send_file(files), send_to_api(dados)) #Criação de uma nova thread para chamar as funções 

    #Libertação da câmera e destruição das janelas
    cam.release()
    cv2.destroyAllWindows()
   
except:
    print("Ocorreu um erro")

finally:
    print("Fim do Programa")