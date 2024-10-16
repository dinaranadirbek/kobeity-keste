def multiplication_table(limit):

    for i in range(1, limit + 1):
        print(f"{i}-ге арналған көбейту кестесі:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()


limit = int(input("Қай санға дейін көбейту кестесін шығару керек екенін енгізіңіз: "))
multiplication_table(limit)

