# Albion Profit Scanner

This project aims to answer the following question:
**Is there any item I could craft from scratch(buying items from market) and profit at current market's prices?**

Secundary questions:
* What is the recipe?
* What is the profit?
* Which city?

![](https://github.com/Tauranis/albion-recipe-discovery/raw/master/images/albion_recipe_discovery.gif)

## Installation

```bash
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Run


Single city
```bash
python -m recipe_discover.app \
--quality 1 \
--city Thetford \
--output_path ./report.csv
```

Multiple cities
```bash
python -m recipe_discover.app \
--quality 1 \
--city Bridgewatch,Fort%20Sterling,Lymhurst,Martlock,Thetford \
--output_path ./report.csv
```
