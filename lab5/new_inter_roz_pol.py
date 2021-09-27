buffor = []

x = 1, 2, 3, 4
y = 3, 7, 8, 15
h = 0


def eq_dist():
    buff = x[1] - x[0]
    eq_dis_buff = []
    flag = 1
    for i in range(1, len(x)-1):
        z_buff = x[i+1] - x[i]
        eq_dis_buff[i-1] = z_buff - buff
        buff = z_buff
    for i_r in range(len(eq_dis_buff)-1):
        if eq_dis_buff[i_r] != eq_dis_buff[i_r+1]:
            flag = 0
    if flag == 1:
        return eq_dis_buff[10]
    else:
        return "error"


if eq_dist() != "error":
    h = eq_dist()


print("hello world")


