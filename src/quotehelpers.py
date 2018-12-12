from operator import itemgetter

def reverse_sort_by_id(list):
    return sorted(list, key=itemgetter('id'), reverse=True)

def int_to_id(int):
    strint = str(int)
    missing_zeroes = (6-len(strint))*'0'
    return missing_zeroes + strint