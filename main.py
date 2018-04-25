from functools import reduce
import numpy as np

def main():
    with open('assets/original_word_stats.txt', 'r', encoding='utf8') as source:
        contents = [content.strip() for content in source.readlines()[:]]
        contents = [content.split(' :: ')[1] for content in contents]
        contents = [content.split(',') for content in contents]
        contents = [list(map(lambda x : x.split(':'), content)) for content in contents]
        contents = [list(reduce(lambda x, y: x + y, content)) for content in contents]

    with open('assets/original_for_google_sheet.csv', 'w', encoding='utf8') as outp:
        for content in contents:
            outp.write('|'.join(content))
            outp.write('\n')

if __name__ == '__main__':
    main()
