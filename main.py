from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

PORT = 3000

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    # Получение параметров
    a = data.get('a')
    b = data.get('b')
    operation = data.get('operation')

    # Проверка наличия всех параметров
    if a is None or b is None or operation is None:
        return jsonify({'error': 'Параметры a, b и operation обязательны'}), 400

    # Выполнение операции
    try:
        if operation == 'add':
            result = a + b
        elif operation == 'sub':
            result = a - b
        elif operation == 'mul':
            result = a * b
        elif operation == 'div':
            if b == 0:
                return jsonify({'error': 'Деление на ноль'}), 400
            result = a / b
        else:
            return jsonify({'error': 'Недопустимая операция'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(host='localhost', port=PORT, debug=True)