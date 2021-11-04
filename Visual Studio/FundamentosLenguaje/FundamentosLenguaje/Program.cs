using System;

namespace FundamentosLenguaje
{
    class Program
    {
        static void Main(string[] args)
        {
            NumeroPositivoNegativo();
        }

        static void NumeroPositivoNegativo()
        {
            Console.WriteLine("Introduzca un número: ");
            //Recupero valor de variable string
            String dato = Console.ReadLine();
            int numero = int.Parse(dato);
            //Evaluamos con condición
            if (numero > 0)
            {
                Console.WriteLine("Positivo")
            } else if (numero == 0)
            {
                Console.WriteLine("Cero");
            } else
            {
                Console.WriteLine("Negativo");
            }

        }
    }
}
