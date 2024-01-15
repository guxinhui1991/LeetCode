X = runif(100000, 0, 10)
y = 10*exp(-2*abs(X-5))
c(mean(y), mean(y))

w = function(x) dunif(x, 0, 10)/dnorm(x, mean=5, sd=1)
f = function(x) 10*exp(-2*abs(X-5))
X=rnorm(1e5, mean=5, sd=1)
Y=w(X)*f(X)
c(mean(Y), var(Y))

