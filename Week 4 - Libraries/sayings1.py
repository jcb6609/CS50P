import sys

from sayings import hello # from 'file' import 'function'

def main():
    if(len(sys.argv) == 2):
        hello(sys.argv[1])

main()