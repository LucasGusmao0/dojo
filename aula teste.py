class funcionario():
    __instance = None

    def __init__(self, nome, salario, cargo, mestrab):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        self.mestrab = mestrab


    def print_nome(self):
        print(self.nome)

    def print_cargo(self):
        print(self.cargo)

    def print_salario(self):
        print(self.salario)

    def calc_13D(self):
       return self.salario * self.mestrab / 12

    def print_tudo(self):
        print("\n")
        print("Nome:", self.nome, "- Salario:", self.salario, "- Cargo:", self.cargo, "- Decimo 13º:", self.calc_13D())


nome = input("digite seu nome: ")
salario = int(input("digite seu salario: "))



cargo = input("digite seu cargo: ")
mesTrab = int(input("digite quantos meses de trabalho voce tem: "))

gerente = funcionario(nome, salario, cargo, mesTrab)
gerente.print_tudo()

teste 1
digite seu nome: mario
digite seu salario: 1000
digite seu cargo: estagiario
digite quantos meses de trabalho voce tem: 2


Nome: mario - Salario: 1000 - Cargo: estagiario - Decimo 13º: 166.66666666666666


***************************************
teste 2
digite seu nome: m3rio - aceitou numero no nome
digite seu salario: -10 - aceitou salario negativo
digite seu cargo: não sei - aceitou qualquer carggo
digite quantos meses de trabalho voce tem: 1


Nome: m3rio - Salario: -10 - Cargo: não sei - Decimo 13º: -0.8333333333333334
**************************************************
teste 3
digite seu nome: 33
digite seu salario: alto
Traceback (most recent call last):
  File "C:/Users/Desenvolvimento/Desktop/Nova pasta/aula teste.py", line 29, in <module>
    salario = int(input("digite seu salario: "))
ValueError: invalid literal for int() with base 10: 'alto'
************************************
teste 4
digite seu nome: 3 letras
digite seu salario: 0
digite seu cargo: 1
digite quantos meses de trabalho voce tem: 0


Nome: 3 letras - Salario: 0 - Cargo: 1 - Decimo 13º: 0.0