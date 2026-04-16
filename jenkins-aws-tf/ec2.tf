resource "aws_instance" "jenkins" {
  ami                         = "ami-0aa31b568c1e8d622"   # use correct AMI
  instance_type               = var.instance_type
  key_name                    = var.key_name
  vpc_security_group_ids      = [aws_security_group.jenkins_sg.id]
  associate_public_ip_address = true

  user_data = file("user_data.sh")

  tags = {
    Name = "Jenkins-Server"
  }
}