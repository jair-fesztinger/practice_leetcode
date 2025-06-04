import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = accounts[accounts['income'] < 20000]
    average = accounts[(accounts['income'] <= 50000) & (accounts['income'] >= 20000)]
    high = accounts[accounts['income'] > 50000] 

    count_low = low['account_id'].count()
    count_av = average['account_id'].count()
    count_high = high['account_id'].count()

    answer = pd.DataFrame({'category': ['High Salary', 'Low Salary', 'Average Salary'], 'accounts_count':[count_high, count_low, count_av]})
    return answer