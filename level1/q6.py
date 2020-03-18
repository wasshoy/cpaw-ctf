def encrypt(s):
    if not type(s) is str:
        print('Please give me string!')
        return
    alphabets = tuple(chr(ord('a') + i) for i in range(26)) + tuple(chr(ord('A') + i) for i in range(26))    
    return ''.join([chr(ord(c) - 3) if c in alphabets else c for c in s])

if __name__ == '__main__':
    res = encrypt('fsdz{Fdhvdu_flskhu_lv_fodvvlfdo_flskhu}')
    print(res)