#agregar nuevo gen
nuevo_gen = "ATGCGTAACTG"
with open("sequences.txt", "a") as file:
    file.write("\n" + nuevo_gen)
#leer secuencias
file = open("sequences.txt")
content = file.read()
sequences = content.splitlines()
file.close()

def has_start_codon(sequences):
    resultado = []
    for x in sequences:
        resultado.append((x,  "ATG" in x    , len(x)))
    return resultado
resultado = has_start_codon(sequences)
for sequence, Has_Codon, longitud in resultado:
    print("Sequence: ", sequence, "---> Star Codon: ", Has_Codon, "; longitud:", longitud)