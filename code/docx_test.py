from docx import Document
import tools

relative_path = '../../material/2-电子版对照.docx'
path = tools.get_path(relative_path)
document = Document(path)


target_path = '../../output/2-diff.docx'
output_path = tools.get_path(target_path)
output_doc = Document()

print('Param numers: ' + str(len(document.paragraphs)))

for para in document.paragraphs:
    print(para.text)
    output_doc.add_paragraph(para.text, para.style)

part = document.part

output_doc.save(output_path)