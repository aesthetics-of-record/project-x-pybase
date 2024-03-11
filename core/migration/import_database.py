from core.table.create_table import create_dynamic_table
from models.import_json import import_json_model

json_data = [
    {
        "id": "dbid1",
        "name": "db1",
        "table": [
            {
                "id": "tableid1",
                "name": "table1",
                "schema": [
                    {
                        "id": "schemaid1",
                        "name": "title",
                        "type": "TEXT"
                    },
                    {
                        "id": "schemaid2",
                        "name": "content",
                        "type": "TEXT"
                    }
                ]
            },
            {
                "id": "tableid2",
                "name": "table2",
                "schema": [
                    {
                        "id": "schemaid1",
                        "name": "title2",
                        "type": "TEXT"
                    },
                    {
                        "id": "schemaid2",
                        "name": "content2",
                        "type": "TEXT"
                    }
                ]
            }
        ]
    }
]


def import_database(import_json: import_json_model):
    for db in import_json:
        for table in db.get('table'):
            table_info = []
            for schema in table.get('schema'):
                table_info.append((schema.get('name'), schema.get('type'), {}))

            create_dynamic_table(table.get('name'), table_info)




