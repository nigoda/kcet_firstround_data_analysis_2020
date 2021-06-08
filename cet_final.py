import pandas as pd

data = pd.read_csv("dhanya.csv")
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]


data.sort_values(by=['Rank'], inplace=True, ascending=True)
data = data.reset_index(drop=True)
print(data.head(1000))





college = data['College_name'].tolist()

rank = data['Rank'].tolist()

code = data['Rank'].tolist()

import plotly.express as px
import pandas as pd
df1 = pd.DataFrame(dict(college=college, RANK=rank, computer_science=rank))
# df2 = pd.DataFrame(dict(Counts=cnt_y))
fig = px.bar(df1, x=df1.college, y=df1.computer_science, color=df1.RANK)


fig.write_html("computer_science.html")

fig.show()
