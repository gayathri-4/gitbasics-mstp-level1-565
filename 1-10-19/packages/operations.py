def add(a,b):
    print("addition",a+b)
def prime(n):
    fact=0
    for i in range(1,n+1):
        if(n%i==0):
            fact=fact+1
    if(fact==2):
        return True
    else:
        return False
rdef primefactor(n):
        if prime(n)==True:
             for i in range(1,n+1):
                if(n%i==0):  
                    print(i)        