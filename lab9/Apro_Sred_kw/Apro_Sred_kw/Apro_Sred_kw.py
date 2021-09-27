import math

#default variables

b = 4
a = 1
n = 3
h = 0
xi = [0] * (n+1)
yi = [0] * (n+1)
Matrix = [[0] * (n+1) for i in range(n+1)]
fynik = [0] * (len(Matrix))
wektorki = [0] * (len(Matrix))

def variables(i_b, i_a, i_n):
    global b, a, n, xi, yi, ti, yti, Matrix, fynik, wektorki
    b = i_b
    a = i_a
    n = i_n
    xi = [0] * (n+1)
    yi = [0] * (n+1)
    ti = [0] * (n)
    yti = [0] * (n)

    Matrix = [[0] * (n+1) for i in range(n+1)]
    fynik = [0] * (len(Matrix))
    wektorki = [0] * (len(Matrix))
    #dodać definiowanie macierzy i listy wyników

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


#funkcja podcałkowa dla trapeza
def func_posz():
    yi[0] = math.sqrt(4*a**2+3) 
    yi[n] = math.sqrt(4*b**2+3)
    for dd in range(1, len(xi)-1):
        x = xi[dd]
        yi[dd] = math.sqrt(4*x**2+3) 

def func_baz(i):
    yi[0] = a**i
    yi[n] = b**i   
    for dd in range(1, len(xi)-1):
        yi[dd] = xi[dd]**i 

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
def inte_trap(t, i):
    h = calc_var()
    calc_points()
    if t == 0:
        func_posz()
    else:
        func_baz(i)
    return(calc_trap(h)) # zmienić na return


def gauss():
    x=0
    i=0 
   

    for i in range(n):
        for row in range(1+i, n+1):
            fraction = Matrix[row][i] / Matrix[i][i]
            fynik[row] -= fraction*fynik[i]
            fynik[row] = round(fynik[row], 4)
            for col in range(n):
                Matrix[row][col] -= fraction * Matrix[i][col]


    
    wektorki[n] = round(fynik[n-1]/Matrix[n-1][n-1], 3)

    for i in range(n-1, -1, -1):
        x = fynik[i]
        for j in range (n-1, -1, -1):
            x -= Matrix[i][j] * wektorki[j]

        wektorki[i] = round(x/Matrix[i][i], 3)



    print("Szukane wektory: ")

    for i in range(len(wektorki)):
        print("|", wektorki[i], "|")



def main():

    variables(-1, 1, 20)

    for x in range(len(Matrix)):
        for y in range(len(Matrix)):
            Matrix[x][y] = round(inte_trap(1, x) * inte_trap(1, y) * 1, 1) #łapać wartości w macierz / funkcja bazowa
    
    for z in range(len(fynik)):
        fynik[z] = round(inte_trap(1, z) * inte_trap(0, z) * 1, 4) # łapie wyniki

    gauss();


def approx(x, y):
    buffap = 0
    for xz in range(x, y):
        for ni in range(n):
            buffap += wektorki[ni]*(xz**ni)
        print(round(buffap, 7))
        buffap = 0



main()


approx(-1, 1)
