def move(n,x,y,z):
    if(n>0):
        move(n-1,x,z,y)
        print('Move disk', n,'form', x,'to', y)
        move(n-1,z,y,x)

while(1):
    a=int(input('您已经进行汉诺塔教程，请选择汉诺塔的数'))
    move(a,'A', 'C', 'B')
    break        
