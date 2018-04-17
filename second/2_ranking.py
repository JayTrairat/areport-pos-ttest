from operator import itemgetter

def main():
    with open('assets/with_position_verification/first_cosine_values.txt', 'r', encoding='utf8') as source:
        contents = source.readlines()
        score_contents = [{'word': content.strip().split('=')[0], 'score': content.strip().split('=')[1]} for content in contents]
        score_contents = sorted(score_contents, key=itemgetter('score'), reverse=True)
        score_contents = score_contents[:100]
        score_contents = [content['word'] + '=' + content['score'] for content in score_contents]

    with open('assets/with_position_verification/first_cosine_values_ranked.txt', 'w', encoding='utf8') as result:
        result.write('\n'.join(score_contents))

if __name__ == '__main__':
    main()
