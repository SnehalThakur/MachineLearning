**Smart Lead Scoring Engine**

Can you identify the potential leads for a D2C startup?




**Problem Statement**

A D2C startup develops products using cutting edge technologies like Web 3.0. Over the past few months, the company has started multiple marketing campaigns offline and digital both. As a result, the users have started showing interest in the product on the website. These users with intent to buy product(s) are generally known as leads (Potential Customers). 
Leads are captured in 2 ways - Directly and Indirectly. 
Direct leads are captured via forms embedded in the website while indirect leads are captured based on certain activity of a user on the platform such as time spent on the website, number of user sessions, etc.
Now, the marketing & sales team wants to identify the leads who are more likely to buy the product so that the sales team can manage their bandwidth efficiently by targeting these potential leads and increase the sales in a shorter span of time.
Now, as a data scientist, your task at hand is to predict the propensity to buy a product based on the user's past activities and user level information.



**About Dataset**

You are provided with the leads data of last year containing both direct and indirect leads. Each lead provides information about their activity on the platform, signup information and campaign information. Based on his past activity on the platform, you need to build the predictive model to classify if the user would buy the product in the next 3 months or not.
Download datasets from below link-
https://drive.google.com/drive/folders/1_HmgY7a3Eq_XiwGc2hfLUyN_pPCu5Jvp?usp=sharing



**Data Dictionary**

You are provided with 3 files - train.csv, test.csv and sample_submission.csv



**Training set**

train.csv contains the leads information of last 1 year from Jan 2021 to Dec 2021. And also the target variable indicating if the user will buy the product in next 3 months or not.

![image](https://user-images.githubusercontent.com/24979087/171991327-7008b475-ece2-4a51-974a-e13af6cebf56.png)



**Test set**

test.csv contains the leads information of the current year from Jan 2022 to March 2022. You need to predict if the lead will buy the product in next 3 months or not.

![image](https://user-images.githubusercontent.com/24979087/171991338-5ef6d12a-3bad-401c-bb31-50569adb4094.png)



**Evaluation metric**

The evaluation metric for this hackathon would be F1 Score of Class 1.


**Public and Private Split**

Test data is further divided into Public (40%) and Private (60%) data. 
