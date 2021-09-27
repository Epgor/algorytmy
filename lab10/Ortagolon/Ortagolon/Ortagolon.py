import math

def variables(i_b, i_a, i_n):
    global b, a, n, xi, yi, Ci, Li, WL
    b = i_b
    a = i_a
    n = i_n
    xi = [0] * (n+1)
    yi = [0] * (n+1)
    Ci = [0] * (n+1)
    Li = [0] * (n+1)
    WL = [0] * (n+1)

    

#wyliczanie wartości h
def calc_var():
    buff = abs(b-a)
    h = buff/n
    return h


#wyliczanie punktów xi
def calc_points():
    xi[0] = 1
    for zi in range(1, n+1):
        xi[zi] = (a+(zi/n)*(b-a))


def func(x):
    yi[0] = math.sqrt(4*a**2 +3)
    yi[n] = math.sqrt(4*a**2+3)
    for dd in range(1, len(xi)-1):
        x = xi[dd]
        yi[dd] = math.sqrt(4*x**2+3) 


#liczenie trapezów
def calc_trap(h):
    buff = 0
    buff +=(yi[0]/2)
    buff +=(yi[n]/2)
    for di in range(1, n):
        buff+=yi[di]
    buff *= h
    return buff


#funkcja główna dla met. trapezowej
def inte_trap():
    h = calc_var()   
    return calc_trap(h)


#work in progress
def main_trap():       
    px = 1 #definiuje wage
    return inte_trap()



def Wiel_Leg(x, b, n):
    WL[0] = 1
    WL[1] = x
    for z in range(1,n-1):
        WL[z+1] = 1/(n+1)*(2*n+1)*x*WL[z]-n*WL[z-1]
    WL[n] = 1/(n+1)*(2*n+1)*b*WL[n]-n*WL[n-1]


def Integer_Lamb(a, b, n): 
    variables(b, a, n)  
    for z in range(n+1):
      calc_points()
      Wiel_Leg(xi[z], b, n)
      for zi in range(n+1):
          yi[zi] = WL[zi]**2
      Li[z] = main_trap()




def Integer_Ci(a, b, n, x):
      variables(b, a, n)  
      for z in range(n+1):
        calc_points()
        Wiel_Leg(xi[z], b, n)
        func(x)
        for zi in range(n+1):
            yi[zi] *= WL[zi] 
        Ci[z] = main_trap()


Integer_Lamb(-1, 1, 2)
Integer_Ci(-1, 1, 2, 0.25)

buff = 0
for di in range(n+1):
    buff += Ci[di]

print("Wynik:")
print(buff)