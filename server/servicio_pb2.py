# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: servicio.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eservicio.proto\"*\n\x05Pizza\x12\x0f\n\x07topping\x18\x01 \x03(\t\x12\x10\n\x08pulgadas\x18\x02 \x01(\x05\"2\n\x05Orden\x12\x16\n\x06pizzas\x18\x01 \x03(\x0b\x32\x06.Pizza\x12\x11\n\tdireccion\x18\x02 \x01(\t\"-\n\x11\x43onfirmacionOrden\x12\x18\n\x10\x65ntrega_estimada\x18\x01 \x01(\x03\"\x06\n\x04Nulo2N\n\x08Pizzeria\x12\x15\n\x05Listo\x12\x05.Nulo\x1a\x05.Nulo\x12+\n\rRegistraOrden\x12\x06.Orden\x1a\x12.ConfirmacionOrdenb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'servicio_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PIZZA']._serialized_start=18
  _globals['_PIZZA']._serialized_end=60
  _globals['_ORDEN']._serialized_start=62
  _globals['_ORDEN']._serialized_end=112
  _globals['_CONFIRMACIONORDEN']._serialized_start=114
  _globals['_CONFIRMACIONORDEN']._serialized_end=159
  _globals['_NULO']._serialized_start=161
  _globals['_NULO']._serialized_end=167
  _globals['_PIZZERIA']._serialized_start=169
  _globals['_PIZZERIA']._serialized_end=247
# @@protoc_insertion_point(module_scope)