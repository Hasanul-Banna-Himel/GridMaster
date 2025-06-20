import cv2
import numpy as np
import easyocr

reader = easyocr.Reader(['en'])

def extract_sudoku(image):
    # You should: find largest square contour, warp it, divide into 81 cells

    # For simplicity, assume image is already the Sudoku area
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cells = []
    h, w = gray.shape
    cell_h, cell_w = h // 9, w // 9

    for y in range(9):
        row = []
        for x in range(9):
            cell = gray[y*cell_h:(y+1)*cell_h, x*cell_w:(x+1)*cell_w]
            cell = cv2.resize(cell, (28, 28))
            result = reader.readtext(cell, detail=0)
            try:
                num = int(result[0]) if result else 0
            except:
                num = 0
            row.append(num)
        cells.append(row)

    return np.array(cells)
