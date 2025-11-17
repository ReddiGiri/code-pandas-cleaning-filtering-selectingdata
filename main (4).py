import pandas as pd
titanic=pd.read_csv("titanic.csv")
print(titanic.isnull().sum())
titanic['Age']=titanic['Age'].fillna(titanic['Age'].median())
print(titanic['Age'])
#removing duplicates
print("Duplicates rows exist:",titanic.duplicated().sum())
print("before removing duplicates:",titanic.shape)
titanic=titanic.drop_duplicates()
print("after removing duplicates:",titanic.shape)
#selecting data
print(titanic[['Name','Age','Fare']].head())
print("first 10 rows:",titanic.head(10))
#filtering data
import pandas as pd
titanic=pd.read_csv("titanic.csv")
male_passengers=titanic[(titanic['Age']<18) & (titanic['Sex']=='Male')]
print(male_passengers)
female_passengers=titanic[(titanic['Fare']>50) & (titanic['Sex']=='Female')]
print(female_passengers)
filtered=titanic[(titanic['Age']>40) & (titanic['Sex']=='Female')]
filtered1=titanic[(titanic['Sex']=='Male')|(titanic['Fare']>100)]
print(filtered)
print(filtered1)