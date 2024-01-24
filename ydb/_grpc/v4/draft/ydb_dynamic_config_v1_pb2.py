# -*- coding: utf-8 -*-
# flake8: noqa
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: draft/ydb_dynamic_config_v1.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ydb._grpc.v4.draft.protos import ydb_dynamic_config_pb2 as draft_dot_protos_dot_ydb__dynamic__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!draft/ydb_dynamic_config_v1.proto\x12\x14Ydb.DynamicConfig.V1\x1a%draft/protos/ydb_dynamic_config.proto2\x81\x08\n\x14\x44ynamicConfigService\x12V\n\tSetConfig\x12#.Ydb.DynamicConfig.SetConfigRequest\x1a$.Ydb.DynamicConfig.SetConfigResponse\x12\x62\n\rReplaceConfig\x12\'.Ydb.DynamicConfig.ReplaceConfigRequest\x1a(.Ydb.DynamicConfig.ReplaceConfigResponse\x12\\\n\x0bGetMetadata\x12%.Ydb.DynamicConfig.GetMetadataRequest\x1a&.Ydb.DynamicConfig.GetMetadataResponse\x12V\n\tGetConfig\x12#.Ydb.DynamicConfig.GetConfigRequest\x1a$.Ydb.DynamicConfig.GetConfigResponse\x12Y\n\nDropConfig\x12$.Ydb.DynamicConfig.DropConfigRequest\x1a%.Ydb.DynamicConfig.DropConfigResponse\x12n\n\x11\x41\x64\x64VolatileConfig\x12+.Ydb.DynamicConfig.AddVolatileConfigRequest\x1a,.Ydb.DynamicConfig.AddVolatileConfigResponse\x12w\n\x14RemoveVolatileConfig\x12..Ydb.DynamicConfig.RemoveVolatileConfigRequest\x1a/.Ydb.DynamicConfig.RemoveVolatileConfigResponse\x12\x62\n\rGetNodeLabels\x12\'.Ydb.DynamicConfig.GetNodeLabelsRequest\x1a(.Ydb.DynamicConfig.GetNodeLabelsResponse\x12\x62\n\rResolveConfig\x12\'.Ydb.DynamicConfig.ResolveConfigRequest\x1a(.Ydb.DynamicConfig.ResolveConfigResponse\x12k\n\x10ResolveAllConfig\x12*.Ydb.DynamicConfig.ResolveAllConfigRequest\x1a+.Ydb.DynamicConfig.ResolveAllConfigResponseBn\n%tech.ydb.proto.draft.dynamicconfig.v1ZBgithub.com/ydb-platform/ydb-go-genproto/draft/Ydb_DynamicConfig_V1\xf8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'draft.ydb_dynamic_config_v1_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%tech.ydb.proto.draft.dynamicconfig.v1ZBgithub.com/ydb-platform/ydb-go-genproto/draft/Ydb_DynamicConfig_V1\370\001\001'
  _DYNAMICCONFIGSERVICE._serialized_start=99
  _DYNAMICCONFIGSERVICE._serialized_end=1124
# @@protoc_insertion_point(module_scope)
