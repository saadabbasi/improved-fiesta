from peewee import *

database = SqliteDatabase('Bill of Material Maker.db', **{})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Tubes(BaseModel):
    diameter = CharField(null=True)
    length = FloatField(null=True)  # float(128)
    location = CharField(null=True)
    part_number = CharField(null=True)
    type = CharField(null=True)

    class Meta:
        db_table = 'Tubes'

class Wires(BaseModel):
    circuit_a = CharField(null=True)
    circuit_b = CharField(null=True)
    colour = CharField(null=True)
    length = UnknownField(null=True)  # float(128)
    part_number = CharField(null=True)
    wire_gauge = UnknownField(null=True)  # float(128)
    wire_type = CharField(null=True)

    class Meta:
        db_table = 'Wires'

class SqliteStat1(BaseModel):
    idx = UnknownField(null=True)  # 
    stat = UnknownField(null=True)  # 
    tbl = UnknownField(null=True)  # 

    class Meta:
        db_table = 'sqlite_stat1'
        primary_key = False

class WireHarnessPartNumbers(BaseModel):
    wire_harness_part_number = CharField(null=True)

    class Meta:
        db_table = 'wire_harness_part_numbers'

