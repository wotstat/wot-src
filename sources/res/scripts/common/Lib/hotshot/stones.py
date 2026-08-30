import errno, hotshot, hotshot.stats, sys, test.pystone

def main(logfile):
    p = hotshot.Profile(logfile)
    benchtime, stones = p.runcall(test.pystone.pystones)
    p.close()
    print b'Pystone(%s) time for %d passes = %g' % (
     test.pystone.__version__, test.pystone.LOOPS, benchtime)
    print b'This machine benchmarks at %g pystones/second' % stones
    stats = hotshot.stats.load(logfile)
    stats.strip_dirs()
    stats.sort_stats(b'time', b'calls')
    try:
        stats.print_stats(20)
    except IOError as e:
        if e.errno != errno.EPIPE:
            raise

    return


if __name__ == b'__main__':
    if sys.argv[1:]:
        main(sys.argv[1])
    else:
        import tempfile
        main(tempfile.NamedTemporaryFile().name)
