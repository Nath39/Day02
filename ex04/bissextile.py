année = int(input ("Saisissez une année\n"))
if (année%4 != 0 ) :
  print ("ce n'est pas une année bissextile")
else : 
  if (année%100 == 0 and année%400 != 0) :
    print ("ce n'est pas une année bissextile")
  else :
   print ("c'est une année bissextile")
