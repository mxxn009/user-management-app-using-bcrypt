from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

users = {}
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reg-success')
def reg_success():
    username = request.args.get('username')
    message = f"{username} registered successfully"
    return render_template('reg_success.html', message=message)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users:
            return "User already exists!", 400

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        users[username] = hashed_password
        return redirect(url_for('reg_success', username=username))

    return render_template('register.html')



@app.route('/success')
def success():
    username = request.args.get('username')
    message = f"{username} signed in successfully"
    return render_template('success.html', message=message)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        hashed_password = users.get(username)
        if not hashed_password or not bcrypt.check_password_hash(hashed_password, password):
            return "Invalid username or password!", 400
        return redirect(url_for('success', username=username))

        return redirect(url_for('home'))

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
