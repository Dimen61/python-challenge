txt = ""
file_object = open('2.txt')
try:
    txt = file_object.read()
finally:
    file_object.close()

# Total line of the file: 1220
line_num = 0
c_dict = {}
for c in txt:
    count = c_dict.get(c, 0)
    c_dict[c] = count + 1

for c in c_dict:
    if (c_dict[c] == 1):
        print 'Char: {0}; Num: {1}'.format(c, c_dict[c])

rare_chars = ''.join([c for c in c_dict if c_dict[c] == 1])
print rare_chars
# The answer is "equality" word.