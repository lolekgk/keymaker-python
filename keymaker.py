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
    result = []
    for i in range(len(matrix[0])):
        if i % 2 == 0:
            result.extend([row[i] for row in matrix])
        else:
            result.extend([row[i] for row in matrix[::-1]])
    return "".join(result)

    
def rotate_right(word, n):
    """
    >>> rotate_right('abcdefgh', 3)
    'fghabcde'
    """
    if n >= 0:
        for num in range(n):
            word = word[-1] + word[:-1]
    else:
        for num in range(-n): 
            word = word[1:] + word[0]
    return word


def get_square_index_chars(word):
    """
    >>> get_square_index_chars('abcdefghijklm')
    'abej'
    """
    last_index = len(word)
    return "".join([word[i**2] for i in range(last_index) if i**2 < last_index])
    

def remove_odd_blocks(word, block_length):
    """
    >>> remove_odd_blocks('abcdefghijklm', 3)
    'abcghim'
    """
    blocks = [word[i:i+block_length] for i in range(0, len(word), block_length)]
    return "".join([blocks[i] for i in range(0, len(blocks), 2)])


def reduce_to_fixed(word, n):
    """
    >>> reduce_to_fixed('abcdefghijklm', 6)
    'bafedc'
    """
    word = word[:n]
    for num in range(n//3):
        word = word[1:] + word[0]
    return "".join(word[::-1])


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


if __name__ == '__main__':
    name = input("Enter your name! ").lower()
    print(f'Your key: {hash_it(name)}')
