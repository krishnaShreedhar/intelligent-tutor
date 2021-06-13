def tf(tf_fid=1):
    dict_tf_functions = {
        1: tf_one,
    }
    return dict_tf_functions[tf_fid]()


def idf(idf_fid=1):
    dict_idf_functions = {
        1: idf_one,
    }
    return dict_idf_functions[idf_fid]()


def tf_idf():
    return tf() * idf()


def tf_one():
    return 1


def idf_one():
    return 1


def binarize(x):
    if x >= 1:
        val = 1
    else:
        val = 0
    return 0


def weighted_binarize(x, r):
    if x == 1:
        val = r
    elif x > 1:
        val = 1
    else:
        val = 0
    return 0
