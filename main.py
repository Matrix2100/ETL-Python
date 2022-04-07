import database.database as db
import etl.extract as extract
import cx_Oracle

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    xt = extract.extrair()
    print(xt)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
