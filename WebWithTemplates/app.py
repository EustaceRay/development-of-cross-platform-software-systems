from flask import Flask, render_template, request
import io
import sys
import pasart  # Убедитесь, что pasart.py существует и корректно подключен

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run():
    # Получаем параметры от пользователя
    o = request.form.get('o')
    t = request.form.get('t')
    q = request.form.get('q')

    # Перенаправляем stdout в буфер
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()

    try:
        o = int(o)
        t = int(t)
        q = int(q)

        # Вызов соответствующей функции в зависимости от выбора пользователя
        if o == 1:
            pasart.pascal_triangle(t, q)
        elif o == 2:
            pasart.double_pascal_art(t, q)
        elif o == 3:
            pasart.four_corners_pascal_art(t, q)
    except Exception as e:
        buffer.write(f"Ошибка: {str(e)}")

    # Получаем результат из буфера и восстанавливаем stdout
    output = buffer.getvalue()
    sys.stdout = old_stdout

    # Возвращаем результат в шаблон
    return output

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
