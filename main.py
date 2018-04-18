from first.a_cosine_similarity import main as first_method
from first.b_ranking import main as second_method
from first.c_pos_tagger import main as third_method
from first.d_stats_preparation import main as fourth_method

def main():
    try:
        first_method()
        second_method()
        third_method()
        fourth_method()
    except Exception as ex:
        print(ex)
    else:
        print('done')

if __name__ == '__main__':
    main()
