#SOL 1.1
import pandas as pd
print(pd.__version__)

#SOL 1.2
data={
    'Name':['Alice','Bob','Charlie'],
    'Age':[25,30,35],
    'City':['New York','Los Angeles','Chicago']
}
df=pd.DataFrame(data)
print(df)

#SOL 2.1
s1=pd.Series([100,200,300,400,500])
print(s1)

#SOL 2.2
print(s1[1])
print(s1[3])

#SOL 2.3
s2=pd.Series([10,20,30,40,50])
result=s1+s2
print(result)

#SOL 3.1
print(df[['Name','City']])

#SOL 3.2
df['Salary']=[50000,60000,70000]
print(df)

#SOL 3.3
average_age=df['Age'].mean()
total_salary=df['Salary'].sum()
print("Average age:",average_age)
print("Total salary:",total_salary)

#SOL 4.1
filtered_df=df[df['Age']>28]
print(filtered_df)

#SOL 4.2
df.set_index('Name',inplace=True)
print(df)
df.reset_index(inplace=True)
print(df)

#SOL 5.1
df=pd.read_csv('employees.csv')
print(df)

#SOL 5.2
df.columns = df.columns.str.strip()
filtered_df = df[df['Salary'] > 55000]
print(filtered_df[['Name', 'Department']])

#SOL 6.1
avg_salary_by_dept=df.groupby('Department')['Salary'].mean()
print(avg_salary_by_dept)

#SOL 6.2
salary_agg=df.groupby('Department')['Salary'].agg(['min','max'])
print(salary_agg)


#SOL 7.1
df1=pd.DataFrame({
    'Name':['John','Jane','Emily'],
    'Department':['Sales','Marketing','HR']
})
df2=pd.DataFrame({
    'Name':['John','Jane','Emily'],
    'Experience(Years)':[5,7,3]
})
merged_df=pd.merge(df1,df2,on='Name')
print(merged_df)

#SOL 8.1
sorted_df=merged_df.sort_values(by='Experience(Years)',ascending=False)
print(sorted_df)
