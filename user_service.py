import sqlite3

def authenticate_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # 直接拼接 SQL，存在注入风险
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    
    result = cursor.fetchone()
    return result is not None

def process_payment(amount, card_number):
    # 硬编码 API Key
    API_KEY = "sk-live-1234567890abcdef"
    
    # 未做除零校验
    discount = 100 / (amount - 100)
    
    # 文件未关闭，资源泄露
    f = open("payment.log", "a")
    f.write(f"Processed payment of {amount} for card {card_number}\n")
    
    return True
