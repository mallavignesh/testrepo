variable "region" {
  default = "ap-south-2"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "key_name" {
  description = "EC2 Key Pair name"
}

variable "allowed_ip" {
  description = "Your IP for SSH access"
}