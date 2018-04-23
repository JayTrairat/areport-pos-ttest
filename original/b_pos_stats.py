from collections import Counter as count

def main():
    # first_method()
    with open('assets/original_tagged.txt', 'r', encoding='utf8') as source:
        contents = (source.readlines()[:64])
        contents = [content.strip().split('|') for content in contents]
        contents = [list(map(lambda x: x.strip().split(',')[1][2:-2], content)) for content in contents]

        result = {key:[] for key in range(0, 28)}
        for content in contents:
            for index in range(0, len(content)):
                result[index].append(content[index])


    with open('assets/original_tagged_stats.txt', 'w', encoding='utf8') as outp:
        for index in result:
            outp.write(('position_' + str(index) + ' :: ' + str(count(result[index]))))
            outp.write('\n')

if __name__ == '__main__':
    main()
