#!/bin/bash

# This script uses the Picard program library,
#   specifically the following java programs:
#   1. AddOrReplaceReadGroups.jar
#   2. SortSam.jar
# to first convert .sam files to .bam, and then to
# sort the bam files.
# for more info on Picard, see
# https://broadinstitute.github.io/picard/

# Convert .sam files to .bam using AddOrReplaceReadGroups.jar:
${EXE_JAVA} \
    -Xmx2g -XX:ParallelGCThreads=1 \
    -Djava.io.tmpdir=${tmp} -jar ${picard}AddOrReplaceReadGroups.jar \
    I=${alg_sam}${sampleID}.sam \
    O=${bam}${sampleID}.bam \
    VALIDATION_STRINGENCY=LENIENT CREATE_INDEX=true \
    SO=queryname ID=${sampleID} LB=FCC007KABXX PU=GTCAATTT PL=illumina SM=${sampleID}

# sort the .bam files using SortSam.jar
${EXE_JAVA} -Xmx2g -XX:ParallelGCThreads=1 -Djava.io.tmpdir=${tmp} \
    -jar ${picard}SortSam.jar \
    SO=coordinate \
    INPUT=${bam}${sampleID}.bam \
    OUTPUT=${bam}${sampleID}.sorted.bam \
    VALIDATION_STRINGENCY=LENIENT CREATE_INDEX=true


