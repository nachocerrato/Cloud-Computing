using System;
using System.Collections.Generic;
using System.Text;

namespace FundamentosLenguaje.Models
{
    public class Director : Empleado
    {
        public override int GetDiasVacaciones()
        {
            int diasEmpleado = base.GetDiasVacaciones();
            return diasEmpleado + 20;
        }
        //UN EMPLEADO DEBERIA COBRAR LO MISMO QUE UN DIRECTOR??
        //VAMOS A CAMBIAR EL SalarioMinimo DE DIRECTOR EN SU CONSTRUCTOR
        public Director()
        {
            //NO PODEMOS PORQUE ES PRIVATE
            this.SalarioMinimo = 1400;
            Console.WriteLine("Constructor Director SIN PARÁMETROS");

        }

        //AUNQUE TENGAMOS OTRO CONSTRUCTOR DENTRO DE ESTA CLASE, TODO SIGUE IGUAL
        public Director (int salario):base(12)
        {
            Console.WriteLine("Constructor Director CON PARÁMETROS");

        }
    }
}