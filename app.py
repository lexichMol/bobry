from pprint import pprint
import requests
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, session

from flask import Flask, render_template, request
from flask_cors import CORS
import requests


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.secret_key = 'keyhigeh363668ifsgjdgagerFFsdflktgiu'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///date.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rooms_count.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///windows_for_room.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///windows_room_count.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///windows.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///floor.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bool.db'
db = SQLAlchemy(app)

class Main(db.Model):
    __tablename__ = 'main'
    id = db.Column(db.Integer, primary_key=True)
    date_d_m_y = db.Column(db.Text, nullable=False)
class Date(db.Model):
    __tablename__ = 'date'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    main_id = db.Column(db.Integer, nullable=False)

class Rooms_count(db.Model):
    __tablename__ = 'rooms_count'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    main_id = db.Column(db.Integer, nullable=False)

class Windows_for_room(db.Model):
    __tablename__ = 'windows_for_room'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    main_id = db.Column(db.Integer, nullable=False)

class Windows_room_count(db.Model):
    __tablename__ = 'windows_room_count'
    id = db.Column(db.Integer, primary_key=True)
    count_windows = db.Column(db.Integer, nullable=False)
    number_room = db.Column(db.Integer, nullable=False)
    windows_for_room = db.Column(db.Integer, nullable=False)

class Windows(db.Model):
    __tablename__ = 'windows'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    main_id = db.Column(db.Integer, nullable=False)

class Floor(db.Model):
    __tablename__ = 'floor'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    windows_id = db.Column(db.Integer, nullable=False)

class Bool(db.Model):
    __tablename__ = 'bool'
    id = db.Column(db.Integer, primary_key=True)
    bool = db.Column(db.Text, nullable=False)
    floor_id = db.Column(db.Integer, nullable=False)



# class Shot(db.Model):
#     __tablename__ = 'shot'
#     id = db.Column(db.Integer, primary_key=True)
#     xy = db.Column(db.Text, nullable=False)
#     id_table = db.Column(db.Text, nullable=False)
#     T_F = db.Column(db.Text, nullable=False)
#
#     def __repr__(self):
#         return self.login

@app.route('/')
def hello_world():  # put application's code here
    response1 = requests.get('https://olimp.miet.ru/ppo_it_final/date', headers={'X-Auth-Token': 'ppo_9_30003'})
    dates = []
    for elem in response1.json()['message']:
        dates.append(elem)


    date = []
    rooms_count = []
    windows_for_room = []
    windows = []
    data = []
    for i in dates:
        day, month, year = i.split("-")
        data_response = requests.get(f'https://olimp.miet.ru/ppo_it_final?day={day}&month={month}&year={year}', headers={'X-Auth-Token': 'ppo_9_30003'})
        data_response_json = data_response.json()['message']

        date.append(data_response_json["date"])
        rooms_count.append(data_response_json["flats_count"])
        windows_for_room.append(data_response_json["windows_for_flat"])
        windows.append(data_response_json["windows"])
    # pprint(data_response_json)
    print(date)
    print(rooms_count)
    print(windows_for_room)
    print(windows)
    print(dates)
    # for i in range(len(dates)):
    #     main_db = Main(date_d_m_y=dates[i])
    #     db.session.add(main_db)
    #     db.session.commit()
    #
    #     date_db = Date(data=date[i]["date"], description=date[i]["description"], main_id=main_db.id)
    #     db.session.add(date_db)
    #     db.session.commit()
    #
    #     rooms_count_db = Rooms_count(data=rooms_count[i]["data"], description=rooms_count[i]["description"], main_id=main_db.id)
    #     db.session.add(rooms_count_db)
    #     db.session.commit()
    #
    #     windows_for_room_db = Windows_for_room(description=windows_for_room[i]["description"], main_id=main_db.id)
    #     db.session.add(windows_for_room_db)
    #     db.session.commit()
    #
    #     perem = windows_for_room[i]["data"]
    #     for j in perem:
    #
    #         windows_room_count_db = Windows_room_count(count_windows=int(j), number_room=windows_for_room_db.id)
    #         db.session.add(windows_room_count_db)
    #         db.session.commit()
    #
    #     windows_db = Windows(description=windows[i]["description"], main_id=main_db.id)
    #     db.session.add(windows_db)
    #     db.session.commit()
    #
    #     for j in range(len(windows[i]["data"])):
    #         windows_db = Windows(number=j+1, windows_id=windows_db.id)
    #         db.session.add(windows_db)
    #         db.session.commit()







    return render_template("index.html", days=len(dates), dates=dates)


@app.route('/api/v1.0/show_rooms', methods=['POST', 'GET'])
def show_rooms():

    date = request.form.get("date").split("-")
    response = requests.get(f'https://olimp.miet.ru/ppo_it_final?day={date[0]}&month={date[1]}&year={date[2]}',
                            headers={'X-Auth-Token': 'ppo_9_30003'})

    rooms = response.json()["message"]["windows"]["data"]
    windows_for_room = response.json()["message"]["windows_for_flat"]["data"]
    rooms_count = response.json()["message"]["flats_count"]["data"]

    rooms_with_light = []
    k = 0
    room_number = 0
    all_windows = []
    for key in rooms:
        r = rooms[key]
        vsp = []
        for i in range(rooms_count):
            room_number += 1
            left_win = sum(windows_for_room[:i])
            right_win = sum(windows_for_room[:i]) + windows_for_room[i]
            for j in range(left_win, right_win):
                if r[j]:
                    vsp.append([True, room_number])
                else:
                    vsp.append([False, room_number])


            if any(r[j] for j in range(left_win, right_win)):
                k += 1
                rooms_with_light.append(room_number)
        all_windows.append(vsp)
    for ind1 in range(len(all_windows)):
        for ind2 in range(len(all_windows[ind1])):
            all_windows[ind1][ind2] = str(all_windows[ind1][ind2][0]) + " " + str(all_windows[ind1][ind2][1])
    for ind1 in range(len(all_windows)):
        all_windows[ind1] = ",".join(all_windows[ind1])

    return {"status": "success",
            "floors_count": len(rooms),
            "k": k,
            "rooms_with_light": " ".join(map(str, rooms_with_light)),
            "rooms_count": rooms_count,
            "window_on_floor": " ".join(map(str, windows_for_room)),
            "all_windows": ";".join(all_windows)
            }





if __name__ == '__main__':

    app.run(host="0.0.0.0")


