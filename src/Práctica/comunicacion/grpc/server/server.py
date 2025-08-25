from concurrent import futures
import logging

import grpc
import person_pb2
import person_pb2_grpc


class PersonService(person_pb2_grpc.PersonServiceServicer):
    def GetOldest(self, request, context):
        # Since the GetOldest method is defined as a stream_unary RPC, the 'request' parameter is an iterator over Person messages.
        # To get the list of people from the request, you can convert the iterator to a list:
        people = list(request)
        
        # Find the oldest person by getting the maximum age
        if not people:
            # Return empty person if no people received
            return person_pb2.Person()
        
        oldest_person = max(people, key=lambda person: person.age)
        print(f"Received {len(people)} people, oldest is {oldest_person.name} with age {oldest_person.age}")
        return oldest_person


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    person_pb2_grpc.add_PersonServiceServicer_to_server(PersonService(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
