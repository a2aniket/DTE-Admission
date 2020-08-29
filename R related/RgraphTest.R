library(plotly)
captest<-read.csv("RgraphTest.csv")
output <- plot_ly(captest, x = ~Gender, y = ~sub.group.name, type = 'scatter', mode = 'lines')
output