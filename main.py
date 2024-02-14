from flask import Flask, url_for, render_template
from routes.home import home_route
from routes.cliente import cliente_route

# Inicializacao
app = Flask(__name__)

# rotas
app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix='/clientes')


app.run(debug=True)