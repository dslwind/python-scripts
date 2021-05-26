with open('ifw-20181211-160540.xml', 'r') as f:
    lines = f.readlines()

lines_w = set([])
with open('out.xml', 'w') as f:
    for line in lines:
        if line in lines_w:
            continue
        f.write(line)
        lines_w.add(line)