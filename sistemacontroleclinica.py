continuar = "S"
totalPacientes = 0
totalConvenios = 0
totalPrioritarios = 0
faturamentoBruto = 0
totalDescontos = 0
faturamentoLiquido = 0
media = 0
maiorValor = 0
menorValor = 0

while continuar == "S":
            totalPacientes = totalPacientes + 1

            nome = input("Digite seu nome: ")
            idade = int(input("Digite sua idade: "))

            print("Atendimentos disponíveis:")
            print("1 - Consulta médica")
            print("2 - Psicologia")
            print("3 - Nutrição")
            print("4 - Fisioterapia")

            codigoAtend = int(input("Digite seu código de Atendimento (1 a 4): "))
            while codigoAtend < 1 or codigoAtend > 4:
                 print("Atendimento inválido, Digite novamente:")
                 codigoAtend = int (input("Digite seu código de Atendimento (1 a 4): "))

            if codigoAtend == 1:
                print("Consulta médica, valor R$180.00")
                valorAtend = 180.00
            elif codigoAtend == 2:
                print("Psicologia, valor R$150.00")
                valorAtend = 150.00
            elif codigoAtend == 3:
                print("Nutrição, valor R$120.00")
                valorAtend = 120.00
            elif codigoAtend == 4:
                print("Fisioterapia, valor R$100.00")
                valorAtend = 100.00

       
            faturamentoBruto = faturamentoBruto + valorAtend

            if idade >= 60 or idade < 12:
                print("Atendimento prioritário")
                totalPrioritarios = totalPrioritarios + 1
            else:
                print("Atendimento comum")

            convenio = input("Digite se voce tem convênio (S/N): ").upper()

            if convenio == "S":
                totalConvenios = totalConvenios + 1

                if idade >= 60 or idade < 12:
                        percentualDesconto = 0.25
                else:
                        percentualDesconto = 0.20


                valorDesconto = valorAtend * percentualDesconto
                valorFinal = valorAtend - valorDesconto
                totalDescontos = valorDesconto + totalDescontos
                

                print(f"Desconto: R$ {valorDesconto:.2f}")
                print(f"Valor final: R$ {valorFinal:.2f}")
            else:
                print("Sem desconto.")
                print(f"Valor final: R$ {valorAtend:.2f}")
                valorFinal = valorAtend


            if totalPacientes == 1:
                maiorValor = valorFinal
                menorValor = valorFinal
            else:
                if valorFinal > maiorValor:
                    maiorValor = valorFinal

                if valorFinal < menorValor:
                    menorValor = valorFinal

            continuar = input("Deseja continuar? (S/N): ").upper()
            while continuar not in ("S", "N"):
                print("Opção inválida. Digite S ou N.")
                continuar = input("Deseja continuar? (S/N): ").upper()

            
print()
print()
faturamentoLiquido = faturamentoBruto - totalDescontos

if totalPacientes > 0:
    media = faturamentoLiquido / totalPacientes  
else:
    media = 0  

print()
print("     Relatório Final do dia     ")
print(f"Total de pacientes atendidos: {totalPacientes}")
print(f"Total de pacientes com convênio: {totalConvenios}")
print(f"Total de pacientes prioritários: {totalPrioritarios}")
print(f"Total de Faturamento Bruto: R$ {faturamentoBruto:.2f}") 
print(f"Total de descontos: R$  {totalDescontos:.2f}")
print(f"Total de Faturamento Líquido: R$ {faturamentoLiquido:.2f}")
print(f"Média final dos atendimentos: R$  {media:.2f}")
print(f"O maior valor no final do atendimento foi: R$ {maiorValor:.2f}")
print(f"O menor valor no final do atendimento foi: R$ {menorValor:.2f}")
