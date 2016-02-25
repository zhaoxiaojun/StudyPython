# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: interfaces.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='interfaces.proto',
  package='interfaces',
  serialized_pb=_b('\n\x10interfaces.proto\x12\ninterfaces\x1a\x0c\x63ommon.proto\"9\n\x12interface_info_ask\x12\x11\n\tuap_topic\x18\x01 \x01(\x0c\x12\x10\n\x08json_ask\x18\x02 \x01(\x0c\"H\n\x12interface_info_ans\x12\x10\n\x08json_ans\x18\x01 \x01(\x0c\x12 \n\x05\x65rror\x18\x02 \x01(\x0b\x32\x11.common.errorinfo')
  ,
  dependencies=[common_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_INTERFACE_INFO_ASK = _descriptor.Descriptor(
  name='interface_info_ask',
  full_name='interfaces.interface_info_ask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uap_topic', full_name='interfaces.interface_info_ask.uap_topic', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='json_ask', full_name='interfaces.interface_info_ask.json_ask', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=103,
)


_INTERFACE_INFO_ANS = _descriptor.Descriptor(
  name='interface_info_ans',
  full_name='interfaces.interface_info_ans',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='json_ans', full_name='interfaces.interface_info_ans.json_ans', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='interfaces.interface_info_ans.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=177,
)

_INTERFACE_INFO_ANS.fields_by_name['error'].message_type = common_pb2._ERRORINFO
DESCRIPTOR.message_types_by_name['interface_info_ask'] = _INTERFACE_INFO_ASK
DESCRIPTOR.message_types_by_name['interface_info_ans'] = _INTERFACE_INFO_ANS

interface_info_ask = _reflection.GeneratedProtocolMessageType('interface_info_ask', (_message.Message,), dict(
  DESCRIPTOR = _INTERFACE_INFO_ASK,
  __module__ = 'interfaces_pb2'
  # @@protoc_insertion_point(class_scope:interfaces.interface_info_ask)
  ))
_sym_db.RegisterMessage(interface_info_ask)

interface_info_ans = _reflection.GeneratedProtocolMessageType('interface_info_ans', (_message.Message,), dict(
  DESCRIPTOR = _INTERFACE_INFO_ANS,
  __module__ = 'interfaces_pb2'
  # @@protoc_insertion_point(class_scope:interfaces.interface_info_ans)
  ))
_sym_db.RegisterMessage(interface_info_ans)


# @@protoc_insertion_point(module_scope)