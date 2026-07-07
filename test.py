from sqlglot import parse_one
from sqlglot.optimizer.annotate_types import annotate_types

dialect = "mysql"
sql = "SELECT Floor(1.9)"

ast = parse_one(sql, dialect=dialect)
annotated = annotate_types(ast, dialect=dialect)

print(repr(annotated))