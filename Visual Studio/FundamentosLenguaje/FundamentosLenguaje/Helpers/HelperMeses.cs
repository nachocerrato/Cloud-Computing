using FundamentosLenguaje.Models;
using System;
using System.Collections.Generic;
using System.Text;

namespace FundamentosLenguaje.Helpers
{
    public class HelperMeses
    {
        //declaramos una propiedad para manejar los meses
        public List<TemperaturaMes> Meses { get; set; }
        //al instanciar la clase, queremos tener ya los meses creados

        public HelperMeses() {
            //creamos/instanciamos la colección de meses
            this.Meses = new List<TemperaturaMes>();
            Random random = new Random();
            //para almacenarlos
            for (int i = 1; i <= 12; i++)
            {
                TemperaturaMes mes = new TemperaturaMes();
                mes.Mes = "Mes " + i;
                mes.Maxima = random.Next(20, 50);
                mes.Minima = random.Next(-10, 19);
                this.Meses.Add(mes);
            }
        }

        public int GetMaximaAnual()
        {
            int maxima = 0;
            foreach (TemperaturaMes mes in this.Meses)
            {
                maxima = Math.Max(maxima, mes.Maxima);
            }
            return maxima;
        }

        public int GetMinimaAnual()
        {
            int minima = 20;
            foreach (TemperaturaMes mes in this.Meses)
            {
                minima = Math.Min(minima, mes.Minima);
            }
            return minima;
        }
        
        public int GetMediaAnual()
        {
            int media = 0;
            foreach(TemperaturaMes mes in this.Meses)
            {
                media = +mes.GetMedia();
            }
            return (media / 12);
        }
    }
}
