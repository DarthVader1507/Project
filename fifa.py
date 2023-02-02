while True:
    import pandas as pd
    import matplotlib.pyplot as plt
    mdf=pd.read_csv(r"D:\Grade 2022-23 Ashwath\Project\Fifa_world_cup_matches.csv")
    a=input('Enter a team name')
    b=a.upper()
    df=mdf[mdf.team1==b]#Extracts rows where a is team 1
    df1=mdf[mdf.team2==b]#Extracts rows where a is team2
    s=0
    s1=0
    s=sum(df.number_of_goals_team1)
    s1=sum(df1.number_of_goals_team2)
    s+=s1
    print(a,"scored",s,"goals")
#Graph
    a1=input("Do you want to see a graphical representation of this?")
    b1=a1.lower()
    if b1=="yes":
        a2=input("Do you want a bar graph or linear graph")
        a2=a2.lower()
        l=list(mdf.team1.unique())
        lgoals=[]
        for i in l:
          dff=mdf[mdf.team1==i]
          dff1=mdf[mdf.team2==i]
          ss=sum(dff.number_of_goals_team1)
          ss1=sum(dff1.number_of_goals_team2)
          ss+=ss1
          lgoals+=[ss]
        for i in range(len(l)):
            l[i]=l[i][:3]
        if a2=="bar":
            plt.bar(l,lgoals)
            plt.xlabel("Team")
            plt.ylabel("Goals")
            plt.title("Goals scored")
            plt.show()
        else:
            plt.plot(l,lgoals)
            plt.xlabel("Team")
            plt.ylabel("Goals")
            plt.title("Goals scored")
            plt.show()
    e=input("Do you want to proceed?")
    e=e.lower()
    if e=="no":
        break
        
