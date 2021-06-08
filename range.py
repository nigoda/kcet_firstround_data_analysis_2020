import pandas as pd
data_df= pd.read_csv("C:\\Users\\aksha\\PycharmProjects\\finalng\\recent.csv")
data_df = data_df.loc[:, ~data_df.columns.str.contains('^Unnamed')]
num = data_df['Numbers'].tolist()
print(data_df.head(len(num)))



print('select range')
from_ = int(input('from'))
to_ = int(input('to'))
filter = data_df[data_df['Numbers'] <= to_ ]
filter = filter[filter['Numbers'] >= from_ ]
num1 = filter['Numbers'].tolist()
print(filter.head(10))

sum_df_=filter.groupby('Numbers',as_index=False)['Amounts(Rs)'].sum()
# print(sum_df_.head())

count_df_ = filter.groupby(['Numbers'],as_index=False).count()
count_df_ = count_df_.rename(columns={'Amounts(Rs)': 'Count'})
# print(count_df_.head())

result_ = pd.merge(sum_df_, count_df_, on='Numbers')
print(result_.head(1000))

k = 1
while(k):
    print('Assending order of Amount(a)/Count(c)')
    assending = input()
    if assending == 'a':
        result_.sort_values(by=['Amounts(Rs)'], inplace=True, ascending=False)
        print(result_.head(1000))

    if assending == 'c':
        result_.sort_values(by=['Count'], inplace=True, ascending=False)
        print(result_.head(1000))


    if assending == 'g':
        result_.sort_values(by=['Numbers'], inplace=True, ascending=True)
        print(result_.head(1000))
        k = 0#