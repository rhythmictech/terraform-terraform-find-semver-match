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
  try:
    return semantic_version.Version.coerce(string.lstrip("vV"))
  except:
    return None       # We don't want the whole thing to fail if there's one invalid version in the list

def getVersions(list):
  return [ f for string in list if (f := getVersion(string)) is not None ]

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
