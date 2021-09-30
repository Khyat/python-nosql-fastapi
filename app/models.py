from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class Product(Model):
    __keyspace__ = "fastapi_app"
    asin = columns.Text(primary_key=true,required=true)
    title = columns.Text()