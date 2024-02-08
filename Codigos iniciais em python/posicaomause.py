import pyautogui
import time

# pega o retorno da posição atual de x e y do mouse e passa o valor da tupla para as duas variaveis

print('Posicione o MOUSE')
time.sleep(5)
x, y = pyautogui.position()
print("Posição atual do mouse:")
print("x = "+str(x)+" y = "+str(y))

# retorna True se x & y estiverem dentro da tela

print("\nEsta dentro da tela?")
resp = pyautogui.onScreen(x, y)
print(str(resp) + "\n")