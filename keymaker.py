def shift_characters(word, shift):
    """
    >>> shift_characters('abby', 5)
    'fggd'
    """
    shifted_char_list = [chr((ord(char) - 97 + shift) % 26 + 97) for char in word]
    return "".join(shifted_char_list)


def pad_up_to(word, shift, n):
    """
    >>> pad_up_to('abb', 5, 11)
    'abbfggkllpq'
    """
    padded_up = ''
    while len(padded_up) <= n:
        padded_up += word
        word = shift_characters(word, shift)
    return padded_up[:n]


def abc_mirror(word):
    """
    >>> abc_mirror('abcd')
    'zyxw'
    """
    mirrored_word = ''
    for i in range(len(word)):
        mirrored_word += chr(ord('z') - (ord(word[i]) - ord('a')))
    return mirrored_word


def create_matrix(word1, word2):
    """
    >>> create_matrix('mamas', 'papas')
    ['bpbph', 'mamas', 'bpbph', 'mamas', 'esesk']
    """
    matrix = []
    for i in range(len(word2)):
        matrix.append(shift_characters(word1, ord(word2[i])-97))
    return matrix
        

def zig_zag_concatenate(matrix):
    """
    >>> zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl'])
    'adgjkhebcfil'
    """
    pass


def rotate_right(word, n):
    """
    >>> rotate_right('abcdefgh', 3)
    'fghabcde'
    """
    pass


def get_square_index_chars(word):
    """
    >>> get_square_index_chars('abcdefghijklm')
    'abej'
    """
    pass


def remove_odd_blocks(word, block_length):
    """
    >>> remove_odd_blocks('abcdefghijklm', 3)
    'abcghim'
    """
    pass


def reduce_to_fixed(word, n):
    """
    >>> reduce_to_fixed('abcdefghijklm', 6)
    'bafedc'
    """
    pass


def hash_it(word):
    """
    >>> hash_it('morpheus')
    'trowdo'
    """
    padded = pad_up_to(word, 15, 19)
    elongated = zig_zag_concatenate(create_matrix(padded, abc_mirror(padded)))
    rotated = rotate_right(elongated, 3000003)
    cherry_picked = get_square_index_chars(rotated)
    halved = remove_odd_blocks(cherry_picked, 3)
    key = reduce_to_fixed(halved, 6)
    return key


#if __name__ == '__main__':
    name = input("Enter your name! ").lower()
    print(f'Your key: {hash_it(name)}')
