import argparse, sys

def main(prefix, dryRun, action, infile, outfile):
    sys.stdout = outfile    # Make print() print to the right output stream
    inputText = infile.read()

    # Do useful things
    print(prefix + inputText.lower())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert input to lowercase and add a prefix.')
    parser.add_argument("PREFIX", help="Prefix to be added")
    parser.add_argument("--dry-run", action="store_true", help="Dry run.")
    parser.add_argument("--action", default="search", choices=["search", "test"], help="Action")
    parser.add_argument('--infile', type=argparse.FileType('r'), default=sys.stdin, help="Input file")
    parser.add_argument('--outfile', type=argparse.FileType('w'), default=sys.stdout, help="Output file")
    args = parser.parse_args()
    main(args.PREFIX, args.dry_run, args.action, args.infile, args.outfile)
