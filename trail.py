#!/usr/bin/python2
import sys
import time

def main(fname):
    oldfsize = 0
    oldset = []
    chunk = 256
    while True:
        with open(fname, 'rt') as f:
            f.seek(1, 2) 
            fsize = f.tell()
            if fsize < chunk and oldfsize != fsize:
                f.seek(0, 0)
                if fsize > 2:
                    lines = f.readlines()[-1]
                    print ''.join(lines).strip()
                oldfsize = fsize
            if fsize > oldfsize:
                f.seek(fsize-chunk, 0)
                set = f.readlines()[-4:]
                newset = [x for x in set if x not in oldset]
                print ''.join(newset).strip()
                oldset = set
            else: time.sleep(0.001)
        oldfsize = fsize

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print """
Usage: trail.py <logfile>
"""
            sys.exit(1)
        else:
            logfile = sys.argv[1]
        main(logfile)
    except KeyboardInterrupt:
        sys.exit(0)
