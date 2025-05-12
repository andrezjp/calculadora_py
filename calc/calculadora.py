while True:
    print("----calculadora----")
    print("Escolha a opção:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    opcao = input("Digite o número da operação desejada: ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        print("Resultado:", num1 + num2)
    elif opcao == "2":
        print("Resultado:", num1 - num2)
    elif opcao == "3":
        print("Resultado:", num1 * num2)
    elif opcao == "4":
        if num2 == 0:
            print("Erro: divisão por zero não é permitida.")
        else:
            print("Resultado:", num1 / num2)
    else:
        print("Operação inválida. Por favor, escolha uma opção de 1 a 4.")

    continuar = input("Deseja realizar outra operação? (s/n): ").lower()
    if continuar != 's':
        print("Obrigado por usar a calculadora. Até a próxima!")
        break