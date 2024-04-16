SPOTREND: Predicting Spotify Song Success - Project Overview & Proposal
By Kenjee Koh, Campbell Singhasemanon, Daniel Nguyen

==============================
1. INTRODUCTION
==============================
The music industry has undergone significant transformations in recent years, with digital streaming platforms and transforming consumer habits revolutionizing how music is consumed. 

As both music production enthusiasts as well avid users of leading music streaming software Spotify, our team recognizes the value in understanding the factors that contribute to a song's streaming success. In this project, we propose to leverage the Spotify API and Python data analytics and machine learning libraries to develop an algorithm that evaluates the relation between a track’s features and it’s streaming success, while also providing a feature for predicting a song’s streaming success based on said factors.


==============================
2. OBJECTIVES
==============================
1. To utilize the Spotify API to retrieve accurate track metadata from the Spotify platform.
2. To develop a predictive algorithm that accurately predicts the streaming success of Spotify songs.
3. To identify key factors that influence a song’s streaming performance on the Spotify platform.
4. To enhance our understanding of machine learning techniques and their applications in the music streaming industry.
5. To showcase our analytical and technical skills by delivering a robust prediction model.


==============================
3. SCOPE
==============================
The scope of this project includes:

- Acquiring and preprocessing the reference Spotify dataset via Spotify API.
- Exploratory data analysis to understand the characteristics of the dataset.
- Feature engineering to extract relevant features for prediction.
- Building and training machine learning models to predict streaming success.
- Evaluating the performance of the prediction algorithm using appropriate metrics.
- Documenting the entire process and findings for future reference.


==============================
4. METHODOLOGY
==============================

- Data Acquisition
    
    Using the Spotify API, we will be directly acquiring the following dataset from the Spotify platform database:
    
    1. Top 50 Streamed Songs of 2023
        - This will give us a dataset to reference for analyzing the dynamic between a song’s features and its streaming success.
        - Additionally, more “technical” feature data included for each track in this dataset includes (but is not limited to):
            - key: *Key of the song*
            - mode: *Mode of the song*
            - danceability_%: *Percentage indicating how suitable the song is for dancing*
            - valence_%: *Positivity of the song’s musical content*
            - energy_%: *Perceived energy level of the song*
            - acousticness_%: *Amount of acoustic sound in the song*
            - instrumentalness_%: *Amount of acoustic sound in the song*
            - liveness_%: *Presence of live performance elements*
            - speechiness_%: *Amount of spoken words in the song*
        - **NOTE:** We are keeping in mind the biases associated with using such a dataset (e.g. most of the songs on the Top 50 have become so successful 	because of the artist’s existing popularity, the song’s massive marketing budget, etc).

- Data Preprocessing
    
    The dataset will undergo minimal cleaning, organization, and formatting to ensure data quality and consistency.
    
    Minimal work will be needed here as the dataset is already fairly organized and formatted by the Spotify API/Spotipy library.
    
- (WIP) Exploratory Data Analysis (EDA)
- (WIP) Feature Engineering
- (WIP) Model Development
- (WIP) Model Evaluation


==============================
5. EXPECTED OUTCOMES
==============================
- An analysis and prediction algorithm capable of accurately forecasting the streaming success of Spotify songs based on the song’s “technical” features.
- Insights into the factors that significantly influence a song’s performance on the Spotify platform.
- Documentation of the entire project process, including data acquisition, preprocessing, model development, and evaluation.
- Presentation of findings through visualizations, reports, and possibly a demo of the prediction algorithm.


==============================
6. TIMELINE
==============================
We are planning to divide this project into multiple phases. 
PHASE 1: Building the Analytic Algorithm

PHASE 2: Building the Predictive Machine Learning Algorithm

PHASE 3: Building the Website to Host the SPOTrend Program


==============================
7. TEAM MEMBERS
==============================
Kenjee Koh - Project Manager & Data Analyst/Software Engineer

Campbell Singhasemanon - Data Analyst/Software Engineer

Daniel Nguyen - Data Analyst


==============================
8. RESOURCES
==============================  
- Spotify Web API
    - https://developer.spotify.com/documentation/web-api
- Python Libraries for API Interaction: spotipy
    - https://spotipy.readthedocs.io/en/2.22.1/#installation
- Python Libraries for Data Analytics: pandas, matplotlib, seaborn
    - https://pandas.pydata.org/docs/
    - https://matplotlib.org/stable/index.html
    - https://seaborn.pydata.org/
- Python Libraries for Machine Learning: pytorch
    - https://pytorch.org/


==============================
9. CONCLUSION
==============================  
This project presents an exciting opportunity to delve into the intersection of music streaming and machine learning, while also highlighting our team’s technical and collaboration skills.

By leveraging the Spotify API for accurate data analytics, we aim to not only develop a predictive model but also gain valuable insights into the dynamics of song popularity on streaming platforms.

We are confident that our interdisciplinary approach and collaborative efforts will lead to a successful outcome that enhances our skills and strengthens our credentials.