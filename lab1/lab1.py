Maciesz = [[-1, 2, 1],
           [1, -3, -2],
           [3, -1, -1]]

fynik = [-1,
         -1,
         4]



print("Czy chcesz użyć ustawień domyślnych?")
czy = input("Y - tak, lub N - nie")

if (czy == 'N'):
    tmp = tmp2 = 0
    tmp = int(input("Podaj rozmiar macierzy(n*n): "))
    tmp2 = tmp

    Maciesz = [[0] * (tmp) for i in range(tmp)]
    fynik = [0] * (len(Maciesz[0]))

    for arow in range(tmp):
        for acol in range(tmp2):
            print("Podaj wyraz ",arow+1, acol+1)
            tmp3 = int(input())
            # if (tmp3 != int):
            #     tmp3 = 0
            Maciesz[arow][acol] = tmp3

    print("Podaj wektor wyrazów wolnych.")

    for arow in range(tmp2):
            print("Podaj wyraz b",arow+1)
            tmp3 = int(input())
            # if (tmp3 != int):
            #     tmp3 = 0
            fynik[arow] = tmp3


wiktor = [0] * (len(Maciesz[0]))

print("Macierz podana: ")
for i in range(len(Maciesz)):
    print(Maciesz[i])

print("Wektor wyrazów wolnych: ")
for i in range(len(fynik)):
    print("|", fynik[i], "|")

#pusta macierz docelowa
# matrix = [[0]*(len(Maciesz)+1)]*(len(Maciesz[0])) --- zle
matrix = [[0] * (len(Maciesz)+1) for i in range(len(Maciesz[0]))]

print("Macierz docelowa: ")

for i in range(len(matrix)):
    print(matrix[i])


print("Pusty wektor wyrazów niewiadmoych: ")
for i in range(len(wiktor)):
    print("|", wiktor[i], "|")

#przepisanie macierzy

for row in range(len(Maciesz)):
    for col in range(len(Maciesz[0])):
        matrix[row][col] = Maciesz[row][col]

print("Przepisanie macierzy: ")

for i in range(len(matrix)):
    print(matrix[i])

#dopisanie wyniku

for row in range(len(Maciesz)):
    matrix[row][len(matrix)] = fynik[row]

print("Dopisanie wektoru wyrazów wolnych: ")

for i in range(len(matrix)):
    print(matrix[i])

try:
    print("Przeprowadzam eliminację metodą Gaussa: ")
    #for x in range(len(matrix)):
    x=0
    i=0

    for x in range(len(matrix)-1):
        for row in range(1 + x, len(matrix)):
            for col in range(x, len(matrix[0])):
                if(i == 0):
                    i = matrix[row][col]
                matrix[row][col] = int((matrix[row][col] - ((i / matrix[x][x])*matrix[x][col])))
            i = 0

    for i in range(len(matrix)):
        print(matrix[i])

    print("Obliczam wektor wyrazów niewiadomych: ")

    #wiktor[len(matrix)-1] = int(matrix[len(matrix)-1][len(matrix[0])-1]/matrix[len(matrix)-1][len(matrix[0])-2])


    for o in range(len(matrix)):
        buffor = (matrix[len(matrix) - 1 - o][len(matrix[0]) - 1])
        for z in range(len(matrix)-1):
            buffor += (-matrix[len(matrix)-1-o][len(matrix)-1-z]*wiktor[len(matrix)-1-z])
        wiktor[len(wiktor)-o-1] = int(buffor/matrix[len(matrix)-1-o][len(matrix)-1-o])
        buffor = 0


    for i in range(len(wiktor)):
        print("|", wiktor[i], "|")
except:
    print("Error 12: Brak rozwiązania")
#print(matrix)
#print(Maciesz)