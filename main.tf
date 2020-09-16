locals {
  versions_string = join(",", var.available_versions)
}


data "external" "target_version" {
  program = ["python", "${path.module}/python/semver-match.py"]

  query = {
    constraint = var.version_constraint
    versions   = local.versions_string
  }
}
