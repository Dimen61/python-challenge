import string

def explore():
    for c in string.ascii_uppercase:
        if c == 'K':
            print 'K ord: {0}; M ord: {1}'.format(ord('K'), ord('M'))
        elif c == 'O':
            print 'O ord: {0}; Q ord: {1}'.format(ord('O'), ord('Q'))
        elif c == 'E':
            print 'E ord: {0}; G ord: {1}'.format(ord('E'), ord('G'))

#### Mehthod 1 #####################
## Don't use string.maketrans
####################################
def decode(c):
    assert type(c) == str
    res = chr(ord(c) + 2)
    if res == '{':
        res = 'a'
    elif res == '"':
        res = ' '
    elif res == '|':
        res = 'b'
    elif res == ')':
        res = "'"
    elif res == '0':
        res = '.'
    elif res == '*':
        res = '('
    elif res == '+':
        res = ')'
    return res

def transform(txt):
    assert type(txt) == str
    res_txt = ""
    for c in txt:
        res_txt += decode(c)
    return res_txt

#### Mehthod 2 #####################
## Use string.maketrans
####################################

def transform(txt):
    assert type(txt) == str
    res_txt = ""
    for c in txt:
        res_txt += chr(ord(c) + 2)
    transtab = string.maketrans('{"|)0*+', "a b'.()")
    return res_txt.translate(transtab)

txt = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
print transform(txt)

url = 'map'
print transform(url)