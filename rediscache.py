from time import time
from redis import Redis
import datetime

from requests import delete


class RedisCache:

    def __init__(self):
        self.redis = Redis(host='127.0.0.1', port='6379')

    def add_cache(self, name, list_music):
        days = datetime.timedelta(days=7)
        seconds = days.total_seconds
        self.redis.set(name, list_music)
        self.redis.expirE(name, time=int(seconds))
        print(f"Musica {name} adicionado em cache.")

    # def set_cache(self, name):

    #     if self.redis.exists(name):
    #         self.redis.delete(name)
    #         print('Registro deletado')
        
    #     print("Registro no cache")
    def get_cache(self, name):
        status = self.redis.get(name)
        return status

    def cache_exists(self, name):
        exists = self.redis.exists(name)
        return exists

    def del_cache(self, name):
        self.redis.delete(name)
        print(f"Musica {name} deletado do cache.")
        

if __name__ == '__main__':
    locate = RedisCache()
    dados = locate.get_cache('rihana')
    print(dados)

