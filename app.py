from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Absolute path for DB file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'medicines.db')

# Ensure DB and table exists
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS medicines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                expiry TEXT,
                quantity TEXT,
                city TEXT,
                donor TEXT,
                mobile TEXT
            )
        ''')
        conn.commit()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        name = request.form.get('name')
        expiry = request.form.get('expiry')
        quantity = request.form.get('quantity')
        city = request.form.get('city')
        donor = request.form.get('donor')
        mobile = request.form.get('mobile')

        if not all([name, expiry, quantity, city, donor, mobile]):
            return "Please fill all fields!", 400

        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            c.execute('''
                INSERT INTO medicines (name, expiry, quantity, city, donor, mobile)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, expiry, quantity, city, donor, mobile))
            conn.commit()

        return redirect(url_for('view_medicines'))

    return render_template('donate.html')

@app.route('/view')
def view_medicines():
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute('SELECT * FROM medicines')
        rows = c.fetchall()
    return render_template('view.html', medicines=rows)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
