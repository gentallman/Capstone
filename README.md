<p align="center">
  <h1>Credit Score Classification</h1>
</p>

At the present time, everyone needs to have good credit because it is seen as a sign of trustworthiness. Financial institutions and credit card issuers use credit scores to determine creditworthiness. It enables banks and credit card companies to issue loans to customers with excellent creditworthiness immediately. 

In today's fast-paced world, doing a manual investigation into each portfolio and generating a credit report both take a significant amount of time. Most of the banks and credit card companies use Machine Learning algorithms to categorize all their customers based on their credit history.

We made a classification system for credit scores to get rid of having to do work by hand. Based on banking data, it is possible to put people into three groups: excellent, standard, and poor. 

We took data from Statso. It is a Data Science Community to Find Case Studies, Datasets and more. This site generates and compiles data from many online sources, and its authors then use this information to develop case studies that show how various types of data can be used to address specific problems.

Data : https://statso.io/credit-score-classification-case-study/

Workflow :
<p align="center">
  <img src="assests/workflow.png"/>
</p>

## Data Cleaning and Preparation
- We removed the ID, Customer_ID, Name, and SSN fields from the dataset because they were irrelevant. We iterate through the dataset and replace any odd numbers, weird digits and undesirable symbolic patterns with nulls. 

- There was a column with the name 'Credit_History_Age' that contained data in the format "XX years and XX months", which was irrelevant for analysis and ML modelling. Thus, we converted those columns to months only.

- Then, we partition the column operation into two categories: numerical and categorical. For categorical NA values, the customer's most recent non-null value will be used to attempt to update the NA. The mean value of the variable is substituted for null values  in numerical ones.

<p align="center">
  <img src="assests/data_cleaning.png"/>
</p>

## Descriptive Statistics 
- Descriptive statistics were utilized for each column of data. And what we discovered was that some of the values in it were completely worthless, while others were much farther away from most of the data points. They are referred to as outliers.

- We resolve on a particular range for the variable's possible values after consulting a variety of sources. The number of credit cards, bank accounts, credit inquiries, and loans that an individual may possess. This stage is performed to make data meaningful because their values were excessively high. In the end, we apply the label encoder to the text-based column in order to get our data ready to fit into the model.

<p align="center">
  <img src="assests/outliers_handling.png"/>
</p>

## Exploratory Data Analysis

1. Individuals with an extended credit history tend to attain higher credit ratings.
<p align="center">
  <img src="assests/eda1.png"/>
</p>

2. The most significant harm to your credit score occurs when you make a payment after the due date of the billing cycle has elapsed.
<p align="center">
  <img src="assests/eda2.png"/>
</p>

3. The decrease in your credit score is directly proportional to the number of credit inquiries made.
<p align="center">
  <img src="assests/eda3.png"/>
</p>
