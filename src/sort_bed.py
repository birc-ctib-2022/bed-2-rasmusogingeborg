"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from typing import TextIO
from bed import (
    read_bed_file, print_line, Table, BedLine
)
# Unødvendigt med BedLine?

def sort_file(table: Table) -> None:
    """Sort each chromosome and update the table.""" # a global 
    # variable is modified. None is returned.
    for chrom, features in table.items(): # features is a list of 
        # BedLines with a specific chrom.
        # Here we iterate through all the chromosomes in the file.
        # You need to sort `features` with respect to chrom_start
        # and then update the table
        for i in range(len(features)): # iterate over all BedLines in
        # list. 
            print(features[i].chrom_start)
        table[chrom] = features  # features should be sorted here

table = {'chr1': [BedLine(chrom='chr1', chrom_start=20100, chrom_end=20101,  
name='foo'), BedLine(chrom='chr1', chrom_start=600, chrom_end=601, 
name='baz')], 'chr3': [BedLine(chrom='chr3', chrom_start=0, 
chrom_end=1, name='bar')], 'chr2': [BedLine(chrom='chr2', chrom_start 
=200, chrom_end=201, name='qux'), BedLine(chrom='chr2', chrom_start= 
199, chrom_end=200, name='qax')]}
print(sort_file(table))

def print_file(table: Table, outfile: TextIO) -> None:
    """Write the content of table to outfile."""
    for chrom in sorted(table.tbl):
        for feature in table.get_chrom(chrom):
            print_line(feature, outfile)




def main() -> None:
    """Run the program."""
    # Setting up the option parsing using the argparse module
    argparser = argparse.ArgumentParser(description="Sorts a BED file")
    # 'infile' is either provided as an input file name or stdin
    argparser.add_argument('infile',
                           nargs='?',                    # 0 or 1 arguments
                           type=argparse.FileType('r'),  # file for reading
                           default=sys.stdin)
    # 'outfile' is either provided as a file name or we use stdout
    argparser.add_argument('outfile',
                           nargs='?',                    # 0 or 1 arguments
                           type=argparse.FileType('w'),  # file for writing
                           default=sys.stdout)

    # Parse options and put them in the table args
    args = argparser.parse_args()

    # With all the options handled, we just need to do the real work
    table = read_bed_file(args.infile)
    sort_file(table)
    print_file(table, args.outfile)


if __name__ == '__main__':
    main()
