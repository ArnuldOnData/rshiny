# What is this about?

Let's say we have a web-application written in R. As of now it has several 100 users and now we want to start serving a million users. When we
start to think in terms of scaling our software, we start to think in terms of concurrency, parallel, or distributed computing. There is a lot of 
confusion around what all these terms mean or if they are related to each other. Let's clear this out first:


### Distributed Computing
Distributed computing is done on a distributed system. A distributed system is a system whose components are located on different networked
computers, which communicate and coordinate their actions by passing messages to one another. The components interact with one another in
order to achieve a common goal. If they fail, they fail independently.


### Parallel Computing
In parallel computing, a computational task is typically broken down into several very similar sub-tasks that can be processed independently and
whose results are combined afterward, upon completion. The sub-tasks might not even need to communicate or talk to each other 
(otherwise known as *perfectly parallel* or *delightfully parallel* or even *embarrassingly parallel*)


### Concurrent Computing
Concurrent computing is a form of modular programming. Modular programming is a software design technique that separates the functionality
of a program into independent, interchangeable modules, such that each contains everything necessary to execute only one aspect of the desired
functionality.

Although both concurrency and parallel-computing can be described as **multiple processes executing during the same period of time**. In
parallel computing, execution occurs at the same physical instant e.g on separate processors of a multi-processor machine. Parallel computing is
impossible on a one-core single processor, as only one computation can occur at any instant. By contrast, concurrent computing consists of 
process lifetimes overlapping, but execution need not happen at the same instant. Different parts of a program execute out-of-order or in a 
partial order, without affecting the final outcome. The goal here is to model processes in the outside world that happen concurrently, such as 
multiple clients accessing a server at the same time.



####  Definitions are from Wikipedia. See here:

https://en.wikipedia.org/wiki/Parallel_computing

https://en.wikipedia.org/wiki/Concurrent_computing

https://en.wikipedia.org/wiki/Distributed_computing
