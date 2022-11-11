# 很简单这里就直接演示了，assert 关键字的主要用处是，若assert 后面的语句为真，则什么也不做，如assert后面的语句为假，则抛出AssertError异常


a = 10

try:
    assert a > 10
    print("a 是一个大于10的数")

except AssertionError:
    print("a 不是一个大于10的数，它的值是：", a)