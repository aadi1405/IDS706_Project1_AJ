# IDS706-Project1-AadilaJasmin

### WHAT IS THE PROJECT?
This project is aimed to query a NETFLIX DATASET (taken from [ Kaggle Netflix Dataset ](https://www.kaggle.com/datasets/ariyoomotade/netflix-data-cleaning-analysis-and-visualization)) that contains information about Movies and TV Shows and act like a recommendation system to users.


![5772D2F0-C56F-4FF8-BBF9-7409799ADE04](https://user-images.githubusercontent.com/67281453/190928384-f7a7450e-c40c-4cf0-b460-412f3c27a6b0.png)

---
### PURPOSE
- To work with **codespaces environment, explore databricks, SQL queries, CLI configuration methods, and get introduced to  big data systems**!
- Build a system that can be used to recommend movies and tv-shows to users based on their likings and can be implemented by streaming platforms.



---

### METHODOLOGY

1) Set up the codespaces virtual environment (MakeFile, Requirements file, github copilot, packages etc.)
2) Set up the databricks account and uploaded the dataset onto the storage system
3) Set up codespaces secret keys and linked codespaces with databricks
4) Created python programs that included SQL Queries to query the database and used click package to create the CLI Application
5) Test with Github actions through the process
6) Tested different functions and performed basic analysis on the dataset in databricks using SQL and Python


---
### FUNCTIONS THAT HAVE BEEN IMPLEMENTED

```
python welcome.py  // To Display a welcome message to the user

./query_db.py cli-query // To display the Dataset of movies from Databricks

python query_db.py --movie='<movie_name>' // Query to find the year of the movie or TV Show

python query_desc.py --movie='<movie_name>' // Query to find the description of the movie or TV Show

python query_age.py --age=<enter an age> // Query to find suitable movies or TV Show based on your age

python query_director.py --director=<director name> // Query to find all shows and movie taken by a particular director

```
---

### Test out databricks

```
databricks clusters list --output JSON | jq
databricks fs ls dbfs:/
databricks jobs list --output JSON | jq

```
---

### Future Prospects 
```
1) Performing more analysis and visualization to understand the data and explore Databricks!
2) Extend the functions of the model and make a complete recommendation system
3) Improve the User Interface (Web Application) for improved convenience.
