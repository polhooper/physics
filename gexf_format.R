#..thanks to https://gist.github.com/Vessy/6047440
#  https://rulesofreason.wordpress.com/2012/11/05/network-visualization-in-r-with-the-igraph-package/

require('igraph')
require('readr')
require('plyr')
require('dplyr')
require('rgexf')
require('ggplot2')

print('Importing and pre-processing data...')
topic_weights <- read_csv('topic_weights.csv')
data <- read_delim('cit-HepTh.txt', delim = '\t', skip = 4, col_names = FALSE)
#data <- data[sample(nrow(data), 5000), ]
ids <- read_csv('ids.csv', col_names = FALSE)[, 1]

#..create a mapping between the dominant topic and the id
topic_key <- data.frame(
  id = ids[[1]], 
  topic = apply(topic_weights, 1, function(x) which(x == max(x))[1])
)
  
#..cast input data as graph data: 
gD <- simplify(graph.data.frame(data, directed=TRUE))
#degAll <- degree(gD, v = V(gD), mode = "all")
#qplot(degAll)

#..subset graph to only contain papers with N-degrees of connections 
bad_vs <- V(gD)[degree(gD) < 50] #identify those vertices part of less than 50 edges
gD <- delete.vertices(gD, bad_vs) 

vs <- V(gD)
vnames <- as.numeric(names(vs))

#..set degree attribute for each node
degAll <- degree(gD, v = vs, mode = "all")
gD <- set.vertex.attribute(gD, "degree", index = vs, value = degAll)

#..set topic attribute for each node (vertex)
topic_key_2 <- filter(topic_key, id %in% vnames)
topic_key_2 <- topic_key_2[sapply(vnames, function(x) which(topic_key_2$id == x)), ]
gD <- set.vertex.attribute(gD, "topic", index = vs, value = topic_key_2$topic)

print('Writing gexf file. This takes a little while...')
g_gexf <- igraph.to.gexf(gD)
sink('physics.gexf', type = 'output')
g_gexf
sink()
