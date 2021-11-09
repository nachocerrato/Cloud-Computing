using System;
using System.Collections.Generic;
using System.Text;

namespace FundamentosLenguaje.Models
{
    //UN EMPLEADO HEREDA DE UNA PERSONA
    public class Empleado : Persona
    {
        public virtual int GetDiasVacaciones()
        {
            //22 días
            return 22;
        }
        public override string ToString()
        {
            return this.Apellidos + " " + this.Nombre + " " + this.Salario + " " + this.SalarioMinimo;
        }
        public override String GetNombreCompleto()
        {
            Console.WriteLine("GetNombreCompleto Empleado");

            return this.Nombre + " " + this.Apellidos + " " + this.Salario;

        }
        public Empleado()
        {
            this.SalarioMinimo = 900;
            this.Salario = 900;
            Console.WriteLine("Constructor Empleado SIN PARÁMETROS");
        }

        public Empleado(int salario)
        {
            Console.WriteLine("Constructor Empleado CON PARÁMETROS");

        }

        public int Salario { get; set; }
        //EL EMPLEADO DEBE TENER UN SALARIO MINIMO
        protected int SalarioMinimo { get; set; }
    }
}