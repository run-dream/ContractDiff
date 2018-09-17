import os
import re
import unicodedata


def get_path(relative_path):
    filepath = os.path.join(__file__, relative_path)
    filepath = os.path.abspath(filepath)
    return filepath


def __read_file(relative_path):
    """读取文件"""
    filepath = get_path(relative_path)
    with open(filepath, 'r') as file:
        s = file.read()
    return s


def __strQ2B(ustring):
    """全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 12288:  # 全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374):
            inside_code -= 65248
        rstring += chr(inside_code)
    return rstring


def __filter_content(content):
    """预处理文本内容"""
    # Replace Chinese Marks
    content = unicodedata.normalize('NFKC', content)
    content = __strQ2B(content)
    # Remove redundant space
    content = ' '.join(re.split(' +|\t', content)).rstrip()
    content = re.sub('\n+', '\n', content)

    def empty(matched):
        value = matched.group('space')
        return re.sub('\s', '', value)

    content = re.sub('(?P<space>[^\s\n] [\u4e00-\u9fbb])', empty, content)
    content = re.sub('(?P<space>\s+\n)', empty, content)
    content = re.sub('(?P<space>\n\s+)', empty, content)
    return content


def get_text(path):
    text = __read_file(path)
    text = __filter_content(text)
    return text