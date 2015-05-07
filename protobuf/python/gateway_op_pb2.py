# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway_op.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway_op.proto',
  package='nway_fs_opterator',
  serialized_pb=_b('\n\x10gateway_op.proto\x12\x11nway_fs_opterator\"\xe9\x02\n\x0cnway_gateway\x12\x14\n\x0cgateway_name\x18\x01 \x02(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05realm\x18\x03 \x01(\t\x12\x11\n\tfrom_user\x18\x04 \x01(\t\x12\x13\n\x0b\x66rom_domain\x18\x05 \x01(\t\x12\x10\n\x08password\x18\x06 \x01(\t\x12\x11\n\textension\x18\x07 \x01(\t\x12\r\n\x05proxy\x18\x08 \x01(\t\x12\x16\n\x0e\x65xpire_seconds\x18\t \x01(\t\x12\x10\n\x08register\x18\n \x01(\t\x12\x1a\n\x12register_transport\x18\x0b \x01(\t\x12\x15\n\rretry_seconds\x18\x0c \x01(\t\x12\x19\n\x11\x63\x61ller_id_in_from\x18\r \x01(\t\x12\x16\n\x0e\x63ontact_params\x18\x0e \x01(\t\x12\x0c\n\x04ping\x18\x0f \x01(\t\x12\x10\n\x08\x66ilename\x18\x10 \x01(\t\x12\x16\n\x0eregister_proxy\x18\x11 \x01(\t\"Q\n\x15get_nway_gateways_req\x12\x0c\n\x04\x66\x61lg\x18\x01 \x02(\t\x12\x11\n\tstart_pos\x18\x02 \x02(\x05\x12\x17\n\x0fnumber_per_page\x18\x03 \x02(\x05\"}\n\x15get_nway_gateways_rsp\x12\x31\n\x06status\x18\x01 \x02(\x0e\x32!.nway_fs_opterator.nway_op_status\x12\x31\n\x08gateways\x18\x02 \x03(\x0b\x32\x1f.nway_fs_opterator.nway_gateway\"H\n\x14\x61\x64\x64_nway_gateway_req\x12\x30\n\x07gateway\x18\x01 \x02(\x0b\x32\x1f.nway_fs_opterator.nway_gateway\"q\n\x14\x61\x64\x64_nway_gateway_rsp\x12\x14\n\x0cgateway_name\x18\x01 \x02(\t\x12\x31\n\x06status\x18\x02 \x02(\x0e\x32!.nway_fs_opterator.nway_op_status\x12\x10\n\x08res_text\x18\x03 \x01(\t\"I\n\x15\x65\x64it_nway_gateway_req\x12\x30\n\x07gateway\x18\x01 \x02(\x0b\x32\x1f.nway_fs_opterator.nway_gateway\"r\n\x15\x65\x64it_nway_gateway_rsp\x12\x14\n\x0cgateway_name\x18\x01 \x02(\t\x12\x31\n\x06status\x18\x02 \x02(\x0e\x32!.nway_fs_opterator.nway_op_status\x12\x10\n\x08res_text\x18\x03 \x01(\t\"J\n\x16\x65rase_nway_gateway_req\x12\x30\n\x07gateway\x18\x01 \x02(\x0b\x32\x1f.nway_fs_opterator.nway_gateway\"s\n\x16\x65rase_nway_gateway_rsp\x12\x14\n\x0cgateway_name\x18\x01 \x02(\t\x12\x31\n\x06status\x18\x02 \x02(\x0e\x32!.nway_fs_opterator.nway_op_status\x12\x10\n\x08res_text\x18\x03 \x01(\t\"B\n\x12reload_gateway_req\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"G\n\x12reload_gateway_rsp\x12\x31\n\x06status\x18\x01 \x02(\x0e\x32!.nway_fs_opterator.nway_op_status*C\n\x0enway_op_status\x12\x0b\n\x07success\x10\x01\x12\n\n\x06\x66\x61iled\x10\x02\x12\x0c\n\x08notfound\x10\x03\x12\n\n\x06unknow\x10\x04')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_NWAY_OP_STATUS = _descriptor.EnumDescriptor(
  name='nway_op_status',
  full_name='nway_fs_opterator.nway_op_status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='success', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='failed', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='notfound', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='unknow', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1327,
  serialized_end=1394,
)
_sym_db.RegisterEnumDescriptor(_NWAY_OP_STATUS)

nway_op_status = enum_type_wrapper.EnumTypeWrapper(_NWAY_OP_STATUS)
success = 1
failed = 2
notfound = 3
unknow = 4



_NWAY_GATEWAY = _descriptor.Descriptor(
  name='nway_gateway',
  full_name='nway_fs_opterator.nway_gateway',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gateway_name', full_name='nway_fs_opterator.nway_gateway.gateway_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='username', full_name='nway_fs_opterator.nway_gateway.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='realm', full_name='nway_fs_opterator.nway_gateway.realm', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_user', full_name='nway_fs_opterator.nway_gateway.from_user', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_domain', full_name='nway_fs_opterator.nway_gateway.from_domain', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='nway_fs_opterator.nway_gateway.password', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extension', full_name='nway_fs_opterator.nway_gateway.extension', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proxy', full_name='nway_fs_opterator.nway_gateway.proxy', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expire_seconds', full_name='nway_fs_opterator.nway_gateway.expire_seconds', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='register', full_name='nway_fs_opterator.nway_gateway.register', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='register_transport', full_name='nway_fs_opterator.nway_gateway.register_transport', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='retry_seconds', full_name='nway_fs_opterator.nway_gateway.retry_seconds', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='caller_id_in_from', full_name='nway_fs_opterator.nway_gateway.caller_id_in_from', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='contact_params', full_name='nway_fs_opterator.nway_gateway.contact_params', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ping', full_name='nway_fs_opterator.nway_gateway.ping', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filename', full_name='nway_fs_opterator.nway_gateway.filename', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='register_proxy', full_name='nway_fs_opterator.nway_gateway.register_proxy', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=40,
  serialized_end=401,
)


_GET_NWAY_GATEWAYS_REQ = _descriptor.Descriptor(
  name='get_nway_gateways_req',
  full_name='nway_fs_opterator.get_nway_gateways_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='falg', full_name='nway_fs_opterator.get_nway_gateways_req.falg', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_pos', full_name='nway_fs_opterator.get_nway_gateways_req.start_pos', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number_per_page', full_name='nway_fs_opterator.get_nway_gateways_req.number_per_page', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=403,
  serialized_end=484,
)


_GET_NWAY_GATEWAYS_RSP = _descriptor.Descriptor(
  name='get_nway_gateways_rsp',
  full_name='nway_fs_opterator.get_nway_gateways_rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='nway_fs_opterator.get_nway_gateways_rsp.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gateways', full_name='nway_fs_opterator.get_nway_gateways_rsp.gateways', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=486,
  serialized_end=611,
)


_ADD_NWAY_GATEWAY_REQ = _descriptor.Descriptor(
  name='add_nway_gateway_req',
  full_name='nway_fs_opterator.add_nway_gateway_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gateway', full_name='nway_fs_opterator.add_nway_gateway_req.gateway', index=0,
      number=1, type=11, cpp_type=10, label=2,
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
  serialized_start=613,
  serialized_end=685,
)


_ADD_NWAY_GATEWAY_RSP = _descriptor.Descriptor(
  name='add_nway_gateway_rsp',
  full_name='nway_fs_opterator.add_nway_gateway_rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gateway_name', full_name='nway_fs_opterator.add_nway_gateway_rsp.gateway_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='nway_fs_opterator.add_nway_gateway_rsp.status', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='res_text', full_name='nway_fs_opterator.add_nway_gateway_rsp.res_text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=687,
  serialized_end=800,
)


_EDIT_NWAY_GATEWAY_REQ = _descriptor.Descriptor(
  name='edit_nway_gateway_req',
  full_name='nway_fs_opterator.edit_nway_gateway_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gateway', full_name='nway_fs_opterator.edit_nway_gateway_req.gateway', index=0,
      number=1, type=11, cpp_type=10, label=2,
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
  serialized_start=802,
  serialized_end=875,
)


_EDIT_NWAY_GATEWAY_RSP = _descriptor.Descriptor(
  name='edit_nway_gateway_rsp',
  full_name='nway_fs_opterator.edit_nway_gateway_rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gateway_name', full_name='nway_fs_opterator.edit_nway_gateway_rsp.gateway_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='nway_fs_opterator.edit_nway_gateway_rsp.status', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='res_text', full_name='nway_fs_opterator.edit_nway_gateway_rsp.res_text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=877,
  serialized_end=991,
)


_ERASE_NWAY_GATEWAY_REQ = _descriptor.Descriptor(
  name='erase_nway_gateway_req',
  full_name='nway_fs_opterator.erase_nway_gateway_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gateway', full_name='nway_fs_opterator.erase_nway_gateway_req.gateway', index=0,
      number=1, type=11, cpp_type=10, label=2,
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
  serialized_start=993,
  serialized_end=1067,
)


_ERASE_NWAY_GATEWAY_RSP = _descriptor.Descriptor(
  name='erase_nway_gateway_rsp',
  full_name='nway_fs_opterator.erase_nway_gateway_rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gateway_name', full_name='nway_fs_opterator.erase_nway_gateway_rsp.gateway_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='nway_fs_opterator.erase_nway_gateway_rsp.status', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='res_text', full_name='nway_fs_opterator.erase_nway_gateway_rsp.res_text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1069,
  serialized_end=1184,
)


_RELOAD_GATEWAY_REQ = _descriptor.Descriptor(
  name='reload_gateway_req',
  full_name='nway_fs_opterator.reload_gateway_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='nway_fs_opterator.reload_gateway_req.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='nway_fs_opterator.reload_gateway_req.port', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='nway_fs_opterator.reload_gateway_req.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1186,
  serialized_end=1252,
)


_RELOAD_GATEWAY_RSP = _descriptor.Descriptor(
  name='reload_gateway_rsp',
  full_name='nway_fs_opterator.reload_gateway_rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='nway_fs_opterator.reload_gateway_rsp.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
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
  serialized_start=1254,
  serialized_end=1325,
)

_GET_NWAY_GATEWAYS_RSP.fields_by_name['status'].enum_type = _NWAY_OP_STATUS
_GET_NWAY_GATEWAYS_RSP.fields_by_name['gateways'].message_type = _NWAY_GATEWAY
_ADD_NWAY_GATEWAY_REQ.fields_by_name['gateway'].message_type = _NWAY_GATEWAY
_ADD_NWAY_GATEWAY_RSP.fields_by_name['status'].enum_type = _NWAY_OP_STATUS
_EDIT_NWAY_GATEWAY_REQ.fields_by_name['gateway'].message_type = _NWAY_GATEWAY
_EDIT_NWAY_GATEWAY_RSP.fields_by_name['status'].enum_type = _NWAY_OP_STATUS
_ERASE_NWAY_GATEWAY_REQ.fields_by_name['gateway'].message_type = _NWAY_GATEWAY
_ERASE_NWAY_GATEWAY_RSP.fields_by_name['status'].enum_type = _NWAY_OP_STATUS
_RELOAD_GATEWAY_RSP.fields_by_name['status'].enum_type = _NWAY_OP_STATUS
DESCRIPTOR.message_types_by_name['nway_gateway'] = _NWAY_GATEWAY
DESCRIPTOR.message_types_by_name['get_nway_gateways_req'] = _GET_NWAY_GATEWAYS_REQ
DESCRIPTOR.message_types_by_name['get_nway_gateways_rsp'] = _GET_NWAY_GATEWAYS_RSP
DESCRIPTOR.message_types_by_name['add_nway_gateway_req'] = _ADD_NWAY_GATEWAY_REQ
DESCRIPTOR.message_types_by_name['add_nway_gateway_rsp'] = _ADD_NWAY_GATEWAY_RSP
DESCRIPTOR.message_types_by_name['edit_nway_gateway_req'] = _EDIT_NWAY_GATEWAY_REQ
DESCRIPTOR.message_types_by_name['edit_nway_gateway_rsp'] = _EDIT_NWAY_GATEWAY_RSP
DESCRIPTOR.message_types_by_name['erase_nway_gateway_req'] = _ERASE_NWAY_GATEWAY_REQ
DESCRIPTOR.message_types_by_name['erase_nway_gateway_rsp'] = _ERASE_NWAY_GATEWAY_RSP
DESCRIPTOR.message_types_by_name['reload_gateway_req'] = _RELOAD_GATEWAY_REQ
DESCRIPTOR.message_types_by_name['reload_gateway_rsp'] = _RELOAD_GATEWAY_RSP
DESCRIPTOR.enum_types_by_name['nway_op_status'] = _NWAY_OP_STATUS

nway_gateway = _reflection.GeneratedProtocolMessageType('nway_gateway', (_message.Message,), dict(
  DESCRIPTOR = _NWAY_GATEWAY,
  __module__ = 'gateway_op_pb2'
  # @@protoc_insertion_point(class_scope:nway_fs_opterator.nway_gateway)
  ))
_sym_db.RegisterMessage(nway_gateway)

get_nway_gateways_req = _reflection.GeneratedProtocolMessageType('get_nway_gateways_req', (_message.Message,), dict(
  DESCRIPTOR = _GET_NWAY_GATEWAYS_REQ,
  __module__ = 'gateway_op_pb2'
  # @@protoc_insertion_point(class_scope:nway_fs_opterator.get_nway_gateways_req)
  ))
_sym_db.RegisterMessage(get_nway_gateways_req)

get_nway_gateways_rsp = _reflection.GeneratedProtocolMessageType('get_nway_gateways_rsp', (_message.Message,), dict(
  DESCRIPTOR = _GET_NWAY_GATEWAYS_RSP,
  __module__ = 'gateway_op_pb2'
  # @@protoc_insertion_point(class_scope:nway_fs_opterator.get_nway_gateways_rsp)
  ))
_sym_db.RegisterMessage(get_nway_gateways_rsp)

add_nway_gateway_req = _reflection.GeneratedProtocolMessageType('add_nway_gateway_req', (_message.Message,), dict(
  DESCRIPTOR = _ADD_NWAY_GATEWAY_REQ,
  __module__ = 'gateway_op_pb2'
  # @@protoc_insertion_point(class_scope:nway_fs_opterator.add_nway_gateway_req)
  ))
_sym_db.RegisterMessage(add_nway_gateway_req)

add_nway_gateway_rsp = _reflection.GeneratedProtocolMessageType('add_nway_gateway_rsp', (_message.Message,), dict(
  DESCRIPTOR = _ADD_NWAY_GATEWAY_RSP,
  __module__ = 'gateway_op_pb2'
  # @@protoc_insertion_point(class_scope:nway_fs_opterator.add_nway_gateway_rsp)
  ))
_sym_db.RegisterMessage(add_nway_gateway_rsp)

edit_nway_gateway_req = _reflection.GeneratedProtocolMessageType('edit_nway_gateway_req', (_message.Message,), dict(
  DESCRIPTOR = _EDIT_NWAY_GATEWAY_REQ,
  __module__ = 'gateway_op_pb2'
  # @@protoc_insertion_point(class_scope:nway_fs_opterator.edit_nway_gateway_req)
  ))
_sym_db.RegisterMessage(edit_nway_gateway_req)

edit_nway_gateway_rsp = _reflection.GeneratedProtocolMessageType('edit_nway_gateway_rsp', (_message.Message,), dict(
  DESCRIPTOR = _EDIT_NWAY_GATEWAY_RSP,
  __module__ = 'gateway_op_pb2'
  # @@protoc_insertion_point(class_scope:nway_fs_opterator.edit_nway_gateway_rsp)
  ))
_sym_db.RegisterMessage(edit_nway_gateway_rsp)

erase_nway_gateway_req = _reflection.GeneratedProtocolMessageType('erase_nway_gateway_req', (_message.Message,), dict(
  DESCRIPTOR = _ERASE_NWAY_GATEWAY_REQ,
  __module__ = 'gateway_op_pb2'
  # @@protoc_insertion_point(class_scope:nway_fs_opterator.erase_nway_gateway_req)
  ))
_sym_db.RegisterMessage(erase_nway_gateway_req)

erase_nway_gateway_rsp = _reflection.GeneratedProtocolMessageType('erase_nway_gateway_rsp', (_message.Message,), dict(
  DESCRIPTOR = _ERASE_NWAY_GATEWAY_RSP,
  __module__ = 'gateway_op_pb2'
  # @@protoc_insertion_point(class_scope:nway_fs_opterator.erase_nway_gateway_rsp)
  ))
_sym_db.RegisterMessage(erase_nway_gateway_rsp)

reload_gateway_req = _reflection.GeneratedProtocolMessageType('reload_gateway_req', (_message.Message,), dict(
  DESCRIPTOR = _RELOAD_GATEWAY_REQ,
  __module__ = 'gateway_op_pb2'
  # @@protoc_insertion_point(class_scope:nway_fs_opterator.reload_gateway_req)
  ))
_sym_db.RegisterMessage(reload_gateway_req)

reload_gateway_rsp = _reflection.GeneratedProtocolMessageType('reload_gateway_rsp', (_message.Message,), dict(
  DESCRIPTOR = _RELOAD_GATEWAY_RSP,
  __module__ = 'gateway_op_pb2'
  # @@protoc_insertion_point(class_scope:nway_fs_opterator.reload_gateway_rsp)
  ))
_sym_db.RegisterMessage(reload_gateway_rsp)


# @@protoc_insertion_point(module_scope)
