import ssl, pika, os

username = os.environ.get("USER")
password = os.environ.get("PASS")
host = os.environ.get("HOST")

ctx = ssl.create_default_context()
params = pika.URLParameters(f"amqps://{username}:{password}@{host}:5671/%2F")
params.ssl_options = pika.SSLOptions(ctx, host)

conn = pika.BlockingConnection(params)
print("External AMQPS OK")
conn.close()
