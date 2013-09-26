import re
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
from nltk.probability import FreqDist  # NOQA
from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder  # NOQA
from nltk.stem.wordnet import WordNetLemmatizer
import nltk.collocations


bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

tokenizer = WordPunctTokenizer()
word_re = re.compile("[a-zA-Z0-9][a-zA-Z0-9'-]*")
bg_re = re.compile("([\d]+)\s+([\w';-]+)\s+([\w';-]+)")
tg_re = re.compile("([\d]+)\s+([\w';-]+)\s+([\w';-]+)\s+([\w';-]+)")

lmtzr = WordNetLemmatizer()
sw = stopwords.words()
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')


def load_words():
    f = open("stopwords.txt", "r")
    res = f.readlines()
    f.close()
    for w in res:
        w = w.lower()
        yield lmtzr.lemmatize(w.strip())


def load_bg():
    f = open("stopword_bigrams.txt", "r")
    res = f.readlines()

    freq = []

    for line in res:
        line = line.lower()
        m = bg_re.match(line)
        if not m:
            #print line
            continue

        freq.append((int(m.group(1)), (m.group(2), m.group(3))))

    for num, s in sorted(freq, key=lambda x: x[0], reverse=True)[:10000]:
        yield [lmtzr.lemmatize(p) for p in s]

    f.close()


def load_tg():
    f = open("stopword_trigrams.txt", "r")
    res = f.readlines()

    freq = []

    for line in res:
        line = line.lower()
        m = tg_re.match(line)
        if not m:
            #print line
            continue

        freq.append((int(m.group(1)), (m.group(2), m.group(3), m.group(4))))

    for num, s in sorted(freq, key=lambda x: x[0], reverse=True)[:10000]:
        yield [lmtzr.lemmatize(p) for p in s]

    f.close()


bg = list(load_bg())
tg = list(load_tg())


sw2 = list(load_words())


def sentences(blob):
    blob = blob.replace("\n", ". ")
    blob = blob.replace("...", ".")
    blob = blob.replace("..", ".")
    blob = blob.replace(",", ".")
    blob = blob.replace("/", " ")

    return [s for s in sent_detector.tokenize(blob, realign_boundaries=True) if len(s) > 3]


def pos_tag(sentence):
    text = nltk.word_tokenize(sentence)
    return nltk.pos_tag(text)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def prep(blob):
    tokens = tokenizer.tokenize(blob)

    words = [x for x in tokens if len(x) > 1]

    num_words = len(words)

    for i, word in enumerate(words):
        if num_words > 1000:
            if i % 100 == 0:
                print i, "of", num_words
        if word not in sw and not is_number(word) and word_re.match(word):
            yield word


def prep_pos(pos_list):
    for word, pos in pos_list:
        word = word.lower()

        if word not in sw and not is_number(word) and word_re.match(word):
            yield word, pos


def has_keyword(body, keywords):
    for kw in keywords:
        if kw in body:
            return True

    return False


def has_exact_keyword(words, keywords):
    for kw in keywords:
        if kw in words:
            return True

    return False


def get_pos_subject(pos_list):
    in_seq = False
    cur_seq = []
    seqs = []

    for word, pos in pos_list:
        if "NN" in pos:
            in_seq = True
            cur_seq.append((word, pos))
        else:
            if in_seq:
                in_seq = False
                seqs.append(cur_seq)
                cur_seq = []

    print seqs
    return seqs


def bigrams(words, max_bigrams=100):
    print "Extracting bigrams"
    bigram_finder = BigramCollocationFinder.from_words(words)

    for bigram, score in bigram_finder.score_ngrams(bigram_measures.raw_freq)[:max_bigrams]:
        l_bigram = [lmtzr.lemmatize(p) for p in bigram]
        if l_bigram in bg:
            print "Common bigram", bigram
            continue
        yield bigram


def trigrams(words, max_trigrams=100):
    print "Extracting trigrams"
    trigram_finder = TrigramCollocationFinder.from_words(words)

    for trigram, score in trigram_finder.score_ngrams(trigram_measures.raw_freq)[:max_trigrams]:
        l_trigram = [lmtzr.lemmatize(p) for p in trigram]
        if l_trigram in tg:
            print "Common trigram", trigram
            continue

        #print trigram, score
        yield trigram


def common_words(words, max_words=100):
    words = set([lmtzr.lemmatize(w) for w in words])

    word_frequencies = FreqDist([w for w in words if w not in sw and w not in sw2])
    for word, cnt in word_frequencies.items()[:max_words]:
        yield word
