# Albion Profit Scanner

![Cover](./images/giphy.gif)


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