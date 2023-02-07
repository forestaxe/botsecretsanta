import logging

import asyncpg
from asyncpg.pool import Pool

from data import config
# results = cur.fetchall()

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





    # cur = Database.cursor()
    # cur.execute = ('''SELECT * FROM public."Admins"''')
    # query_results = cur.fetchall()
    # text = '\n\n'.join([', '.join(map(str, x)) for x in query_results])
    # return (str(text))
    # sql = '''create schema cracktable'''

    # @staticmethod

    # async def get_categories() -> List[Item]:
    #     return await


    # def format_args(sql, parameters: dict):
    #     sql += " AND ".join([
    #         f"{item} = ${num}" for num, item in enumerate(parameters, start=1)
    #     ])
    #     return sql, tuple(parameters.values())
    #
    # async def add_user(self, id: int, name: str, email: str = 0):
    #     sql = "INSERT INTO public.UserTopics (chatid, author, title) VALUES($1, $2, $3)"
    #     return await self.pool.execute(sql, id, name, email)
    #
    # async def select_all_users(self):
    #     sql = '''SELECT * FROM UserTopics'''
    #     logging.info('Select table users. . .')
    #     return await self.pool.fetch(sql)
    #
    # async def select_user(self, **kwargs):
    #     sql = "SELECT * FROM users WHERE "
    #     sql, parameters = self.format_args(sql, kwargs)
    #     await self.pool.fetchrow(sql, *parameters)
    #
    # async def save(self):
    #     logging.info('Select table users. . .')
    #     # return self.pool.fetch('''SELECT COUNT(*) FROM Admins''')
    #     # sql = '''INSERT INTO admins (id, email) VALUES (1, 2)'''
    #     sql = '''SELECT COUNT(*) FROM public."Users";'''
    #     return await self.pool.execute(sql)
