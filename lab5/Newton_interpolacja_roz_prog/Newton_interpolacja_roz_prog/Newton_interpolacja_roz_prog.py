import math

buffor = []
Buffor = 0

#x = [1, 2, 3, 4]
x = [-4, -2, 0, 2, 4]
#y = [3, 7, 8, 15]
y = [-734, -66, 2, -2, -318]

#x_zadany = 2.5
x_zadany = 1

h = 0
eq_dis_buff = [0] * (len(x))
prog_roz_matrix = [[0] * (len(x)) for i in range(len(x)-1)]


def eq_dist():
    flag = 1
    for i in range(len(x)-1):
        eq_dis_buff[i] = x[i+1] - x[i]
    for i_r in range(len(eq_dis_buff)-2):
        if eq_dis_buff[i_r] != eq_dis_buff[i_r+1]:
            flag = 0
    if flag == 1:
        return eq_dis_buff[1]
    else:
        return "error"


def roz_prog():
	for xi in range(len(prog_roz_matrix[0])-1):
		prog_roz_matrix[xi][0] = y[xi+1] - y[xi]
		print(prog_roz_matrix[xi][0])
	for xz in range(1, len(prog_roz_matrix[0])):
		for xr in range(len(prog_roz_matrix[0])-xz-1):
			prog_roz_matrix[xr][xz] = prog_roz_matrix[xr+1][xz-1] - prog_roz_matrix[xr][xz-1]



if eq_dist() != "error":
    h = eq_dist()
else:
	print("Nieregularny dystans - wynik powinien być błędny")

roz_prog()

for i in range(len(prog_roz_matrix)):
    print(prog_roz_matrix[i])


def wspol_b(st):
    bufi = 1
    for xi in range(st+1):
        bufi *= (x_zadany-x[xi])
       # print("x-x", (x_zadany-x[xi]))
    return bufi


def wspol_a(st):
	return prog_roz_matrix[0][st]/((math.factorial(st+1))*(pow(h, (st+1))))


def w_od_x():
    Buffor = y[0] # a było x[0] xDDD
    for i in range(len(x)-1):
        print("wspol a", wspol_a(i))
        print("wspol b", wspol_b(i))
        Buffor += wspol_a(i)*wspol_b(i)
    return Buffor



print("Wynik to: ")
print(w_od_x())

