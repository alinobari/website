# #!/opt/bin/python3

import os
import sys
import binascii
import re

def encode(xx):

 W = []
 X = []
 Z = []

 f = open(xx, 'r')

 ww = str(f.read())                   #added for spaces

 for line in f:
    W.append('\n')
    for x in line.split():
         W.append(x)

# W.pop(0)                             # removed for spaces 

# print(ww)
# sys.exit()

 yy = 0

 W = re.split(r'(\s*)', ww)            # added for spaces
 W.pop(len(W) - 1)                     # added for spaces
# print(W)
# sys.exit()

 for x in range(0, len(W)):
     ii = W[x]
     if ii[0] == '\n':
         Z.append(W[x])
     elif(W[x] not in X):
         X.append(W[x])
         Z.append(yy + 1)
         Z.append(W[x])
         yy = yy + 1
     else:
         i = X.index(W[x])
         word = X[i]
         X.remove(word)
         X.append(word)
         Z.append(len(X) - i)

# print(Z)
# sys.exit()

 ZZ= []

 x = 0

 while x < len(Z):
     if str(Z[x]).isalpha():
         ZZ.append(Z[x])
         x = x + 1
     elif Z[x] == '\n':
         ZZ.append(Z[x])
         x = x + 1
     elif type(Z[x]) == int:
         if Z[x] < 121:
             n = Z[x]
             n = n + 128
             n = hex(n).split('x')[1]
             n = '0x' + str(n)
             ZZ.append(n)
             x = x + 1
         elif Z[x] > 120 and Z[x] < 376:
             n = 249
             n = hex(n).split('x')[1]
             n = '0x' + str(n)
             ZZ.append(n)
             n = Z[x]
             n = n - 121
             n = hex(n).split('x')[1]
             n = '0x' + str(n)
             ZZ.append(n)
             x = x + 1
         else: #if Z[x] > 375 and Z[x] < 65912: 
             n = 250
             n = hex(n).split('x')[1]
             n = '0x' + str(n)
             ZZ.append(n)
             n = Z[x]
             n = (n - 376)//256
             n = hex(n).split('x')[1]
             n = '0x' + str(n) 
             ZZ.append(n)
             n = Z[x]
             n = (n - 376)%256
             n = hex(n).split('x')[1]
             n = '0x' + str(n)
             ZZ.append(n)
             x = x + 1 
     elif (len(str(Z[x])) == 1) and (Z[x] != 1) and (Z[x] != 2) and (Z[x] != 3) and (Z[x] != 4) and (Z[x] != 5) and (Z[x] != 6) and (Z[x] != 7) and (Z[x] != 8) and (Z[x] != 9):
         n = ord(Z[x])
         n = hex(n).split('x')[1]
         n = '0x' + str(n)
         ZZ.append(n)
         x = x + 1
     else:
         n = Z[x]
        # print(n)
         p = ''
         y = 0
         while y < len(n):
             if str(n[y]).isalpha():
                 p = p + n[y]
                 y = y + 1
             else:
                 if p != '':
                     ZZ.append(p)
                 p = ''
                 nn = ord(n[y])
                 nn = hex(nn).split('x')[1]
                 nn = '0x' + str(nn)
                 ZZ.append(nn)
                 y = y + 1
         if p != '':
             ZZ.append(p)
         x = x+1

# print(ZZ) 
# sys.exit()

#     else:
 #        n = ord(X[x])
  #       n = hex(n).split('x')[1]
   #      n = '0x' + str(n)
    #     ZZ.append(n)
     #    x = x + 1 



 Z = ZZ

# print(Z)

# sys.exit()

 
 f.close()

 f_in = open(xx,'wb')
# f_in = open('/home/alinobar/alinobar/assign3/hello.txt','wb')
 xxx= bytearray()
 xxx.append(0xfa)
 xxx.append(0xce)
 xxx.append(0xfa)
 xxx.append(0xdf)

 Q = []

 f_in.write(xxx)

 for x in range(0, len(Z)):
     if Z[x].isalpha():
         n = Z[x].encode('latin1')
       #  print(n)
         f_in.write(n)
     elif Z[x] == '\n':
         X = '\n'
         f_in.write(bytes(X, 'UTF-8'))
     #elif type(Z[x]) != int:
      #   n = Z[x].encode('latin1')
       #  f_in.write(n)         
     else:
        # print(Z[x])
         xxx = bytearray()
         xxx.append(int(Z[x], 16))
         f_in.write(xxx)

# X = '\n'                                    #taken out for spaces $$$Check
# f_in.write(bytes(X, 'UTF-8'))               #taken out for spaces $$$Check

 f_in.close()

 thisFile = xx
 base = os.path.splitext(thisFile)[0]
 os.rename(thisFile, base + ".mtf")

def decode(xx):

 f = open(xx, 'rb+')
 c = f.read(4)

 v = b'\xfa\xce\xfa\xde'    #check the code
 u = b'\xfa\xce\xfa\xdf'

 if c == v:
     o = 0
 elif c == u:
     o = 0
 else:
     print('wrong special number')  #if special number is wrong, exit
     sys.exit()

 a = str(f.read())
 q = open(xx, 'rb')

 b = ''
 b = q.read()
 q.close()
 
 X = []     #used to store words 
 Y = []

 p = ''
 pp = ''              # for spaces

 for x in range(5, len(b)+1):       #store the words
     X.append((b[x-1:x]).decode('latin1'))

 x = 0
 while x <len(X):       #decode the list of Z
     z = X[x].encode('latin1')
     if z.isalpha() or z.isdigit():
         p = p + X[x]
         if x == len(X)-1:
             Y.append(p)
             x = x + 1
         else:
             x = x + 1
     elif (ord(X[x]) >= 33 and ord(X[x]) <= 47) or (ord(X[x]) >= 91 and ord(X[x]) <= 96) or (ord(X[x]) >= 58  and ord(X[x]) <= 64) or (ord(X[x]) >= 123  and ord(X[x]) <= 126): # for any symbol 
         vv = ord(X[x])
         ww = bytearray()
         ww.append(vv)
         p = p + ww.decode('latin') 
         x = x + 1     
     elif ord(X[x]) == 32:                  	#for spaces
         pp = ' '
         x = x + 1
         while x < len(X) and ord(X[x]) == 32:  #combine the spaces 
             pp = pp + ' '
             x = x + 1
         Y.append(pp)                           
     elif ord(X[x]) == 9:                  	#for tab
         pp = '\t'
         x = x + 1
         while x < len(X) and ord(X[x]) == 9:   #combine tabs
             pp = pp + '\t'
             x = x + 1
         Y.append(pp)
     elif ord(X[x]) == 10:                  #for new line                	
         pp = '\n'
         x = x + 1
         while x < len(X) and ord(X[x]) == 10:      #combine the new line
             pp = pp + '\n'
             x = x + 1
         Y.append(pp)                  
     else:                                  #for the numbers that are encrypted
         ll = ord(X[x]) 
         if ll == 0xf9:             #for the second set of numbers
             x = x + 1
             c = ord(X[x])
             c = c + 121
             if p != '':
                 Y.append(p)
                 p = ''
                 Y.append(c)
                 x = x+1
             else:
                 Y.append(c)
                 x = x+1 
         elif ll == 0xfa:           #for the third set of numbers
             x = x + 1
             a = ord(X[x])
             x = x + 1
             b = ord(X[x])
             cc = (a*256) +b + 376 
             if p != '':
                 Y.append(p)
                 p = ''
                 Y.append(cc)
                 x = x+1
             else:
                 Y.append(cc)
                 x = x+1 
         else:                      #for the first set of numbers
             if p != '':
                 Y.append(p)
                 p = ''
                 if X[x] == '\n':
                     Y.append('\n')    
                 else:
                     Y.append(ord(X[x])- 128)
                 x = x+1
             else:
                 if X[x] == '\n':
                     Y.append('\n')
                 else:
                     Y.append(ord(X[x])-128)
                 x = x+1

 X = []
 Z = []
 t = 1
 
 while len(Y)> 0:               #put the list back together
     a = Y[0]
     if t == a:
         Y.pop(0)
         X.append(Y[0])
         Z.append(Y[0])
         Y.pop(0)
         t = t + 1
     elif a == '\n':
         X.append('\n')
         Y.pop(0)
     elif a == '\t':
         X.append('\t')
         Y.pop(0)
     elif str(a)[0] == ' ':                 
         X.append(a)
         Y.pop(0)
     else:
         Z.reverse()
         if len(Z) != 0:
             X.append(Z[a-1])
             H = Z[a-1]
             Z.remove(Z[a-1])
             Z.reverse()
             Z.append(H)
             Y.pop(0)

 R = ''.join(str(e) for e in X)     #join the list back
 f_in = open(xx,'w')

 f_in.write(R)      #write in the list

 f_in.close()
 f.close()

 thisFile = xx      #rename the file again
 base = os.path.splitext(thisFile)[0]
 os.rename(thisFile, base + ".txt") 
