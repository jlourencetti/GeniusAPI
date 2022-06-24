from calendar import day_abbr
from functools import cache
from genius import Genius
from flask import Flask, request
from flask_restful import Resource, Api
from rediscache import RedisCache
from dynamodb import DynamoDB


app = Flask(__name__)
api = Api(app)


class Artist(Resource):

    def __init__(self):
        self.songs_api = Genius()
        self.cache = RedisCache()
        self.db = DynamoDB()
        self.db.create_table_artists()

    def get(self, name, music_number=10):
        popular_music = self.songs_api.get_music(name, music_number)
        artist = {f'{name.title()}': popular_music}

    #------------------------------------------------------------
        if request.args.get('cache') is None:
            cache_query_string = True
        else:
            cache_query_string = eval(request.args('cache'))
        
        if self.cache.cache_exists(name):
                self.cache.cache_exists(name)
                music_list = self.cache.get_cache(name)
                artist = f'{name.title()} popular_music {music_list}'
        else:
            popular_music = self.songs_api.get_music(name, music_number)
            self.db.insert_artists_songs(name, popular_music)
            artist = {f"{name.title()} {popular_music} cache {cache_query_string}" }
            self.cache.add_cache(name, str(popular_music))
                    
        if not cache_query_string:
            self.cache.del_cache(name)
            popular_musics = self.songs_api.get_music(name, music_number)
            self.db.insert_artists_songs(name, popular_musics)
        else:
            print("Utilzando daos em cache")

        return artist


api.add_resource(Artist, '/artist/<name>')

if __name__ == '__main__':
    app.run(debug=True)
