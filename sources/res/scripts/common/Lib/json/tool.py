import sys, json

def main():
    if len(sys.argv) == 1:
        infile = sys.stdin
        outfile = sys.stdout
    elif len(sys.argv) == 2:
        infile = open(sys.argv[1], b'rb')
        outfile = sys.stdout
    elif len(sys.argv) == 3:
        infile = open(sys.argv[1], b'rb')
        outfile = open(sys.argv[2], b'wb')
    else:
        raise SystemExit(sys.argv[0] + b' [infile [outfile]]')
    with infile:
        try:
            obj = json.load(infile)
        except ValueError as e:
            raise SystemExit(e)

    with outfile:
        json.dump(obj, outfile, sort_keys=True, indent=4, separators=(b',', b': '))
        outfile.write(b'\n')
    return


if __name__ == b'__main__':
    main()
