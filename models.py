from peewee import *

database = SqliteDatabase('Bill of Material Maker.db', **{})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Tubes(BaseModel):
    diameter = CharField(null=True)
    length = UnknownField(null=True)  # float(128)
    location = CharField(null=True)
    part_number = CharField(null=True)
    type = CharField(null=True)

    class Meta:
        db_table = 'Tubes'

class Connectors(BaseModel):
    colour = CharField(null=True)
    dwg_part_number = CharField()
    identified_part_number = CharField(null=True)
    location = CharField()

    class Meta:
        db_table = 'connectors'

class ChildTerminals(BaseModel):
    parent_connector = ForeignKeyField(db_column='parent_connector', null=True, rel_model=Connectors, to_field='id')
    part_number = CharField(null=True)

    class Meta:
        db_table = 'child_terminals'

class Circuits(BaseModel):
    circuit_a = CharField(null=True)
    circuit_b = CharField(null=True)
    from_terminal = ForeignKeyField(db_column='from_terminal_id', null=True, rel_model=ChildTerminals, to_field='id')
    to_terminal = ForeignKeyField(db_column='to_terminal_id', null=True, rel_model=ChildTerminals, related_name='child_terminals_to_terminal_set', to_field='id')
    wire_colour = CharField(null=True)
    wire_gauge = CharField(null=True)
    wire_type = CharField(null=True)

    class Meta:
        db_table = 'circuits'

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

