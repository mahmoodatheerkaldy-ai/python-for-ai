import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("E:\\SERPENT PROJECTS\\statistic_homework\\data\\survey_role_of_ai_english.csv")
df.head()

def draw_digram(df, column):
    plt.figure(figsize=(10, 6))
    df[column].value_counts().plot(kind='bar')
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

draw_digram(df, 'Age')