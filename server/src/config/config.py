import psycopg2

class Config:
  def __init__():
    conn = psycopg2.connect(
      database = "postgres",
      user = "postgres",
      password = "yaelizcool",
      host = "localhost",
      port = "5432"
      )
    print("Opened Database Connection Successfully")