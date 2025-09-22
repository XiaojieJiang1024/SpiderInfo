import requests
import os
import re


def download_image(url, name, folder, base_directory):

    try:
        # 验证参数
        if not base_directory or not folder:
            raise ValueError("base_directory 和 folder 参数不能为空")

        # 清理文件夹名称中的非法字符
        sanitized_folder = re.sub(r'[\\/:*?"<>|]', '_', folder)

        # 构建完整的保存目录路径
        save_directory = os.path.join(base_directory, sanitized_folder)

        # 确保保存目录存在，不存在则创建
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        # 发送 HTTP 请求获取图片内容
        url = "http://apposs.aiguqin.com/" + url
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 检查请求是否成功

        # 确定图片文件的扩展名
        content_type = response.headers.get('Content-Type')
        if 'image/jpeg' in content_type:
            extension = '.jpg'
        elif 'image/png' in content_type:
            extension = '.png'
        elif 'image/gif' in content_type:
            extension = '.gif'
        elif 'image/webp' in content_type:
            extension = '.webp'
        else:
            # 无法确定扩展名时默认使用 .jpg
            extension = '.jpg'

        # 构建完整的保存路径（直接保存到 folder 目录）
        save_path = os.path.join(save_directory, f"{name}{extension}")

        # 保存图片文件
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"图片已成功保存到: {save_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"下载失败: {e}")
        return False
    except Exception as e:
        print(f"发生错误: {e}")
        return False

# 使用示例
# download_image("https://example.com/image.jpg", "幽兰第五02", "images_2022", "./data")
# 保存为 ./data/images_2022/幽兰第五02.jpg