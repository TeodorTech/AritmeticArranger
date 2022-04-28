from tabulate import tabulate
sums = ["32 - 698", "1 - 3801", "45 + 43", "123 + 49"]

def arithmetic_arranger(sums):
   line1 = []
   line2 = []
   line3 = []
   line4 = []
   lenght = len(sums)
   for numb in sums:
       a = int(numb.split()[0])
       sign = numb.split()[1]
       b = int(numb.split()[2])
       line1.append(a)
       if len(str(a))>len(str(b)):
        line2.append(str(sign) + "  "*(len(str(a))-len(str(b))) +str(b))
       else:
           line2.append(str(sign) + "  "  + str(b))
       line3.append( '_' * (len(numb.split()[0]) + len(numb.split()[2])))
       if sign == "+":
           line4.append(str(a + b))
       else:
           line4.append(str(a- b))

   for i in range(lenght):
           print(f"{line1[i]:>12}",end=" ")
   print()
   for j in range(lenght):
           print(f"{line2[j]:>12}", end=" ")
   print()
   for k in range(lenght):
           print(f"{line3[k]:>12}", end=" ")
   print()
   for z in range(lenght):
           print(f"{line4[z]:>12}", end=" ")
   print()

# verification of the problems
def verification():
    if len(sums) < 5:
     for g in sums:
      if g.split()[1] == ("+"):
         if  g.split()[0].isdigit():
              if len(g.split()[0]) <= 4:
                if  g.split()[2].isdigit():
                    if len(g.split()[2]) <= 4:
                        x = 1
                    else:
                        x = 0
                        print("Error: Numbers cannot be more than four digits")
                        break
                else:
                    x = 0
                    print("Error: Numbers must only contain digits.")
                    break
              else:
                  x = 0
                  print("Error: Numbers cannot be more than four digits")
                  break
         else:
             x = 0
             print("Error: Numbers must only contain digits.")
             break
      else:
          if g.split()[1] == ("-"):
              if len(g.split()[0]) <= 4:
                  if len(g.split()[2]) <= 4:
                      x = 1
                  else:
                      x = 0
                      print("Error: Numbers cannot be more than four digits")
                      break
              else:
                  x = 0
                  print("Error: Numbers cannot be more than four digits.")
                  break
          else:
           x = 0
           print("Error: Operator must be '+' or '-'.")
           break

    else:
         x = 0
         print("Error: Too many problems.")
    if x == 1:

       arithmetic_arranger(sums)

verification()




