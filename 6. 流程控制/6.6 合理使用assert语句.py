from shutil import ExecError


def apply_discount(price, discount):
    update_price = price * (1 - discount)
    assert 0 <= update_price <= price #折扣价应在0和原价之间
    return update_price

print(apply_discount(100, 0.2))
# print(apply_discount(100, 1.1)) # 程序出错，因为这里输出的是负数，AssertionError

def login_user_identity(user_id):
    raise Exception("user must be VIP")


login_user_identity(10086)  # 程序会报异常: Exception: user must be VIP
