# terraform-terraform-find-semver-match
Given a version constraint and a list of versions, finds the most appropriate semver match.

[![tflint](https://github.com/rhythmictech/terraform-terraform-find-semver-match/workflows/tflint/badge.svg?branch=master&event=push)](https://github.com/rhythmictech/terraform-terraform-find-semver-match/actions?query=workflow%3Atflint+event%3Apush+branch%3Amaster)
[![tfsec](https://github.com/rhythmictech/terraform-terraform-find-semver-match/workflows/tfsec/badge.svg?branch=master&event=push)](https://github.com/rhythmictech/terraform-terraform-find-semver-match/actions?query=workflow%3Atfsec+event%3Apush+branch%3Amaster)
[![yamllint](https://github.com/rhythmictech/terraform-terraform-find-semver-match/workflows/yamllint/badge.svg?branch=master&event=push)](https://github.com/rhythmictech/terraform-terraform-find-semver-match/actions?query=workflow%3Ayamllint+event%3Apush+branch%3Amaster)
[![misspell](https://github.com/rhythmictech/terraform-terraform-find-semver-match/workflows/misspell/badge.svg?branch=master&event=push)](https://github.com/rhythmictech/terraform-terraform-find-semver-match/actions?query=workflow%3Amisspell+event%3Apush+branch%3Amaster)
[![pre-commit-check](https://github.com/rhythmictech/terraform-terraform-find-semver-match/workflows/pre-commit-check/badge.svg?branch=master&event=push)](https://github.com/rhythmictech/terraform-terraform-find-semver-match/actions?query=workflow%3Apre-commit-check+event%3Apush+branch%3Amaster)
<a href="https://twitter.com/intent/follow?screen_name=RhythmicTech"><img src="https://img.shields.io/twitter/follow/RhythmicTech?style=social&logo=twitter" alt="follow on Twitter"></a>

## Example
Here's what using the module will look like
```hcl
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
```

## About
This module was designed for finding the desired GitHub release from a semver constraint instead of being limited to `latest` or a specific version

<!-- BEGINNING OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
## Requirements

| Name | Version |
|------|---------|
| terraform | >= 0.12.28 |
| external | ~> 1.2.0 |

## Providers

| Name | Version |
|------|---------|
| external | ~> 1.2.0 |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| available\_versions | List of versions available | `list` | n/a | yes |
| version\_constraint | The version constraint you want to follow in NPM format (eg: '~1.0.1') | `string` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| target\_version | Version from the list that best matches the constraint |

<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->

## The Giants Underneath this Module
- [pre-commit.com](pre-commit.com)
- [terraform.io](terraform.io)
- [github.com/tfutils/tfenv](github.com/tfutils/tfenv)
- [github.com/segmentio/terraform-docs](github.com/segmentio/terraform-docs)
