import time
import winsound
segundos=int(input("Alarme para quantos segundos : "))
print("ALARME LIGADO ACORDAAA !")
time.sleep(segundos)
winsound.Beep(1000, 500)
winsound.Beep(1000, 500)
print("TEMPO ACABOU !!!!!")