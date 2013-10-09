import sys
import nl_util


def main(in_file, out_file):
    f = open(in_file, 'r')
    lines = f.readlines()
    f.close()

    words = []
    
    for line in lines:
        words += [s.lower() for s in nl_util.prep(line)]

    common = list(nl_util.common_words(words, 1000))
    bigrams = list(nl_util.bigrams(words, 1000))
    trigrams = list(nl_util.trigrams(words, 1000))

    f = open(out_file, "w")

    for word in common:
        f.write(word + "\n")

    for words in bigrams:
        f.write(" ".join(words) + "\n")

    for words in trigrams:
        f.write(" ".join(words) + "\n")

    f.close()

if __name__ == '__main__':
    in_file = sys.argv[1]
    out_file = sys.argv[2]

    main(in_file, out_file)
