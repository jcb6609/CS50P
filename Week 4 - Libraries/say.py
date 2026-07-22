import cowsay # installed when we wrote 'pip install cowsay'
import sys

if(len(sys.argv) == 3):
    cowsay.cow(f"hello, {sys.argv[1]}")
    cowsay.trex(f"hello, {sys.argv[2]}")
