#!/bin/bash

# This script uses the Picard program library,
#   specifically the following java programs:
#   1. MarkDuplicates.jar
# to mak duplicates in the sorted .bam files.
# For more info on Picard, see:
# https://broadinstitute.github.io/picard/command-line-overview.html

# Mark duplicates using MarkDuplicates.jar:
${EXE_JAVA} \
    -Xmx2g -XX:ParallelGCThreads=1 -Djava.io.tmpdir=${tmp} \
    -jar ${picard}MarkDuplicates.jar \
    INPUT=${bam}${sampleID}.sorted.bam \
    OUTPUT=${bam}${sampleID}.sorted.marked.bam \
    METRICS_FILE=${tmp}${sampleID}_L1_index6.metric CREATE_INDEX=true \
    VALIDATION_STRINGENCY=LENIENT
