counts = {}


def makeword(word):
    result = ""
    for letter in word.lower():
        if letter.isalpha() or letter == "'":
            result = result + letter
    return result


def get_counts_dict(filename):
    file_object = open(filename, "r")
    counts = {}

    for line in file_object:
        for word in line.split():
            processed_word = makeword(word)
            if processed_word in counts:
                current_count = counts[processed_word]
            else:
                current_count = 0
            counts[processed_word] = current_count + 1
    file_object.close()
    return counts


def get_sorted_counts_list(counts_dict):
    result = []
    for key in counts_dict:
        result.append((counts_dict[key], key))
    result.sort()
    return result

def print_top_n_words(counts_list, n):
    for pair in counts_list[-n:]:
        print("    {}: {}".format(pair[1], pair[0]))


counts_dict = get_counts_dict("mobydick.txt")
counts_list = get_sorted_counts_list(counts_dict)
print_top_n_words(counts_list, 20)
