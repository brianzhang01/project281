# Final project for CS 281, Fall 2013  
### Predicting Intersection-Specific Accidents Using New York City Crash Data  
### Brian Zhang '15 and Irene Chen '14  


Abstract: In the context of crash data, probabilistic models allow city officials to better understand
crash trends and implement preventative actions. In this paper, we examine
a dataset of New York City crash reports over the past three years labeled
by intersection. Given an unseen intersection, we seek to predict the number of
collisions in a given time period, evaluating our results using cross-validation assuming
a Poisson likelihood. Building from a simple baseline of predicting the
average, we tested a K-nearest neighbor (KNN) regressor with uniform and inverse
distance weighting and the Gaussian process method of kriging. Our prediction
results ranked KNN with uniform weighting first on both the Manhattan
and Brooklyn datasets. However, our Gaussian process model is more readily interpretable
and gives information about the distribution of crashes through both a
visual representation and optimal hyperparameter values.
