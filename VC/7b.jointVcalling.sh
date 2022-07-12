#!/bin/bash

# this step uses:
#   1. samtools mpileup
#   2. bcftools call
# to first join all samples (with 1.), and then to joint call
# variants over the sample set (with 2.)

# create array of sample *.final.bam file names:
sampleIDs=($(cat ${fastq}sampleIDs.txt))
sampleFiles=()
for id in ${sampleIDs[@]}
do
    sampleFiles+=("${bam}${id}"'.final.bam')
done

# combine sample *.final.bam files using samtools mpileup,
# and do joint calling of variants for whole sample set with bcftools:
${samtools} mpileup -ugf ${refast} ${sampleFiles[@]} | ${EXE_BCFTOOL} call -mv > ${vcf}joint_call.vcf
