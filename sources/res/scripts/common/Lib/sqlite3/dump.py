def _iterdump(connection):
    cu = connection.cursor()
    yield b'BEGIN TRANSACTION;'
    q = b'\n        SELECT "name", "type", "sql"\n        FROM "sqlite_master"\n            WHERE "sql" NOT NULL AND\n            "type" == \'table\'\n            ORDER BY "name"\n        '
    schema_res = cu.execute(q)
    for table_name, type, sql in schema_res.fetchall():
        if table_name == b'sqlite_sequence':
            yield b'DELETE FROM "sqlite_sequence";'
        elif table_name == b'sqlite_stat1':
            yield b'ANALYZE "sqlite_master";'
        elif table_name.startswith(b'sqlite_'):
            continue
        else:
            yield b'%s;' % sql
        table_name_ident = table_name.replace(b'"', b'""')
        res = cu.execute((b'PRAGMA table_info("{0}")').format(table_name_ident))
        column_names = [str(table_info[1]) for table_info in res.fetchall()]
        q = (b'SELECT \'INSERT INTO "{0}" VALUES({1})\' FROM "{0}";').format(table_name_ident, (b',').join((b'\'||quote("{0}")||\'').format(col.replace(b'"', b'""')) for col in column_names))
        query_res = cu.execute(q)
        for row in query_res:
            yield b'%s;' % row[0]

    q = b'\n        SELECT "name", "type", "sql"\n        FROM "sqlite_master"\n            WHERE "sql" NOT NULL AND\n            "type" IN (\'index\', \'trigger\', \'view\')\n        '
    schema_res = cu.execute(q)
    for name, type, sql in schema_res.fetchall():
        yield b'%s;' % sql

    yield b'COMMIT;'
    return
