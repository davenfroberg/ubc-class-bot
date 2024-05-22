import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/building', methods=['GET'])
def building_info():
    buildingCode = request.args.get('code')

    if buildingCode is None:
        return jsonify({'error': 'Missing building code field'}), 400

    with open('buildings.json', 'r') as f:
        data = json.load(f)

    for building in data:
        if building['code'] == buildingCode:
            return jsonify(building)

    return jsonify({'error': 'Building not found'}), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
