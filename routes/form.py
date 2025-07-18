from flask import Blueprint, render_template, redirect, url_for, session, request
from forms import UsuarioForm

form_route = Blueprint('form', __name__)

@form_route.route('/', methods=['GET', 'POST'])
def login():
    form = UsuarioForm()

    if form.validate_on_submit():
        nome = form.nome.data
        session['usuario'] = nome
        
        usuario = session.get('usuario')
        if usuario:
            return render_template('logado.html', usuario = usuario)
    
    return render_template('login.html', form = form)

@form_route.route('/logout')
def logout():
    session.pop('usuario', None)
    return url_for('form.form')