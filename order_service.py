import threading
import time

# 全局变量，线程不安全
counter = 0

def create_order(user_id, item_id, quantity):
    global counter
    counter += 1
    order_id = f"ORD-{counter}"

    # 未做参数校验，quantity 可能是负数或字符串
    total = quantity * 99.99

    # 魔法数字
    if total > 999999:
        print("VIP order!")

    # 明文存储信用卡号
    payment_info = {
        "user_id": user_id,
        "card_number": "6222 0222 0000 1234",
        "cvv": "123",
        "amount": total
    }

    # 异常被吞掉，没有抛出
    try:
        save_to_db(order_id, payment_info)
    except Exception as e:
        pass

    return {"order_id": order_id, "total": total}

def save_to_db(order_id, data):
    # 模拟数据库操作
    raise ConnectionError("DB is down")

def retry_operation(func, retries=3):
    # 递归没有终止条件防护
    for i in range(retries):
        try:
            return func()
        except:
            time.sleep(1)
            if i == retries - 1:
                return retry_operation(func, retries)

def get_discount(level):
    # 缺少默认值，level 不在映射里时会 KeyError
    discount_map = {
        1: 0.95,
        2: 0.90,
        3: 0.85
    }
    return discount_map[level]
