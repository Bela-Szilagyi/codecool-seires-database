from flask import Flask, render_template, url_for, request
from data import data_manager

app = Flask('codecool_series')


@app.route('/')
def index():
    result = data_manager.execute_select('SELECT id, title FROM shows;')
    return render_template('index.html', shows=result)



@app.route('/<show_id>/<season_number>/')
def episodes(show_id, season_number):
    query = """SELECT episodes.episode_number, episodes.title 
             FROM episodes JOIN seasons ON seasons.id = episodes.season_id JOIN shows ON seasons.show_id=shows.id 
             WHERE shows.id = %s AND seasons.season_number= %s;"""
    values = (shows_id, season_number, )
    result = data_manager.execute_select(query, values)
    return render_template('index.html', shows=result)


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run()


if __name__ == '__main__':
    main()
