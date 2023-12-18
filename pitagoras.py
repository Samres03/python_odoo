import math
cateto1 = int(input("dame el primer cateto\n"))
cateto2 = int(input("dame el segundo cateto\n"))

hipotenusa = math.sqrt((pow(cateto1,2) + pow(cateto2,2)))

print("la hipotenusa es {}".format(hipotenusa))