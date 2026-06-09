gene_expression = {
    "BRCA1": 12.5,
    "TP53": 8.3,
    "MYC": 15.7
}
for gene, expression in gene_expression.items():
    if expression > 10:
        print(f"{gene} esta sobreexpresado")