import pandas as pd

add_df = pd.DataFrame(columns = ['College_code','College_name','Rank'])


i = 1
while(i):
    code = input("code : ")
    name = input("college name: ")
    rank = int(input("rank : "))
    if code != '1':
        data = [[code, name , rank]]
        df = pd.DataFrame(data, columns=['College_code','College_name','Rank'])

        frames = [df, add_df]
        add_df = pd.concat(frames)
        add_df = add_df.reset_index(drop=True)
        nm = add_df['College_code'].tolist()
        print(add_df.head(len(nm)))
        print("Number of input : ", i)
        add_df.to_csv('datascience.csv')
        result = add_df
    else:
        i = 0

