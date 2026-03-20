import pandas as pd 
from jinja2 import Environment, FileSystemLoader

bets_df=pd.read_csv('bets.csv')
bank_df=pd.read_csv('bank.csv')

bets_dict=bets_df.to_dict(orient='records')
bank_dict=bank_df.to_dict(orient='records')

total_inputs=round(bets_df[' Input '].sum(),2)
total_payouts=round(bets_df[' Payout'].sum(),2)
total_injections=round(bank_df[bank_df[' Type']==' Injection'][' Amount'].sum(),2)
    

print(f'Total payouts :{total_payouts}\n Total Inputs :{total_inputs}\n Total Injections : {total_injections}')

bank_balance=round((total_payouts-total_inputs)+total_injections,2)
print(f'Bank Balance {bank_balance}')

daily_summary=bets_df.groupby('Date')[[' Payout', ' Input ']].sum()
daily_summary=daily_summary.reset_index()
print(f'Daily Summary :{daily_summary}')

summary_dict=daily_summary.to_dict(orient='records')
# print(f'Daily Summary record :{summary_dict}')

env = Environment(loader=FileSystemLoader('.'))
template=env.get_template('template.html')
html_output=template.render(balance=bank_balance, summary=summary_dict, bets= bets_dict,bank=bank_dict)

with open('index.html', 'w') as f:
    f.write(html_output)
