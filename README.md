# IDS706-Project1-AadilaJasmin

## Intro
A command line tool to query data stored in databricks

## Usage

#### Test out databricks
```
databricks clusters list --output JSON | jq
databricks fs ls dbfs:/
databricks jobs list --output JSON | jq
```

#### Use command line tool 
```
./query_db.py cli-query // Try default query
./query_db.py cli-query --query=<query statement> // Query from dimonds database
```

```
./query_db.py cli-query-carat-price // Try default carat price query
./query_db.py cli-query-carat-price --carat=<float carat amount> // Query to find the average price of diamonds given carat
```

#### Access fast api web app
```
python3 ./fastapi_app.py
```
Then open the url with the pop-up window
And appedn uri for query average diamond price (e.g. `/query_avg_price/0.23`)
