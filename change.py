def change():
    expense = 23.75
    money = 100
    restante = money - expense
    print("Ingresar Gasto:")
    print(expense)
    print("Dinero recibido:")
    print(money)
    print("")
    print("""Vuelto:
    """)
    print("Pesos:")
    print(int(restante))
    print("Centavos:")
    print(int((restante - int(restante))*100))
change()
