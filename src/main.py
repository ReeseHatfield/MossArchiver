import sys

def main():
    link = parse_args()
    print(f"Link: {link}")


def parse_args():
    if len(sys.argv) != 2:
        sys.exit(1)
        
    return sys.argv[1]

if __name__ == "__main__":
    main()
    