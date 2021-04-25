import streamlit as st
from recipe_discovery.discovery import ProfitDiscover
from recipe_discovery.config import CITY_LIST, QUALITY_DICT

# Keep state from objects
# Ref: https://discuss.streamlit.io/t/save-user-input-into-a-dataframe-and-access-later/2527/2
@st.cache(allow_output_mutation=True)
def get_scanner():
    return ProfitDiscover()


@st.cache(allow_output_mutation=True)
def get_recipies_obj():
    return None


def scan_recipes(ps, city, quality, clear_cache):

    stats = ps.scan(city=city, quality=quality, use_buffer=(not clear_cache))

    if stats is None:
        return stats

    stats = stats[stats["profitability"] > 0].reset_index(drop=True)
    return stats


def show_recipes(recipes):
    if recipes is not None:
        st.dataframe(recipes)


# Profit discover
profitDiscover = get_scanner()

# Sidebar widgets
city = st.sidebar.selectbox("City", CITY_LIST, help="City to scan prices")
quality = st.sidebar.selectbox(
    "Item quality", list(QUALITY_DICT.keys()), help="Item quality"
)
btn_run_gen, btn_clear_cache_gen = st.sidebar.beta_columns(2)
btn_run = btn_run_gen.button("Scan", help="Scan recipies")
btn_clear_cache = btn_clear_cache_gen.checkbox(
    "Clear cache", help="Clear cache and request updated prices from server"
)

# Display
st.title("Albion Online Profit Scanner")
st.markdown(f"City: **{city}** Quality: **{quality}**")


recipies_df = get_recipies_obj()

# Add callbacks
if btn_run:
    recipes_df = scan_recipes(
        profitDiscover, city, quality, clear_cache=btn_clear_cache
    )
    show_recipes(recipes_df)
