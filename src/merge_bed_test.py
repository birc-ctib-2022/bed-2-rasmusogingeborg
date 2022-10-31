# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from pathlib import Path

file_path1=Path(r"c:\Users\Ralle\OneDrive\Universitet\Computational thinking\bed-2-rasmusogingeborg\data\merge_test")

def test_merge():
 
    with open(file_path1) as file_1:
 
        while True:
  
            # Get next line from file
            line = file_1.readline()
            line2 = file_1.readline()
            # if line is empty
            # end of file is reached
            if not line or not line2:
                break
            
            chrom1, start1, end1, feature1 = line.split()
            chrom2, start2, end2, feature1 = line2.split()

            if chrom1==chrom2:
                assert int(start1)<=int(start2)
            else:
                assert chrom1<chrom2
