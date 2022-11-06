#OSNOVE
#1.
'''
recenica=input('String: ')
razmaci=1
for i in range(len(recenica)):
    if recenica[i]==' ':
        razmaci+=1
print(razmaci)
'''
#2.
'''
recenica=input('String: ')
brmM=0
for i in range(0,len(recenica)):
    if recenica[i]=='M' or recenica[i]=='m':
        brmM+=1
print(brmM)
'''
#3
'''
br=0
string=input('string:')
brojevi='1234567890'
for i in range(0,len(string)):
    if string[i] in brojevi:
        br+=1
print(br)
'''
#4
'''
br=0
string=input('string:')
for i in range(0,len(string)):
    if if 122-ord(string[i])<=25 and 122-ord(string[i])>=0::
        br+=1
print(br)
'''
#5
'''
br1=0
br2=0
string=input('string:')
for i in range(0,len(string)):
    if 122-ord(string[i])<=25 and 122-ord(string[i])>=0:
        br1+=1
    if 90-ord(string[i])<=25 and 90-ord(string[i])>=0:
        br2+=1

if br2<br1:
    print('vise ima malih slova',br1,'velikih: ',br2)
else:
    print('vise ima velikih slova',br2,'malih: ',br1)
'''
#6
'''
string=input('string: ')
if string == string[::-1]:
    print('palindrom')
else:
    print('nije palindrom')
'''
#7
'''
string_unos=input('string: ')
string = string_unos
string=string.replace(' ','')
 
if string == string[::-1]:
    print(string_unos,' je palindrom')
else:
    print(string_unos,' nije palindrom')
'''
#8
'''
string=input('string: ')
string2=''
for i in range(0,len(string)):
    if string[i].isupper():
        a=string[i]
        a=a.swapcase()
        string2+=a
    else:
        string2+=string[i]
print(string2)
'''
#9
'''
string=input('string: ')
a=string.find(' ',-1)
print(a+1)
'''
#19
'''
string=input('string: ')
string2=''
for i in range(0,len(string)):
    if string[i]=='A':
        string2+='I'
    elif string[i]=='a':
        string2+='i'
    elif string[i]=='I':
        string2+='A'
    elif string[i]=='i':
        string2+='a'
    elif string[i]!='...':
        string2+=string[i]
print(string2)
    '''
#20
'''
a=',pitamo se.'
b=',vicemo.'
stringA=input('string: ')
stringB=''
for i in range(0,len(stringA)):
    if stringA[i]=='?':
        stringB+=a
    else:    
        if stringA[i]=='!':
            stringB+=b
        else:
            stringB+=stringA[i]
print(stringB)
'''
#21
'''
string=input('string: ')
string=string.swapcase()
print(string)
'''
#22
'''
string=input('string: ')
string2=''
for i in range(0,len(string)):
    a=ord(string[i])
    a+=1
    if (a>97 and a <=123) or (a>65 and a <= 91):
        if a>97 and a <=123:
            if a==123:
                a=97
            string2+=chr(a)
        if a>65 and a <= 91:
            if a==91:
                a=65
            string2+=chr(a)
    else:
        string2+=string[i]
print(string2)
'''

        
    
    
          


