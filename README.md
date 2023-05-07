<a href='https://medium.com/@sankarbareddy/using-machine-learning-for-predicting-failure-of-trucks-d3cb9267a024'>Blog Link</a>

# Introduction:	
This case study was sourced from the competition held by the IDA (Intelligent Data Analysis) 2016 Industrial Challenge. 
It is about predicting the failure of a specific component of the APS (Air Pressure system) which uses compressed air to signal the actuator which applies the brakes. 
The high potential energy of the compressed air enables the driver to stop the truck with much less effort. The data was sponsored by SCANIA. 

# Business Problem:										
The business objective is to reduce the cost of maintenance by replacing manual inspection with automatic inspection system.  
It finds out whether a truck is prone to imminent failure of the APS system. Data extracted from the trucks themselves are used for the prediction. 

# ML Formulation of the business problem:					
The outcome of the prediction would be either positive indicating apparent failure of the APS or negative indicating the failure other than the APS components. 
This could be formulated as a simple binary classification. 

# Business Constraints:									
The misclassification i.e. predicting  no failure of APS when there actually is might be an expensive error. 
So we must prioritise reducing the number of False Negatives There is no latency problem in this context because anyhow the inspection of a truck is meticulous procedure.

# Data set column analysis:								
The data set provided is a completely numerical data. Features are either single numerical counters or histogram bin counters. 
It is also highly imbalanced where out of 60,000 train instances 1000 were positive and 59,000 were negative classes. 
Large no.of values in the dataset are missing i.e. NaN. 
There are two datasets provided one is the train dataset which contains 60,000 instances along with class labels and another one is the test dataset which contains 16,000 instances on which predictions are made.		

# Performance Metric:										
Since it is an imbalanced dataset the performance metric suggested in the competition was to use the metric called ‘Total_cost’ . 
It comprises of  False Negatives and False Positives such that the penalty for False Negative i.e. predicting no fault in APS when there is an actual failure is 500 much greater than the 10 for the False Positive i.e. predicting a fault in APS when there is no actual failure involved.
Total_cost = (cost_1  no. of False Positives) +  (cost_2  no. of False Negatives) 
False Positives are defined as Type I failure and corresponding cost_1 = 10 is accrued due to unnecessary checks that needs to be done by a mechanic at a workshop.																	
False Negatives are defined as Type II failure and corresponding cost_2 = 500 is accrued due to missing checks on faulty trucks which may cause a breakdown.
