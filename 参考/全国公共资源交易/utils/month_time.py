from datetime import datetime

# 获取当前时间
now = datetime.now()

# 获取本月第一天
first_day = datetime(year=now.year, month=now.month, day=1)

# 格式化输出
print("当前时间:", now.strftime("%Y-%m-%d"))
print("本月第一天:", first_day.strftime("%Y-%m-%d"))