import pandas as pd


add_df = pd.DataFrame(columns = ['Numbers','Amounts(Rs)'])

i = 0
j = 1#

while(j):
    i = i + 1
    number = input("Number : ")
    amount = int(input("Amount : "))
    print(len(number))
    if len(number) != 100:
        print("successfully inputed number ", number, " and amount ", amount)
        data = [[number,amount]]
        df = pd.DataFrame(data, columns = ['Numbers','Amounts(Rs)'])

        frames = [add_df,df]
        add_df = pd.concat(frames)
        add_df = add_df.reset_index(drop=True)
        nm = add_df['Numbers'].tolist()
        print(add_df.head(len(nm)))
        print("Number of input : ", i)
        add_df.to_csv('recent.csv')

    else:
        print("unsuccessfully input number ", number, " and amount ", amount)
        print("invalid input.\nEnter 3 digit number only")
        j = 0#

delect = input('delect recent input(y/n)')
if delect == 'y':
    index = int(input('Enter row number to delect'))
    add_df = add_df.drop(index)

sum_df=add_df.groupby('Numbers',as_index=False)['Amounts(Rs)'].sum()
# print(sum_df.head())

count_df = add_df.groupby(['Numbers'],as_index=False).count()
count_df = count_df.rename(columns={'Amounts(Rs)': 'Count'})
# print(count_df.head())

result = pd.merge(sum_df, count_df, on='Numbers')
print(result.head())


k = 1#
while(k):
    print('Assending order of Amount(a)/Count(c)')
    assending = input()
    if assending == 'a':
        result.sort_values(by=['Amounts(Rs)'], inplace=True, ascending=False)
        print(result.head(1000))

    if assending == 'c':
        result.sort_values(by=['Count'], inplace=True, ascending=False)
        print(result.head(1000))


    if assending == 'g':
        result.sort_values(by=['Numbers'], inplace=True, ascending=True)
        print(result.head(1000))
        k = 0#

print("ClEAR download & clear(d)/ clear(clr)")
clear = input()
if clear == 'd':
    from datetime import datetime
    now = datetime.now()
    # print("now =", now)
    dt_string = now.strftime("%d%m%Y%H%M%S")
    print("date and time =", dt_string)
    result.to_csv('ngd'+dt_string+'.csv')

    add_df = pd.DataFrame(columns=['Numbers', 'Amounts(Rs)'])


if clear == 'clr':
    add_df = pd.DataFrame(columns=['Numbers', 'Amounts(Rs)'])


