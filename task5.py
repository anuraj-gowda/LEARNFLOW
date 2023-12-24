[20:42, 24/12/2023] MEGHANA G: pip install Flask
[20:43, 24/12/2023] MEGHANA G: pip install shortuuid
[20:43, 24/12/2023] MEGHANA G: from flask import Flask, request, redirect, render_template
import sqlite3
import shortuuid

app = Flask(_name_)

# Initialize the database
conn = sqlite3.connect('url_shortener.db')
conn.execute('CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY, short_url TEXT, long_url TEXT)')
conn.close()

def generate_short_url():
    return shortuuid.ShortUUID().random(length=6)

def save_url_mapping(short_url, long_url):
    conn = sqlite3.connect('url_shortener.db')
    conn.execute('INSERT INTO urls (short_url, long_url) VALUES (?, ?)', (short_url, long_url))
    conn.commit()
    conn.close()

def get_long_url(short_url):
    conn = sqlite3.connect('url_shortener.db')
    cursor = conn.cursor()
    cursor.execute('SELECT long_url FROM urls WHERE short_url = ?', (short_url,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form.get('long_url')
    if not long_url.startswith(('http://', 'https://')):
        long_url = 'http://' + long_url

    short_url = generate_short_url()
    save_url_mapping(short_url, long_url)

    return render_template('result.html', short_url=request.url_root + short_url)

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = get_long_url(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return render_template('not_found.html'), 404

if _name_ == '_main_':
    app.run(debug=True)