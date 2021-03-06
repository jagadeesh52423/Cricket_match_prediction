def str_to_num(a):
	total=0
	for i in a:
		total+=(i-'0')
	return total
import pandas as pd
total_data = pd.read_csv('Ball_by_Ball.csv')
#indeces=[0,2,4]
#new_data = pd.DataFrame(columns=[match_data.columns[[0,2,4]]])
#new_data=pd.DataFrame(columns=total_data.columns[[0,1,2]])
new_data=total_data[total_data.columns[[0,4,6,10]]]
#new_data=new_data[new_data.columns[[0,4,6]]]
#new_data=new_data.groupby(['Match_Id','Team_Batting_Id','Striker_Id']).sum();
info={}
#print new_data
for i in new_data.values:
	try:
		i[3]=int(i[3])
	except ValueError:
		i[3]=0
	try:
		info[i[0]][i[1]][i[2]]+=i[3]
	except KeyError:
		if(i[0] not in info.keys()):
			info[i[0]]={}
		if(i[1] not in info[i[0]].keys()):
			info[i[0]][i[1]]={}
		if(i[2] not in info[i[0]][i[1]].keys()):
			info[i[0]][i[1]][i[2]]=int(i[3])
final=[]
for i in sorted(info):
	for j in sorted(info[i]):
		for k in sorted(info[i][j]):
			list={'Match_Id':i,'Team_Batting_Id':j,'Striker_Id':k,'Runs_Scored':info[i][j][k]}
			final.append(list)
new_data=pd.DataFrame(final)
new_data.to_csv('New_data.csv',columns=['Match_Id','Team_Batting_Id','Striker_Id','Runs_Scored'])
