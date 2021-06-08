import pandas as pd
data_df= pd.read_csv("C:\\Users\\aksha\\PycharmProjects\\finalng\\recent.csv")
data_df = data_df.loc[:, ~data_df.columns.str.contains('^Unnamed')]
# data_df['Numbers'] = data_df['Numbers'].apply(str)
num = data_df['Numbers'].tolist()
print(data_df.head(len(num)))

sum_df_=data_df.groupby('Numbers',as_index=False)['Amounts(Rs)'].sum()
# print(sum_df_.head())

count_df_ = data_df.groupby(['Numbers'],as_index=False).count()
count_df_ = count_df_.rename(columns={'Amounts(Rs)': 'Count'})
# print(count_df_.head())

result_ = pd.merge(sum_df_, count_df_, on='Numbers')
result_.sort_values(by=['Numbers'], inplace=True, ascending=True)
print(result_.head(1000))\


print('select range')
from_ = int(input('from'))
to_ = int(input('to'))
filter_ = result_[result_['Numbers'] <= to_ ]
filter_ = filter_[filter_['Numbers'] >= from_ ]
num1 = filter_['Numbers'].tolist()
print(filter_.head(10))

num_x = filter_['Numbers'].tolist()
amt_c = filter_['Amounts(Rs)'].tolist()
cnt_y = filter_['Count'].tolist()


import plotly.express as px
import pandas as pd
df1 = pd.DataFrame(dict(Numbers=num_x, Amounts= amt_c , Counts=cnt_y))
# df2 = pd.DataFrame(dict(Counts=cnt_y))
fig = px.bar(df1, x=df1.Numbers, y=df1.Counts, color=df1.Amounts)

fig.show()

