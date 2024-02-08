import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk


def save_qrcode():
    # Informações da sua rede Wi-Fi
    ssid = 'BANKAY'
    password = 'Alicemateus@0616'
    encryption = 'WPA2'  # Tipo de criptografia (pode ser WEP, WPA, WPA2)

    # Criação do QR Code
    wifi_info = f'WIFI:T:{encryption};S:{ssid};P:{password};;'
    img = qrcode.make(wifi_info)

    # Salvar o QR Code como uma imagem
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    img.save(file_path)

    # Converter a imagem do QR Code em um formato que possa ser exibido pelo widget Label
    img = Image.open(file_path)
    img = img.resize((200, 200))
    img = ImageTk.PhotoImage(img)

    # Atualizar o widget Label com a imagem do QR Code
    qrcode_label.config(image=img)
    qrcode_label.image = img

# Criação da janela principal

root = tk.Tk()
root.title("Gerador de QR Code Wi-Fi")

# Criação do botão para gerar o QR Code
generate_qrcode_button = tk.Button(root, text="Gerar QR Code", command=save_qrcode)
generate_qrcode_button.pack()

# Criação do widget Label para exibir o QR Code
qrcode_label = tk.Label(root)
qrcode_label.pack()

# Iniciar o loop principal da janela principal
root.mainloop()