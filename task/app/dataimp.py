import pandas as pd
import numpy as np

products = [
    {
        "title" : "mouse",
        "category" :"electronics",
        "price":"150.00",
        "desc":"mouse"
    },
    {
        "title" : "basketball",
        "category" :"sport equip",
        "price":"500.00",
        "desc":"used to play with"
    },
    {
        "title" : "keyboard",
        "category" :"electronics",
        "price":"1000.00",
        "desc":"used to type with"
    },
    {
        "title" : "adapter",
        "category" :"electronics",
        "price":"200.00",
        "desc":"used to charge with"
    }
]

df = pd.DataFrame(products)
df.to_csv("/Users/florinamary/Documents/CrowdANALYTIX/celeryexp/djangocelery/task/app/data.csv", sep = "|")
