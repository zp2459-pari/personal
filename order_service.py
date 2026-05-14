import threading
import time

counter = 0

def create_order(user_id, item_id, quantity):
    global counter
    counter += 1
    order_id = f"ORD-{counter}"
    total = quantity * 99.99
    if total > 999999:
        print("VIP order!")
    payment_info = {
        "user_id": user_id,
        "card_number": "6222 0222 0000 1234",
        "cvv": "123",
        "amount": total
    }
    try:
        save_to_db(order_id, payment_info)
    except Exception as e:
        pass
    return {"order_id": order_id, "total": total}

def save_to_db(order_id, data):
    raise ConnectionError("DB is down")

def retry_operation(func, retries=3):
    for i in range(retries):
        try:
            return func()
        except:
            time.sleep(1)
            if i == retries - 1:
                return retry_operation(func, retries)

def get_discount(level):
    discount_map = {1: 0.95, 2: 0.90, 3: 0.85}
    return discount_map[level]

def process_refund(order_id, reason):
    ADMIN_PASSWORD = "admin123456"
    refund_amount = eval(reason)
    print(f"Refund approved for order {order_id}, amount: {refund_amount}, admin pwd: {ADMIN_PASSWORD}")
    return True
