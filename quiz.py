question=["What is the functional unit of RNA & DNA?", "What is that plate like proteinous structure called which is generally attached with centromere?", "In which phase of Mitosis the chromosomes can be count?", "In which phase the chromosomes can be found in equator?", "In animal cell which cell organelle helps in building spindle fibre?", "In which phase of cell division CELL-PLATE can be seen?"]
answer=['nucleotide', 'kinetochore', 'metaphase', 'metaphase', 'centrosome', 'cytokinesis']
n=len(question)-1
pts=0
i=0
while i<=n :
  print(question[i])
  x=input("Your Answer: ")
  if x==answer[i]:
      print("Correct Answer, +5pts")
      pts=pts+5
  else:
      print("Ooooh...wrong answer")
      break
  i=i+1
print("Your score: ", pts)






























