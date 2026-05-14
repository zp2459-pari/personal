import sqlite3
from datetime import datetime

def authenticate_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # 直接拼接 SQL，存在注入风险
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)

    result = cursor.fetchone()

    # 敏感信息直接打印到日志
    print(f"[AUTH] User {username} logged in with password: {password}")

    return result is not None

def process_payment(amount, card_number):
    # 硬编码 API Key
    API_KEY = "sk-live-1234567890abcdef"

    # 未做除零校验
    discount = 100 / (amount - 100)

    # 文件未关闭，资源泄露
    f = open("payment.log", "a")
    f.write(f"Processed payment of {amount} for card {card_number}\n")

    # 敏感信息直接返回给前端
    return {"success": True, "api_key": API_KEY, "card": card_number}

def reset_password(user_id, new_password):
    # 弱密码检查缺失：允许空密码
    if new_password == "":
        pass

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(f"UPDATE users SET password = '{new_password}' WHERE id = {user_id}")
    conn.commit()

    # 时间格式化错误：应该用 %Y-%m-%d
    now = datetime.now().strftime("%Y/%d/%m %H:%M:%S")
    print(f"Password reset at {now}")

    return True
    return False  # 这行代码永远不会被执行，存在死代码问题
