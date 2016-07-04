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

 ww = f.read()                   #read the file 

 x = 0
 word = ''                  #empty word used to add letter to it, then add word to list
 while x < len(ww):
     word = ''              #start with empty word
     if ord(ww[x]) == 32:                           #split by spaces
         word = word + ' '
         x = x + 1
         while x < len(ww) and ord(ww[x]) == 32:    #combine the spaces together
             word = word + ' '
             x = x + 1
         W.append(word)
     elif ord(ww[x]) == 10:                         #split by new line
         word = word + '\n'
         x = x + 1
         while x < len(ww) and ord(ww[x]) == 10:    #combine new line together
             word = word + '\n'
             x = x + 1
         W.append(word)        
     elif ord(ww[x]) == 9:                          #split by tab
         word = word + '\t'
         x = x + 1
         while x < len(ww) and ord(ww[x]) == 9:     #combine tabs together
             word = word + '\t'
             x = x + 1
         W.append(word)
     else:                                          #combine words
         word = word + ww[x]
         x = x + 1
         while x < len(ww) and (ord(ww[x]) != 9) and (ord(ww[x]) != 10) and (ord(ww[x]) != 32):     #if next value isn't tab, space, or new line, add next value
             word = word + ww[x]
             x = x + 1
         W.append(word)


 yy = 1         #used to add number to new words
 for x in range(0, len(W)):
     if(W[x] not in X):         #too add the number to the word
         X.append(W[x])
         Z.append(yy)
         Z.append(W[x])
         yy = yy + 1
     else:                      #reference position of existing word in the list
         i = X.index(W[x])      #find position of word
         X.remove(W[x])         #remove word
         X.append(W[x])         #add it to the end of the list
         Z.append(len(X) - i)   #note the position of the word that should be entered

 ZZ = []    #list to store encrypted numbers
 x = 0      #counter for position of words
 while x < len(Z):
     if str(Z[x]).isalpha():        #store words
         ZZ.append(Z[x])
         x = x + 1
     elif Z[x] == '\n':
         ZZ.append(Z[x])
         x = x + 1
     elif type(Z[x]) == int:        #store position values
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


 Z = ZZ
 f.close()

 f_in = open(xx,'wb')
 xxx= bytearray()       #write the key code
 xxx.append(0xfa)
 xxx.append(0xce)
 xxx.append(0xfa)
 xxx.append(0xdf)

 Q = []
 f_in.write(xxx)        #write the key code

 for x in range(0, len(Z)):   #write in the words  
     if Z[x].isalpha():
         n = Z[x].encode('latin1')
         f_in.write(n)
     elif Z[x] == '\n':
         X = '\n'
         f_in.write(bytes(X, 'UTF-8'))         
     else:
         xxx = bytearray()
         xxx.append(int(Z[x], 16))
         f_in.write(xxx)
 f_in.close()

 thisFile = xx
 base = os.path.splitext(thisFile)[0]   #split the file name
 os.rename(thisFile, base + ".mtf")     #add extension

def decode(xx):

 
 f = open(xx, 'rb+')

 c = f.read(4)

 v = b'\xfa\xce\xfa\xde'
 
 u = b'\xfa\xce\xfa\xdf'

 if c == v:
     o = 0
 elif c == u:
     o = 0
 else:
     print('wrong special number')
     sys.exit()

 a = str(f.read())

 q = open(xx, 'rb')

 b = ''

 b = q.read()
 
 X = []

 Y = []

 p = ''
 pp = ''              # for spaces

 for x in range(5, len(b)+1):
     X.append((b[x-1:x]).decode('latin1'))

 x = 0

 tt = 0

 prob = 0
 prob2= 0
 prob3= 0
 prob4= 0

# print(X)

# sys.exit()
 
 while x <len(X):
     z = X[x].encode('latin1')
     if z.isalpha() or z.isdigit():
         p = p + X[x]
         if x == len(X)-1:
             Y.append(p)
         else:
             x = x + 1
     elif (ord(X[x]) >= 33 and ord(X[x]) <= 47) or (ord(X[x]) >= 91 and ord(X[x]) <= 96) or (ord(X[x]) >= 58  and ord(X[x]) <= 64) or (ord(X[x]) >= 123  and ord(X[x]) <= 126):  
         vv = ord(X[x])
         ww = bytearray()
         ww.append(vv)
         p = p + ww.decode('latin') 
         x = x + 1     
     elif ord(X[x]) == 32:                  	# for spaces
         pp = ' '
         x = x + 1
         while ord(X[x]) == 32:
             pp = pp + ' '
             x = x + 1
         Y.append(pp)                           # end of for spaces
     else:
         ll = ord(X[x])
         if ll == 0xf9:
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
         elif ll == 0xfa:
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
         else:
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
 
# print(Y)

# sys.exit()

 x = 0
        
 X = []

 Z = []

 t = 1
 
 while len(Y)> 0:
     a = Y[0]
    # print(X)
     if t == a:
         Y.pop(0)
         X.append(Y[0])
        # X.append(' ')                #Taken out for spaces
         Z.append(Y[0])
         Y.pop(0)
         t = t + 1
     elif a == '\n':
         X.reverse()
         if len(X) != 0:
             if X[0] == ' ':
                 X.pop(0)
                 X.reverse()
             else:
                 X.reverse()
         else: 
             X.reverse() 
         X.append('\n')
         Y.pop(0)
     elif str(a)[0] == ' ':                 # added for spaces
         X.reverse()
         if len(X) != 0:
             if X[0] == ' ':
                 X.pop(0)
                 X.reverse()
             else:
                 X.reverse()
         else:
             X.reverse()
         X.append(a)
         Y.pop(0)
     else:
         Z.reverse()
         if len(Z) != 0:
             X.append(Z[a-1])
            # X.append(' ')             #Taken out for spaces
             H = Z[a-1]
             Z.remove(Z[a-1])
             Z.reverse()
             Z.append(H)
             Y.pop(0)

# print(X)

# sys.exit()

# X.pop(len(X) - 1)                      # for spaces

# print(X)

# sys.exit()

 R = ''.join(str(e) for e in X)
 f_in = open(xx,'w')

 f_in.write(R)

 thisFile = xx
 base = os.path.splitext(thisFile)[0]
 os.rename(thisFile, base + ".txt") 
