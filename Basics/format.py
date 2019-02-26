
temp='''This is a multi line string. This code challenge is to
    test your understanding about strings.
    You need to print some part of this string.
    From here print this text without manually counting the indexes.'''
    
c=0
r=list(temp)

for i in range(0,len(temp)):
    if(r[i]=='.'):
        c=c+1
    
    if(c==3):
        break
        x=i
        
e=r[x:]
y=''.join(e)
print(y)
