import logging
import asyncpg
from asyncpg.pool import Pool
from data import config


class Database:
    def __init__(self, pool):
        self.pool: Pool = pool


    @classmethod
    async def create(cls):

        pool = await asyncpg.create_pool(
            user=config.dbuser, password=config.dbpassword, host=config.ip
        )
        logging.info('Connecting to database. . .')
        return cls(pool)

    async def get_user_id(self, user_id):
        sql = f'''INSERT INTO public.user VALUES ( {user_id} )'''
        logging.info('Get user id. . .')
        return await self.pool.fetch(sql)

    async def user_data(self):
        sql = f'''SELECT userid FROM public.user '''
        logging.info('Get user id. . .')
        return await self.pool.fetch(sql)

    async def get_all_id(self, row_num):
        sql = f'''SELECT userid FROM public.user LIMIT 1 offset {row_num}'''
        return await self.pool.fetchval(sql)

    async def insert_data(self, id, name, wish):
        sql = f'''INSERT INTO public.data VALUES({id}, '{name}', '{wish}')'''
        return await self.pool.fetch(sql)

    async def write_enduser(self, id):
        sql = f'''INSERT INTO public.enduser VALUES({id})'''
        return await self.pool.fetch(sql)

    async def delete_enduser(self):
        sql = f'''DELETE FROM public.enduser'''
        return await self.pool.fetch(sql)

    async def read_all_enduser(self):
        sql = f'''SELECT id FROM public.enduser'''
        return await self.pool.fetch(sql)

    async def read_enduser(self, row_num):
        sql = f'''SELECT id FROM public.enduser LIMIT 1 offset {row_num}'''
        return await self.pool.fetchval(sql)

    async def read_id_data(self, id):
        sql = f'''SELECT tg_id FROM public.data LIMIT 1 offset {id}'''
        return await self.pool.fetchval(sql)

    async def read_name_data(self, id):
        sql = f'''SELECT name FROM public.data WHERE tg_id={id}'''
        return await self.pool.fetchval(sql)

    async def read_wish_data(self, id):
        sql = f'''SELECT wish FROM public.data WHERE tg_id={id}'''
        return await self.pool.fetchval(sql)

    async def change_data(self, oldstring, newstring):
        sql = f'''UPDATE public.data set wish = replace(wish, '{oldstring}', '{newstring}')'''
        return await self.pool.fetch(sql)
