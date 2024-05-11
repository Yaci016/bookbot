def read_book(path):
    with open(path) as f:
        return f.read()


def count_number_of_words(book_content):
    return len(book_content.split())


def main():
    content = read_book('books/frankenstein.txt')
    word_count = count_number_of_words(content)
    print(word_count)


main()
