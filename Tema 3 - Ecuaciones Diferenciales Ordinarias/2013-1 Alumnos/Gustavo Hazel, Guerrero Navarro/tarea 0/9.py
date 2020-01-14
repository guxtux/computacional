tB=0
tA=0
bA=1
bB=1
tf=60*24

while tA<tf:
  bA=bA*2
  tA=tA+60
print 'el número de bacterias en el medio A es', bA

while tB<tf:
  bB=bB*2
  tB=tB+90
print 'el número de bacterias en el medio B es', bB

