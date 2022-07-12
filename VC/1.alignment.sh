#!/bin/bash

# this step uses the Burrows-Wheeler Aligner, bwa mem,
# to align the reads against the human reference (refast).
# for more info, see:
# http://bio-bwa.sourceforge.net/

${bwa} mem \
    -M \
    -t 12 \
    ${refast} \
    ${fastq}${sampleID}_L001_R1_001.trim.fastq.gz ${fastq}${sampleID}_L001_R2_001.trim.fastq.gz \
    > ${alg_sam}${sampleID}.sam
