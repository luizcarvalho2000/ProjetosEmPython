import turtle

# Configuração inicial
window = turtle.Screen()
window.bgcolor("white")

# Criando uma tartaruga
tartaruga = turtle.Turtle()
tartaruga.speed(3)
tartaruga.pensize(3)

# Desenhando o logotipo do Instagram
tartaruga.color("#E1306C")  # Cor do gradiente
tartaruga.circle(100)       # Círculo externo

tartaruga.penup()
tartaruga.goto(-45, 0)      # Posiciona a tartaruga para desenhar o retângulo interno
tartaruga.pendown()

tartaruga.color("white")    # Cor do retângulo
tartaruga.setheading(0)     # Define a orientação para a direita
tartaruga.forward(90)       # Largura do retângulo
tartaruga.setheading(90)    # Define a orientação para cima
tartaruga.forward(180)      # Altura do retângulo
tartaruga.setheading(180)   # Define a orientação para a esquerda
tartaruga.forward(90)       # Largura do retângulo

# Fechando a janela ao clicar
window.exitonclick()
