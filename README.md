
# Inferential Insights into King County Housing Prices

For this project, our goal is to build a model that provides inferential insights into real-world housing data.


## TABLE OF CONTENTS

Our home repository contains the project environment and information about our project.

#### notebooks:

-report folder which houses an organized polished file containing the entire project
-exploratory folder, which houses an exploration of the data we each individually took part in, which constituted our workflow.
    
The notebook folder also contains readme files to further explain the contents.

#### data

-raw folder contains all the data we needed to import for the project.
Note: As many of these files are too large to include in the repo, you can download the data using the instructions we have provided in our final notebook
-clean folder contains a csv of our cleaned dataset

#### reports

contains the pdf presentation of our project. 
-figures folder in which we outputted all of our images.
    

#### references 

contains any sources we used to aid our project.


## BACKGROUND

The factors that influence housing prices interest many people, from homeowners hoping to improve the market potential of their current homes, to policymakers making decisions about investment in public projects. Often we rely on the "expert judgement" of real estate professionals to determine which factors are the most important, but these recommendations may be out-of-date, irrelevant to our particular housing market, or otherwise inaccurate.


## PROJECT GOAL

Stakeholders in King County, WA have requested statistical analysis to validate several claims about housing prices in the most recent full calendar year, 2019.

These claims can be addressed directly with the three datasets (from the King County Department of Assessments) described later in this document:

1. Higher square footage increases home sale price
2. Having a porch increases home sale price
3. Having a beachfront or lakefront increases home sale price
4. The presence of a nuisance (power lines, traffic noise, airport noise) decreases home sale price

We will build a linear regression model to represent sales prices in King County, and use it to address these claims as well find other features that have a correlation with  home sale price.

We will specifically be focusing on finding what features of a house can increase home sale price and suggest to a house flipper what they can do to add value to a house.


## THE DATASET

For this project, we will be working with the King County House Sales dataset.
The data itself (CSV files) and descriptions of the data (DOC files) can be downloaded [here](https://info.kingcounty.gov/assessor/DataDownload/default.aspx).

Additional information about the `MAJOR` and `MINOR` attributes can be found [here](https://www5.kingcounty.gov/sdc/Metadata.aspx?Layer=parcel#AttributeInfo).

<u>The particular tables we are using for this analysis are:</u>

 - Real Property Sales
 - Residential Building
 - Parcel

There is also a table called "Lookup" that explains the meaning of many of the attributes in the above tables (e.g. the `Street Surface` attribute of a parcel is a number with lookup code 60, which indicates that `1` means `PAVED`, `2` means `GRAVEL`, `3` means `DIRT`, and `4` means `UNDEVELOPED`).


## THE PROCESS


### Data Preparation

Through Pandas, we performed necessary data cleaning, including merging of tables, and pulled in all relevant data for analysis in a linear regression model. We included columns from the data sets that we thought would have a correlation with Sale Price. We filtered, remapped, and cleaned the data to feed into our model. We considered many features as well as scaling or one-hot encoding required to feed the data into a linear regression model.


### Data Exploration

We have generated visualizations of the data during this phase to get a good sense of the data including different features and how they affected the price of homes. First we calculated the correlation values of each feature to sale price and focused on exploring features with high correlation to price. For these visualizations, we used matplotlip, geopandas, and seaborn.


Sale Price Range we are including in the data:
Min:  $10,000 
Max:  $10,050,000 
Average:  $810,713

As we can see below, most of the houses fall under $2 million. We chose to include a high range of Sales Prices even though it heavily right skewed the distribution because we wanted to know what features of a house were included in very expensive houses.

<img src="reports/figures/Sales_Dist.png" width="400" height="320" >

The building grade (the quality of a house) has a high correlation with the sales price so this feature seems like it will be very statistically significant on our model.

<img src="reports/figures/Building_Grade.png" width="500" height="320" >

While square feet also had quite a high correlation with sale price, we cannot include it in our model as it has too much correlation wtih another feature - building grade. The size of the house must be a factor in determining building quality.

<img src="reports/figures/sqftvsPrice.png" width="500" height="300" >

We decided to one hot encode the Waterfront locations to delve deeper into the features

<img src="reports/figures/Is_WaterFront_Loc.png" width="470" height="300" >

In particular Lake Sammamish and Lake Washington were correlated with high sales prices 

<img src="reports/figures/WaterFront_Loc.png" width="420" height="330" >

Some more visual explorations:

<img src="reports/figures/Has_Open_Porch.png" width="450" height="300" >

<img src="reports/figures/Has_Finished_Basement.png" width="450" height="300" >

<img src="reports/figures/Has_Deck.png" width="450" height="300" >

Nuisances don't seem to have much of an effect on Price of House, but we broke down nuisances to further inspect.

<img src="reports/figures/Nuisances.png" width="450" height="300" >

Aha! While noise and other nuisances dont really affect the sales prices, the presence of power lines do negatively affect the value.

<img src="reports/figures/Power_Lines.png" width="400" height="320" >



### Modeling

NOTE to Angelica from Sindhu: The following was just included in the original readme, i didnt write any of that but it provided a dece framework as a placeholder to make it easier for you to fill in

The modeling phase in this project should be a brief stop-over as you are jumping back and forth between the data preparation and the evaluation phases.  If the data preparation was done correctly, it only takes a few lines of code to build a linear regression model.  Then you should be able to print out your model's metrics and quickly move to the evaluation phase.

(In future modules, there will be more complex steps involved with tuning the model itself.)


 - Build a linear regression model with a target variable of home sale price, which is statistically valid such that any interpretation of coefficients are valid
    - Do your best to have features meet the assumptions of a linear regression (no multicollinearity, linear with respect to the outcome variable, errors are normally distributed, etc.). 
      - Note: This is difficult! We will be looking most of all for _improvement_ on this score. In order to demonstrate improvement, you should create a (not very good) model that will serve as a kind of _baseline_. Then you can compare future regression models that you build with that baseline.
    - Try to maximize R<sup>2</sup> _without breaking any assumptions_
 - Address at least 3 of the 9 claims about housing prices made by subject-matter experts
    - Report the effect size as well as the statistical significance
    - It is perfectly acceptable to report a non-finding here
 - Communicate your findings


### Conclusion
 

### Deployment

When you are approaching the end of the available time, choose your best model and report what it says about your research questions. An example finding you might report is: "There is a statistically significant relationship between `<x variable>` and housing price. For every increase of 1 `<x variable>`, the housing price increases by `<amount>`, all else being equal". Consider what types of visualizations would help to communicate the scale and direction of these findings.

Beyond just the numbers, tie these findings into a broader narrative that incorporates your business understanding.  Complete the deliverables listed above, and make sure you can answer the following questions about your process:

 - "How did you pick the question(s) that you did?"
 - "Why are these questions important from a business perspective?"
 - "How did you decide on the data cleaning options you performed?"
 - "Why did you choose a given method or library?"
 - "Why did you select those visualizations and what did you learn from each of them?"
 - "Why did you pick those features as predictors?"
 - "How would you interpret the results?"
 - "How confident are you in the predictive quality of the results?"
 - "What are some of the things that could cause the results to be wrong?"
 

## Citations


