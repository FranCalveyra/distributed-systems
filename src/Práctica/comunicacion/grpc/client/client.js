const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const path = require('path');

// Load the protobuf definition
const PROTO_PATH = path.join(__dirname, '..', 'person.proto');
const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true
});

// Load the service from the package definition
const personProto = grpc.loadPackageDefinition(packageDefinition).communication;

// Create a client instance
const client = new personProto.PersonService('localhost:50051', grpc.credentials.createInsecure());

// Sample data - list of persons
const persons = [
    { name: "Alice", age: 25 },
    { name: "Bob", age: 30 },
    { name: "Charlie", age: 35 },
    { name: "Diana", age: 28 },
    { name: "Eve", age: 42 },
    { name: "Frank", age: 19 }
];

function findOldestPerson() {
    return new Promise((resolve, reject) => {
        // Create a client-side streaming call
        const call = client.GetOldest((error, response) => {
            if (error) {
                console.error('Error from server:', error);
                reject(error);
            } else {
                console.log('Oldest person received:', response);
                resolve(response);
            }
        });

        // Send all persons to the server
        console.log('Sending persons to server:');
        persons.forEach(person => {
            console.log(`  Sending: ${person.name}, age ${person.age}`);
            call.write(person);
        });

        // Signal that we're done sending data
        call.end();
    });
}

// Main execution
async function main() {
    try {
        console.log('=== gRPC Client: Find Oldest Person ===\n');
        
        const oldest = await findOldestPerson();
        
        console.log('\n=== Result ===');
        console.log(`The oldest person is: ${oldest.name}, age ${oldest.age}`);
        
    } catch (error) {
        console.error('Client error:', error.message);
    }
}

// Run the client
main();