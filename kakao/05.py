
import copy

def is_valid_remove(maps, req):

    copy_map = copy.deepcopy(maps)

    x = req[0]
    y = req[1]

    # remove [x, y]
    copy_map[x][y][req[2]] = 5

    # Near
    for i in range(3):
        for j in range(3):
            if x+i-1 == x and y+j-1 == y:
                None
            else:
                # Pic. (Not [x, y]0
                pic = copy_map[x+i-1][y+j-1]
                if pic[0] == 1:
                    copy_map[x+i-1][y+j-1][0] = 5

                    new_req = [x+i-1, y+j-1, 0, 1]
                    ret = is_valid(copy.deepcopy(copy_map), new_req)
                    if ret == False:
                        print('fail', new_req)
                        return False
                if pic[1] == 1:
                    copy_map[x+i-1][y+j-1][1] = 5

                    new_req = [x+i-1, y+j-1, 1, 1]
                    ret = is_valid(copy.deepcopy(copy_map), new_req)
                    if ret == False:
                        print('fail', new_req)
                        return False

    return True

def is_valid(maps, req):
    x = req[0]
    y = req[1]

    print(req)

    if req[3] == 0:
        ret = is_valid_remove(maps, req)
        if ret == True:
            return ret

    else:
        if req[2] == 1:
            # bow. -1F is Gi
            if maps[x][y-1][0] == 1 or maps[x+1][y-1][0] == 1:
                return True

            # bow. bow-bow-bow
            print('LST', maps[x-1])
            if maps[x-1][y][1] == 1 and maps[x+1][y][1] == 1:
                return True

        if req[2] == 0:
            # Gi

            # Gi. Floor
            if y == 0 :
                return True

            # Gi. -1F is Gi
            if maps[x][y-1][0] == 1:
                return True

            # Gi. -1F is Bow
            if maps[x-1][y][1] == 1 or maps[x][y][1] == 1:
                return True

    return False

def print_maps(maps):

    for i in maps:
        for j in i:
            print(j, end='')
        print()

def gen_maps(maps):
    
    ret = []
    l = len(maps)
    for i in range(l):
        for j in range(l):
            if maps[i][j][0] == 1:
                ret.append([i, j, 0])
            if maps[i][j][1] == 1:
                ret.append([i, j, 1])
    return ret

def solution(n, build_frame):

    maps = [[[5, 5] for i in range(n+1)] for j in range(n+1)]
    print_maps(maps)

    for i in build_frame:
        ret = is_valid(maps, i)
        print('ret', ret)
        if ret == True:
            if i[3] == 0:
                print('REMOVE', i[0], i[1])
                maps[i[0]][i[1]][i[2]] = 5
            else:
                if i[2] == 0:
                    maps[i[0]][i[1]][0] = 1
                if i[2] == 1:
                    maps[i[0]][i[1]][1] = 1
        print_maps(maps)
        print('-------')

    ret = gen_maps(maps)
    print(ret)


n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
solution(n, build_frame)

build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
solution(n, build_frame)


