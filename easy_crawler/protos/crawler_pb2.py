# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crawler.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='crawler.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\rcrawler.proto\"\xc7\x01\n\x0e\x43rawlerRequest\x12\x0b\n\x03url\x18\x01 \x01(\t\x12&\n\x06method\x18\x02 \x01(\x0e\x32\x16.CrawlerRequest.Method\x12\x18\n\x07headers\x18\x03 \x03(\x0b\x32\x07.Header\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\x12\x0f\n\x07timeout\x18\x05 \x01(\x02\x12\x11\n\tmax_retry\x18\x06 \x01(\x05\x12\x17\n\x0f\x61llow_redirects\x18\x07 \x01(\x08\"\x1b\n\x06Method\x12\x07\n\x03GET\x10\x00\x12\x08\n\x04POST\x10\x01\"\xd6\x01\n\x0f\x43rawlerResponse\x12\'\n\x06status\x18\x01 \x01(\x0e\x32\x17.CrawlerResponse.Status\x12\x0c\n\x04\x62ody\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\x05\x12\x18\n\x07headers\x18\x04 \x03(\x0b\x32\x07.Header\x12\x0b\n\x03msg\x18\x05 \x01(\t\x12\x11\n\tretry_num\x18\x06 \x01(\x05\x12 \n\x07request\x18\x07 \x01(\x0b\x32\x0f.CrawlerRequest\"\"\n\x06Status\x12\x0b\n\x07\x46\x41ILURE\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\"$\n\x06Header\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t29\n\x07\x43rawler\x12.\n\x07request\x12\x0f.CrawlerRequest\x1a\x10.CrawlerResponse\"\x00\x62\x06proto3')
)



_CRAWLERREQUEST_METHOD = _descriptor.EnumDescriptor(
  name='Method',
  full_name='CrawlerRequest.Method',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POST', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=190,
  serialized_end=217,
)
_sym_db.RegisterEnumDescriptor(_CRAWLERREQUEST_METHOD)

_CRAWLERRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='CrawlerResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=400,
  serialized_end=434,
)
_sym_db.RegisterEnumDescriptor(_CRAWLERRESPONSE_STATUS)


_CRAWLERREQUEST = _descriptor.Descriptor(
  name='CrawlerRequest',
  full_name='CrawlerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='CrawlerRequest.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='method', full_name='CrawlerRequest.method', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='headers', full_name='CrawlerRequest.headers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='CrawlerRequest.data', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='CrawlerRequest.timeout', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_retry', full_name='CrawlerRequest.max_retry', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allow_redirects', full_name='CrawlerRequest.allow_redirects', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CRAWLERREQUEST_METHOD,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=217,
)


_CRAWLERRESPONSE = _descriptor.Descriptor(
  name='CrawlerResponse',
  full_name='CrawlerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='CrawlerResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='CrawlerResponse.body', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='CrawlerResponse.code', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='headers', full_name='CrawlerResponse.headers', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='CrawlerResponse.msg', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retry_num', full_name='CrawlerResponse.retry_num', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request', full_name='CrawlerResponse.request', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CRAWLERRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=220,
  serialized_end=434,
)


_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Header.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Header.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=436,
  serialized_end=472,
)

_CRAWLERREQUEST.fields_by_name['method'].enum_type = _CRAWLERREQUEST_METHOD
_CRAWLERREQUEST.fields_by_name['headers'].message_type = _HEADER
_CRAWLERREQUEST_METHOD.containing_type = _CRAWLERREQUEST
_CRAWLERRESPONSE.fields_by_name['status'].enum_type = _CRAWLERRESPONSE_STATUS
_CRAWLERRESPONSE.fields_by_name['headers'].message_type = _HEADER
_CRAWLERRESPONSE.fields_by_name['request'].message_type = _CRAWLERREQUEST
_CRAWLERRESPONSE_STATUS.containing_type = _CRAWLERRESPONSE
DESCRIPTOR.message_types_by_name['CrawlerRequest'] = _CRAWLERREQUEST
DESCRIPTOR.message_types_by_name['CrawlerResponse'] = _CRAWLERRESPONSE
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CrawlerRequest = _reflection.GeneratedProtocolMessageType('CrawlerRequest', (_message.Message,), dict(
  DESCRIPTOR = _CRAWLERREQUEST,
  __module__ = 'crawler_pb2'
  # @@protoc_insertion_point(class_scope:CrawlerRequest)
  ))
_sym_db.RegisterMessage(CrawlerRequest)

CrawlerResponse = _reflection.GeneratedProtocolMessageType('CrawlerResponse', (_message.Message,), dict(
  DESCRIPTOR = _CRAWLERRESPONSE,
  __module__ = 'crawler_pb2'
  # @@protoc_insertion_point(class_scope:CrawlerResponse)
  ))
_sym_db.RegisterMessage(CrawlerResponse)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
  DESCRIPTOR = _HEADER,
  __module__ = 'crawler_pb2'
  # @@protoc_insertion_point(class_scope:Header)
  ))
_sym_db.RegisterMessage(Header)



_CRAWLER = _descriptor.ServiceDescriptor(
  name='Crawler',
  full_name='Crawler',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=474,
  serialized_end=531,
  methods=[
  _descriptor.MethodDescriptor(
    name='request',
    full_name='Crawler.request',
    index=0,
    containing_service=None,
    input_type=_CRAWLERREQUEST,
    output_type=_CRAWLERRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CRAWLER)

DESCRIPTOR.services_by_name['Crawler'] = _CRAWLER

# @@protoc_insertion_point(module_scope)
