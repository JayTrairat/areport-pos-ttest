from collections import Counter as count

def main():
        with open('assets/with_position_verification/first_cosine_values_ranked_tagged.txt', 'r', encoding='utf8') as source:
            contents = (source.readlines())
            contents = [content.strip().split('=')[0].split('|') for content in contents]

            # max size of content is 10
            a_position = []
            b_position = []
            c_position = []
            d_position = []
            e_position = []
            f_position = []
            g_position = []
            h_position = []
            i_position = []
            j_position = []

            for i in range(0, len(contents)):
                if(len(contents[i]) == 1):
                    a_position.append(contents[i][0])
                elif(len(contents[i]) == 2):
                    a_position.append(contents[i][0])
                    b_position.append(contents[i][1])
                elif(len(contents[i]) == 3):
                    a_position.append(contents[i][0])
                    b_position.append(contents[i][1])
                    c_position.append(contents[i][2])
                elif(len(contents[i]) == 4):
                    a_position.append(contents[i][0])
                    b_position.append(contents[i][1])
                    c_position.append(contents[i][2])
                    d_position.append(contents[i][3])
                elif(len(contents[i]) == 5):
                    a_position.append(contents[i][0])
                    b_position.append(contents[i][1])
                    c_position.append(contents[i][2])
                    d_position.append(contents[i][3])
                    e_position.append(contents[i][4])
                elif(len(contents[i]) == 6):
                    a_position.append(contents[i][0])
                    b_position.append(contents[i][1])
                    c_position.append(contents[i][2])
                    d_position.append(contents[i][3])
                    e_position.append(contents[i][4])
                    f_position.append(contents[i][5])
                elif(len(contents[i]) == 7):
                    a_position.append(contents[i][0])
                    b_position.append(contents[i][1])
                    c_position.append(contents[i][2])
                    d_position.append(contents[i][3])
                    e_position.append(contents[i][4])
                    f_position.append(contents[i][5])
                    g_position.append(contents[i][6])
                elif(len(contents[i]) == 8):
                    a_position.append(contents[i][0])
                    b_position.append(contents[i][1])
                    c_position.append(contents[i][2])
                    d_position.append(contents[i][3])
                    e_position.append(contents[i][4])
                    f_position.append(contents[i][5])
                    g_position.append(contents[i][6])
                    h_position.append(contents[i][7])
                elif(len(contents[i]) == 9):
                    a_position.append(contents[i][0])
                    b_position.append(contents[i][1])
                    c_position.append(contents[i][2])
                    d_position.append(contents[i][3])
                    e_position.append(contents[i][4])
                    f_position.append(contents[i][5])
                    g_position.append(contents[i][6])
                    h_position.append(contents[i][7])
                    i_position.append(contents[i][8])
                elif(len(contents[i]) == 10):
                    a_position.append(contents[i][0])
                    b_position.append(contents[i][1])
                    c_position.append(contents[i][2])
                    d_position.append(contents[i][3])
                    e_position.append(contents[i][4])
                    f_position.append(contents[i][5])
                    g_position.append(contents[i][6])
                    h_position.append(contents[i][7])
                    i_position.append(contents[i][8])
                    j_position.append(contents[i][9])

            a_position = [content[1:-1].split(',')[1][2:-1] for content in a_position]
            b_position = [content[1:-1].split(',')[1][2:-1] for content in b_position]
            c_position = [content[1:-1].split(',')[1][2:-1] for content in c_position]
            d_position = [content[1:-1].split(',')[1][2:-1] for content in d_position]
            e_position = [content[1:-1].split(',')[1][2:-1] for content in e_position]
            f_position = [content[1:-1].split(',')[1][2:-1] for content in f_position]
            g_position = [content[1:-1].split(',')[1][2:-1] for content in g_position]
            h_position = [content[1:-1].split(',')[1][2:-1] for content in h_position]
            i_position = [content[1:-1].split(',')[1][2:-1] for content in i_position]
            j_position = [content[1:-1].split(',')[1][2:-1] for content in j_position]

        with open('assets/with_position_verification/first_cosine_values_ranked_tagged_stats.txt', 'w', encoding='utf8') as result:
            result.write('position_1 :: ' + str(count(a_position)))
            result.write('\n')
            result.write('position_2 :: ' + str(count(b_position)))
            result.write('\n')
            result.write('position_3 :: ' + str(count(c_position)))
            result.write('\n')
            result.write('position_4 :: ' + str(count(d_position)))
            result.write('\n')
            result.write('position_5 :: ' + str(count(e_position)))
            result.write('\n')
            result.write('position_6 :: ' + str(count(f_position)))
            result.write('\n')
            result.write('position_7 :: ' + str(count(g_position)))
            result.write('\n')
            result.write('position_8 :: ' + str(count(h_position)))
            result.write('\n')
            result.write('position_9 :: ' + str(count(i_position)))
            result.write('\n')
            result.write('position_10 :: ' + str(count(j_position)))

if __name__ == '__main__':
    main()
