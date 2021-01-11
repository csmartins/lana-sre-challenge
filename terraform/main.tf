module "memorystore" {
  source         = "terraform-google-modules/memorystore/google"
  version        = "1.3.1"
  name           = "basket-memorystore"
  project        = "challenges"
  memory_size_gb = "1"
  enable_apis    = "true"
}