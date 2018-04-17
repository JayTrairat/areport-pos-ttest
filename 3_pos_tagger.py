from pythainlp.tag import pos_tag
from pythainlp.tokenize import word_tokenize

def main():
    with open('assets/with_position_verification/first_cosine_values_ranked.txt', 'r', encoding='utf8') as source:
        contents = (source.readlines())
        contents = [{'words':content.strip().split('=')[0].split('|'), 'score':content.strip().split('=')[1]} for content in contents]


    tagged_pos = [(pos_tag(content['words'], engine='artagger')) for content in contents]
    contents = [{'words': tagged_pos[index], 'score': content['score']} for index, content in enumerate(contents)]
    contents = [str('|'.join(str(x) for x in content['words'])) + '=' + content['score'] for content in contents]

    with open('assets/with_position_verification/first_cosine_values_ranked_tagged.txt', 'w', encoding='utf8') as result:
        result.write('\n'.join(contents))
if __name__ == '__main__':
    main()
