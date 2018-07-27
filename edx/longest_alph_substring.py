s = 'rhmvadzewpfdcfjvw'
n = 0
count = 0
position = 0
maxv = -1
lstring = ''
while (n < len(s)-1):
    if (s[n] <= s[n+1]):
        count += 1
    else:
        if (count > maxv):
            lstring = s[position:position+count+1]
            maxv = count
        count = 0
        position = n+1
    n += 1
if (count != 0 and count > maxv):
    lstring = s[position:position+count+1]
print('Longest substring in alphabetical order is: ' + lstring)
