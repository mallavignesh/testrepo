resource "aws_instance" "jenkins" {
  ami                         = "ami-0aa31b568c1e8d622"   # use correct AMI
  instance_type               = var.instance_type
  key_name                    = var.key_name
  vpc_security_group_ids      = [aws_security_group.jenkins_sg.id]
  associate_public_ip_address = true
  iam_instance_profile        = aws_iam_instance_profile.ec2_profile.name

  root_block_device {
    volume_size = 30
    volume_type = "gp3"
  }

  user_data = file("user_data.sh")

  tags = {
    Name = "Jenkins-Server"
  }
}