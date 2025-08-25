# gRPC Person Service

This project demonstrates a gRPC service that finds the oldest person from a stream of Person objects.

## Protocol Buffer Definition

The service is defined in `person.proto`:

```protobuf
syntax = "proto3";
package communication;

service PersonService{
    rpc GetOldest(stream Person) returns (Person);
}

message Person {
    string name=1;
    int32 age=2;
}
```

### Service Definition

- **Service**: `PersonService`
- **RPC Method**: `GetOldest`
- **Type**: Client-side streaming (client sends multiple messages, server returns one)
- **Input**: Stream of `Person` messages
- **Output**: Single `Person` message (the oldest one)

### Message Definition

The `Person` message contains:
- `name` (string): The person's name
- `age` (int32): The person's age

## Code Generation

### Python Code Generation

To generate Python gRPC code from the protobuf definition:

```bash
python3 -m grpc_tools.protoc -I. --python_out=server --pyi_out=server --grpc_python_out=server person.proto
```

**Command breakdown:**
- `-I.`: Include current directory for imports
- `--python_out=server`: Generate Python message classes in the `server` directory
- `--pyi_out=server`: Generate Python type stubs for better IDE support
- `--grpc_python_out=server`: Generate gRPC service classes in the `server` directory
- `person.proto`: The protobuf file to compile

**Prerequisites:**
Install the gRPC tools:
```bash
pip install grpcio-tools
```

**Generated files:**
- `person_pb2.py`: Contains the `Person` message class
- `person_pb2_grpc.py`: Contains the `PersonService` stub and servicer classes
- `person_pb2.pyi`: Type stubs for better IDE support

### JavaScript Code Generation

The JavaScript client uses dynamic loading with `@grpc/proto-loader`, so no code generation is required. The protobuf definition is loaded at runtime.

**Prerequisites:**
```bash
npm install @grpc/grpc-js @grpc/proto-loader
```

## Project Structure

```
grpc/
├── person.proto          # Protocol buffer definition
├── server/               # Python server
│   ├── server.py         # Server implementation
│   ├── person_pb2.py     # Generated message classes
│   ├── person_pb2_grpc.py # Generated service classes
│   └── person_pb2.pyi    # Type stubs
├── client/               # JavaScript client
│   ├── client.js         # Client implementation
│   ├── package.json      # Node.js dependencies
│   └── node_modules/     # Installed dependencies
└── README.md            # This file
```

## Running the Application

### 1. Start the Python Server

```bash
cd server
python3 server.py
```

The server will start listening on port 50051.

### 2. Run the JavaScript Client

```bash
cd client
npm start
# or
node client.js
```

The client will:
1. Connect to the server on localhost:50051
2. Send a stream of Person objects with sample data
3. Receive the oldest person back from the server
4. Display the result

## Sample Data

The client sends these sample persons:
- Alice (age 25)
- Bob (age 30)
- Charlie (age 35)
- Diana (age 28)
- Eve (age 42) ← Expected oldest
- Frank (age 19)

**Expected output:** Eve (age 42) should be returned as the oldest person.

## How It Works

1. **Client-side streaming**: The client establishes a connection and sends multiple `Person` messages
2. **Server processing**: The server collects all incoming `Person` objects and finds the one with the maximum age
3. **Response**: The server returns the oldest `Person` object to the client
4. **Completion**: The client displays the result

This demonstrates the client-side streaming pattern in gRPC, where the client sends multiple messages and the server responds with a single result after processing all input.
