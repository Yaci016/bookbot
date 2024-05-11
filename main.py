def main():
    content = read_book('books/frankenstein.txt')
    word_count = count_number_of_words(content)
    letter_list = get_letter_list(content.split())
    x = calculate_char_occurence_dist_in_list(letter_list)
    log(word_count, x)


def read_book(path):
    with open(path) as f:
        return f.read()


def count_number_of_words(book_content):
    return len(book_content.split())


def get_letter_list(word_list):
    letter_list = []
    for word in word_list:
        for char in word:
            if (not char.isalpha()):
                continue
            else:
                letter_list.append(char.lower())
    return letter_list


def calculate_char_occurence_dist_in_list(letter_list):
    dist = {}
    for letter in letter_list:
        if letter in dist:
            dist[letter] += 1
        else:
            dist[letter] = 1
    return dist


def sort_on(dict):
    return dict["occurence_count"]


def dict_to_list(dict) -> list:
    final_dict = []
    for val in dict:
        x = {}
        x['char'] = val
        x['occurence_count'] = dict[val]
        final_dict.append(x)
    return final_dict


def log(word_count, char_occurence_dict):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{word_count} words found in the document')
    x = dict_to_list((char_occurence_dict))
    x.sort(reverse=True, key=sort_on)
    for dict in x:
        print(
            f"The '{dict['char']}' character was found {dict['occurence_count']} times")
    print('--- End report ---')


main()
