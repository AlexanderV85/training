from string import punctuation

Word = []


def longest_word_in_file(file_name):
    k = 0
    r = open(file_name, encoding='utf-8')
    # text = r.readline().split()
    r = r.read()
    for i in r:
        if i in punctuation:
            r = r.replace(i, '')
    for i in r.split():
        if len(i) >= k:
            Word.append(i)
            k = len(i)
    return Word[-1]


print(longest_word_in_file(r'C:\Python\pythonProject\Навчання\55555.txt'))
