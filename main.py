from calculator import pix_coord_calculator
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/api', methods=['POST'])
def calculate():
    data = request.get_json(force=True)
    dim = data['dimension']
    corner_points = data['corner points']
    solution = pix_coord_calculator(dim, corner_points)
    return jsonify(solution)


if __name__ == '__main__':
    app.run(port=9000, debug=True)
