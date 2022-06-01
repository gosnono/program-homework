import pandas as pd


def main():
    conn = sqlite3.connect('text.db')
    print("Opened atabase.successfully")

    df_company = pd.read_sql_query('select * from company', conn)
    print(df_company)

    df_company.to_sql("company_pd", conn, index=False, if_exists='replace')

    conn.close()

if __name__ =="__main__":
    main()
