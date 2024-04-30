import pandas as pd
import matplotlib.pyplot as plt

# Встановлюємо стиль графіків
plt.style.use('ggplot')

# Зчитуємо дані з файлу, переконуємось що колонка з датами правильно інтерпретується як індекс
# і що вона парситься як datetime об'єкти з датами у форматі день-місяць-рік
fixed_df = pd.read_csv('data.csv', encoding='latin1', parse_dates=['Date'], dayfirst=False, index_col='Date')

# Виводимо перші 3 записи для перевірки правильності зчитування даних
print(fixed_df.head(3))

# Виводимо всі дані для огляду
print(fixed_df)

# Створюємо графік з даними. Якщо у вашому DataFrame більше однієї числової колонки, вони всі будуть відображені на графіку
fixed_df.plot(figsize=(15, 10))

# Показуємо графік
plt.show()

# Виводимо на екран список доступних велодоріжок
print("Назви велодоріжок:Rachel / Papineau,Berri1,Maisonneuve_1,Maisonneuve_2,Brébeuf,Parc,PierDup,\n"
      "CSC (Côte Sainte-Catherine),Pont_Jacques_Cartier,Totem_Laurier,Notre-Dame,Rachel / Hôtel de Ville,\n"
      "Saint-Antoine,René-Lévesque,Viger,Boyer,Maisonneuve_3,University,Saint-Urbain")

# Запитуємо у користувача назву велодоріжки для аналізу
n = input("Введіть назву велодоріжки:")

# Групуємо дані за місяцями і обчислюємо загальні суми по кожній колонці
total_monthly_data = fixed_df.groupby(fixed_df.index.month).sum()

# Визначаємо місяць з найбільшими показниками для вибраної велодоріжки
most_popular_month_general = total_monthly_data[n].idxmax()

# Виводимо на екран найпопулярніший місяць для обраної велодоріжки
print(f"Загально найпопулярніший місяць: {most_popular_month_general}")
