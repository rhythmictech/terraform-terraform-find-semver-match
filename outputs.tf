output "target_version" {
  description = "Version from the list that best matches the constraint"
  value       = data.external.target_version.result.value
}
