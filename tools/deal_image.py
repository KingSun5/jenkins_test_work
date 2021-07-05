import argparse


def init_option():
   
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dst', dest='dst path', default=False, help='jenkins workspace')
    parser.add_argument('-n', '--name', dest='build id', default=False, help='build task name')
    args = parser.parse_args()
    return args

def main():
    args = init_option()
    print("System action: build start!!!! ")
    print(args)

if __name__ == "__main__":
    main()
