########
# Algoritmo genético
# código escrito por Sergio Melero Royo
# Modelos matemáticos
########

#-----------------------------------


#cuerpo principal del código

$tam_pob= 10;
$r = 5;
$casillas = 100;
#-----------------------------------
&generacion_inicial;

print"\n----\noperador seleccion\n----\n";

&seleccion;

print"\n----\noperador crossover\n----\n";

&crossover;

print"\n----\noperador mutación\n----\n";

&mutacion;



############################ GENERACION INICIAL ################################

sub generacion_inicial
	{
        print "hola, soy la generacion inicial\n";
        for ($i=0; $i<$tam_pob; $i++)
           {
           @$i = ();
             for($j=0; $j<$r; $j++)
               {
                $$i[$j] = int(rand(2));
               }
           $aptitudes[$i] = &aptitud(@$i);
           print"individuo $i --> @$i --> aptitud $aptitudes[$i] \n";

           }
         &mejor;
         print" mejor individuo $mejor_ind --> @$mejor_ind --> aptitud $mejor_apt\n";
         print" media de la generación --> $media\n";
        }


############################ APTITUD ################################

sub aptitud
     {
     @ind = @_;
     $apt = 0;
      for($j=0; $j<$r; $j++)
               {
                $apt = $apt + $ind[$j];
               }
      $apt;
     }


############################ MEJOR ################################

sub mejor
	{
         $mejor_apt = 0;
         $mejor_ind = 0;
         $media = 0;
         for ($i=0; $i<$tam_pob; $i++)
           {
          if($aptitudes[$i] > $mejor_apt)
          	{
                 $mejor_apt = $aptitudes[$i];
                 $mejor_ind = $i;
                }
          $media = $media + $aptitudes[$i];
           }
         $media = $media / $tam_pob;
        }

############################ SELECCION ################################

sub seleccion
	{
        print "hola, soy la seleccion\n";
        $sum_apt = 0;
        @p = ();
        @alpha = ();
        @cota_inf = ();
        @cota_sup = ();
          for ($i=0; $i<$tam_pob; $i++)
          	{
                 $aptitudes[$i] = $aptitudes[$i] +1;
                 $sum_apt = $sum_apt + $aptitudes[$i];
                }
    	print "lista de aptitudes --> @aptitudes --> suma $sum_apt\n";

           for ($i=0; $i<$tam_pob; $i++)
          	{
                 $p[$i] = $aptitudes[$i]/ $sum_apt; #le calcula la probabilidad a cada uno
                }
        print "lista de probabilidades --> @p \n";
        $suma_alpha = 0;
        for ($i=0; $i<$tam_pob; $i++)
          	{
                 $alpha[$i] = int($p[$i] * $casillas);
                 $suma_alpha = $suma_alpha + $alpha[$i];
                }
        print "lista de casillas --> @alpha --> suma $suma_alpha \n";
        if( $suma_alpha < $casillas)
        	{
                $alpha[$mejor_ind] = $alpha[$mejor_ind] + ($casillas - $suma_alpha);
                $suma_alpha = $casillas;
                }
        print "lista de casillas --> @alpha --> suma $suma_alpha \n";

        #########    Asignar casillas
        $suma_alpha = 0;
         for ($i=0; $i<$tam_pob; $i++)
          	{
                $cota_inf[$i] = $suma_alpha;
                $suma_alpha = $suma_alpha + $alpha[$i];
                $cota_sup[$i] = $suma_alpha -1;
                print"individuo $i --> casillas $alpha[$i] --> intervalo [$cota_inf[$i],$cota_sup[$i]]\n";
                }
        for ($i=0; $i<$tam_pob; $i++)
    	    {
             print"\ngirando la ruleta...\n";
             $tirada = int(rand(100));
             print"...ha salido el numero $tirada\n";

      $selec = 0;
             ############ SELECCIONAR EL GANADOR
              for ($j=0; $j<$tam_pob; $j++)
              	{

                 if($tirada <= $cota_sup[$j] and $tirada >= $cota_inf[$j])
                 		{
                 		$selec = $j;
                                print" El individuo seleccionado es $selec con intervalo [$cota_inf[$j],$cota_sup[$j]] \n";
                                  }
                }

            $guardar = $tam_pob + $i;
            @$guardar = @$selec;

            }

            for ($i=0; $i<$tam_pob; $i++)
               {
                $guardar = $tam_pob + $i;
                @$i = @$guardar;
                $aptitudes[$i] = &aptitud(@$i);
          	print"individuo $i --> @$i --> aptitud $aptitudes[$i] \n";

               }
           &mejor;
         print" mejor individuo $mejor_ind --> @$mejor_ind --> aptitud $mejor_apt\n";
         print" media de la generación --> $media\n";
        }


############################ CROSSOVER ################################

sub crossover
	{
        print "hola, soy el crossover\n";
        }


############################ MUTACION ################################

sub mutacion
	{
        print "hola, soy la mutacion\n";
        }