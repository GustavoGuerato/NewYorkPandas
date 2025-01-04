import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

NewYork = pd.read_csv("AB_NYC_2019.csv")
print(NewYork.head())


NewYork["name"].fillna("Unknown", inplace=True)
NewYork["host_name"].fillna("Unknown Host", inplace=True)
NewYork["last_review"].fillna("2000-01-01", inplace=True)
NewYork["reviews_per_month"].fillna(0.0, inplace=True)
NewYork["last_review"] = pd.to_datetime(NewYork["last_review"])

neighbourhood_apartments = NewYork["neighbourhood_group"].value_counts()
print(neighbourhood_apartments)
print(NewYork.head())
sns.barplot(x=neighbourhood_apartments.index, y=neighbourhood_apartments.values)
plt.title("Número de Apartamentos por Bairro")
plt.xticks(rotation=90)
plt.show()

neighbourhood_reviews = (
    NewYork.groupby("neighbourhood")["reviews_per_month"].mean().head(5)
)
neighbourhood_reviews.sort_values().plot(kind="barh", color="lightgreen")
plt.title("Média de Avaliações Mensais por Bairro")
plt.xlabel("Média de Avaliações Mensais")
plt.ylabel("Bairro")
plt.show()

avg_room_price = NewYork.groupby("room_type")["price"].mean()
avg_room_price.plot(kind="bar")
plt.title("Preço Médio por Tipo de Quarto")
plt.xticks(rotation=45)
plt.show()

neighbourhood_availability = (
    NewYork.groupby("neighbourhood")["availability_365"].mean().head(5)
)
neighbourhood_availability.sort_values().plot(kind="barh")
plt.title("Media de Disponibilidade por Bairro")
plt.show()

sns.histplot(NewYork["price"], bins=50)
plt.show()
