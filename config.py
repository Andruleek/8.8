from mongoengine import connect

connect(
    db="your_database_name",
    username="your_username",
    password="your_password",
    host="your_cluster_host",
    port=your_port
)
