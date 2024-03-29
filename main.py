import argparse, sys, tqdm

def main(prefix, dryRun, action, infile, outfile):
    # Check that input has data and make print() print to outfile
    sys.stdout = outfile
    if infile.isatty():
        print("ERROR: Input is a terminal, use a file or pipe data to stdin.")
        exit(1)
    inputText = infile.read()

    # Do useful things
    result = ""
    result += prefix
    for i in tqdm.tqdm(range(len(inputText))):
        c = inputText[i]
        result += c.lower()

    # If you need to use csv files:
    # inRows = [row for row in csv.DictReader(infile)]
    # writer = csv.DictWriter(outfile, fieldnames=headerStrings)
    # writer.writeheader()
    # writer.writerows(outRows)

    # Print the output
    print(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="convert input to lowercase and add a prefix.")
    parser.add_argument('PREFIX', help="prefix to be added")
    parser.add_argument('--dry-run', action='store_true', help="dry run")
    parser.add_argument('--action', default='search', choices=['search', 'test'], help="action")
    parser.add_argument('--infile', type=argparse.FileType('r'), default=sys.stdin, help="input file")
    parser.add_argument('--outfile', type=argparse.FileType('w'), default=sys.stdout, help="output file")
    args = parser.parse_args()
    main(args.PREFIX, args.dry_run, args.action, args.infile, args.outfile)
