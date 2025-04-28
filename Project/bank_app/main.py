from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'bank_secret_key'
USER_DIR = 'users'

os.makedirs(USER_DIR, exist_ok=True)

def get_user_path(username):
    return os.path.join(USER_DIR, f"{username}.txt")

def read_user(username):
    try:
        with open(get_user_path(username), 'r') as f:
            lines = f.read().splitlines()
            return {'password': lines[0], 'balance': float(lines[1])}
    except:
        return None

def write_user(username, password, balance):
    with open(get_user_path(username), 'w') as f:
        f.write(f"{password}\n{balance}")

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if os.path.exists(get_user_path(username)):
            return "User already exists!"
        write_user(username, password, 0.0)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = read_user(username)
        if user and user['password'] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        return "Invalid credentials!"
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    user = read_user(session['username'])
    return render_template('dashboard.html', username=session['username'], balance=user['balance'])

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        amount = float(request.form['amount'])
        user = read_user(session['username'])
        user['balance'] += amount
        write_user(session['username'], user['password'], user['balance'])
        return redirect(url_for('dashboard'))
    return render_template('deposit.html')

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        amount = float(request.form['amount'])
        user = read_user(session['username'])
        if amount > user['balance']:
            return "Insufficient balance!"
        user['balance'] -= amount
        write_user(session['username'], user['password'], user['balance'])
        return redirect(url_for('dashboard'))
    return render_template('withdraw.html')

@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        to_user = request.form['to_user']
        amount = float(request.form['amount'])
        from_user = read_user(session['username'])
        to_user_data = read_user(to_user)
        if not to_user_data:
            return "Recipient does not exist!"
        if amount > from_user['balance']:
            return "Insufficient balance!"
        from_user['balance'] -= amount
        to_user_data['balance'] += amount
        write_user(session['username'], from_user['password'], from_user['balance'])
        write_user(to_user, to_user_data['password'], to_user_data['balance'])
        return redirect(url_for('dashboard'))
    return render_template('transfer.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
