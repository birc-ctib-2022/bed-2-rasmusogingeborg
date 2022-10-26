"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from typing import TextIO
from bed import (
    parse_line, print_line, BedLine
)


def read_bed_file(f: TextIO) -> list[BedLine]:
    """Read an entire sorted bed file."""
    # Handle first line...
    line = f.readline()
    if not line:
        return []

    res = [parse_line(line)]
    for line in f:
        feature = parse_line(line)
        prev_feature = res[-1]
        assert prev_feature.chrom < feature.chrom or \
            (prev_feature.chrom == feature.chrom and
             prev_feature.chrom_start <= feature.chrom_start), \
            "Input files must be sorted"
        res.append(feature)

    return res


def merge(f1: list[BedLine], f2: list[BedLine], outfile: TextIO) -> None:
    """Merge features and write them to outfile.
    >>> merge([BedLine(chrom='chr1', chrom_start=600, chrom_end=601, name='qux'), \
        BedLine(chrom='chr1', chrom_start=20100, chrom_end=20101, name='qux'), \
        BedLine(chrom='chr2', chrom_start=199, chrom_end=200, name='qux'), \
        BedLine(chrom='chr2', chrom_start=200, chrom_end=201, name='qux'), \
        BedLine(chrom='chr3', chrom_start=0, chrom_end=1, name='qux')], \
        [BedLine(chrom='chr1', chrom_start=600, chrom_end=601, name='qax'), \
        BedLine(chrom='chr1', chrom_start=20100, chrom_end=20101, name='qax'), \
        BedLine(chrom='chr2', chrom_start=199, chrom_end=200, name='qax'), \
        BedLine(chrom='chr2', chrom_start=200, chrom_end=201, name='qax'), \
        BedLine(chrom='chr3', chrom_start=0, chrom_end=1, name='qax')])
    """
    # Antag at hver nucleotid kun én gang i hver fil.
    # Hvordan håndtere, hvis et nucleotid ikke findes i begge filer men kun én. 
    # Hvis samme chromosome og samme chrom_start, skal features merges. 
    for nucleotide1 in f1:
        for nucleotide2 in f2:
            if nucleotide1.chrom == nucleotide2.chrom and nucleotide1.chrom_start == nucleotide2.chrom_start:
                print(BedLine(nucleotide1.chrom_start, nucleotide1.chrom_start, nucleotide1.chrom_end, (nucleotide1.name, nucleotide2.name)))

        



def main() -> None:
    """Run the program."""
    # Setting up the option parsing using the argparse module
    argparser = argparse.ArgumentParser(description="Merge two BED files")
    argparser.add_argument('f1', type=argparse.FileType('r'))
    argparser.add_argument('f2', type=argparse.FileType('r'))
    argparser.add_argument('-o', '--outfile',  # use an option to specify this
                           metavar='output',   # name used in help text
                           type=argparse.FileType('w'),  # file for writing
                           default=sys.stdout)

    # Parse options and put them in the table args
    args = argparser.parse_args()

    # With all the options handled, we just need to do the real work
    features1 = read_bed_file(args.f1)
    features2 = read_bed_file(args.f2)
    print(features1)
    print(features2)
    #merge(features1, features2, args.outfile)


if __name__ == '__main__':
    main()
