def info(*data):
    print(data)


class Info:
    def __init__(self, title, content, time):
        self.title = title
        self.content = content
        self.time = time

    def __str__(self):
        return f"Title: {self.title}, Content: {self.content}, Time: {self.time}"


# 创建 Info 类的实例
info_obj = Info("张三", "qwe123", "2025.6.9")

# 打印对象，会调用 __str__
print(info_obj)

