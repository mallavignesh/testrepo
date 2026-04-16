output "jenkins_url" {
  value = "http://${aws_instance.jenkins.public_ip}:8080"
}

output "ssh_command" {
  value = "ssh -i <your-key.pem> ec2-user@${aws_instance.jenkins.public_ip}"
}

output "jenkins_password_command" {
  value = "ssh -i your-key.pem ec2-user@${aws_instance.jenkins.public_ip} 'sudo cat /var/lib/jenkins/secrets/initialAdminPassword'"
}