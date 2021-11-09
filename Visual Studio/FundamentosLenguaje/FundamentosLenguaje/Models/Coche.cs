using System;
using System.Collections.Generic;
using System.Text;

namespace FundamentosLenguaje.Models
{
    public class Coche
    {
        //public String Estado { get; set; }
        private bool Estado;
        public String Marca { get; set; }
        public String Modelo { get; set; }

        public String Direccion { get; set; }
        public int Velocidad { get; set; }
        //public int VelocidadMaxima { get; set; }
        private int VelocidadMaxima;


        public Coche()
        {
            this.Velocidad = 0;
            this.VelocidadMaxima = 120;
            this.Direccion = "Norte";
            this.Marca = "Opel";
            this.Modelo = "Corsa";
            //this.Estado = "Detenido";
            this.Estado = false;
        }


        //métodos
        public void Arrancar()
        {
            if(this.Velocidad == 0)
            {
                this.Estado = true;
            }
            else
            {
                throw new Exception("El coche ya está arrancado.");
            }
        }

        public void Acelerar()
        {
            if(this.Estado == true)
            {
                this.Velocidad += 20;
                if(this.Velocidad > this.VelocidadMaxima)
                {
                    this.Velocidad = this.VelocidadMaxima;
                }
            }
            else
            {
                throw new Exception("Primero debes arrancar el coche.");
            }

        }

        public void AcelerarIncremento()
        {
            if(this.Estado == true)
            {
                Console.WriteLine("Introduce el incremento de velocidad ");
                int incremento = int.Parse(Console.ReadLine());

                int nuevaVelocidad = this.Velocidad + incremento;
                if (nuevaVelocidad > this.VelocidadMaxima)
                {
                    this.Velocidad = this.VelocidadMaxima;
                    Console.WriteLine("No puedes acelerar más que la velocidad máxima permitida. ");
                }
                else
                {
                    this.Velocidad = nuevaVelocidad;
                }
            }
            else
            {
                throw new Exception("Primero debes arrancar el coche.");
            }
        }


        public void Frenar()
        {
            this.Velocidad -= 20;
            if(this.Velocidad <= 0)
            {
                this.Velocidad = 0;
                this.Estado = false;
            }
        }

        public void Girar()
        {
            if(this.Direccion == "Norte")
            {
                this.Direccion = "Este";
            }
            else if(this.Direccion == "Este") 
            {
                this.Direccion = "Sur";
            }
            else if(this.Direccion == "Sur")
            {
                this.Direccion = "Oeste";
            }
            else
            {
                this.Direccion = "Norte";
            }
        }


        //public String GetDatos()
        //{
            //return "Datos del coche \n"
            //    + this.Marca + " " + this.Modelo + "\n"
            //    + "Estado: " + this.Estado
            //    + "\n Velocidad: " + this.Velocidad + "km/h"
            //    + " en dirección: " + this.Direccion;
        //}

        public override string ToString()
        {
            return "Datos del coche \n"
              + this.Marca + " " + this.Modelo + "\n"
              + "Estado: " + this.Estado
              + "\n Velocidad: " + this.Velocidad + "km/h"
              + " en dirección: " + this.Direccion;
        }

        public String GetMenu()
        {
            return ToString()
                + "\n"
                + "1. Arrancar\n2. Acelerar\n3. Frenar\n4. Girar\n5. Acelerar incremento\n6. Salir";
        }

    }
}
