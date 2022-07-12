# READ THE LINES BELOW AS NOT ALL THE COMMANDS ARE R COMMANDS


# we will use GCTA to calculate PCA in this dataset

eigenvals = read.table('MERGED_pruned.eigenval')
eigenvals$percvar = eigenvals$V1 / sum(eigenvals$V1)

plot(1:20,eigenvals$percvar[1:20])

pcs = read.table('MERGED_pruned2.eigenvec')
# edit headers

names(pcs)[1:8] = c('POP','IID','PC1','PC2','PC3','PC4','PC5','PC6')

# again, here's the code to plot, save it in a pdf labeled, e.g.:
# Africa55K_10Pops_PC1_vs_PC2.pdf

png("MERGED_pruned2.png", width = 780, height = 480)

plot(pcs$PC1,pcs$PC2,pch=20,col=pcs$POP,xlab='PC1',ylab='PC2')
legend('bottomleft',legend=unique(pcs$POP),col=unique(pcs$POP),pch=20)

# try again with other PCs. What populations pop out?
dev.off()
