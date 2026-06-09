gene_expression = {
    "BRCA1": 12.5,
    "TP53": 8.2,
    "EGFR": 15.1
}
#gene_expression["BRCA1"] = '15'
#del gene_expression["BRCA1"]


#Example to update
#student = {'name':'John','age':25,'courses':['Math','Physics','Chemistry']}
#age = student.pop('age')
#student.update({'name':'jane','age':'26','phone':'55555'})


#print(gene_expression.get('phone', 'Not found'))
for key, value in gene_expression.items():
    print(key, value)