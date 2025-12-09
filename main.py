from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
# --- Código de Inicio ---
if __name__ == '__main__':
    # Esto inicia el servidor de desarrollo
    # host='0.0.0.0' hace que sea accesible externamente (útil en Docker o VM)
    # debug=True activa el modo de depuración (recarga automática)
    app.run(host='0.0.0.0', port=5000, debug=True)