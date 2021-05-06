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

#-----------------------------------

def name (n = 'arian', j = 'dastranj'):
    if n == 'neda' and  j == 'jenab':
        return 'your name is True'
    else:
        return 'your name is False'
name('neda')       #  'your name is False' : جواب 

#------------------------------------

def adad(a, b):
    if a * b > 100 :
        return 'Your number is greater than one hundred'
    else:
        return 'Your number is less than one hundred'
adad (9, 3)        # 'Your number is less than one hundred' : جواب 

#-------------------------------------

def arian (s, d):
    if s == 13 and d == 5 :
        return s * d
    else :
        return s // d
arian (13, 3)     # جواب : 4

#--------------------------------------

def esm (f, g) :
    if f == 'neda ' and g == 'jenab':
        return f + g
    else:
        return False
esm ('neda ', 'jenab' )     # 'neda jenab' : جواب 

#---------------------------------------

def adad (a, s, d):
    if a == 34 and s == 3 and d == 4 :
        return a * s + d
        print ('True')
    else :
        return a * s // d
        print ('False')
adad (34, 3, 5)           # جواب : 20

#----------------------------------------

def riyazi (m, a, n) :
    if m < 44 and a > 12 and n == 8:
        return m * a + n
    else :
        return m // a - n
riyazi (43, 13, 10)       # جواب : -7

#-----------------------------------------

def arian_code (a = 'ali ', b = 'dastranj', c = 'dooset darm') :
    if a == 'neda ' and b == 'jenab ' and c == 'dooset darm':
        return a + b + c
    else :
        return 'arian ' + 'dastranj ' + 'dooset darm'
arian_code ('ned ', 'jenab ', 'dooset darm')       # arian dastraj dooset darm : جواب 

#------------------------------------------

def adad (a, m, s, d, g, t) :
    if a == 44 and m == 13 and s == 38 and d == 46 and g == 33 and t == 80 :
        return a * m * s * d * g * t
    else :
        return a + m + s + d + g + t
        print ('adad shoma nadorost ast')
arian = adad (44, 13, 38, 46, 33, 80) 
print (arian)           # جواب : 2639619840

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

#---------------------------------------

def adad_avval(s):
    lst = []
    for m in range(2, s + 1):
        c = 0
        for i in range (1, m+1):
            if m % i == 0 :
                c = c + 1
        if c == 2 :
            lst.append(i)
    return lst
adad_avval(13)    # جواب : [2, 3, 5, 7, 11, 13]

#-----------------------------------------

def avval(num):
    c = 0
    for i in range(1, num + 1):
        if num % i == 0:
            c = c + 1     
    if c == 2:
        return True
    else:
        return False          
x = avval(103)     
print(x)                    #  True : جواب
 
#------------------------------------------

def my_function (x) :
    return x [::-1]
n = my_function ('amir')
print (n)       #rima : جواب

#--------------------------------------------

def fibonacci (x) :
    a, b = 0, 1
    while a < x :
        print (a, end=' ')
        a, b = b, a + b
fibonacci (10)       # جواب : 0 1 1 2 3 5 8

#---------------------------------------------

def rev_name (x) :
    a = ''
    for i in x :
        a = i + a
    return a
d = rev_name ('amir')
print (d)














