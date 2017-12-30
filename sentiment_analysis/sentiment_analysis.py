from collections import Counter
import numpy as np


def pretty_print_review_and_label(i):
    print(labels[i] + "\t:\t" + reviews[i][:80] + "...")


g = open('reviews.txt', 'r')  # What we know!
reviews = list(map(lambda x: x[:-1], g.readlines()))
g.close()

g = open('labels.txt', 'r')  # What we WANT to know!
labels = list(map(lambda x: x[:-1].upper(), g.readlines()))
g.close()

print("labels.txt \t: \treviews.txt\n")
pretty_print_review_and_label(2137)
pretty_print_review_and_label(12816)
pretty_print_review_and_label(6267)
pretty_print_review_and_label(21934)
pretty_print_review_and_label(5297)
pretty_print_review_and_label(4998)

# Create three Counter objects to store positive, negative and total counts
positive_counts = Counter()
negative_counts = Counter()
total_counts = Counter()

for i in range(len(reviews)):
    if labels[i] == 'POSITIVE':
        for word in reviews[i].split(" "):
            positive_counts[word] += 1
            total_counts[word] += 1
    else:
        for word in reviews[i].split(" "):
            negative_counts[word] += 1
            total_counts[word] += 1

# print(len(positive_counts))
# print(len(negative_counts))
# print(len(total_counts))

# print(positive_counts.most_common())
# print(negative_counts.most_common())


# Create Counter object to store positive/negative ratios
pos_neg_ratios = Counter()

# TODO: Calculate the ratios of positive and negative uses of the most common words
#       Consider words to be "common" if they've been used at least 100 times
for term, cnt in list(total_counts.most_common()):
    if cnt > 100:
        pos_neg_ratio = positive_counts[term] / float(negative_counts[term] + 1)
        pos_neg_ratios[term] += pos_neg_ratio

print("Pos-to-neg ratio for 'the' = {}".format(pos_neg_ratios["the"]))
print("Pos-to-neg ratio for 'amazing' = {}".format(pos_neg_ratios["amazing"]))
print("Pos-to-neg ratio for 'terrible' = {}".format(pos_neg_ratios["terrible"]))

for word, ratio in pos_neg_ratios.most_common():
    pos_neg_ratios[word] = np.log(ratio)

print("Pos-to-neg ratio for 'the' = {}".format(pos_neg_ratios["the"]))
print("Pos-to-neg ratio for 'amazing' = {}".format(pos_neg_ratios["amazing"]))
print("Pos-to-neg ratio for 'terrible' = {}".format(pos_neg_ratios["terrible"]))

# words most frequently seen in a review with a "POSITIVE" label
# print(pos_neg_ratios.most_common())

# words most frequently seen in a review with a "NEGATIVE" label
# print(list(reversed(pos_neg_ratios.most_common()))[0:30])

# TODO: Create set named "vocab" containing all of the words from all of the reviews
vocab = set(total_counts.keys())

vocab_size = len(vocab)
print(vocab_size)

# TODO: Create layer_0 matrix with dimensions 1 by vocab_size, initially filled with zeros
layer_0 = np.zeros((1, vocab_size))

print(layer_0.shape)

# Create a dictionary of words in the vocabulary mapped to index positions
# (to be used in layer_0)
word2index = {}
for i, word in enumerate(vocab):
    word2index[word] = i


# display the map of words to indices
# print(word2index)


def update_input_layer(review):
    """ Modify the global layer_0 to represent the vector form of review.
    The element at a given index of layer_0 should represent
    how many times the given word occurs in the review.
    Args:
        review(string) - the string of the review
    Returns:
        None
    """
    global layer_0
    # clear out previous state by resetting the layer to be all 0s
    layer_0 *= 0

    # TODO: count how many times each word is used in the given review and store the results in layer_0
    for word in review.split(" "):
        layer_0[0][word2index[word]] += 1


update_input_layer(reviews[0])
print(layer_0)


def get_target_for_label(label):
    """Convert a label to `0` or `1`.
    Args:
        label(string) - Either "POSITIVE" or "NEGATIVE".
    Returns:
        `0` or `1`.
    """
    # TODO: Your code here
    if label == "POSITIVE":
        return 1
    else:
        return 0


print(labels[0])

print(get_target_for_label(labels[0]))

print(labels[1])

print(get_target_for_label(labels[1]))
