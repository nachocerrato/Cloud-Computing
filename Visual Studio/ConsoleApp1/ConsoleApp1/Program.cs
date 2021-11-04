using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            
            Console.Title = "Soy la primera app con C#";
            Console.WriteLine("Escriba un número: ");
            string dato = Console.ReadLine();
            int num1 = int.Parse(dato);
            Console.WriteLine("Escriba otro número: ");
            dato = Console.ReadLine();
            int num2 = int.Parse(dato);
            int num3 = num1 + num2;
            Console.WriteLine("La suma es: " + num3);
        }
    }
}
