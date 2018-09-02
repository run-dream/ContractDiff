import os
import re
import unicodedata
import difflib
import tools
from functools import reduce

filepath1 = '../../material/2-打印出纸质版.ocr.txt'
filepath2 = '../../material/2-电子版对照.txt'
text1 = tools.get_text(filepath1)
text2 = tools.get_text(filepath2)

#diffpath = '../../output/difflib.html'
#diff = difflib.HtmlDiff()
#result = diff.make_file(text1,text2)

diffpath = '../../output/difflib.txt'
diff = difflib.Differ()
result_iter = diff.compare(text1,text2)
result = reduce(lambda x,y: '{}{}\n'.format(x,y),result_iter)


with open(tools.get_path(diffpath),'w') as file:
    file.write(result)





