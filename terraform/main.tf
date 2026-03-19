provider "aws" {
  region = "eu-central-1"
}

resource "aws_security_group" "db_sg" {
  name = "enterprise_db_sg"

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_db_instance" "postgres" {
  allocated_storage    = 20
  storage_type         = "gp2"
  engine               = "postgres"
  engine_version       = "15.17"
  instance_class       = "db.t3.micro"
  db_name              = "transaction_db"
  username             = "enterprise_user"
  password             = "secretpassword123"
  parameter_group_name = "default.postgres15"
  publicly_accessible  = true
  skip_final_snapshot  = true
  vpc_security_group_ids = [aws_security_group.db_sg.id]
}

output "db_endpoint" {
  value = aws_db_instance.postgres.endpoint
}