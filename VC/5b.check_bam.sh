#!/bin/bash

# this step uses samtools, specifically:
#   1. samtools view
# to check the bam files just before we do variant calling.
# for more information, see:
# http://www.htslib.org/doc/samtools.html

${samtools} view -h ${bam}${sampleID}.final.bam | cut -f3 | uniq |sort  > ${wk}CHR/${sampleID}.chr
