import os
import sqlite3
from datetime import datetime, timedelta
from flask import Flask, render_template, request, g

app = Flask(__name__)
DATABASE = os.path.join(os.path.dirname(__file__), 'data', 'sensor_data.db')

def get_db():
    """
    Returns a database connection, stored in Flask's g object.
    Ensures only one connection per request context.
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row  # So we can access columns by name
    return db

@app.teardown_appcontext
def close_connection(exception):
    """
    Close the database connection at the end of each request.
    """
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Displays a page with:
    1) A dropdown of distinct dates
    2) Two line charts (temperature & humidity) for the selected date
    """
    conn = get_db()
    cursor = conn.cursor()

    # Get all distinct dates from readings
    cursor.execute("SELECT DISTINCT DATE(time) as reading_date FROM sensor_readings ORDER BY reading_date DESC")
    available_dates = [row['reading_date'] for row in cursor.fetchall()]

    # By default, use the first available date if none is selected
    selected_date = request.form.get('selected_date', available_dates[0] if available_dates else None)

    # Query data for the selected_date
    if selected_date:
        cursor.execute("""
            SELECT time, temp, humidity
            FROM sensor_readings
            WHERE DATE(time) = ?
            ORDER BY time
        """, (selected_date,))
        rows = cursor.fetchall()
    else:
        rows = []

    # Prepare lists for Chart.js (timestamps, temperatures, humidities)
    time_labels = [row['time'] for row in rows]
    temperatures = [row['temp'] for row in rows]
    humidities = [row['humidity'] for row in rows]

    return render_template(
        'index.html',
        available_dates=available_dates,
        selected_date=selected_date,
        time_labels=time_labels,
        temperatures=temperatures,
        humidities=humidities
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
