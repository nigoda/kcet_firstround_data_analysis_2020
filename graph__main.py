import pandas as pd
data_gh= pd.read_csv("C:\\Users\\aksha\\PycharmProjects\\finalng\\recent.csv")
data_gh = data_gh.loc[:, ~data_gh.columns.str.contains('^Unnamed')]
num = data_gh['Numbers'].tolist()
print(data_gh.head(len(num)))

sum_df_=data_gh.groupby('Numbers',as_index=False)['Amounts(Rs)'].sum()
# print(sum_df_.head())

count_df_ = data_gh.groupby(['Numbers'],as_index=False).count()
count_df_ = count_df_.rename(columns={'Amounts(Rs)': 'Count'})
# print(count_df_.head())

data_gh = pd.merge(sum_df_, count_df_, on='Numbers')
data_gh.sort_values(by=['Numbers'], inplace=True, ascending=True)
print(data_gh.head(1000))\

ranges = ['001-099','100-199','200-299','300-399','400-499','500-599','600-699','700-799','800-899','900-999']

data_0= data_gh[data_gh['Numbers'] <= 99]
data_00 = data_0[data_0['Numbers'] >= 0]
amt_0 = sum(data_00['Amounts(Rs)'].tolist())
cnt_0 = sum(data_00['Count'].tolist())

data_1= data_gh[data_gh['Numbers'] <= 199]
data_11 = data_1[data_1['Numbers'] >= 100]
amt_1 = sum(data_11['Amounts(Rs)'].tolist())
cnt_1 = sum(data_11['Count'].tolist())

data_2= data_gh[data_gh['Numbers'] <= 299]
data_22 = data_2[data_2['Numbers'] >= 200]
amt_2 = sum(data_22['Amounts(Rs)'].tolist())
cnt_2 = sum(data_22['Count'].tolist())

data_3= data_gh[data_gh['Numbers'] <= 399]
data_33 = data_3[data_3['Numbers'] >= 300]
amt_3 = sum(data_33['Amounts(Rs)'].tolist())
cnt_3 = sum(data_33['Count'].tolist())

data_4= data_gh[data_gh['Numbers'] <= 499]
data_44 = data_4[data_4['Numbers'] >= 400]
amt_4 = sum(data_44['Amounts(Rs)'].tolist())
cnt_4 = sum(data_44['Count'].tolist())

data_5= data_gh[data_gh['Numbers'] <= 599]
data_55 = data_5[data_5['Numbers'] >= 500]
amt_5 = sum(data_55['Amounts(Rs)'].tolist())
cnt_5 = sum(data_55['Count'].tolist())

data_6= data_gh[data_gh['Numbers'] <= 699]
data_66 = data_6[data_6['Numbers'] >= 600]
amt_6 = sum(data_66['Amounts(Rs)'].tolist())
cnt_6 = sum(data_66['Count'].tolist())

data_7= data_gh[data_gh['Numbers'] <= 799]
data_77 = data_7[data_7['Numbers'] >= 700]
amt_7 = sum(data_77['Amounts(Rs)'].tolist())
cnt_7 = sum(data_77['Count'].tolist())

data_8= data_gh[data_gh['Numbers'] <= 899]
data_88 = data_8[data_8['Numbers'] >= 800]
amt_8 = sum(data_88['Amounts(Rs)'].tolist())
cnt_8 = sum(data_88['Count'].tolist())

data_9= data_gh[data_gh['Numbers'] <= 999]
data_99 = data_9[data_9['Numbers'] >= 900]
amt_9 = sum(data_99['Amounts(Rs)'].tolist())
cnt_9 = sum(data_99['Count'].tolist())

amt_sum = [amt_0, amt_1, amt_2, amt_3, amt_4, amt_5, amt_6, amt_7, amt_8, amt_9]
cnt_sum = [cnt_0, cnt_1, cnt_2, cnt_3, cnt_4, cnt_5, cnt_6, cnt_7, cnt_8, cnt_9]

# print(amt_sum)
list = [0,1,2,3,4,5,6,7,8,9]
print(list)
print(cnt_sum)

import plotly.express as px
import pandas as pd
df1 = pd.DataFrame(dict(Numbers=ranges, Amounts=amt_sum, Counts=cnt_sum))
# df2 = pd.DataFrame(dict(Counts=cnt_y))
fig = px.bar(df1, x=df1.Numbers, y=df1.Counts, color=df1.Amounts)

fig.show()
