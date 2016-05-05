######################################
#Implementation 1
######################################
txt = ''
# file_object = open('2.txt')
# try:
#     txt = file_object.read()
# finally:
#     file_object.close()
with open('2.txt') as file_object:
    txt = file_object.read() # Would read in white space char

# Total line of the file: 1220
line_num = 0
c_dict = {}
for c in txt:
    count = c_dict.get(c, 0)
    c_dict[c] = count + 1

for c in c_dict:
    if (c_dict[c] == 1):
        print 'Char: {0}; Num: {1}'.format(c, c_dict[c])

# rare_chars = ''.join([c for c in c_dict if c_dict[c] == 1])
# print rare_chars
rare_chars = ''.join([c for c in txt if c_dict[c] == 1])
print 'Answer:', rare_chars
# The answer is "equality" word.

######################################
#Implementation 2
######################################
import collections
txt = ''.join([line.rstrip() for line in open('2.txt')]) # One line to open a file
occurrence = collections.OrderedDict() # A subclass of Dict
for c in txt:
    occurrence[c] = occurrence.get(c, 0) + 1
# Print answer
print 'Answer:', ''.join([c for c in occurrence if occurrence[c] == 1])

######################################
#Implementation 3
######################################
import string
txt = ''.join([line.rstrip() for line in open('2.txt')])
print 'Answer:', filter(lambda x: x in string.letters , txt)
