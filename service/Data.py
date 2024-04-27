from bs4 import BeautifulSoup
from urllib.request import urlopen,Request
from flask import jsonify
from model.Data import db,Data
from flask_restful import Resource,marshal_with
from datetime import datetime

def scrapeData():

        url = 'https://www.psychologytoday.com/intl'

        data = []

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        req = Request(url, headers=headers)
        page = urlopen(req)

        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")

        elements = soup.find_all("div",class_="teaser-lg--main")


        for element in elements:
            text = element.find("h2",class_="teaser-lg__title").select("a")[0].text
            image_link = element.find("div",class_="teaser-lg__image").select("img")[0]["src"]
            decription = element.find("p",class_="teaser-lg__summary").text
            article_link = 'https://www.psychologytoday.com'+element.find("h2",class_="teaser-lg__title").select("a")[0]["href"]
            #item = {"title":text,"decription":decription,"image_link":image_link,"link":article_link}
            
            print(Data.query.filter_by(link=article_link).first())
            if(not(Data.query.filter_by(link=article_link).first())):
                d = Data(title=text,description=decription,image_link=image_link,link=article_link,last_modification=datetime.now())

                db.session.add(d)

        db.session.commit()

        return data

def getData():

    data_list = []
    for data in Data.query.all():
        data_list.append(data.serialize())

    # Serialize the list of dictionaries to JSON
    return jsonify(data_list)