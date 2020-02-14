
string = str(input("Enter: "))
r = ["1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","(",")","-","_","=","+","`","~","/","?","<",">",".",","]
pp = []
write = []
i = 0
while i < len(string):
    if string[i:i+1] in r:
        pp.append(string[i:i+1])
        i += 1
    else:
        write.append(string[i:i+1])
        i += 1
oo = write[::-1]
ww = ''.join(oo)
print(ww)
'''
try :
t`a=e+r8g 9e78r3a4 u^o%y*
d82e23m122h49a
1s2o3c4a5t6
e@!ta452loco3>h??c k&&?l>>i<<m54 ht341i#@%w d!1e11))r%ev865%%oc`~ )--sre^$$fa*=w y!7p6si54rC
5327$ه!#$%ل^ا&* )()*&ب^ا%$#@!@#$%^&ل*ز6!34%66ق?,><>/``
'''



#t`a=e+r8g 9e78r3a4 u^o%y* d82e23m122h49a 1s2o3c4a5t6 e@!ta452loco3>h??c k&&?l>>i<<m54 ht341i#@%w d!1e11))r%ev865%%oc`~ )--sre^$$fa*=w y!7p6si54rC