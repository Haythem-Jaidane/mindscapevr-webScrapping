import json
from model.Data import Data, db
from service.Data import scrapeData,getData


def index():
    return {'status': 'OK',
            'localhost:8000/machines/create': 'Create table in mysql database',
            'localhost:8000/machines/insert': 'Insert data in mysql database table(Inserttable)'}


def scrape():
    return scrapeData()


# insert data into table.
def getScrappedData():
    return getData()  