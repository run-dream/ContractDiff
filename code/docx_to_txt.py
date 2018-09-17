from docx import Document
from docx.document import Document as _Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph


def iter_block_items(parent):
    if isinstance(parent, _Document):
        parent_elm = parent.element.body
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("something's not right")

    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)


def word_to_txt(source, target):
    document = Document(source)

    content = ''
    for block in iter_block_items(document):
        is_paragraph = isinstance(block, Paragraph)
        text = ''
        if (is_paragraph):
            text = block.text
        else:
            table = block
            for row in table.rows:
                for cell in row.cells:
                    for paragraph in cell.paragraphs:
                        if text == '':
                            text = paragraph.text
                        else:
                            text = '{}    {}'.format(text, paragraph.text)
                    text += '\n'
        if(content == ''):
            content = text
        else:
            content = '{}\n{}'.format(content, text)
    with open(target, 'w') as file:
        file.write(content)