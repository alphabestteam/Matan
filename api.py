from flask import Flask, request, jsonify
import params
import mysql.connector


app = Flask(__name__)


def create_db_connection():
    connection = mysql.connector.connect(
        host=params.MYSQL_HOST,
        port=3306,
        user=params.MYSQL_USER,
        password=params.MYSQL_PASSWORD,
        database=params.MYSQL_DB,
    )
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {params.MYSQL_DB}")
    cursor.execute(f"USE {params.MYSQL_DB}")
    return connection


my_db = create_db_connection()
my_cursor = my_db.cursor()


def create_table_if_not_exists(cursor, db_name: str):
    cursor.execute(f"SHOW TABLES LIKE '{db_name}'")
    table_exists = cursor.fetchone()

    if not table_exists:
        cursor.execute(
            f"CREATE TABLE {db_name} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"
        )


@app.route("/<db>", methods=["POST"])
def add_data(db: str):
    create_table_if_not_exists(my_cursor, db)
    data = request.json

    if data:
        name = data.get("name")
        if name:
            query = f"INSERT INTO {db} (name) VALUES ('{name}')"
            my_cursor.execute(query)
            my_db.commit()
            inserted_id = my_cursor.lastrowid
            return (
                f"User {name} was successfully added to '{db}' db with id {inserted_id}"
            )
        else:
            return "No valid name supplied in the JSON"
    else:
        return "No valid JSON was supplied!"


@app.route("/<db>", methods=["GET"])
def get_data(db: str):
    query = f"SELECT * FROM {db}"
    my_cursor.execute(query)
    result = my_cursor.fetchall()
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
