variable "available_versions" {
  type        = list
  description = "List of versions available"
}

variable "version_constraint" {
  type        = string
  description = "The version constraint you want to follow in NPM format (eg: '~1.0.1')"
}
