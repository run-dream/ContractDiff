import diff_match_patch
import tools


def save_file(diff, path):
    with open(path, 'a') as file:
        for line in diff:
            file.write('flag:{} content:\n{}\n'.format(line[0], line[1]))
    print('Saved to {}'.format(path))


filepath1 = '../../material/2-打印出纸质版.ocr.txt'
filepath2 = '../../material/2-电子版对照.txt'
diffpath = '../../output/diff_of_patch.txt'
text1 = tools.get_text(filepath1)
text2 = tools.get_text(filepath2)

diff = diff_match_patch.diff_match_patch().diff_main(text1, text2, True)

print(diff)
save_file(diff, tools.get_path(diffpath))
