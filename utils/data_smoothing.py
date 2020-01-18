def plus_one():
    pass


def good_turing(corpus, words):
    """

    :param corpus:
    :param words:
    :return:
    """
    for w in words:
        if w in corpus:
            raise ValueError('未登录词有误!')

    r_dict = {}
    for w in corpus:
        if r_dict.get(w) is None:
            r_dict[w] = 1
        else:
            r_dict[w] += 1

    n_dict = {}
    for r in r_dict.values():
        if n_dict.get(r) is None:
            n_dict[r] = 1
        else:
            n_dict[r] += 1

    prob_of_words = n_dict[1] / len(words)
    total = prob_of_words

    temp_prob = {}
    for k, v in r_dict:
        if v < max(r_dict.values()):
            r_star = (r_dict[k] + 1) * n_dict[r_dict[k] + 1] / n_dict[r_dict[k]]
            temp_prob[k] = r_star / len(corpus)
        else:
            temp_prob[k] = r_dict[k] / len(corpus)
        total += temp_prob[k]

    # 归一化
    ret = {}
    for w in corpus:
        ret[w] = temp_prob[w] / total
    for w in words:
        ret[w] = prob_of_words / total
    return ret


def katz_back_off():
    pass
