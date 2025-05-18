from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

PORT = 3000

@app.route('/calculate', methods=['POST'])
def calculate_sum():
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({'error': 'Неверный формат JSON'}), 400

        # Проверка: тело должно быть словарем
    if not isinstance(data, dict):
        return jsonify({'error': 'Ожидается JSON-объект с числовыми значениями'}), 400

    total = 0

    for key, value in data.items():
        if not isinstance(value, (int, float)):
            return jsonify({'error': f'Значение "{key}" не является числом'}), 400
        total += value

    return jsonify({'sum': total})

if __name__ == '__main__':
    app.run(host='localhost', port=PORT, debug=True)