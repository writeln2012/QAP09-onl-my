import collections


file_7 = open('file7.txt', 'r')
file_7 = file_7.read()

file_8 = open('file8.txt', 'r')
file_8 = file_8.read()

file_9 = open('file9.txt', 'r')
file_9 = file_9.read()


class File():

    def __init__(self, name):
        self.name = name
        print(f"{self.name}:")

    @staticmethod
    def count_symbol(file):
        list_file = [i for i in file]
        list_let = []
        list_numb = []
        list_symb = []
        for i in list_file:
            if i.isalpha():
                list_let.append(i)
            elif i.isdigit():
                list_numb.append(i)
            else:
                list_symb.append(i)
        print(f"{len(list_let)} letters, {len(list_numb)} numbers, {len(list_symb)} symbols")

    @staticmethod
    def aver_numb(file):
        list_file = [i for i in file]
        sum_file = 0
        count_numb = 0
        for i in list_file:
            if i.isdigit():
                sum_file += float(i)
                count_numb += 1
        aver = round(sum_file / count_numb, 1)
        print(f"average of numbers: {aver}")

    @staticmethod
    def max_amount(file):

        text_low = file.lower()
        text_list = list(text_low)
        list_letters = [i for i in text_list if i.isalpha() is True]
        letters_count = collections.Counter(list_letters)
        letters_count_tup = letters_count.most_common(3)
        print("Top 3 letters:")
        print(f"{letters_count_tup[0][0].upper()} - amount: {letters_count_tup[0][1]}")
        print(f"{letters_count_tup[1][0].upper()} - amount: {letters_count_tup[1][1]}")
        print(f"{letters_count_tup[2][0].upper()} - amount: {letters_count_tup[2][1]}")

    @staticmethod
    def unique_letters(*args):
        list_args = [list(i) for i in args]
        letters_list_args = [[]] * len(list_args)
        for i in list_args:
            for j in i:
                if j.isalpha():
                    letters_list_args[list_args.index(i)].append(j.lower())

        count_letters_list_args = []
        for i in letters_list_args:
            count_letters_list_args.append(len(set(i)))

        count = collections.Counter(count_letters_list_args)
        number_of_repeat = count[max(count_letters_list_args)]

        if number_of_repeat == len(count_letters_list_args):
            print(f"All files have the same number of unique letters ({max(count_letters_list_args)})")
        else:
            for i in count_letters_list_args:
                if i == max(count_letters_list_args):
                    print(f"File_{count_letters_list_args.index(i)} has the maximum number of unique letters "
                          f"({max(count_letters_list_args)})")

    @staticmethod
    def sum_numbers(*args):
        list_args = [list(i) for i in args]
        letters_list_args = [[]] * len(list_args)
        for i in list_args:
            for j in i:
                if j.isdigit():
                    letters_list_args[list_args.index(i)].append(float(j))

        sum_numb = 0
        for i in letters_list_args:
            sum_numb += sum(i)
        print(f"Sum of all numbers: {sum_numb}")

    @staticmethod
    def symbols(*args):
        list_args = [list(i) for i in args]
        letters_list_args = [[]] * len(list_args)
        for i in list_args:
            for j in i:
                if j.isalpha():
                    pass
                elif j.isdigit():
                    pass
                else:
                    letters_list_args[list_args.index(i)].append(j)

        sum_list = []
        for i in letters_list_args:
            sum_list.append(len(i))

        sum_symb = sum(sum_list)

        symb_args = [[]] * len(list_args)
        for i in letters_list_args:
            for j in i:
                if j == "!" or j == "," or j == "?" or j == "." or j == "-" or j == "(" or j == ")" or j == ":" or\
                        j == ";":
                    symb_args[letters_list_args.index(i)].append(j)

        sum_symb_args = []
        for i in symb_args:
            sum_symb_args.append(len(i))

        other_symb = sum_symb - sum(sum_symb_args)
        print(f"All files have {sum(sum_symb_args)} punctuation marks and {other_symb} other symbols")


file_te_read_1 = File("File_1")
file_te_read_1.count_symbol(file_7)
file_te_read_1.aver_numb(file_7)
file_te_read_1.max_amount(file_7)

file_te_read_2 = File("File_2")
file_te_read_2.count_symbol(file_8)
file_te_read_2.aver_numb(file_8)
file_te_read_2.max_amount(file_8)

file_te_read_3 = File("File_3")
file_te_read_3.count_symbol(file_9)
file_te_read_3.aver_numb(file_9)
file_te_read_3.max_amount(file_9)

file_te_read_1.unique_letters(file_7, file_8, file_9)
file_te_read_1.sum_numbers(file_7, file_8, file_9)
file_te_read_1.symbols(file_7, file_8, file_9)































































































