import math

recipe_html_cell = """

<!DOCTYPE html>
<html>
   <head>
      <style>
         
        p {{
            font-family: IBM Plex Sans, sans-serif;
            font-size: 14px;
        }}

        .recipe_title {{
            font-family: IBM Plex Sans, sans-serif;
            font-size: 16px;
            font-weight: bold;
        }}

         .container {{
         background-color: lightblue;    
         text-align: left;
         height:auto;
         border-spacing:2px;
         display:flex;
         }}
         
         
        .product_info{{        
        border-style: solid;
        border-right-color: grey;
         width: 300px;
         }}
         
         .product_image {{
         flex: 1;
         text-align: left;
         width:90px;
         float:left;
         }}
         
         .product_stats {{
         text-align: left;
         width:210px;
         float:right;
         }}
         
         .product_recipe {{
         float: left;
         height:auto;
         width: auto;
         }}

         .table{{ 
         display: table;
         }}
         
         .tr{{ 
         display:flex;
         }}
         
         .td{{ 
         display: table-cell; 
         border-style: dashed;
         border-width: 0px 3px 3px 0px;
         border-color: red;
         width: 250px;
         }}
      </style>
   </head>
   <body>
      <div class="container">
         <div class = "product_info">
            <div class="product_image">
               <img src="https://albiononline2d.ams3.cdn.digitaloceanspaces.com/thumbnails/orig/{item_id}" alt="{item_id}" width="84px">  
            </div>
            <div class="product_stats">
               <p>
                <b>{item_id}</b><br>
                Recipe cost: {recipe_price:.0f}<br>
                Market sell price: {market_sell_price:.0f}<br>
                Profit: {profit:.0f}<br>
                Profitability: {profitability:.2f} %
               </p>
            </div>
         </div>
         <div class="product_recipe">
            <center><div class="recipe_title">Recipe</div></center>
            {recipe_items_html}
         </div>
      </div>
   </body>
</html>

"""


def generate_recipe_html(items, ncols=3):

    nrows = int(math.ceil(len(items) / ncols))

    recipe_html_str = """
        <div class="table">
    """

    for i in range(nrows):
        recipe_html_str += """
            <div class="tr">
        """

        for j in range(ncols):

            item_idx = ncols * i + j

            if item_idx >= len(items):
                break

            item_id = items[item_idx].item_id
            item_id_short = item_id[0:18]
            item_unit_price = items[item_idx].price
            item_quantity = float(items[item_idx].quantity)
            item_total_price = item_unit_price * item_quantity

            recipe_html_str += f"""
            <div class="td">
                <div class = "product_image"  style="width: 70px; height: 100%; vertical-align: middle;">
                    <img src="https://albiononline2d.ams3.cdn.digitaloceanspaces.com/thumbnails/orig/{item_id}" alt="{item_id}" width="64px">
                </div>
                <div class="product_stats" style="width: 180px;  height: 100%;  vertical-align: middle;">
                    <p>
            """
            recipe_html_str += f"""
            <b>{item_id_short}</b><br>
            """

            if item_quantity.is_integer():
                recipe_html_str += f"""
                Amount: {item_quantity:.0f}<br>
                Unit price: {item_unit_price:.0f} <br>
                Total: {item_total_price:.0f}
                """
            else:
                recipe_html_str += f"""
                Amount: {item_quantity:.2f}<br>
                Unit price: {item_unit_price:.0f} <br>
                Total: {item_total_price:.2f}
                """

            recipe_html_str += """      
                    </p>
                </div>
            </div>
            """

        recipe_html_str += """
            </div>
        """

    recipe_html_str += """
        </div>
    """

    return recipe_html_str
