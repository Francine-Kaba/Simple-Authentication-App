from ariadne import load_schema_from_path
from ariadne.contrib.federation import (FederatedObjectType, make_federated_schema)
from ariadne.asgi import GraphQL
from Src.resolvers.Authentication.signup.mutations import Login, Signup
from Src.resolvers.Authentication.signup.query import UserQuery


type_defs = load_schema_from_path("schema")

query = FederatedObjectType("Query")
mutation = FederatedObjectType("Mutation")

# login
mutation.set_field("signUp", Signup.signup)
mutation.set_field("login", Login.login)
query.set_field("allUsers", UserQuery.list_users)


url = "http://127.0.0.1:8000"

print("🚀🚀 Server is up and running on 🔥🔥 " + url)

schema = make_federated_schema(type_defs, mutation, query)
app = GraphQL(schema, debug=True)

if __name__ == '__main__':
    app.run()
