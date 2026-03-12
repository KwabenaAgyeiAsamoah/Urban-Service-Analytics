resource "azurerm_resource_group" "urban_rg" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_storage_account" "urban_storage" {
  name                     = var.storage_account_name
  resource_group_name      = azurerm_resource_group.urban_rg.name
  location                 = azurerm_resource_group.urban_rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  account_kind             = "StorageV2"

  tags = {
    project = "urban-service-analytics"
    env     = "dev"
  }
}

resource "azurerm_storage_container" "raw_data" {
  name                  = "raw-data"
  storage_account_id    = azurerm_storage_account.urban_storage.id
  container_access_type = "private"
}

resource "azurerm_storage_container" "processed_data" {
  name                  = "processed-data"
  storage_account_id    = azurerm_storage_account.urban_storage.id
  container_access_type = "private"
}