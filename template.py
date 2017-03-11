# template.py

def main():
    usage = "file.py -i infile -o outfile etc...\n"
    argvals  = parse_arguments(sys.argv)
    infile   = get_argval("i", argvals)
    outfile  = get_argval("o",argvals)
    
    if not infile == None:
        pass
    else:
        print usage
    return

## Default main function

if __name__ == '__main__':
    main()
