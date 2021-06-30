import argparse


def init_option():
   
    parser = argparse.ArgumentParser()
    parser.add_argument('-0', '--debug', dest='debug', default=False, help='Build debug')
    args = parser.parse_args()
    return args

def main():
    args = init_option()
    print("System action: build start!!!! ")

if __name__ == "__main__":
    main()
