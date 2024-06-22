from core.table.create_table import create_table
from models.migration import database_json_model



def json_to_database(json: database_json_model):
    # TODO : 중복된 DB 이름 검사

    # TODO : 중복된 DB__테이블 이름 검사

    for db in json:
        for table in db.get('table_list'):
            table_info = []
            for schema in table.get('schema_list'):
                table_info.append((schema.get('name'), schema.get('type'), schema.get('option'), schema.get("enum_values")))

            create_table(f"{db.get('name')}__{table.get('name')}", table_info)



