#!/usr/bin/env python3

import json
import semantic_version

from sys import stdin


DATA = json.loads( stdin.read() )

def getList(string):
  return string.split(',')

def getSpec(string):
  return semantic_version.NpmSpec(string)

def getVersion(string):
  return semantic_version.Version.coerce(string)

def getVersions(list):
  return [getVersion(string) for string in list]

def getTargetVersion(spec, versionList):
  return str(spec.select(versionList))

print(
  json.dumps({
    'value': getTargetVersion(
      getSpec(DATA['constraint']),
      getVersions(getList(DATA['versions']))
    )
  })
)
