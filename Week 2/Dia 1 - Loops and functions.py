#successful = False
#for number in range (1, 10, 2):
    #print("STD A", number + 1, (number + 1) * ".")
    #if successful:
        #print("Run the secuence")
        #break
#else:
    #print("No run")
#for x in range (5):
 #   for y in range(3):
  #      print(f"({x},{y})")
#for x in "Python":
 #   print(x)
#for x in [1, 2, 3, 4]:
    #print(x)
#shopping_cart = ("huevos", "harina", "Pan")
#for item in shopping_cart:
 #   print(item)
from operator import truediv

#count = 0
# for number in range (1, 10):
    #if number % 2 == 0:
     #   count += 1
      #  print(number)
#print(f"we have {count} even numbers")

dna_sequences = [
    "ATGCGTAA",
    "GGGCTA",
    "TTATGCC",
    "AACCAA",
    "ATGTTT"
]
#atg_count=0
#for seq in dna_sequences:
 #   if "ATG" in seq:
  #      atg_count+=1
   #     print("sequence with ATG:", atg_count)
def has_start_codon(sequence):
    if "ATG" in sequence:
        return True
    else:
        return False
for seq in dna_sequences:
    result = has_start_codon(seq)
    print(seq, result)
