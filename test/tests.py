from pipelines.tasks import *
import pytest
import os
import sqlite3

connection_string = 'db.db'
table_name = 'table_for_tests'
test_data_file_path = '../test/test_data.csv'
file_result_name = 'test_output'


def test_load():
    task = LoadFile(table_name, test_data_file_path, connection_string)
    task.run()
    cursor = sqlite3.connect(connection_string).cursor()
    cursor.execute("SELECT COUNT(*) from " + table_name)
    actual_num_of_rows = cursor.fetchone()[0]
    assert actual_num_of_rows == 2
    cursor.close()
    delete_trash()


def test_export():
    LoadFile(table_name, test_data_file_path, connection_string).run()
    CopyToFile(table_name, file_result_name, connection_string).run()
    if os.path.isfile(file_result_name + '.csv'):
        with open(file_result_name + '.csv', 'r') as check_file:
            reader = csv.reader(check_file)
            actual_num_of_rows = len(list(reader)) - 1
            assert actual_num_of_rows == 2

        delete_trash()
    else:
        pytest.fail("404 - file was not created")


def delete_trash():
    RunSQL('drop table ' + table_name, connection_string).run()
    if os.path.isfile(file_result_name + '.csv'):
        os.remove(file_result_name + '.csv')
        os.remove(connection_string)
