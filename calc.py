def Calc():
    print("Modo soma")
    nums = []

    while True:
        print(f"{nums}")
        i = input("SOMA> ")

        if i == "exit":
            break

        if i == "calc":
            calc = sum(nums)
            print(f"Result: {calc}")
            break

        try:
            i = float(i)
            nums.append(i)

        except ValueError:
            print("Erro: não é um número válido.")
