import os
import requests
import colorama
from colorama import Fore, Style
import json
import re
import pyfiglet

def check():
    
    
    os.system("cls")
    font = pyfiglet.Figlet(font='slant')
    art = Fore.YELLOW+font.renderText('Insta Demon')+Fore.RESET #le quiero poner un nombre yy no se me ocurre nada xdd
    print(art)
    print(Fore.RED+Style.BRIGHT+"Code By @Criftcking"+Fore.RESET)
    user = input(Fore.YELLOW+'Escribe el usuario que deseas Buscar: '+Fore.RESET)
    url= 'https://www.pathsocial.com/wp-admin/admin-ajax.php'
    
    
    data = {
        'action': 'get_instagram_data_for_analyzer',
        'account_handle': user
    }
    

    
    headers = {
        
        "Host": "www.pathsocial.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://www.pathsocial.com",
        "Connection": "keep-alive",
        "Referer": "https://www.pathsocial.com/es/free-instagram-tools/instagram-profile-analyzer/",
        "TE": "trailers",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    }
    
    
    response = requests.post(url=url, data=data)
    texto = response.text
    if "Couldn't find profile data" in response.text:
        os.system("cls")
        font = pyfiglet.Figlet(font='slant')
        art = Fore.YELLOW+font.renderText('Insta Demon')+Fore.RESET #le quiero poner un nombre yy no se me ocurre nada xdd
        print(art)
        print(Fore.RED+"Code By @Criftcking"+Fore.RESET)
        print()
        print("Error: "+Fore.GREEN+Style.BRIGHT+"--Usuario No Encontrado--"+Fore.RESET)
        
        print()
        print(Fore.GREEN+"Desea Buscar otro Usuario?")
        print(Fore.RED+"[1]-Si\n[2]-No"+Fore.RESET)
        print(Fore.YELLOW+"")
        resp2 = int(input(("Escribe tu Opcion---> ")))
        print(""+Fore.RESET)
        
        if resp2 == 1:
            check()
        else:
            pass
        
        
        
        
        
    else:
        if response.status_code == 200:
            print("Info: "+Fore.GREEN+Style.BRIGHT+"Usuario Encontrado"+Fore.RESET)
        
    
            inicio = texto.find('"username":"') + 1
            fin = texto.find('",', inicio)
            valor = texto[inicio:fin]
            valore = valor[11:]
            print(Fore.YELLOW+"Username: "+Fore.RESET+valore)
            
            inicio1 = texto.find('followers":"') + 1
            fin1 = texto.find('",', inicio1)
            valor1 = texto[inicio1:fin1]
            valore1 = valor1[11:]
            print(Fore.YELLOW+"Seguidores: "+Fore.RESET+valore1)
            
            inicio2 = texto.find('total_posts":') + 1
            fin2 = texto.find(',"', inicio2)
            valor2 = texto[inicio2:fin2]
            valore2 = valor2[12:]
            print(Fore.YELLOW+"Publicaciones: "+Fore.RESET+valore2)
            
            inicio5 = texto.find('biography":"') + 1
            fin5 = texto.find('",', inicio5)
            valor5 = texto[inicio5:fin5]
            valore5 = valor5[12:]
            print(Fore.YELLOW+"Biografia: "+Fore.RESET+valore5.replace("u2022", "").replace(r"\u00b0", "").replace(r"\n", "\n").replace("\\", ""))
            ###########################################################################################
            print()
            print(Fore.GREEN+"---Random_Publicacion_Info---"+Fore.RESET)#+valore3.replace('{"image":', ']'))
            ###########################################################################################
            inicio3 = texto.find('comments":') + 1
            fin3 = texto.find(',"', inicio3)
            valor3 = texto[inicio3:fin3]
            valore3 = valor3[9:]
            print(Fore.YELLOW+"Comentarios: "+Fore.RESET+valore3)
            
            inicio6 = texto.find('likes":') + 1
            fin6 = texto.find(',"', inicio6)
            valor6 = texto[inicio6:fin6]
            valore6 = valor6[6:]
            print(Fore.YELLOW+"Likes: "+Fore.RESET+valore6)
            
            inicio7 = texto.find('hastags":') + 1
            fin7 = texto.find('}', inicio7)
            valor7 = texto[inicio7:fin7]
            valore7 = valor7[8:]
            print(Fore.YELLOW+"Hastags: "+Fore.RESET+valore7)
            
            inicio8 = texto.find('shortcode":"') + 1
            fin8 = texto.find('"}', inicio8)
            valor8 = texto[inicio8:fin8]
            if 'shortcode":"' in response.text:
                valore8 = valor8[11:]
                print(Fore.YELLOW+"Publicacion_URL: "+Fore.RESET+f"https://www.instagram.com/p/{valore8}/")
            else:
                pass
            
    
            
            
            
            
            print()
            print(Fore.GREEN+"Desea Buscar otro Usuario?")
            print(Fore.RED+"[1]-Si\n[2]-No\n[3]-Mostrar URL del Perfil"+Fore.RESET)
        
            
            print(Fore.YELLOW+"")
            resp = int(input(("Escribe tu Opcion---> ")))
            print(""+Fore.RESET)
            

            
            if resp == 1:
                check()
            elif resp == 2:
                pass
            elif resp == 3:
                print("INFO URL: "+Fore.BLUE+f"https://www.instagram.com/{valore}/"+Fore.RESET)
                print()
                input(Fore.YELLOW+"Presiona 'Enter' Para Reiniciar"+Fore.RESET)
            else:
                pass
            
            
        
        else:
            print("Usuario No Encontrado")

    





#AHORA VA LA INTERFAZ GRAFICA |||| 
os.system("cls")
font = pyfiglet.Figlet(font='slant')
art = Fore.YELLOW+font.renderText('Insta Demon')+Fore.RESET #le quiero poner un nombre yy no se me ocurre nada xdd
print(art)
print(Fore.RED+Style.BRIGHT+"Code By @Criftcking"+Fore.RESET)




print(Fore.YELLOW+"Elige una Opcion: "+Fore.RESET)
print(Fore.BLUE+"[1]-Iniciar\n[2]-Salir"+Fore.RESET)
print(Fore.YELLOW+"")
var = int(input(("Escribe tu Opcion---> ")))
print(""+Fore.RESET)


if var == 1:
    check()
    
elif var == 2:
    pass
else:
    pass









