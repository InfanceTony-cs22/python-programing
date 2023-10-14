from itertools import groupby

def compress_string(s):
    compressed = [(len(list(g)), int(k)) for k, g in groupby(s)]
    result = ' '.join([f'({count}, {key})' for count, key in compressed])
    return result

if __name__ == "__main__":
    s = input()
    compressed_string = compress_string(s)
    print(compressed_string)
