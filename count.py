"""
Описание столбцов:
ACCOUNT_RK – номер договора
INTERNAL_ORG_ORIGINAL_RK – номер точки продажи (POS)
LOAN_AMOUNT – сумма кредита
APPLICATION_DT – дата

 Необходимо написать скрипт на Python, который посчитает и выведет:
- сумму выдач в разрезе дат и точек продаж (даты и номера точек отсортированы по возрастанию)
- процент суммы выдач в разрезе дат и точек от общей суммы выдач в дату

В реализации можно использовать любые библиотеки, но достаточно csv и datetime.
"""
import pandas as pd

df = pd.read_csv('data.csv', delimiter=';')
df1 = df.copy(deep=True)

df1['percentPOS'] = df1['LOAN_AMOUNT'] / df1.groupby(['APPLICATION_DT'])['LOAN_AMOUNT'].transform('sum')
pivot_table = pd.pivot_table(df1,
                             index=['APPLICATION_DT'],
                             columns=['INTERNAL_ORG_ORIGINAL_RK'],
                             values=['LOAN_AMOUNT', 'percentPOS'],
                             aggfunc={'LOAN_AMOUNT': 'sum', 'percentPOS': 'mean'},
                             fill_value=0
                             )

print(pivot_table)
