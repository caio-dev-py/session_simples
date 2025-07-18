from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# registrando blueprints
from routes.home import home_route
from routes.form import form_route

app.register_blueprint(home_route)
app.register_blueprint(form_route, url_prefix='/login')

if __name__ == '__main__':
    app.run(debug=True)