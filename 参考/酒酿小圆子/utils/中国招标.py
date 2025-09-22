from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors


def WritePdf(text_content, output_filename="output.pdf"):
    """
    将文本内容写入PDF文件，支持中文显示

    参数:
    text_content (str): 要写入的文本内容
    output_filename (str): 输出的PDF文件名，默认为'output.pdf'
    """
    # 注册中文字体（使用系统自带的SimSun字体）
    try:
        pdfmetrics.registerFont(TTFont('SimSun', 'simsun.ttc'))
    except:
        # 如果找不到字体，尝试其他常见名称
        try:
            pdfmetrics.registerFont(TTFont('SimSun', 'SimSun.ttf'))
        except:
            raise ValueError("未找到SimSun字体文件，请确保系统中存在中文字体")

    # 创建PDF文档
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    # 创建自定义样式
    styles = getSampleStyleSheet()
    chinese_style = ParagraphStyle(
        'ChineseStyle',
        parent=styles['BodyText'],
        fontName='SimSun',
        fontSize=10,
        leading=14,
        alignment=TA_LEFT,
        textColor=colors.black
    )

    # 处理文本内容
    story = []
    lines = text_content.strip().split('\n')

    for line in lines:
        if line.strip():  # 跳过空行
            # 添加段落
            p = Paragraph(line.strip(), chinese_style)
            story.append(p)
            # 添加段落间距
            story.append(Spacer(1, 12))

    # 生成PDF
    doc.build(story)


# 使用示例
if __name__ == "__main__":
    text_content = """
河南省档案馆中福公司英文档案整理与开发项目流标公告 国家档案局  中钰招标有限公司 2025.06.09 10:22:12

杭锦旗城市公用事业服务中心杭锦旗锡尼镇荣乌连接线、呼和木独街、滨河南路（109国道南），蒙医院及南出入口绿化养护与环境卫生清扫保洁服务项目中标（成交）结果公告 杭锦旗城市公用事业服务中心  鄂尔多斯市蓉升项目管理有限责任公司 2025.06.09 10:05:38
"""
    WritePdf(text_content, "announcements.pdf")