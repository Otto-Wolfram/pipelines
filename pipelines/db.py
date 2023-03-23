import sqlite3
import pandas
import re
import csv


def load(file, table, connection_string='db.db'):
    database = sqlite3.connect(connection_string)
    pandas.read_csv(f'{file}').to_sql(name=table, con=database, if_exists='append', index=False)


def get_domain(url):
    temp = "((?<=http:\/\/)|(?<=https:\/\/)).+?(?=\/)"
    result = re.search(temp, str(url)).group(0)
    return result


def create(table, query, connection_string='db.db'):
    database = sqlite3.connect(connection_string)
    database.create_function("domain_of_url", 1, get_domain)
    database.execute("create table if not exists " + table + " as " + query)


def save(file, table, connection_string='db.db'):
    with open(f"{file}.csv", "w", newline='') as file:
        cur = sqlite3.connect(connection_string).cursor()
        writer = csv.writer(file)

        first_line = file.readline()
        first_line.split(",")
        writer.writerow(first_line.split(","))

        data = cur.execute("SELECT * FROM " + table)
        writer.writerows(data)


def sql(query, connection_string='db.db'):
    database = sqlite3.connect(connection_string)
    database.execute(query)
    database.commit()