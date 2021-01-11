terraform {
  backend "gcs" {
    bucket  = "tf-state-basket-api"
    prefix  = "challenges"
  }
}