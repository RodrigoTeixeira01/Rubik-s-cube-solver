import random

cubo = [i // 8 for i in range(48)]
buffer = ""

def mov(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23,
        a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45,
        a46, a47):
    global cubo
    cubo = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22,
            a23, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, a36, a37, a38, a39, a40, a41, a42, a43,
            a44, a45, a46, a47]
def printe(text):
    global buffer
    buffer += str(text)

def cubop():
    global cubo
    for a in cubo:
        print(a, end=" ")
    print("")


def u():
    global cubo
    mov(cubo[6], cubo[7], cubo[0], cubo[1], cubo[2], cubo[3], cubo[4], cubo[5], cubo[16], cubo[17], cubo[18], cubo[11],
        cubo[12], cubo[13], cubo[14], cubo[15], cubo[24], cubo[25], cubo[26], cubo[19], cubo[20], cubo[21], cubo[22],
        cubo[23], cubo[32], cubo[33], cubo[34], cubo[27], cubo[28], cubo[29], cubo[30], cubo[31], cubo[8], cubo[9],
        cubo[10], cubo[35], cubo[36], cubo[37], cubo[38], cubo[39], cubo[40], cubo[41], cubo[42], cubo[43], cubo[44],
        cubo[45], cubo[46], cubo[47])


def l():
    global cubo
    mov(cubo[36], cubo[1], cubo[2], cubo[3], cubo[4], cubo[5], cubo[34], cubo[35], cubo[14], cubo[15], cubo[8], cubo[9],
        cubo[10], cubo[11], cubo[12], cubo[13], cubo[0], cubo[17], cubo[18], cubo[19], cubo[20], cubo[21], cubo[6],
        cubo[7], cubo[24], cubo[25], cubo[26], cubo[27], cubo[28], cubo[29], cubo[30], cubo[31], cubo[32], cubo[33],
        cubo[46], cubo[47], cubo[40], cubo[37], cubo[38], cubo[39], cubo[16], cubo[41], cubo[42], cubo[43], cubo[44],
        cubo[45], cubo[22], cubo[23])


def r():
    global cubo
    mov(cubo[0], cubo[1], cubo[18], cubo[19], cubo[20], cubo[5], cubo[6], cubo[7], cubo[8], cubo[9], cubo[10], cubo[11],
        cubo[12], cubo[13], cubo[14], cubo[15], cubo[16], cubo[17], cubo[42], cubo[43], cubo[44], cubo[21], cubo[22],
        cubo[23], cubo[30], cubo[31], cubo[24], cubo[25], cubo[26], cubo[27], cubo[28], cubo[29], cubo[4], cubo[33],
        cubo[34], cubo[35], cubo[36], cubo[37], cubo[2], cubo[3], cubo[40], cubo[41], cubo[38], cubo[39], cubo[32],
        cubo[45], cubo[46], cubo[47])


def d():
    global cubo
    mov(cubo[0], cubo[1], cubo[2], cubo[3], cubo[4], cubo[5], cubo[6], cubo[7], cubo[8], cubo[9], cubo[10], cubo[11],
        cubo[36], cubo[37], cubo[38], cubo[15], cubo[16], cubo[17], cubo[18], cubo[19], cubo[12], cubo[13], cubo[14],
        cubo[23], cubo[24], cubo[25], cubo[26], cubo[27], cubo[20], cubo[21], cubo[22], cubo[31], cubo[32], cubo[33],
        cubo[34], cubo[35], cubo[28], cubo[29], cubo[30], cubo[39], cubo[46], cubo[47], cubo[40], cubo[41], cubo[42],
        cubo[43], cubo[44], cubo[45])


def f():
    global cubo
    mov(cubo[0], cubo[1], cubo[2], cubo[3], cubo[10], cubo[11], cubo[12], cubo[7], cubo[8], cubo[9], cubo[40], cubo[41],
        cubo[42], cubo[13], cubo[14], cubo[15], cubo[22], cubo[23], cubo[16], cubo[17], cubo[18], cubo[19], cubo[20],
        cubo[21], cubo[6], cubo[25], cubo[26], cubo[27], cubo[28], cubo[29], cubo[4], cubo[5], cubo[32], cubo[33],
        cubo[34], cubo[35], cubo[36], cubo[37], cubo[38], cubo[39], cubo[30], cubo[31], cubo[24], cubo[43], cubo[44],
        cubo[45], cubo[46], cubo[47])


def b():
    mov(cubo[26], cubo[27], cubo[28], cubo[3], cubo[4], cubo[5], cubo[6], cubo[7], cubo[2], cubo[9], cubo[10], cubo[11],
        cubo[12], cubo[13], cubo[0], cubo[1], cubo[16], cubo[17], cubo[18], cubo[19], cubo[20], cubo[21], cubo[22],
        cubo[23], cubo[24], cubo[25], cubo[44], cubo[45], cubo[46], cubo[29], cubo[30], cubo[31], cubo[38], cubo[39],
        cubo[32], cubo[33], cubo[34], cubo[35], cubo[36], cubo[37], cubo[40], cubo[41], cubo[42], cubo[43], cubo[14],
        cubo[15], cubo[8], cubo[47])


def move(m):
    {"U":u,
     "L":l,
     "F":f,
     "R":r,
     "B":b,
     "D":d}[m]()



def exec_alg(alg: str) -> None:
    global letters
    for letter in alg:
        move(letter)
    printe(alg.replace(" ", ""))

def brute_force(cond, accepted_moves="ULFRBD", depth=None):
    global buffer
    if depth == None:
        depth = 0
        while ...:
            if brute_force(cond, accepted_moves, depth):
                print(buffer,"at",cond)
                return
            print(f"depth: {depth}")
            depth += 1
    if depth == 0:
        return cond()
    for move in accepted_moves:
        #print(f"trying {move} at depth {depth}.")
        exec_alg(move)
        if brute_force(cond, accepted_moves, depth-1):
            return True
        exec_alg(move*2)
        if brute_force(cond, accepted_moves, depth-1):
            return True
        exec_alg(move)
        buffer = buffer[:-4]
    return False
def is_eo():
    global cubo
    for i in (1, 3, 5, 7, 19, 23, 35, 39, 41, 43, 45, 47):
        if cubo[i] in (1, 3):
            return False
    for i in (9, 11, 13, 15, 17, 21, 25, 27, 29, 31, 33, 37):
        if cubo[i] in (0, 5):
            return False
    return True

def is_g1():
    global cubo
    for i in (0,1,2,3,4,5,6,7,40,41,42,43,44,45,46,47):
        if cubo[i] != 0 and cubo[i] != 5:
            return False
    for i in (11,15,27,31):
        if cubo[i] != 1 and cubo[i] != 3:
            return False
    for i in (19,23,35,39):
        if cubo[i] != 2 and cubo[i] != 4:
            return False
    return True

def is_lb_and_lf_e_slice():
    global cubo
    return cubo[23] in (1, 2, 3, 4) and cubo[35] in (1, 2, 3, 4) and is_eo()


def is_rb_and_rf_e_slice():
    global cubo
    return cubo[19] in (1, 2, 3, 4) and cubo[39] in (1, 2, 3, 4) and is_lb_and_lf_e_slice() and is_eo()


def count_u_layer_oriented_corner_pieces():
    count = 0
    for i in (0, 2, 4, 6):
        if cubo[i] in (0, 5):
            count += 1
    return count


# yellow top
# green front

if False:
    for i in range(20):
        choice = "ULFRBD"[random.randrange(0, 6)]
        print(choice, end=" ")
        move(choice)
else:
    i = 0
    for n in input(""):
        cubo[i] = int(n)
        i += 1
print()
print()


def is_df_white():
    global cubo
    return cubo[41] == 5

def is_line_solved():
    global cubo
    return cubo[41]==5 and cubo[45]==5 and cubo[21]==2 and cubo[37]==4

def sticker_solved(n):
    global cubo
    return cubo[n]==n>>3

def all_solved(*n):
    for i in n:
        if not sticker_solved(i):
            return False
    return True

def is_dl_solved():
    return all_solved(13,47)

def is_first_pair_solved():
    return all_solved(13,47,14,15,46,35,36)

def is_left_half_solved():
    return all_solved(11,12,13,14,15,22,23,35,36,40,46,47)

def is_f2l_minus_1_solved():
    return all_solved(27,28,29,38,39,43,44)

def is_f2l_solved():
    return all_solved(27,28,29,38,39,43,44,19,20,30,31,42)

def is_oll():
    return all_solved(0,1,2,3,4,5,6,7,27,28,29,38,39,43,44,19,20,30,31,42)

def is_cube_solved():
    return all_solved(*range(48))

def solve():
    global buffer, cubo
    buffer = ""
    # EO:
    brute_force(is_eo)
    # rest maybe
    brute_force(is_line_solved,"ULRD")
    brute_force(is_dl_solved, "ULR")
    brute_force(is_first_pair_solved, "ULR")
    brute_force(is_left_half_solved, "ULR")
    brute_force(is_f2l_minus_1_solved, "UR")
    brute_force(is_f2l_solved, "UR")
    while ...:
        count = count_u_layer_oriented_corner_pieces()
        print("count:",count)
        if count == 0:
            while cubo[8] != 0 or cubo[10] != 0:
                exec_alg("U")
                print("AUFing")
            if cubo[18] == 0:
                exec_alg("RUURRUUURRUUURRUUR")
                break
        elif count == 1:
            while cubo[6] != 0:
                exec_alg("U")
                print("AUFing")
            if cubo[8] == 0:
                exec_alg("LUULLLUUULUUULLL")
                break
        elif count == 2:
            while cubo[0] != 0:
                exec_alg("U")
                print("AUFing")
            if cubo[4] == 0:
                while cubo[16] != 0:
                    exec_alg("U")
                    print("AUFing")
                exec_alg("RRRFRBBBRRRFFFRB")
            else:
                if cubo[6] == 0:
                    exec_alg("U")
                    print("AUFing")
                exec_alg("FFFLLLBLFLLLBBBL" if cubo[10] == 0 else "RRDRRRUURDDDRRRUURRR")
            break
        elif count == 3:
            print("CORNER TWIST DETECTED")
            exit(1)
        else:
            break
        exec_alg("RURRRURUURRR")
    while cubo[8] != cubo[10] or cubo[16] != cubo[18]:
        for i in range(4):
            if cubo[32] == cubo[34]:
                break
            exec_alg("U")
        exec_alg("RRRFRRRBBRFFFRRRBBRR")
    while cubo[8] != cubo[9] or cubo[16] != cubo[17]:
        for i in range(4):
            if cubo[32] == cubo[33]:
                break
            exec_alg("U")
        exec_alg("FF")
        while cubo[17] != cubo[20]:
            exec_alg("U")
        exec_alg("LRRRFFLLLR")
        while cubo[5] != 5:
            exec_alg("U")
        exec_alg("FF")
    while cubo[8] != cubo[11]:
        exec_alg("U")
def improve_obvious(arg: str) -> str:
    buffer = arg
    cont = True
    while cont:
        cont = False
        for i in ["BF", "RL", "DU"]:
            if i in buffer:
                buffer = buffer.replace(i, i[::-1])
                cont = True
    for letter in "ULFRBD":
        buffer = buffer.replace(letter, letter+" ")

    cont = True
    while cont:
        cont = False
        for letter in "ULFRBD":
            if (letter+" ")*4 in buffer:
                buffer = buffer.replace((letter+" ")*4, "")
                cont = True
        if "R U R R R U U U " * 6 in buffer:
            buffer = buffer.replace("R U R R R U U U " * 6, "")
            cont = True
        if "R U R R R U U U " * 5 in buffer:
            buffer = buffer.replace("R U R R R U U U " * 5, "U R U U U R R R ")
            cont = True
        if "R U R R R U U U " * 4 in buffer:
            buffer = buffer.replace("R U R R R U U U " * 4, "U R U U U R R R " * 2)
            cont = True
    cont = True
    while cont:
        cont = False
        for letter in "ULFRBD":
            if (letter+" ")*3 in buffer:
                buffer = buffer.replace((letter+" ")*3, letter+"' ")
                cont = True
            if (letter+" ")*2 in buffer:
                buffer = buffer.replace((letter+" ")*2, letter+"2 ")
                cont = True
    return buffer
solve()

print("buffer:", buffer)

solution = improve_obvious(buffer)

print(solution)
print(f"\n\nDONE IN {solution.count(' ')} moves\n")
#cubop()
