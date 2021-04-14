from time import sleep
from cprint import cprint  # IF YOU DONT HAVE CPRINT INSTALLED. USE NORMAL PRINT
from datetime import datetime
while True:
	x = datetime.now()
	cprint.info(x.strftime("%H:%M:%S"))
	sleep(1)


    #imprimir en la terminal de la compu para que funcione