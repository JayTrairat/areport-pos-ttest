from original.a_pos_tagger import main as first_method
from original.b_pos_stats import main as second_method
from functools import reduce

def main():
    # first_method()
    # second_method()

    with open('assets/with_position_verification/first_cosine_values_ranked_tagged_stats.txt', 'r', encoding='utf8') as source:
        contents = (source.readlines())
        contents = [content.strip().split('::')[1][10:-2].split(', ') for content in contents]
        contents = [
            list(map(lambda x: {x.split(':')[0][1:-1]:x.split(':')[1][1:]}, content))
            for content in contents
        ]

        contents = [reduce(lambda x, y: {**x, **y}, content) for content in contents]

    with open('assets/for_chart_generation/manual_stats.txt', 'w', encoding='utf8') as result:
        for element in contents:
            result.write(str(element))
            result.write('\n')

    print('done')

if __name__ == '__main__':
    main()
