from collections import Counter as count

def main():
    with open('assets/original_tagged.txt', 'r', encoding='utf8') as source:
        contents = source.readlines()
        contents = [content.strip().split('|') for content in contents]

    result = {index:[] for index in range(0, 28)}
    for content in contents:
        for index in range(0, len(content)):
            result[index].append(content[index])
    with open('assets/original_word_stats.txt', 'w', encoding='utf8') as outp:
        for index in result:
            outp.write(('position_' + str(index) + ' :: ' + str(count(result[index]))))
            outp.write('\n')

if __name__ == '__main__':
    main()
