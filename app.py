from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import base64
import utils.sudoku_extractor as extractor
from utils.solver import solve_sudoku

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json['image']
    img_data = base64.b64decode(data.split(',')[1])
    nparr = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    try:
        board = extractor.extract_sudoku(img)
        solved = solve_sudoku(board.copy())
        return jsonify({"solved": solved.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
