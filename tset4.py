from __future__ import division
def read_file(file_name):
    open(file_name, 'r')
    content = file_name.read()
    return content
def count_word(content):
    word_dict = {}
    for word in content.split():
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict
def find_max_word(word_dict):
    max_count = max(word_dict.values())
    max_words = [word for word, count in word_dict.items() if count == max_count]
    return max_words, max_count
def main():
    text = read_file(input('enter file name: '))
    word_count = count_word(text)
    most_common_word, most_count = find_max_word(word_count)
    print(most_common_word, ': ', most_count)
    
if __name__ == '__main__':
    main()