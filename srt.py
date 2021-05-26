with open('sn.txt', 'r') as f:
    s = f.readlines()

with open('sn1.srt', 'w') as f:
    for i in range(len(s)):
        if s[i] == s[i - 4] and s[i] != '\n':
            pass
        else:
            f.write(s[i])