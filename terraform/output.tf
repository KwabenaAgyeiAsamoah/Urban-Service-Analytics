output "resource_group_name" {
  value = azurerm_resource_group.urban_rg.name
}

output "storage_account_name" {
  value = azurerm_storage_account.urban_storage.name
}

output "raw_container_name" {
  value = azurerm_storage_container.raw_data.name
}

output "processed_container_name" {
  value = azurerm_storage_container.processed_data.name
}