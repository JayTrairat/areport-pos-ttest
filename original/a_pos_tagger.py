from pythainlp.tag import pos_tag
from pythainlp.tokenize import word_tokenize

def main():
    try:
        with open('assets/original.txt', 'r', encoding='utf8') as source:
            contents = (source.readlines())
            contents = [content.strip().split('|') for content in contents]
            contents = [list(filter(lambda x : x.strip(), content)) for content in contents]

            tagged_pos = [(pos_tag(content, engine='artagger')) for content in contents]
            contents = [{'words': tagged_pos[index]} for index, content in enumerate(contents)]
            contents = [str('|'.join(str(x) for x in content['words']))for content in contents]

            with open('assets/original_tagged.txt', 'w', encoding='utf8') as result:
                result.write('\n'.join(contents))
    except Exception as ex:
        print(ex)
    else:
        print('done')

if __name__ == '__main__':
    main()
