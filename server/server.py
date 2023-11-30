from servicio_pb2_grpc import PizzeriaServicer, add_PizzeriaServicer_to_server
from servicio_pb2 import ConfirmacionOrden

import grpc
from concurrent import futures

class ServicioPizzeria(PizzeriaServicer):
    
    def Listo(self, request, context):
        return request
    
    def RegistraOrden(self, request, context):
        print(f"Orden recibida de {request.direccion}, pizzas {len(request.pizzas)}")
        
        return ConfirmacionOrden(entrega_estimada = 10)
    
def start():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_PizzeriaServicer_to_server(ServicioPizzeria(), server)
    server.add_insecure_port('[::]:50051')
    print("The server is running!!")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    start()