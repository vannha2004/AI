import matplotlib.pyplot as plt
from Image_Processing import load_image, convert_to_matrix
from Astar import a_star_search, heuristic


def onclick(event, location):
    if event.xdata and event.ydata:
        location.append((int(event.ydata), int(event.xdata)))
        plt.plot(event.xdata, event.ydata, 'go' if len(location) == 1 else 'ro')
        plt.draw()

def select_points(binary_matrix):
    #Chọn điểm bắt đầu, đích
    coords = []
    plt.imshow(binary_matrix, cmap='gray')
    plt.gcf().canvas.mpl_connect('button_press_event', lambda event: onclick(event, coords))
    plt.show()
    return coords


def display_result(binary_matrix, path):
    #Vẽ đường đi trong ma trận
    plt.imshow(binary_matrix, cmap='gray')
    if path:
        plt.plot(*zip(*[(y, x) for x, y in path]), color='blue', linewidth=2)
    plt.show()

matrix = convert_to_matrix(load_image('D:/AI/map4.png'))
points = select_points(matrix)

if len(points) == 2:
    start, goal = points
    if matrix[start[0], start[1]] == 1 and matrix[goal[0], goal[1]] == 1:
        path, f_n = a_star_search(matrix, start, goal)
        display_result(matrix, path) if path else print("Không tìm thấy đường đi.")
        if f_n is not None:
            print("Tông chi phí: ", f_n[goal])
    else:
        print("Lỗi khi chọn điểm")
