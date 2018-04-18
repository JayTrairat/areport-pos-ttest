from first.a_cosine_similarity import main as first_method_a
from first.b_ranking import main as second_method_a
from first.c_pos_tagger import main as third_method_a
from first.d_stats_preparation import main as fourth_method_a

from second.a_cosine_similarity import main as first_method_b
from second.b_ranking import main as second_method_b
from second.c_pos_tagger import main as third_method_b
from second.d_stats_preparation import main as fourth_method_b

def main():
    try:
        # first_method_a()
        # second_method_a()
        # third_method_a()
        # fourth_method_a()
        # print('a finished')

        # first_method_b()
        # second_method_b()
        # third_method_b()
        # fourth_method_b()
        # print('b finished')
    except Exception as ex:
        print(ex)
    else:
        print('done')

if __name__ == '__main__':
    main()
