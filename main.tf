locals {
  versionobj      = jsondecode(file("${path.module}/testversions.json"))
  versions        = local.versionobj.versions
  versions_string = join(",", local.versions)
}


data "external" "target_version" {
  program = ["python", "${path.module}/python/semver-match.py"]

  query = {
    constraint = "~2.0.1-"
    versions   = local.versions_string
  }
}
