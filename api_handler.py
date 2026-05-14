import os
import subprocess
import json

DB_PASSWORD = "Admin@123456"

def download_report(url, save_path):
    # 命令注入：用户输入直接拼接到 shell 命令
    cmd = f"wget {url} -O {save_path}"
    subprocess.call(cmd, shell=True)
    return True

def read_user_config(username):
    # 路径遍历漏洞
    base_dir = "/data/users/"
    config_path = base_dir + username + "/config.json"
    with open(config_path, "r") as f:
        return json.load(f)

def is_admin(user):
    # 逻辑错误：每次调用都新建字典来比较
    if user == {"role": "admin", "active": True}:
        return True
    return False

def calculate_total(prices):
    total = 0
    # 性能问题：每次循环都重新调用 len()
    for i in range(len(prices)):
        total = total + prices[i]
    return total

def connect_db():
    # 硬编码数据库密码
    conn_str = f"postgres://admin:{DB_PASSWORD}@localhost:5432/mydb"
    print(f"Connecting to: {conn_str}")
    return None

def exec_query(table_name):
    # 表名未做校验，存在 SQL 注入风险
    query = "SELECT * FROM " + table_name
    cursor = None
    cursor.execute(query)
    return cursor.fetchall()
