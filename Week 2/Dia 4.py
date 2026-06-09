#file = open("sequences.txt")
#content = file.read()
#sequences = content.splitlines()
#print(content)
#file.close()
#for seq in sequences:
 #   if "CG" in seq:
  #      print("High CG content")
   # else:
    #    print("Low CG content")
    #ATG_counter = seq.count('ATG')
    #print(seq, "Longitud:",len(seq), "---ATG counter:", ATG_counter)

#output = open("result.txt", "w")
#output.write("Analysis complete")
#output.close()
file = open("sequences.txt")
content = file.read()
sequences = content.splitlines()
file.close()

results = open("results.txt", "w")

for seq in sequences:
    if "CG" in seq:
        cg_message = "High CG content"
    else:
        cg_message = "Low CG content"

    ATG_counter = seq.count("ATG")

    results.write("Sequence: " + seq + "\n")
    results.write("Length: " + str(len(seq)) + "\n")
    results.write("ATG counter: " + str(ATG_counter) + "\n")
    results.write("CG message: " + cg_message + "\n")
    results.write("\n")

results.close()