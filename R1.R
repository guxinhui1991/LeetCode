BubbleSort = function(c){
  len = length(c)
  pnl = c[2:len] - c[1:(len-1)]
  serieMaxLoss = pnl[1]
  for (i in 1:(len-1)){
    if(serieMaxLoss > pnl[i])
      serieMaxLoss = pnl[i]
  }
  return(serieMaxLoss)
} 