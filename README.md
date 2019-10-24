# data-science-stacks


This is a simple *starter pack* to learn about serious computer science,  
or a if you got some data and you wanna make some serious inquires

#### pipenv / docker based data science starter stacks
  


## getting started

```ssh
#
# IMPORTANT          #  it will say some shit like 👇
#                           The Jupyter Notebook is running at:
#                                👉http://34cd4227ea1a:8888/
#              
docker-compose up    #  pay it no mind, its lying to you
```

open a browser and go to [localhost:8888](localhost:8888)


## Stack

The stack is simplest described using an example below


## The [voting example](https://backtick.se/blog/adventure-vote)

On codecation19, a troop of programmers(17 st) ranked 8 different activities (1 for most prioritized). This is how to over engineer a simple vote

open the [Adventure jupyter notebook](https://backtick.se/blog/adventure-vote). 


### First cell
```python
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
sns.set_style("white", rc={'figure.figsize':(18.7,9.27)})
```

- We use `panda` as our dataframe handler etc, etc..
- We use seaborn for *reasons unknown*
- KMeans is used to try to split our adventures in similar interest groups
- `matplotlib` or `plt` is used to draw beutiful diabrams
- The interested reader can find out what the last instruction does (then write it down and send in as a pull request


