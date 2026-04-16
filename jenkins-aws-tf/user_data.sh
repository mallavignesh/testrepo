#!/bin/bash

yum update -y

# Install Java 21
yum install java-21-amazon-corretto -y

# Install tools
yum install -y yum-utils git awscli

# Terraform install
yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
yum install terraform -y

# Jenkins install
wget -O /etc/yum.repos.d/jenkins.repo \
https://pkg.jenkins.io/redhat-stable/jenkins.repo

rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key

yum install jenkins -y

# Fix Java path
sed -i '/JENKINS_JAVA_CMD/d' /etc/sysconfig/jenkins
echo 'JENKINS_JAVA_CMD=/usr/bin/java' >> /etc/sysconfig/jenkins

# Start Jenkins
systemctl daemon-reexec
systemctl daemon-reload
systemctl start jenkins
systemctl enable jenkins