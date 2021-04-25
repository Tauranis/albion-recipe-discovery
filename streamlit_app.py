import streamlit as st
from recipe_discovery.discovery import ProfitDiscover
from recipe_discovery.config import CITY_LIST, QUALITY_LIST


def scan_recipes(city,quality):
    profitDiscover = ProfitDiscover(city,quality,True)
    stats = profitDiscover.scan()
    stats = stats[stats["profitability"]>0].reset_index(drop=True)

    return stats


## Sidebar widgets
city = st.sidebar.selectbox("City",CITY_LIST)
quality = st.sidebar.selectbox("Item quality",QUALITY_LIST)


st.title("Albion Online Profit Scanner")
st.text(f"City: {city} Quality:{quality}")



## run script
recipes = scan_recipes(city, quality)
st.write(recipes)