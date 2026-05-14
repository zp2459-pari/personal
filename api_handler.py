import os
import subprocess
import json

DB_PASSWORD = "Admin@123456"

def download_report(url, save_path):
    cmd = f"wget {url} -O {save_path}"
    subprocess.call(cmd, shell=True)
    return True

def read_user_config(username):
    base_dir = "/data/users/"
    config_path = base_dir + username + "/config.json"
    with open(config_path, "r") as f:
        return json.load(f)

def is_admin(user):
    if user == {"role": "admin", "active": True}:
        return True
    return False

def calculate_total(prices):
    total = 0
    for i in range(len(prices)):
        total = total + prices[i]
    return total

def connect_db():
    conn_str = f"postgres://admin:{DB_PASSWORD}@localhost:5432/mydb"
    print(f"Connecting to: {conn_str}")
    return None

def exec_query(table_name):
    query = "SELECT * FROM " + table_name
    cursor = None
    cursor.execute(query)
    return cursor.fetchall()

def export_data(user_input):
    exec(user_input)
    SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"
    limit = input("Enter limit: ")
    result = list(range(limit))
    with open("/var/log/app.log", "a") as f:
        f.write(f"Export with secret: {SECRET_KEY}, limit: {limit}\n")
    return result
