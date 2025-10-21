# F1 Data Analysis
In this project, I want to create a model that predicts qualifying result and hopefully will be able to predict the top 3-5 in the future and create a model that based on the Qualifying prediction makes a model that predicts the race winner or where the polesitter will finish.
## Learning
### Feature Importance and Logistic Regression
[DataCamp-Model Validation](https://campus.datacamp.com/courses/model-validation-in-python/cross-validation?ex=4) <br>
[DataCamp-K Fold Cross Validation](https://www.datacamp.com/tutorial/k-fold-cross-validation) <br>
[GeeksForGeeks](https://www.geeksforgeeks.org/machine-learning/understanding-feature-importance-in-logistic-regression-models/)

I completed 80 courses on [DataCamp](https://www.datacamp.com/portfolio/JamieWoodward?view=true) on Python, SQL and Machine Learning Theory in order to prepare for this project

### Reference Models
[yngjoel, Australian Race Prediction](https://github.com/yngjoel/F1_Australian_Prediction_Model/tree/main) <br>

[mar-antaya Qualifying Prediction](https://github.com/mar-antaya/2025_f1_predictions)

[SaiUbc Qualifying time](https://medium.com/@SaiUbc/whos-fastest-predicting-f1-qualifying-lap-times-with-machine-learning-ebf42d473115)

[Guang Yang Qualifying time](https://aws.amazon.com/blogs/machine-learning/predicting-qualification-ranking-based-on-practice-session-performance-for-formula-1-grand-prix/)

[Spencer Staub race prediction](https://github.com/SpencerStaub/Capstone) [Presentation](https://datasci.columbian.gwu.edu/sites/g/files/zaxdzs4746/files/2023-02/f1-final-presentation.pdf)

[nooruq Track Clustering](https://github.com/nooruq101/INST-414-Module-4) [article](https://medium.com/inst414-data-science-tech/clustering-formula-one-tracks-based-on-structure-and-geography-2cc4c6644f7a)

### Reference Analysis
[F1 Data Analysis](https://x.com/fdataanalysis?lang=en)<br>
[Big Data F1](https://www.bigdataf1.com)

## Data Used
### Historic Data
[Ergast](https://api.jolpi.ca/ergast/)
[Circuit Data](https://github.com/toUpperCase78/formula1-datasets/blob/master/Formula1_2023season_calendar.csv)
### Telemetry
[FastF1](https://docs.fastf1.dev) gives Free Practice and Qualifying data as well as speed through at the lap. Other data provided by the website include Track and Air Temperature at 1 minute intervals throughout each session.

### Weather Data
[Meteostat](https://meteostat.net/en/) gives weather data such as rain and wind speed during the races

### Data Analysis 

### Features

#### FP3 & FP2 Deltas
I used the FP3 and FP2 Deltas as they are the most recent points of data from the drivers and gives an accurate representation of their performance through out the weekend. I calculated the correlation between FP3 Delta and Quali Delta at 0.68. To maintain this correlation i capped the data at 4s to remove outliers from crashes or car issues. 

#### Previous Quali Delta & Previous 5 Qualifying Delta
I have used both the previous race's qualifying data aswell as the mean from the last 5 races. This is because i want to give more emphasis to recent qualifying performances over ones more races further in the past while still nullifying outlier performances in the last race. 

#### Team Data
I have used the team data to help neutralize the effects of crashes in FP3 which would remove data or have unrepresentitave data from sessions by averageing both drivers in a team
### Ideas
[Ensemble Learning](https://www.geeksforgeeks.org/machine-learning/a-comprehensive-guide-to-ensemble-learning) - Combining the results from multiple models in a Classifier, ie. Voting Classifier <br>
<br>
<img width="800" height="401" alt="image" src="https://github.com/user-attachments/assets/c5e426c2-1c6d-4101-b46f-bc745f2d04f1" />
