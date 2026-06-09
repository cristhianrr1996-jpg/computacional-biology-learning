gene_expression = {
    "BRCA1": 12.5,
    "TP53": 8.2,
    "EGFR": 15.1,
    "MYC": 20.3
}
total = 0
maximun = 0
minimum = list(gene_expression.values())[0]
for gene, expression in gene_expression.items():
    print("Gene: ", gene, " ---> Expression: ", expression)
    if expression > 10:
        print(f" esta sobreexpresado")
    else:
        print(f" expresion normal")
    total += expression
    if expression > maximun:
        maximun = expression
    if expression < minimum:
        minimum = expression

print("Total", round(total, 2))
average = total / len(gene_expression)
print("Average:", round(average,2))
print("Maximum:", maximun)
print("Min", minimum)