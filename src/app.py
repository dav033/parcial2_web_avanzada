from flask import Flask, request, jsonify, redirect, render_template

app = Flask(__name__)
# app.register_blueprint(ruta_cliente, url_prefix = "/api" )
# app.register_blueprint(ruta_prestamo, url_prefix = "/api" )

@app.route("/")
def index():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(debug=True, port=5001, host='0.0.0.0')