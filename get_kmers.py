# get_kmers.py

def get_kmers(k, alph=['A','C','G','T']):
    kmers = []
    k = int(k)
    if k<=0:
        return kmers
    if k==1:
        return alph
    kmers = []
    for s in get_kmers(k-1,alph):
        for a in alph:
            sa = str(s + a)
            kmers.append(sa)
    return kmers

def main():
    usage = "file.py -i infile -o outfile etc...\n"
    return

## Default main function

if __name__ == '__main__':
    main()
