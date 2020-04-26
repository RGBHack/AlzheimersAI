import os
import time
from flask import Flask, render_template, make_response, flash, redirect, request, url_for, send_from_directory
from werkzeug.utils import secure_filename
from pathlib import Path
import ai

upP = "./templates/usr_data/"
pkl_file = "./pkl_file"

ALLOWED_EXTENSIONS = {"jpg"}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)

app.config['SECRET_KEY'] = '7dd0ad7c011a27198393149305d6dd8c'

def format_server_time():
    server_time = time.localtime()
    return time.strftime("%I:%M:%S %p", server_time)

@app.route('/')
def render_static_index():
    context = {'server_time': format_server_time()}
    return render_template('home.html', context=context)

@app.route('/about')
def render_static_about():
    context = {'server_time': format_server_time()}
    return render_template('about.html', context=context)

@app.route('/login')
def render_static_login():
    context = {'server_time': format_server_time()}
    return render_template('login.html', context=context)

@app.route('/static/assets/usr/<filename>')
def uploaded_file(filename):
    return send_from_directory(upP, filename)

@app.route('/neuralz', methods=["POST", "GET"])
def render_static_product():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part in POST')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            actual_file_path = os.path.join(upP, filename)
            file.save(os.path.join(upP, filename))
            aiout = ai.test(actual_file_path, pkl_file)
            return render_template('product.html', aiout=aiout)
    return render_template('product.html')

@app.route('/aiout')
def render_static_aiout(actual_file_path):
    return ai.test(actual_file_path, pkl_file)

@app.route('/signup')
def render_static_signup():
    context = {'server_time': format_server_time()}
    return render_template('signup.html', context=context)

@app.route('/quiz')
def render_static_quiz():
    context = {'server_time': format_server_time()}
    return render_template('quiz.html', context=context)

@app.route('/password')
def render_static_password():
    context = {'server_time': format_server_time()}
    return render_template('password.html', context=context)

@app.route('/stats')
def render_stats():
    context = {'server_time': format_server_time()}
    return render_template('stats.html', context=context)

@app.route('/profile')
def profile():
    context = {'server_time': format_server_time()}
    return render_template('profile.html', context=context)

@app.route('/signout')
def logout():
    context = {'server_time': format_server_time()}
    return render_template('logout.html', context=context)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=int(os.environ.get('PORT', 5003)))