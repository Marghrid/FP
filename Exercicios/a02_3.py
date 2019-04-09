fabrico=eval(input("\n\nQual o custo de fabrico?\n"))
percentagem = eval(input("\nQual a percentagem do vendedor?\n"))
imposto = eval(input("\nQual a percentagem de imposto sobre o custo de fabrico?\n"))

preco = fabrico*((100+percentagem+imposto)/100)

print("O preco de venda ao publico e': ", preco)
