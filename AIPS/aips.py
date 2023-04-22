#Segmento de codigo para mostrar caracter por caracter
from time import sleep
import sys
from os import system

#Funcion de texto
def txt_hs(text):
	for c in text:
		print (c, end='')
		sys.stdout.flush()
		sleep(0.1)
		
		
#Funcion COMANDOS DEL SISTEMA (syscmd)
def syscmd():
	while True:
		sys = input ("syscmd> ")
		
		if (sys == "syscmd -e"):
			break
		else:
			system(sys)
		

text = ("FUNCION DE TEXTO IMPLEMENTADA\n")
txt_hs(text)

text = ("Cargando time  \n")
txt_hs(text)
	
text = ("Importando Sleep de Time  \n")
txt_hs(text)
	
#Importando colorama para usar color en el texto
from colorama import Fore, Back, Style, init

	
text = ("Cargando colorama  \n")
txt_hs(text)

text = ("Importando Fore, Back, Style, init  \n")
txt_hs(text)

text = ("Comprobando colores\n\n")
txt_hs(text)
	
print (Fore.GREEN + "COLOR VERDE")
print (Fore.RED + "COLOR ROJO")
print (Fore.YELLOW + "COLOR AMARILLO")
print (Fore.BLUE + "COLOR AZUL")
print (Fore.MAGENTA + "COLOR MAGENTA")			
print (Fore.CYAN + "COLOR CYAN")
print (Fore.WHITE + "COLOR WHITE")

text = (Style.BRIGHT + Fore.YELLOW + "\n\nCORRECTO, COLORES FUNCIONANDO\n")
txt_hs(text)

#Importar libreria tqdm para barra de progreso
from tqdm import tqdm, trange

text = (Style.BRIGHT + Fore.RED + "\nINICIAR SECUENCIA DE ARRANQUE\n")
txt_hs(text)


#Creando barra de progreso
for num in tqdm(range(100)):
    sleep(0.01) 
    
text = (Style.BRIGHT + Fore.MAGENTA + "\nAI" + Fore.CYAN + "PS" + Fore.GREEN + " CARGADO\n" + Style.RESET_ALL)
txt_hs(text)

print (Fore.RESET)	

#Bloque While para interpretar comandos
while True:
    shell = input ("> ")
    
    if (shell == "exit"):
            break
    elif (shell == "help"):
    	text = ("\nBLOQUE AYUDA\nComandos implementados hasta el momento:\nabout    --muestra la version del programa\ncalc     --una calculadora aun en desarrollo\nnotebloc --un bloc de notas con interfaz grafica\nsyscmd   --accede a comandos del sistema, solo se ha probado en linux\n")
    	txt_hs(text)
    
    elif (shell == "about"):
    	text = ("Version 0.45\n")
    	txt_hs(text)
        
    elif (shell == "calc"):
        print (Style.BRIGHT + Fore.YELLOW + "\nCARGANDO CALCULADORA\n" + Style.RESET_ALL)
        exec(open("mod_calc.py").read())
    
    elif (shell == "notebloc"):
    	text = (Fore.GREEN + Style.BRIGHT + "CARGANDO BLOC DE NOTAS\n" + Style.RESET_ALL + Fore.RESET)
    	txt_hs(text)
    	exec(open("notebloc.py").read())
    	
    elif (shell == "syscmd"):
    	text = (Fore.GREEN + Style.BRIGHT + "CARGANDO COMANDOS DEL SISTEMA\n" + Style.RESET_ALL + Fore.RESET)
    	txt_hs(text)
    	text = (Fore.GREEN + Style.BRIGHT + "para salir use 'syscmd -e'\n\n" + Style.RESET_ALL + Fore.RESET)
    	txt_hs(text)
    	syscmd()
    
    elif (shell == "reset"): #crea un bucle, no funciona
    	exec(open("aips.py").read())
        
    else:
        print ("Shell: comando no reconocido")
        


