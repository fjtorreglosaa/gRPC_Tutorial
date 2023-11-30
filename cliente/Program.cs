using Grpc.Net.Client;

namespace client
{
    class Program
    {
        static void Main(string[] args)
        {
            AppContext.SetSwitch("System.Net.Http.SocketsHttpHandler.Http2UnencryptedSupport", true);
            var channel = GrpcChannel.ForAddress("http://localhost:50051");
            var client = new Pizzeria.PizzeriaClient(channel);

            client.Listo(new Nulo());

            var pizza = new Pizza
            {
                Pulgadas = 10,
            };

            pizza.Topping.Add("Pepperoni");

            var orden = new Orden
            {
                Direccion = "Calle Falsa 123"
            };

            orden.Pizzas.Add(pizza);

            var confirmacion = client.RegistraOrden(orden);

            Console.WriteLine($"Nuestra pizza llegará en {confirmacion.EntregaEstimada}");
        }
    }
}

// Canal de gRPC