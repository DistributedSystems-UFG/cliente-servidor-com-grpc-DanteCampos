# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ncalc.proto\x12\x04\x63\x61lc\"!\n\tInNumbers\x12\t\n\x01\x61\x18\x01 \x01(\x01\x12\t\n\x01\x62\x18\x02 \x01(\x01\"\x1b\n\tOutNumber\x12\x0e\n\x06result\x18\x01 \x01(\x01\x32\x8e\x01\n\nCalculator\x12)\n\x03\x61\x64\x64\x12\x0f.calc.InNumbers\x1a\x0f.calc.OutNumber\"\x00\x12*\n\x04mult\x12\x0f.calc.InNumbers\x1a\x0f.calc.OutNumber\"\x00\x12)\n\x03pow\x12\x0f.calc.InNumbers\x1a\x0f.calc.OutNumber\"\x00\x62\x06proto3')



_INNUMBERS = DESCRIPTOR.message_types_by_name['InNumbers']
_OUTNUMBER = DESCRIPTOR.message_types_by_name['OutNumber']
InNumbers = _reflection.GeneratedProtocolMessageType('InNumbers', (_message.Message,), {
  'DESCRIPTOR' : _INNUMBERS,
  '__module__' : 'calc_pb2'
  # @@protoc_insertion_point(class_scope:calc.InNumbers)
  })
_sym_db.RegisterMessage(InNumbers)

OutNumber = _reflection.GeneratedProtocolMessageType('OutNumber', (_message.Message,), {
  'DESCRIPTOR' : _OUTNUMBER,
  '__module__' : 'calc_pb2'
  # @@protoc_insertion_point(class_scope:calc.OutNumber)
  })
_sym_db.RegisterMessage(OutNumber)

_CALCULATOR = DESCRIPTOR.services_by_name['Calculator']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INNUMBERS._serialized_start=20
  _INNUMBERS._serialized_end=53
  _OUTNUMBER._serialized_start=55
  _OUTNUMBER._serialized_end=82
  _CALCULATOR._serialized_start=85
  _CALCULATOR._serialized_end=227
# @@protoc_insertion_point(module_scope)
