import socket

hosts = [
    "ac-mztctvd-shard-00-00.yxkkqg4.mongodb.net",
    "ac-mztctvd-shard-00-01.yxkkqg4.mongodb.net",
    "ac-mztctvd-shard-00-02.yxkkqg4.mongodb.net"
]
port = 27017

for host in hosts:
    print(f"Connecting to {host}:{port}...")
    try:
        s = socket.create_connection((host, port), timeout=5)
        print(f"✅ Success! Connected to {host}")
        s.close()
    except Exception as e:
        print(f"❌ Failed to connect to {host}: {e}")
