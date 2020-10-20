# R program to demonstrate a few parallel computing tools
# "parallel" package

library(parallel)

# Repeating a loop
reploop <- function(my_range) {
  for (i in 1:my_range) {
    v <- rnorm(i)
  }
}


# non parallel
start_time <- Sys.time()
lapply(1:1000, function(x) reploop(x))
end_time <- Sys.time()
print(end_time - start_time)


# mcapply is parallel version of lapply
# we can tell it how many cpu cores to use
# Let's keep one CPU reserved for our system tasks
num_of_cpus <- detectCores() - 1
start_time <- Sys.time()
mclapply(1:1000, FUN = function(x) reploop(x), mc.cores = num_of_cpus)
end_time <- Sys.time()
print(end_time - start_time)



# let's make use of clusters
cl <- makeCluster(num_of_cpus)
# When you use clusters, parallel processes don't have the data
# that main paralell program has
# So you need to use this to make your data (reploop in our case)
# availbale to all the
clusterExport(cl, "reploop")

# Let's time it
start_time <- Sys.time()
parLapply(cl, 1:100, function(x) reploop(x))
end_time <- Sys.time()
print(end_time - start_time)

# You need to destroy the clusters to clean up everything
# after you are done
stopCluster(cl)
