# -*- coding: utf-8 -*-
# flake8: noqa
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: draft/ydb_maintenance_v1.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ydb._grpc.v3.draft.protos import ydb_maintenance_pb2 as draft_dot_protos_dot_ydb__maintenance__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='draft/ydb_maintenance_v1.proto',
  package='Ydb.Maintenance.V1',
  syntax='proto3',
  serialized_options=b'\n tech.ydb.proto.draft.maintenanceZ@github.com/ydb-platform/ydb-go-genproto/draft/Ydb_Maintenance_V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1e\x64raft/ydb_maintenance_v1.proto\x12\x12Ydb.Maintenance.V1\x1a\"draft/protos/ydb_maintenance.proto2\x9c\x06\n\x12MaintenanceService\x12g\n\x10ListClusterNodes\x12(.Ydb.Maintenance.ListClusterNodesRequest\x1a).Ydb.Maintenance.ListClusterNodesResponse\x12p\n\x15\x43reateMaintenanceTask\x12-.Ydb.Maintenance.CreateMaintenanceTaskRequest\x1a(.Ydb.Maintenance.MaintenanceTaskResponse\x12r\n\x16RefreshMaintenanceTask\x12..Ydb.Maintenance.RefreshMaintenanceTaskRequest\x1a(.Ydb.Maintenance.MaintenanceTaskResponse\x12m\n\x12GetMaintenanceTask\x12*.Ydb.Maintenance.GetMaintenanceTaskRequest\x1a+.Ydb.Maintenance.GetMaintenanceTaskResponse\x12s\n\x14ListMaintenanceTasks\x12,.Ydb.Maintenance.ListMaintenanceTasksRequest\x1a-.Ydb.Maintenance.ListMaintenanceTasksResponse\x12r\n\x13\x44ropMaintenanceTask\x12+.Ydb.Maintenance.DropMaintenanceTaskRequest\x1a..Ydb.Maintenance.ManageMaintenanceTaskResponse\x12_\n\x0e\x43ompleteAction\x12&.Ydb.Maintenance.CompleteActionRequest\x1a%.Ydb.Maintenance.ManageActionResponseBd\n tech.ydb.proto.draft.maintenanceZ@github.com/ydb-platform/ydb-go-genproto/draft/Ydb_Maintenance_V1b\x06proto3'
  ,
  dependencies=[draft_dot_protos_dot_ydb__maintenance__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_MAINTENANCESERVICE = _descriptor.ServiceDescriptor(
  name='MaintenanceService',
  full_name='Ydb.Maintenance.V1.MaintenanceService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=91,
  serialized_end=887,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListClusterNodes',
    full_name='Ydb.Maintenance.V1.MaintenanceService.ListClusterNodes',
    index=0,
    containing_service=None,
    input_type=draft_dot_protos_dot_ydb__maintenance__pb2._LISTCLUSTERNODESREQUEST,
    output_type=draft_dot_protos_dot_ydb__maintenance__pb2._LISTCLUSTERNODESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateMaintenanceTask',
    full_name='Ydb.Maintenance.V1.MaintenanceService.CreateMaintenanceTask',
    index=1,
    containing_service=None,
    input_type=draft_dot_protos_dot_ydb__maintenance__pb2._CREATEMAINTENANCETASKREQUEST,
    output_type=draft_dot_protos_dot_ydb__maintenance__pb2._MAINTENANCETASKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RefreshMaintenanceTask',
    full_name='Ydb.Maintenance.V1.MaintenanceService.RefreshMaintenanceTask',
    index=2,
    containing_service=None,
    input_type=draft_dot_protos_dot_ydb__maintenance__pb2._REFRESHMAINTENANCETASKREQUEST,
    output_type=draft_dot_protos_dot_ydb__maintenance__pb2._MAINTENANCETASKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetMaintenanceTask',
    full_name='Ydb.Maintenance.V1.MaintenanceService.GetMaintenanceTask',
    index=3,
    containing_service=None,
    input_type=draft_dot_protos_dot_ydb__maintenance__pb2._GETMAINTENANCETASKREQUEST,
    output_type=draft_dot_protos_dot_ydb__maintenance__pb2._GETMAINTENANCETASKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListMaintenanceTasks',
    full_name='Ydb.Maintenance.V1.MaintenanceService.ListMaintenanceTasks',
    index=4,
    containing_service=None,
    input_type=draft_dot_protos_dot_ydb__maintenance__pb2._LISTMAINTENANCETASKSREQUEST,
    output_type=draft_dot_protos_dot_ydb__maintenance__pb2._LISTMAINTENANCETASKSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DropMaintenanceTask',
    full_name='Ydb.Maintenance.V1.MaintenanceService.DropMaintenanceTask',
    index=5,
    containing_service=None,
    input_type=draft_dot_protos_dot_ydb__maintenance__pb2._DROPMAINTENANCETASKREQUEST,
    output_type=draft_dot_protos_dot_ydb__maintenance__pb2._MANAGEMAINTENANCETASKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CompleteAction',
    full_name='Ydb.Maintenance.V1.MaintenanceService.CompleteAction',
    index=6,
    containing_service=None,
    input_type=draft_dot_protos_dot_ydb__maintenance__pb2._COMPLETEACTIONREQUEST,
    output_type=draft_dot_protos_dot_ydb__maintenance__pb2._MANAGEACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MAINTENANCESERVICE)

DESCRIPTOR.services_by_name['MaintenanceService'] = _MAINTENANCESERVICE

# @@protoc_insertion_point(module_scope)
