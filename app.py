from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/sumar', methods=['GET', 'POST'])
def sumar():
    if request.method == 'POST':
        data = request.get_json(silent=True) or {}
        a = data.get('a', None)
        b = data.get('b', None)
    else:  # GET
        a = request.args.get('a', type=float)
        b = request.args.get('b', type=float)

    # Normaliza a números si llegan como string
    try:
        a = float(a) if a is not None else None
        b = float(b) if b is not None else None
    except ValueError:
        return jsonify({'error': 'a y b deben ser numéricos'}), 400

    if a is None or b is None:
        return jsonify({'error': 'Parámetros a y b requeridos'}), 400

    return jsonify({'resultado': a + b})


@app.route('/api/info')
def info():
    return jsonify({
        'nombre': 'Microservicio Base - Tratamiento de Datos Paralelo A',
        'version': '1.0.0',
        'descripcion': 'Este microservicio realiza operaciones basicas de suma y proporciona informacion del servicio.',
        'autor': 'Jenny Alava'
    })
@app.route('/')
def home():
    return """
    <!doctype html>
    <html>
      <body style="font-family: system-ui; max-width: 480px; margin: 40px auto;">
        <h2>SUMAR</h2>
        <label>a: <input id="a" type="number" step="any" /></label>
        <label>b: <input id="b" type="number" step="any" /></label>
        <button onclick="sumar()">Calcular</button>
        <pre id="out" style="background:#f6f8fa;padding:12px;border-radius:8px;"></pre>
        <script>
          async function sumar() {
            const a = parseFloat(document.getElementById('a').value);
            const b = parseFloat(document.getElementById('b').value);
            const res = await fetch('/api/sumar', {
              method: 'POST',
              headers: {'Content-Type': 'application/json'},
              body: JSON.stringify({a, b})
            });
            document.getElementById('out').textContent = await res.text();
          }
        </script>
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
