import math
#variables
#obliczanie działa, jeśli w tym miejscu ręcznie ustawimy wartości a, b i n
#to do - funkcja do ustawiania b, a oraz n - definiowanie zmiennych globalnie
##wewnątrz fukncji

def variables(i_b, i_a, i_n):
    global b, a, n, xi, yi, ti, yti
    b = i_b
    a = i_a
    n = i_n
    xi = [0] * (n+1)
    yi = [0] * (n+1)
    ti = [0] * (n)
    yti = [0] * (n)
    

b = 10
a = 4
n = 6
h = 0
xi = [0] * (n+1)
yi = [0] * (n+1)

#DO SIMSONA

ti = [0] * (n)
yti = [0] * (n)

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
    print("xi points", xi)


#funkcja podcałkowa dla trapeza
def func():
    yi[0] = (2+2*a**5-4*a**3)/(4*a)
   
    yi[n] = (2+2*b**5-4*b**3)/(4*b)
    
    for dd in range(1, len(xi)-1):
        x = xi[dd]
        yi[dd] = (2+2*x**5-4*x**3)/(4*x)
    print("yi tab", yi)
        


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
    calc_points()
    func()
    print("Wynik metodą trapeów to: ")
    print(calc_trap(h))


#funkcja podcałkowa dla simsona
def func_simp():
    for dd in range(len(ti)):      
        x = ti[dd]
        yti[dd] = (2+2*x**5-4*x**3)/(4*x)
    print("yti tab", yti)

#liczenie h oraz ti dla metody simsona
def simp_calc_var():
    for ss in range(len(ti)):
        ti[ss] = (xi[ss+1]+xi[ss])/2
    h = (xi[n]-xi[n-1])/2
    print("h ", h)
    print("ti tab", ti)
    return h


#liczenie parabol simsona
def calc_simp(h):
    buff = 0
    buff += yi[n]
    buff += yi[0]
    for di in range(0, len(ti)):
        buff+=yti[di]*4
    for di in range(1, len(yi)-1):
        buff+=yi[di]*2
    buff *= h/3
    return buff


#funkcja glówna dla met. simsona
def inte_simp():
    calc_points()
    func()    
    h = simp_calc_var()
    func_simp()
    print("wynik metodą simpsona to : ")
    print(calc_simp(h))

#work in progress
def main():
    flag = "Y"
    in_flag = "Y"

    print("Czy chcesz skorzystać z ustawień domyślnych?")
    print("Y = TAK")
    print("N = NIE")
    in_flag = input()

    if in_flag != "Y":
        print("Podaj n: ")
        n = int(input())
        print("Podaj a: ")
        a = float(input())
        print("Podaj b: ")
        b = float(input())
        variables(b, a, n)
    else:
        print("Okey!")


    print("Z jakiej metody chcesz skorzystać?")
    print("T =  CAŁKOWANIE NUMERYCZNE: METODA TRAPEZÓW")
    print("S =  CAŁKOWANIE NUMERYCZNE: SIMPSONA")

    flag = input()


    if flag == "T":
        inte_trap()
    elif flag == "S":
        inte_simp()
    else:
        print("Error 404. Kończę działanie programu.")


main()