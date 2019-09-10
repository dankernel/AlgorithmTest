import copy

def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

def is_open(maps, start, end):

    for i in range(start, end):
        for j in range(start, end):
            if maps[i][j] != 1:
                return False
        print()

    return True

def overmap(big_lock, key, i, j):

    for ii in range(len(key)):
        for jj in range(len(key)):
            big_lock[i + ii][j + jj] += key[ii][jj]

    return big_lock

def print_map(maps):
    # Debug..
    for i in maps:
        for j in i:
            print(format(j, "2d"), end='')
        print()

def solution(key, lock):

    temp_size = len(lock) + ((len(key) - 1) * 2)

    # Init new BIG lock
    big_lock = [[0] * temp_size for i in range(temp_size)]
    
    # Copy to lock to BIG lock
    for i in range(len(lock)):
        for j in range(len(lock)):
            big_lock[i + len(key) - 1][j + len(key) - 1] = lock[i][j]

    ll = len(big_lock) - len(key) + 1
    for r in range(4):
        for i in range(ll):
            for j in range(ll):
                ret = overmap(copy.deepcopy(big_lock), key, i, j)

                """
                print(r, i, j)
                print_map(ret)
                """
                ret = is_open(ret, len(key)-1, len(big_lock) - len(key) + 1)
                if ret == True:
                    return True
                print()
        key = rotate_90(key)

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
ret = solution(key, lock)
print(ret)
