# Python server

1. ir a la carpeta server e iniciar los siguientes comandos
2. pipenv install grpcio-tools grpcio googleapis-common-protos
3. pipenv shell
4. pipenv graph
5. pipenv run python -m grpc_tools.protoc -I../definiciones --python_out=. --grpc_python_out=. ../definiciones/servicio.proto

# .NET C# client

1. dotnet add package Google.Api.CommonProtos
2. dotnet add package Grpc.Net.Client
3. dotnet add package Grpc.Tools
4. dotnet add package Grpc.Core

https://grpc.io/docs/what-is-grpc/introduction/
