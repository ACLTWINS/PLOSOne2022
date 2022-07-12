#!/bin/bash

# This script uses the Picard program library,
#   specifically the following java programs:
#   1. FixMateInformation.jar
# and samtools programs,
#   specifically:
#   1. samtools calmd
#   2. samtools index

# fix mating information using FixMateInformation.jar:
${EXE_JAVA} \
    -Xmx2g -XX:ParallelGCThreads=1 -Djava.io.tmpdir=${tmp}flx-auswerter \
    -jar ${picard}FixMateInformation.jar \
    INPUT=${bam}${sampleID}.sorted.marked.bam \
    OUTPUT=${bam}${sampleID}.sorted.marked.fixed.bam \
    SO=coordinate VALIDATION_STRINGENCY=LENIENT CREATE_INDEX=true

# generate the MD tag for *.sorted.marked.fixed.bam files using samtools calmd:
${samtools} calmd -Erb ${bam}${sampleID}.sorted.marked.fixed.bam ${refast} > ${bam}${sampleID}.final.bam

# index the coordinate-sorted bam files *.final.bam using samtools index:
${samtools} index ${bam}${sampleID}.final.bam

