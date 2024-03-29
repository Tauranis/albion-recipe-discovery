# Albion Profit Scanner

This project aims to answer the following question:
**Is there any item I could craft from scratch(buying items from market) and profit at current market's prices?**

Secundary questions:
* What is the recipe?
* What is the profit?
* Which city?

<!--![](https://github.com/Tauranis/albion-recipe-discovery/raw/master/images/albion_recipe_discovery.gif)-->
![](https://github.com/Tauranis/albion-recipe-discovery/raw/master/images/albion_online_profit_scanner.png)

## Albion Online Data Project

This project is built uppon [Albion Data Project](https://www.albion-online-data.com/).

In order to have the most updated prices, download their client and follow their instructions to work properly.


## Installation

```bash
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Run

### CLI

Single city
```bash
python -m recipe_discovery.app \
--quality Normal \
--city Thetford \
--output_path ./report.csv
```

Multiple cities
```bash
python -m recipe_discovery.app \
--quality Normal \
--city Bridgewatch,Fort%20Sterling,Lymhurst,Martlock,Thetford \
--output_path ./report.csv
```

### Streamlit

```bash
streamlit run ./streamlit_app.py
```