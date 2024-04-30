import pandas as pd

# Створення словника з даними
data = {
    'Прізвище': ['Петров', 'Костян', 'Сидоров', 'Коваленко', 'Морозов', 'Семенов', 'Захарченко', 'Лютий', 'Литвиненко', 'Козлов'],
    'Зріст': [180, 175, 170, 165, 160, 155, 150, 145, 140, 135]
}

# Перетворення словника в датафрейм
df = pd.DataFrame(data)

# Вивід датафрейму
print("Початковий датафрейм:")
print(df)
print("\n")

# Виведення основних статистик зросту
print("Основні статистики зросту:")
print(df['Зріст'].describe())
print("\n")

# Додавання нової колонки з категоріями зросту
df['Категорія зросту'] = pd.cut(df['Зріст'], bins=[130, 150, 170, 190], labels=['Низький', 'Середній', 'Високий'])

# Групування за категоріями і підрахунок кількості осіб в кожній категорії
grouped = df.groupby('Категорія зросту',  observed = False).size()

# Вивід результату групування
print("Розподіл осіб по категоріях зросту:")
print(grouped)

# DataFrame. count: Count number of non-NA/ null observations.
# DataFrame. max: Maximum of the values in the object.
# DataFrame. min: Minimum of the values in the object.
# DataFrame. mean: Mean of the values.
# DataFrame. std: Standard deviation of the observations.
# DataFrame. select_dtypes: Subset of a DataFrame including/ excluding columns based on their dtype.