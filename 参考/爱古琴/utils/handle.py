def php_unserialize(data):
    """
    简单的PHP序列化数据反序列化函数
    增加了对空输入和解析异常的处理
    默认在解析失败时返回空字典
    """
    # 处理空输入的情况
    if not data:
        return {}

    def parse_value(data, pos):
        # 确保还有足够的数据可供解析
        if pos >= len(data):
            raise ValueError("解析位置超出数据范围")

        # 解析数据类型和值
        data_type = data[pos:pos + 1].decode('utf-8')
        pos += 2  # 跳过类型和冒号

        if data_type == 'i':  # 整数
            end_pos = data.find(b';', pos)
            if end_pos == -1:
                raise ValueError("未找到整数结束标记;")
            value = int(data[pos:end_pos])
            pos = end_pos + 1

        elif data_type == 's':  # 字符串
            # 解析字符串长度
            len_end_pos = data.find(b':', pos)
            if len_end_pos == -1:
                raise ValueError("未找到字符串长度结束标记:")
            str_len = int(data[pos:len_end_pos])
            pos = len_end_pos + 2  # 跳过冒号和引号

            # 解析字符串内容
            if pos + str_len > len(data):
                raise ValueError("字符串内容长度不足")
            value = data[pos:pos + str_len].decode('utf-8')
            pos += str_len + 2  # 跳过字符串和引号

        elif data_type == 'a':  # 数组
            # 解析数组长度
            len_end_pos = data.find(b':', pos)
            if len_end_pos == -1:
                raise ValueError("未找到数组长度结束标记:")
            arr_len = int(data[pos:len_end_pos])
            pos = len_end_pos + 2  # 跳过冒号和大括号

            # 解析数组元素
            value = {}
            for _ in range(arr_len):
                # 解析键
                try:
                    key, pos = parse_value(data, pos)
                except Exception as e:
                    print(f"解析数组键时出错: {e}")
                    key = None  # 默认为None

                # 解析值
                try:
                    val, pos = parse_value(data, pos)
                except Exception as e:
                    print(f"解析数组值时出错: {e}")
                    val = None  # 默认为None

                value[key] = val

            # 确保有结束大括号
            if pos < len(data) and data[pos:pos + 1] == b'}':
                pos += 1  # 跳过结束大括号
            else:
                raise ValueError("未找到数组结束标记}")

        else:
            raise ValueError(f"不支持的数据类型: {data_type}")

        return value, pos

    # 将输入转换为字节类型（如果是字符串）
    if isinstance(data, str):
        data = data.encode('utf-8')

    # 从数据开始位置解析
    try:
        value, _ = parse_value(data, 0)
        return value
    except Exception as e:
        print(f"反序列化失败: {e}")
        return {}  # 默认返回空字典


# 使用示例
if __name__ == "__main__":
    # 有效序列化数据
    serialized = 'a:2:{s:3:"key1";s:5:"value";s:3:"key2";i:123;}'
    data = php_unserialize(serialized)
    print("有效数据解析结果:", data)

    # 空输入
    data = php_unserialize("")
    print("空输入解析结果:", data)

    # 无效数据
    data = php_unserialize("invalid_data")
    print("无效数据解析结果:", data)

    # 安全遍历结果
    for key, value in data.items():
        print(f"键: {key}, 值: {value}")