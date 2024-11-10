# Create DNS zone
resource "google_dns_managed_zone" "domain_zone" {
  name        = "rail-times-zone"
  dns_name    = "${var.domain}."
  description = "DNS zone for rail-times app"
}

resource "google_dns_record_set" "domain_verification" {
  name         = "${var.domain}."
  managed_zone = google_dns_managed_zone.domain_zone.name
  type         = "TXT"
  ttl          = 300
  rrdatas      = ["google-site-verification=4DusUkjGsSnzZ-a7UQR2Mhjl4CpxCQHBUWSyU-23dZ0"]  # Replace with code from Search Console
}




resource "google_dns_record_set" "frontend_domain_www" {
  name         = "www.${var.domain}."
  managed_zone = google_dns_managed_zone.domain_zone.name
  type         = "CNAME"
  ttl          = 300

  rrdatas = ["rail-times-uk.com."]
}


