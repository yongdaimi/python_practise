str = "网站名称：{:>9s} \t 地址：{:s}"
print(str.format("百度", "http://www.baidu.com")) # 输出：网站名称：       百度 	 地址：http://www.baidu.com


# 以多种形式显示数值
# 货币形式
print("货币形式:{:,d}".format(1000000)) # 输出: 货币形式:1,000,000

# 科学计数法
print("科学计数法:{:E}".format(1200.12)) # 输出：科学计数法:1.200120E+03

# 十六进制形式
print("十六进制形式:{:#X}".format(255)) # 输出：0XFF

# 百分比形式
print("百分比形式:{:.0%}".format(0.15))

# 货币计数
print("result is: {:,d}".format(10000000))
