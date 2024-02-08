def calcular_salario_liquido(horas_por_dia, preco_hora, dias_trabalhados):
    salario_bruto = horas_por_dia * preco_hora * dias_trabalhados
    desconto = 0.21 * salario_bruto
    salario_liquido = salario_bruto - desconto
    return salario_liquido

def main():
    try:
        horas_por_dia = float(input("Digite a quantidade de horas trabalhadas por dia: "))
        preco_hora = float(input("Digite o preço da hora trabalhada: "))
        dias_trabalhados = int(input("Digite a quantidade de dias trabalhados no mês: "))

        salario_liquido = calcular_salario_liquido(horas_por_dia, preco_hora, dias_trabalhados)
        print("O salário líquido é: R$", salario_liquido)

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números corretos para as variáveis.")

if __name__ == "__main__":
    main()
