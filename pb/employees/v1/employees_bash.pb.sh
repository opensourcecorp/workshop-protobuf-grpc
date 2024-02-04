#!/usr/bin/env bash
set -euo pipefail

#################################################
# Code generated by protoc-gen-bash. DO NOT EDIT.
#
# source file: employees/v1/employees.proto
#################################################

printf 'The messages defined in the provided proto file(s) are:\n'

printf '
  employees.v1.GetEmployeeRequest (fields: short_name:string)
  employees.v1.GetEmployeeResponse (fields: employee:message)
  employees.v1.GetEmployeeResponse.Employee (fields: id:int64, full_name:string, birthday:string)
  employees.v1.ListEmployeesRequest (fields: None)
  employees.v1.ListEmployeesResponse (fields: short_names:repeated_string)
'
