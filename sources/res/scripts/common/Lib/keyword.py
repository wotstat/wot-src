__all__ = [
 b'iskeyword', b'kwlist']
kwlist = [
 2, 
 3, 
 4, 
 5, 
 6, 
 7, 
 8, 
 9, 
 10, 
 11, 
 12, 
 13, 
 14, 
 15, 
 16, 
 17, 
 18, 
 19, 
 20, 
 21, 
 22, 
 23, 
 24, 
 25, 
 26, 
 27, 
 28, 
 29, 
 30, 
 31, 
 32]
iskeyword = frozenset(kwlist).__contains__

def main():
    import sys, re
    args = sys.argv[1:]
    iptfile = args and args[0] or b'Python/graminit.c'
    if len(args) > 1:
        optfile = args[1]
    else:
        optfile = b'Lib/keyword.py'
    fp = open(iptfile)
    strprog = re.compile(b'"([^"]+)"')
    lines = []
    for line in fp:
        if b'{1, "' in line:
            match = strprog.search(line)
            if match:
                lines.append(b"        '" + match.group(1) + b"',\n")

    fp.close()
    lines.sort()
    fp = open(optfile)
    format = fp.readlines()
    fp.close()
    try:
        start = format.index(b'#--start keywords--\n') + 1
        end = format.index(b'#--end keywords--\n')
        format[start:end] = lines
    except ValueError:
        sys.stderr.write(b'target does not contain format markers\n')
        sys.exit(1)

    fp = open(optfile, b'w')
    fp.write((b'').join(format))
    fp.close()
    return


if __name__ == b'__main__':
    main()
