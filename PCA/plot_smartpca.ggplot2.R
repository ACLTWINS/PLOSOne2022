#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

library(dplyr)
library(ggplot2)
library(grid)
library(gridExtra)
library(RColorBrewer)

pdf("MERGE2.smart22.pdf", width = 980, height = 780)

eval <- read.table(args[1])

evec1.pc <- round(eval[1,1]/sum(eval)*100,digits=2)
evec2.pc <- round(eval[2,1]/sum(eval)*100,digits=2)

evec <- read.table(args[2],header=T)

evec <- mutate(evec, symbol=(1:nrow(evec)) %% 26)

#evec$PC1

xlab <- paste("\n\n",evec1.pc, "% of observed genetic variation (PC1)", sep="")
ylab <- paste("\n",evec2.pc, "% of observed genetic variation (PC2)", sep="")

n <- length(evec$symbol)
#qual_col_pals = brewer.pal.info[brewer.pal.info$category == 'qual',]
#col_vector = unlist(mapply(brewer.pal, qual_col_pals$maxcolors, rownames(qual_col_pals)))

color2 <- grDevices::colors()[grep('gr(a|e)y', grDevices::colors(), invert = T)]
col2 <- sample(color2, n)
col2 

p <- ggplot(evec,aes(x=PC1,y=PC2)) #+ scale_color_viridis()

#p <- p+geom_point(aes(color=pop,pch=pop),alpha = 0.5,stroke=1.4) + xlab(xlab) + ylab(ylab) ##+scale_x_log10()
p <- p +  theme_light(base_size = 18) + theme(panel.grid.minor = element_blank())
#jit <- position_jitter(seed = 123)  
#p <- p +  geom_jitter(aes(shape = Ethnics, color = Ethnics),size =4,position = jit) + scale_shape_manual(values = evec$symbol)
#p <- p+scale_colour_manual(values = col2)+ theme(legend.position = "bottom")
#p <- p + theme(legend.box.just = "left",panel.background = element_rect(fill = 'grey75'),panel.grid.major = element_line(colour = "orange", size=1), panel.grid.minor = element_line(colour = "blue"))

#p <- p +  opts(legend.key.width=unit(5,"line"))+opts(legend.key.height=unit(3,"line"))
p
dev.off()

###rep(15:18, len = 8)


#theme(legend.text = element_text(colour="blue", size = 16, face = "bold"))
