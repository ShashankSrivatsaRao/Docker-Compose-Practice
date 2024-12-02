from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="db",  # Hostname matches the database service name in Docker Compose
        database="testdb",
        user="testuser",
        password="testpass"
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT 1;')
    result = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify({'message': 'Database connection successful!', 'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
