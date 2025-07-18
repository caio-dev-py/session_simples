from flask import Blueprint, render_template, session

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    usuario = session.get('usuario')
    if usuario:
        return render_template('logado.html', usuario = usuario)
    return render_template('nao_logado.html')