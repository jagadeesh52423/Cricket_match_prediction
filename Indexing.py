import pandas as pd
df=pd.read_csv('Ball_by_Ball_changed.csv')
df=df.set_index(['Match_Id','Team_Batting_Id','Striker_Id'])
df=df[columns=['Match_Id','Team_Batting_Id','Striker_Id','Batsman_Scored']]
df.to_csv("checking.csv")
