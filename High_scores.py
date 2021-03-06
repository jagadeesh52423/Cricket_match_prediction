import pandas as pd
df=pd.read_csv('Ball_by_Ball_changed.csv')
output=pd.DataFrame(columns=['Match_Id','Team_Batting_Id','Striker_Id','Runs_scored'])
for i in df['Match_Id'].unique():
	match=df[df['Match_Id']==i]
	for j in match['Team_Batting_Id'].unique():
		innings=pd.DataFrame(columns=['Match_Id','Team_Batting_Id','Striker_Id','Runs_scored'])
		team=match[match['Team_Batting_Id']==j]
		for k in team['Striker_Id'].unique():
			batsman=team[team['Striker_Id']==k]
			runs=0
			for l in batsman['Batsman_Scored']:
				try:
					runs+=int(l)
				except Exception:
					continue
			df1=pd.DataFrame([[i,j,k,runs]],columns=['Match_Id','Team_Batting_Id','Striker_Id','Runs_scored'])
			innings=innings.append(df1)
		print innings[,'Batsman_Scored']
	break
		#output.append(innings.loc[innings['Runs_scored'].idxmax()])
#output.to_csv('High_Scores.csv',index=False)
