#punkty opisujące
N = 4
#stopien
m = 2
n = m+1
#punkty zadane funkcji
xi = [1,2,3,4]
yi = [6,19,40,69]
#do gaussa
matrix = [[0] * (m+1) for i in range(m+1)]
fynik = [0] * (len(matrix))
wektorki = [0] * (len(matrix))

def set_var():
    global N, m, n, xi, yi, matrix, fynik, wektorki
    
    N = 4

    m = 3
    n = m+1

    xi = [-1, -0.5, 0, 0.5, 1]
    yi = [2.65,2,1.73,2, 2.65]

    matrix = [[0] * (m+1) for i in range(m+1)]
    fynik = [0] * (len(matrix))
    wektorki = [0] * (len(matrix))


def gauss():
    x=0
    i=0
   


    for i in range(n-1):
        for row in range(1+i, n):
            fraction = matrix[row][i] / matrix[i][i]
            fynik[row] -= fraction*fynik[i]
            for col in range(n):
                matrix[row][col] -= fraction * matrix[i][col]


    
    wektorki[n-1] = round(fynik[n-1]/matrix[n-1][n-1], 3)

    for i in range(n-2, -1, -1):
        x = fynik[i]
        for j in range (n-1, -1, -1):
            x -= matrix[i][j] * wektorki[j]

        wektorki[i] = round(x/matrix[i][i], 3)


    for i in range(len(matrix)):
        print(matrix[i])
    
    print("Szukane wektory: ")

    for i in range(len(wektorki)):
        print("|", wektorki[i], "|")


def S(k, j):
    buff = 0
    for i in range(n):
        buff += xi[i]**(k+j)
    return buff

def T(k):
    buff = 0
    for i in range(n):
        buff += xi[i]**k*yi[i]
    return buff
###
def Wiel_Approx(x_zadany):
    buff = 0 
    for mi in range(len(wektorki)):
        buff += wektorki[mi]*x_zadany**(mi)
    return buff


def NMK(x_zadany):
    set_var()

    for k in range(len(matrix[0])):
        for j in range(len(matrix[0])):
            matrix[k][j] = S(k, j)

    for k in range(len(fynik)):
        fynik[k] = T(k)

    gauss()

    print("W(", x_zadany, ") =")
    print(Wiel_Approx(x_zadany))




#NMK(5)
print("1.8027869529665")