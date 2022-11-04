"""Tool for cleaning up a BED file."""

import argparse
from re import A  # we use this module for option parsing. See main for details.

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
    
    """
    # Input bedlines er sorted. 
    # Hver region kun én nucleotid lang. 

    a=0
    b=0

    while a <= len(f1)-1 and b <= len(f2)-1:
        if f1[a][0]==f2[b][0]:
            if f1[a][1]<f2[b][1]:
                print_line(f1[a],outfile)
                a+=1
            elif f1[a][0]>f2[b][0]:
                print_line(f1[b],outfile)
                b+=1
            elif f1[a][1]==f2[b][1]:
                print_line(f1[a],outfile)
                a+=1
                print_line(f1[b],outfile)
                b+=1
                
            
        else:
            if f1[a][0]<f2[b][0]:
                print_line(f1[a],outfile)
                a+=1
            elif f1[a][0]>f2[b][0]:
                print_line(f1[b],outfile)
                b+=1
    
    if a != len(f1)-1:
        for i in range(a,len(f1)-1):
            print_line(f1[i],outfile)
    elif b != len(f2)-1:
        for i in range(b,len(f2)-1):
            print_line(f1[i],outfile)


   



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
    merge(features1, features2, args.outfile)


if __name__ == '__main__':
    main()
