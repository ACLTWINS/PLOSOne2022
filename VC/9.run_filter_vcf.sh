#!/bin/bash

# this step uses a python script to cut all variants
# that have a quality score lower than a chosen
# threshold.
# a general call of the python script is:
# python 9.filter_vcf.py \
#   <annotated vcf> \
#   <outfile> \
#   <cutoff:integer>

# load config file:
. /mnt/lustre/users/dfeldmann/PhD_Project/config.sh

# call python script to filter annotated vcf file:
python ${wk}script/9.filter_vcf.py \
    ${vcf}SEPTEMBER.FA.bcftools.vcf \
    ${vcf}SEPTEMBER.FA.filtered.2.vcf \
    50
