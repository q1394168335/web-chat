from flask import session, redirect, url_for, render_template, request
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    if request.form.get('name') is not None:
        session['name'] = request.form['name']
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        return render_template('index.html')


@main.route('/chat')
def chat():
    """
    获取用户的姓名
    """
    name = session.get('name', '')
    if name == '':
        return redirect(url_for('.index'))
    return render_template('chat.html')
