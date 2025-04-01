from faker import Faker
from faker_food import FoodProvider
import  random
from common_func import get_conf_dev, get_connection_to_psql, execute_psql_query


class DataGenerator():
    def __init__(self, generate_user_profile=True, count_users_rows=1000, generate_shop=True, count_goods_rows=1000):
        self.generate_user_profile = generate_user_profile
        self.generate_shop = generate_shop
        self.count_users_rows = count_users_rows
        self.count_goods_rows = count_goods_rows


    def generate(self):
        fake = Faker("ru_RU")
        conf = get_conf_dev()
        conn = get_connection_to_psql(conf)

        if self.generate_shop:
            query_set = self._parce_sql_in_queries_list("shop.sql")
            for query in query_set: execute_psql_query(query, conn)
            self._fill_dict(conn, "shop.units")
            self._fill_dict(conn, "shop.category")
            self._create_goods(fake, conn)

        if self.generate_user_profile:
            query_set = self._parce_sql_in_queries_list("user_data.sql")
            for query in query_set: execute_psql_query(query, conn)
            self._create_users(fake, conn)

    def _create_users(self, fake, conn):
        rows= []
        for i in range(0, self.count_users_rows):
            row = [
                i,
                fake.phone_number(),
                fake.email(),
                fake.address(),
                int(fake.credit_card_number())
            ]
            rows+=row


    def _create_goods(self, fake, conn):
        rows = []
        fake.add_provider(FoodProvider)
        for i in  range(0, self.count_goods_rows):
            row = [
                i,
                random.randint(1, 8),
                fake.vegetable(),
                round(random.uniform(0,100), 1),
                random.randint(1, 8),
                round(random.uniform(0, 1000), 2),
                fake.dish_description(),
                None
            ]
            rows+=row


    def _parce_sql_in_queries_list(self, file_name):
        with open(f"./databases/psql/{file_name}") as file:
            file = file.read()
            query_set = file.split(';')
        return  query_set

    def _fill_dict(self, conn, dict_name):
        match dict_name:
            case "shop.units":
                col_names = self._dict_shop_units()[0]
                dict = self._dict_shop_units()[1:]
            case "shop.category":
                col_names = self._dict_shop_category()[0]
                dict = self._dict_shop_category()[1:]

        tuples = [tuple(x) for x in dict]
        query = "INSERT INTO %s(%s) VALUES %%s" % (dict_name, col_names)
        execute_psql_query(conn, query, tuples)

    def _dict_shop_units(self):
        return [
            ["id", "name"],
            [1, 'кг'],
            [2, 'г'],
            [3, 'л'],
            [4, 'мл']
        ]

    def _dict_shop_category(self):
        return  [
            ["id", "name", "description"],
            [1, 'Овощи', 'Свежие овощи, выращенные на местных фермах'],
            [2, 'Фрукты', 'Сочные фрукты из разных уголков мира'],
            [3, 'Зелень', 'Разнообразная свежая зелень'],
            [4, 'Ягоды', 'Спелые ягоды всех видов'],
            [5, 'Экзотические', 'Редкие и необычные фрукты и овощи'],
            [6, 'Консервированные', 'Законсервированные продукты длительного срока'],
            [7, 'Сухофрукты', 'Высушенные фрукты и ягоды'],
            [8, 'Замороженные', 'Быстро замороженные овощи и фрукты']
        ]


generator = DataGenerator(
    generate_user_profile=True,
    count_users_rows=1000,
    generate_shop=True,
    count_goods_rows=1000
)
generator.generate()



