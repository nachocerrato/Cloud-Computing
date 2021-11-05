using System;

namespace FundamentosLenguaje
{
    class Program
    {
        static void Main(string[] args)
        {
            //NumeroPositivoNegativo();
            //ConjeturaCollatz();
            SumarNumeros();
        }


      
        static void ConjeturaCollatz()
        {
            Console.WriteLine("Escriba un número: ");
            String dato = Console.ReadLine();
            int numero = int.Parse(dato);
            while (numero != 1)
            {
                if (numero % 2 == 0)
                {
                    numero = numero / 2;
                }
                else
                {
                    numero = numero * 3 + 1;
                }
                Console.WriteLine(numero);
            }
        }

        static void NumeroPositivoNegativo()
        {
            Console.WriteLine("Introduzca un número");
            //RECUPERO EL VALOR EN UNA VARIABLE STRING
            String dato = Console.ReadLine();
            //DECLARAMOS UN int PARA CONVERTIR EL DATO
            int numero = int.Parse(dato);
            //EVALUAMOS CON UNA CONDICION POSITIVO, NEGATIVO O CERO
            if (numero > 0)
            {
                Console.WriteLine("POSITIVO");
            }
            else if (numero == 0)
            {
                Console.WriteLine("CERO");
            }
            else
            {
                Console.WriteLine("NEGATIVO");
            }
        }

        static void SumarNumeros()
        {
            Console.WriteLine("Introduzca un número: ");
            string dato = Console.ReadLine();
            int numero = int.Parse(dato);
            int total = numero;
            int total_ant = 0;

            while (numero != 0)
            {
                Console.WriteLine("Total: " + total_ant + " + " + numero + " = " + total);
                Console.WriteLine("Introduzca un número: ");
                dato = Console.ReadLine();
                numero = int.Parse(dato);
                total_ant = total;
                total = total + numero;
            }

            Console.WriteLine("Fin del programa");
        }
    }
}
