                            #--------------Function--------------         از فیلم های آموزشی یاد گرفتم 
def show (n ,a):
    print (n / a)
show(10, 5)        # جواب : 2.0

#-----------------------------------

def show (e, b):
    print(e * b)
show (5,6)     # جواب : 30
          
#-----------------------------------

def show (r, b):
    print(r - b)
show (10,2)    # جواب : 8

#-----------------------------------

def show (x, b):
    print(x * b)
show (10,10)
print ('you Good')   # جواب :  you Good 100 

#------------------------------------

def show(a, b):
    print(a * b)
show(3 , 7)       # جواب : 21

#------------------------------------

def tea (name):
    print ('Hello ' + name)
tea ('arian')       # جواب : Hello arian

#-----------------------------------

def k (name):
    if name == 'ali':
        return None
    else:
        return 'Thanks ' + name
x = k ('ali')
print (x)       # جواب : None

#-----------------------------------

def Function (a = 3, b = 5):
    return a * b
c = Function()
print (c)       # جواب : 15

#-----------------------------------

def show (a, b = []):
    b.append(a)
    return b
x = show(5)
x = show(7)
print (x)      # جواب : {7, 5}

#-----------------------------------

def show (a, b = []):
    b.append(a)
    return b
x = show (4 * 2)
x = show (20 *8 +8 / 2)
x = show (108 * 5)
print (x)    # جواب : [8, 164.0, 540]

#-----------------------------------

def arian (ferstname):
    if ferstname == 'ali':
        return 'good name'
    else :
        return 'bad name' + ferstname 
a = arian ('ali')
print (a)          #جواب : good name

#-----------------------------------

def show (ferstname, lastname = 'mamadi'):
    if ferstname + lastname == 'ali' + 'dastranj':
        return 'good name'
    else :
        return 'your name = ' + ferstname + lastname
a = show ('ali ')
print (a)           # جواب : your name = ali mamadi

#-----------------------------------

def show ():
    x = 0
    while x <10 :
        print('you good', end='  ')
        x = x + 1
    return x
show()                  #  you good جواب : 10 تا 

#-----------------------------------

def show ():
    for x in range(3):
        for s in range(1, 11):
            print ("\U0001F600" * s)
show ()      # جواب : استیکر

#-----------------------------------

def show (lastname):
    if lastname == 'dastranj':
        return 'arian ' + lastname
    else:
        return 'your lastname is fals : ' + lastname
x = show('mohamadi')
print (x)       # جواب : your lastname is fals : mohamadi

#-----------------------------------

def show () :
    adad = int(input('pls enter your number : '))
    print ('===========================')
    tedad = 0
    for i in range (1, adad + 1):
        if (adad % i == 0):
            tedad = tedad + 1
            return tedad
a = show()
print(a)
print ('===========================')
print ('tedad shomarande ha : ' , a )

#-----------------------------------

def jam_tafrigh_zarb_taghsim(a, s, d, f):
    return a + s * d / f
s = jam_tafrigh_zarb_taghsim (10,11, 2, 2)
print (s)      # جواب : 21.0

#-----------------------------------

def show(n, j, d, m):
    if n == 'ali' and j == 'dastranj' and d == 'dooset' and m == 'darm':
        return True
    else :
        return False
c = show('ali' , 'dastranj' , 'dooset' , 'darm')
print(c)      # جواب : True

#-----------------------------------

def esm(q, w, e):
    return q + w + e  
c = esm ('arian ' + 'dastranj     ' , 'ali ' + 'dastranj      ' , 'farhad ' + 'dastranj '   )
print (c)     # جواب : arian dastranj     ali dastranj      farhad dastranj


#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
                            #--------------Function--------------   # از استاد خودم یاد گرفتم

def sum_num(a, b, c):
    tot = 0
    for i in range(a,b + 1, c):
        tot = tot + i
    return tot
x = sum_num(100, 600, 2)
print(x)       # جواب : 87850

#--------------------------------------

def bakhshpaziri(n):
    list = []
    for i in range(1, n + 1):
        if n % i == 0 :
            list.append(i)
    return list
x = bakhshpaziri (24)
print (x)          # جواب : [1, 2, 3, 4, 6, 8, 12, 24]






































