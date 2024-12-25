from PIL import Image
import numpy as np

def load_image(image_path):
    #Mở hình ảnh và chuyển sang grayscale
    image = Image.open(image_path)
    image = image.convert('L')
    return image

def convert_to_matrix(image, threshold=128):
    #Chuyển hình ảnh grayscale thành ma trận nhị phân
    image_matrix = np.array(image)
    binary_matrix = (image_matrix >= threshold).astype(int)
    #1: Các ô có thể đi qua
    #0: Vật cản, ko thể đi qua
    return binary_matrix
