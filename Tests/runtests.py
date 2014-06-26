#!/usr/bin/env python
import sys
import os.path

if __name__ == '__main__':
    dpath = os.path.dirname(__file__)
    if dpath:
        os.chdir(dpath)

    sys.path.insert(0, os.path.realpath(os.path.pardir))
    import srllib.testing
    srllib.testing.run_tests("srllib")
