import csv
import re

def main():
    counts = {} # empty dict
    words = get_words("address.txt") # this line simply opens up the argument file and returns a list of individual words found in the adress' file

    # List comprehension: Excellent way to create new lists based on existing iterables while applying transformations or conditional filterings

    lowercase_words = [word.lower() for word in words if len(word) > 4] # we want to iterate to rather a list with only lowercase values, so that any mixed undercase and uppercase values are not taken as different

    for word in lowercase_words: # iterate over each 'word' on the 'words' list
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    save_counts(counts)

##########################################################################

def get_words(filename):
    with open(filename, "r") as f:
        contents = f.read()

    contents = " ".join(contents.split())
    contents = re.sub(r"[^\w\- ]", "", contents)
    contents = re.sub(r"\-\-", " ", contents)
    return contents.split()


def save_counts(counts):
    with open("counts.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Word", "Count"])
        for word, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
            writer.writerow([word, count])


main()


# Let's try to make our own dictionary comprehension:
"""
def main():
    words = get_words("address.txt") # this line simply opens up the argument file and returns a list of individual words found in the adress' file
    lowercase_words = [word.lower() for word in words if len(word) > 4] # we want to iterate to rather a list with only lowercase values, so that any mixed undercase and uppercase values are not taken as different

    counts = {word: lowercase_words.count(word) for word in lowecase_words} # 'words.count(word)' --> the number of times the word appears in the words list

    save_counts(counts)

main()

"""