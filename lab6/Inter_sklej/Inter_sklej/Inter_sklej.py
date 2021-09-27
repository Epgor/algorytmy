eps = 1e-12

#x = [1, 3, 5, 7]
x = [-4, -2, 0, 2, 4]

#y = [1, 8, 9, 17]
y = [-734, -66, 2, -2, -318]


x_zadany = 1

#pochx1 = 1
pochx_4 = 668
#pochx7 = 1
pochx4 = -372

Maciesz = [[0] * (len(x)+3) for i in range(len(x)+2)]
fynik = [0] * (len(Maciesz))
wiktor = [0] * (len(Maciesz))

matrix = [[0] * (len(Maciesz)) for i in range(len(Maciesz[0])-1)]
n = len(matrix)
wektorki = [0]*n


def dop_wyn():
    for fyn in range(len(y)):
        fynik[fyn] = y[fyn]
    
    fynik[5] = 668
    fynik[6] = -372

    for row in range(len(Maciesz)):
        Maciesz[row][len(Maciesz)] = fynik[row]


for wi in range(len(x)):
    wiktor[wi] = y[wi]


def w3(xz):
    for xi in range(len(x)):
        Maciesz[xz][xi] = (1*(x[xz]**xi))


def niew_alfa(xx):
    for xy in range(1, xx):
        buffor =  1*((x[xx] - x[xy])**3)
        if(xy > 2):
            pass
        else:
            if buffor == 0:
                pass
            else:
                Maciesz[xx][len(x)+xy-1] = buffor


def w2():
    for xi in range(len(x)-1):
        Maciesz[len(x)][xi+1] = ((1+xi)*(x[0]**xi))


def wezel_ost():
    for xd in range(1, len(x)):
        Maciesz[len(Maciesz)-1][xd] = ((xd)*(x[4]**(xd-1)))
    for xe in range(2):
        buffor =  x[1]*((x[4] - x[xe+1])**2)
        if buffor == 0:
           pass
        else:
           Maciesz[len(Maciesz)-1][len(Maciesz[0])-3+xe] = buffor
         


def inter_sklej():
    for xi in range(len(x)):
        w3(xi)
        niew_alfa(xi)
        w2()
        wezel_ost()

inter_sklej()

dop_wyn()

for i in range(len(Maciesz)):
    print(Maciesz[i])

def gauss():
    x=0
    i=0
   
 

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            matrix[row][col] = Maciesz[row][col]
    for i in range(len(matrix)):
        print(matrix[i])
   # for x in range(len(Maciesz)-1):
      #  for row in range(1 + x, len(Maciesz)):
         #   for col in range(x, len(Maciesz[0])):
            #    if(i == 0):
             #       i = Maciesz[row][col]
              #  Maciesz[row][col] = ((Maciesz[row][col] - ((i / Maciesz[x][x])*Maciesz[x][col])))
          #  i = 0

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



gauss()


def oblicz_wielomian(zex):
    flag = 0
    buffor = wektorki[0]
    mult = 0
    for xen in range(len(x)):
        if zex > x[xen]:
           flag += 1
        else:
           pass
    print(flag)
    if flag == 0:
        return ("Brak rozwiazan")
    elif flag == 1:
        for xi in range(1, len(wektorki)-2):
            mult +=1
            buffor += wektorki[xi]*zex**mult
            print("wektorki * mult", wektorki[xi]*zex**mult)
            
    elif flag == 2:
        for xi in range(1, len(wektorki)-2):
            mult +=1
            buffor += wektorki[xi]*zex**mult
            print("wektorki * mult", wektorki[xi]*zex**mult)
            
        buffor += wektorki[zex-2]*(zex-x[1])**mult
    elif flag >= 3:
        for xi in range(1, len(wektorki)-2):
            mult +=1
            buffor += wektorki[xi]*zex**mult
            print("wektorki * mult", wektorki[xi]*zex**mult)
            
        buffor += wektorki[zex-2]*(zex-x[1])**mult
        buffor += wektorki[zex-1]*(zex-x[2])**mult
        print("wektorki * mult zex1", wektorki[zex-2]*(zex-x[1])**mult)
        print("wektorki * mult zex2", wektorki[zex-1]*(zex-x[2])**mult)
    else:
        buffor = "Error"

    print("Wynik to: ")
    return (buffor)


print(oblicz_wielomian(x_zadany))

