Here we are using the "parallel" package which is available in the core (or base ) of the R language. These days we have multi-CPU machines
available for cheap even for home desktop systems. So we will use a multi-cpu (one phsycial CPU with multiple cores). We will compare one serial
version and two parallel computing versions of R and measure the time difference.

*lapply()* simply applies the 2nd argument to the first argument. It returns a list of the same length as the first argument.

*mclapply()* is a parallelized version of *lapply()*. It relies on UNIX style forking and hence is not available on Windows

*Clustering* is another way of parallel-computing in R.


# How to use

Just download the file and run this in your R interpreter:

`source("reploop.R")`

You will get this:

![picture](https://i.postimg.cc/jdLYRh2X/Screenshot-from-2020-10-20-13-03-11.png)

You see, *mcapply()* is almost 8 times faster than the *lapply()* (serial version)  and *clustering* is 400 times faster than the serial version. 
Also, *clustering* is 50 times faster than *mcpply()*.



### More Info:

https://support.rstudio.com/hc/en-us/articles/201057987-Quick-list-of-useful-R-packages

https://www.r-bloggers.com/2015/02/how-to-go-parallel-in-r-basics-tips/

https://tutorial.guidotti.dev/pa78y/
