#!/bin/bash

# Short variant discovery using GATK 4,
#   specifically the java program:
#   1. GenomeAnalysisTK.jar
#   is run, with selected subroutine:
#   2. HaplotypeCaller
# for more information on GATK see:
# https://software.broadinstitute.org/gatk/documentation/
# and for specific info on HaplotypeCaller:
# https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_haplotypecaller_HaplotypeCaller.php

${EXE_JAVA} \
    -Xmx8g -XX:ParallelGCThreads=1 -Djava.io.tmpdir=${tmp} \
    -jar ${gatk} \
    -T HaplotypeCaller \
    -R ${refast} \
    -I ${bam}${sampleID}.final.bam \
    --filter_bases_not_stored \
    --filter_mismatching_base_and_quals \
    --emitRefConfidence GVCF \
    --filter_reads_with_N_cigar \
    --genotyping_mode DISCOVERY \
    -stand_call_conf 30 \
    -stand_emit_conf 30 \
    -nct 4 \
    -variant_index_type LINEAR -variant_index_parameter 128000 \
    -o ${vcf}${sampleID}.g.vcf
