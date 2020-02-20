# Xinhui Gu
# May 2nd, 2017
# Question 1
# To get the max drawdown
MaxDD = function(c){
  len = length(c)
  pnl = c[2:len] - c[1:(len-1)]
  serieMaxLoss = pnl[1]
  for (i in 1:(len-1)){
    if(serieMaxLoss > pnl[i])
      serieMaxLoss = pnl[i]
  }
  return(serieMaxLoss)
} 

MaxDD(c(-1, 2, 3,10, 5))

# Question 2
# To get the BS gamma
BlackScholes = function(S, K, r = 0.01, sigma = 0.15, time =0.3, dividend = 0){
  q=dividend
  d1=(log(S/K) + (r-q-sigma^2/2)*T)/(sigma*sqrt(T))
  gamma = dnorm(d1)*exp(-q*T)/(S*sigma*sqrt(T))
  return(gamma)
} 

# Question 3
# To get the probability of same birthday
BirthdayProb = function(N){
  prob = (factorial(365))/(365^N*factorial(365-N+1))
  return(prob)
} 

# Question 4
# To get the R2
NonLmR2 = function(x, y){
  len = length(x)

  new_x = matrix(cbind(const, x), len, 2)
  new_x_t = matrix(t(new_x), 2, len)
  new_y = matrix(y, len, 1) 
  b1=sum((x-mean(x))*(y-mean(y)))/(sum((x-mean(x))^2))
  b0=mean(y)-b1*mean(x)
  beta_hat =c(b0,b1)
  y_hat = new_x%*%beta_hat
  y_bar = mean(y)
  sum((y - y_hat)^2)
  sum((y - y_bar)^2)
  R2 = sum((y_hat - y_bar)^2)/sum((y - y_bar)^2)
  
  return(R2)
} 
