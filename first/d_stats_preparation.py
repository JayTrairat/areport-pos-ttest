from collections import Counter as count

def main():
        with open('assets/with_out_position_verification/first_cosine_values_ranked_tagged.txt', 'r', encoding='utf8') as source:
            contents = (source.readlines())
            contents = [content.strip().split('=')[0].split('|') for content in contents]
            contents = [content for content in contents if len(content) == 3]

            first_position = [content[0] for content in contents]
            second_position = [content[1] for content in contents]
            third_position = [content[2] for content in contents]

            first_position = [content[1:-1].split(',')[1][2:-1] for content in first_position]
            second_position = [content[1:-1].split(',')[1][2:-1] for content in second_position]
            third_position = [content[1:-1].split(',')[1][2:-1] for content in third_position]

        with open('assets/with_out_position_verification/first_cosine_values_ranked_tagged_stats.txt', 'w', encoding='utf8') as result:
            result.write('position_1 :: ' + str(count(first_position)))
            result.write('\n')
            result.write('position_2 :: ' + str(count(second_position)))
            result.write('\n')
            result.write('position_3 :: ' + str(count(third_position)))

if __name__ == '__main__':
    main()
