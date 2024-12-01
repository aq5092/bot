import gspread
from google.oauth2.service_account import Credentials
from gspread_dataframe import set_with_dataframe, get_as_dataframe

#import online rp
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("key2.json", scopes= scopes)
client = gspread.authorize(creds)
#sheet_from = "19cZOxRm-vntquo2lsi1wuejMA-KptAb9HbHWN99upeU"
#workbook = client.open_by_key(sheet_from)
#online = workbook.worksheet("rp")

sheet_to = "1SQ7XsnvF39EY1b-z-OYtJirSu2-bjrZ7ORmMfLVQK5Q"
workbook2 = client.open_by_key(sheet_to)
topshiriq = workbook2.worksheet("ochiq xat")

def get_from_google():
    data = get_as_dataframe(topshiriq, drop_empty_columns=True, drop_empty_rows=True)
    df = data[['nomer', 'javobgar', 'Status','Natijasi']]
    
    return df

res = get_from_google()
print(res)