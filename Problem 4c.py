from unittest import result


def mutate_sentences(sentence: str):
    """
    Given a sentence (sequence of words), return a list of all "similar"
    sentences.
    We define a sentence to be "similar" to the original sentence if
      - it has the same number of words, and
      - each pair of adjacent words in the new sentence also occurs in the
        original sentence (the words within each pair should appear in the same
        order in the output sentence as they did in the original sentence).
    Notes:
      - The order of the sentences you output doesn't matter.
      - You must not output duplicates.
      - Your generated sentence can use a word in the original sentence more
        than once.
    Example:
      - Input: 'the cat and the mouse'
      - Output: ['and the cat and the', 'the cat and the mouse',
                 'the cat and the cat', 'cat and the cat and']
                (Reordered versions of this list are allowed.)
    """
    # BEGIN_YOUR_CODE (our solution is 17 lines of code, but don't worry if you deviate from this)
    def appended_options(a, options):
        return [a + [option] for option in options]
    words = sentence.split()
    # 找出每个单词后面的出现的单词
    next_options_map = {}
    for index, word in enumerate(words):
        if word not in next_options_map:  # 添加关键字
            next_options_map[word] = []
        if index + 1 < len(words):  # 如果不是最后一个单词，添加值
            next_options_map[word].append(words[index + 1])
    print(next_options_map)

    temp = []
    results = []
    # 遍历字典中的关键字，找出所有可能的相似句
    for key in next_options_map:
        temp = []
        temp.append([key])
        print('##########', key, '##########')
        i = 0  # 可添加单词的最大序号
        while i < len(temp):
            if len(temp[i]) < len(words) and len(next_options_map[temp[i][-1]]) > 0:
                print(
                    '-------------', temp[i], next_options_map[temp[i][-1]], '---------------')
                # 对每一个结果的最后一个单词，查找字典
                print('i=', i, temp)
                temp += appended_options(temp[i],
                                            next_options_map[temp[i][-1]])
                print('i=', i, temp)
                del temp[i]
                print('i=', i, temp)
                print('末尾选择数', len(next_options_map[temp[i][-1]]), '\n')
            else:
                i += 1
        results += list(set([' '.join(result)
                        for result in temp if len(result) == len(words)]))
    return list(set([''.join(result) for result in results]))


sentence = 'the cat and the mouse'
print('final result', mutate_sentences(sentence))
