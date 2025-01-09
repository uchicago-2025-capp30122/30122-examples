# argdemo.py
import sys

if __name__ == "__main__":
    print("program name:", sys.argv[0])
    for idx, arg in enumerate(sys.argv[1:]):
        print(f"argv[{idx + 1}]", arg)
