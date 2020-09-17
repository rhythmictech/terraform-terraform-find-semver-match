module "find_semver_match" {
  source  = "rhythmictech/find-semver-match/terraform"
  version = "1.0.0-rc1"

  available_versions = [
    "1.0.0",
    "1.0.1",
    "1.1.0"
  ]
  version_constraint = "~1.0.0"
}

output "desired_version" {
  value = module.find_semver_match.outputs.target_version
}
