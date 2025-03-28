from faker import Faker
from


class DataGenerator():
    def __init__(self, generate_user_profile=True, count_users_rows=1000, generate_shop=True, count_goods_rows=1000):
        self.generate_user_profile = generate_user_profile
        self.generate_shop = generate_shop
        self.count_users_rows = count_users_rows
        self.count_goods_rows = count_goods_rows


    def generate(self):
        if self.generate_shop:


        if self.generate_user_profile:
            pass

    def _parce_sql_in_queries_list(self, file_name):
        with open(f"./databases/psql/{file_name}") as file:
            file = file.read()
            file.

    def _create_tables_and_schemas(self, queries):
        for query in queries:
            pass

    def _dict_shop_units(self):
        return [
            [1, 'кг'],
            [2, 'г'],
            [3, 'л'],
            [4, 'мл']
        ]

    def _dict_shop_category(self):
        return  [
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



