# logging 模块可以用来打log, 并且将log输出到指定的文件

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s', filename="./log.txt", filemode="a")

# 禁用log, 参数如果不写，默认将会禁用 CRITICAL 级别以下的所有log
# logging.disable()

for i in range(10):
    logging.debug("i = %d" %(i))                        # 输出Debug类型的log

logging.info("code has execute here...")






