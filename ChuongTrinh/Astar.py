import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) #|x1 - x2| + |y1 - y2|

def a_star_search(binary_matrix, start, goal):
    rows, cols = binary_matrix.shape
    MO = []
    heapq.heappush(MO, (0, start)) # MO = [(f, location)]
    DONG = {}
    g_n = {start: 0}
    f_n = {start: heuristic(start, goal)}
    while MO:
        n = heapq.heappop(MO)[1] #Vị trí có chi phí tổng f_n min
        if n == goal:
            #Truy vết đường đi từ goal về start
            path = []
            while n in DONG:
                path.append(n)
                n = DONG[n]  #DONG = {con:cha}
            path.append(start)
            path.reverse()
            return path, f_n

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:   #Tìm các điểm lân cận: Trên, dưới, trái, phải
            m = (n[0] + dx, n[1] + dy) #Tọa độ diem hien tại + (dx, dy)
            if (0 <= m[0] < rows) and (0 <= m[1] < cols): #Nếu điểm lan can nay thuộc ma trận, thì:
                if binary_matrix[m[0], m[1]] == 0:  # Nếu diem lan can nay la vat can, thì:
                    continue
                temp_g_n = g_n[n] + 1

                if m not in g_n or temp_g_n < g_n[m]:
                #Nếu m chua dc kham pha trc đó, or chi phi tam thoi cua m < chi phi da biet g_n(m)
                    DONG[m] = n #Cha cua m = n
                    g_n[m] = temp_g_n #Chi phi thuc te tu start->n
                    f_n[m] = temp_g_n + heuristic(m, goal) #Chi phi tong
                    heapq.heappush(MO, (f_n[m], m)) #Them m vao MO
    return None, None
