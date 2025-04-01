import json
import psycopg2
import psycopg2.extras as extras



def get_conf_dev():
    try:
        with open("./dev_config/conf.json") as file:
            conf = json.load(file)
        return conf
    except IOError as e:
        print(e)
        raise "Не удалось считать конфигурацию"

def get_connection_to_psql(conf):
    psql_conf = conf["postgres_dev"]
    try:
        conn = psycopg2.connect(host=psql_conf["host"],
                                    port=psql_conf["port"],
                                    user=psql_conf["user"],
                                    password=psql_conf["password"],
                                    database=psql_conf["database"])
        return conn
    except psycopg2.OperationalError as e:
        print(e)
        raise "Не удалось подключиться к Postgres"


def execute_psql_query(query, conn, tpl=None):
    if tpl is None:
        with conn.cursor() as cur:
            cur.execute(query)
    else:
        with conn.cursor() as cur:
            extras.execute_values(cur, query, tpl)
