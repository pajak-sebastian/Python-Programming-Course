config = {
    "website" : "example.com",
    "dbType" : "mysql",
    "dbUser" : "admin",
    "dbPassword" : "12345",
}

# print(config["website"])
print(len(config))
print(config["dbType"])
for key, value in config.items():
    print(f"Klucz w config: {key} z wartością {value}")