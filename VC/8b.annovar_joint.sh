#!/bin/bash

# This step uses annovar, specifically:
#   1.table_annovar.pl
# from the annovar library to annotate jointly called variants.
# For more information, please see:
# http://annovar.openbioinformatics.org/en/latest/user-guide/startup/

# define some helpful variables:
humandb=${annot}humandb/
data=${vcf}joint_call.vcf
out=${vcf}joint_call.annot.vcf

# annotate the variants:
${annot}table_annovar.pl ${data} ${humandb} -buildver hg19 -out ${out} \
-remove -protocol refGene,cytoBand,exac03,avsnp147,dbnsfp30a,\
1000g2014oct_all,1000g2014oct_afr,\
1000g2014oct_eas,1000g2014oct_eur,ljb26_all \
-operation g,r,f,f,f,f,f,f,f,f -nastring . -vcfinput

