from functools import reduce

def main():
    # first_method()
    # second_method()

    with open('assets/original_tagged_stats.txt', 'r', encoding='utf8') as source:
        contents = (source.readlines())
        contents = [content.strip().split('::')[1][10:-2].split(', ') for content in contents]
        contents = [
            list(map(lambda x: {x.split(':')[0][1:-1]:x.split(':')[1][1:]}, content))
            for content in contents
        ]

        contents = [reduce(lambda x, y: {**x, **y}, content) for content in contents]

    with open('assets/for_chart_generation/actual_stats.txt', 'w', encoding='utf8') as result:
        for element in contents:
            result.write(str(element))
            result.write('\n')

if __name__ == '__main__':
    main()
