########
# Algoritmo genético
# código escrito por Sergio Melero Royo
# Modelos matemáticos
########

#-----------------------------------

use Math::Trig; ### para pi y seno y coseno

#cuerpo principal del código

#ENUNCIADO DEL PROBLEMA

$a = -1; ###extremo izquierdo      (0,0,0,0...0) será -1 en la realidad
$b = 2;  ###extremo derecho
$p = 6; ### precision

###------------------
  #parametros del algoritmo genetico que NO se pueden modificar
  #alfabeto y longitud

$s = 2; #numero de simbolo del alfabeto
$q = ($b - $a) * 10**$p +1;   ### todos los numeros enteros por la cantidad de numeros posibles por numero entero, +1;
$r = int(log($q) / log(2)) +1;   ### calcula LONGITUD DE LA CADENA mínima para englobar a los q numeros posibles con los que estamos trabajando

print"intervalo [a,b] --> [$a,$b] con precisión $p --->  $q numeros ---> longitud cadena $r\n";


#parametros del algoritmo genetico que se pueden modificar
$tam_pob= 100;
$num_generaciones = 200;
$pc = 0.8;
$pm = 0.01;

$casillas = 100;

#####practica 4




#-----------------------------------

$num_generacion = 0;
&generacion_inicial;

print "\n\nGENERACION $num_generacion\n\n";
&mejor;
print "mejor individuo $mejor_ind --> @$mejor_ind --> aptitud $mejor_apt\n";
print "media de la generación --> $media\n";

open (f_mejor,">C:/Users/Sergio/Desktop/f_mejor");
print f_mejor "\n\nGENERACION $num_generacion\n\n";
print f_mejor "mejor individuo $mejor_ind --> @$mejor_ind --> aptitud $mejor_apt\n"; #Imprime en el archivo
print f_mejor "media de la generación --> $media\n";
close(f_mejor);

while ($num_generacion < $num_generaciones) {

	print"\n----\noperador seleccion\n----\n";
	&seleccion;
	print"\n----\noperador crossover\n----\n";
	&crossover;
	print"\n----\noperador mutación\n----\n";
	&mutacion;

        $num_generacion++;
        print "\n\nGENERACION $num_generacion\n\n";
        for($i=0; $i<$tam_pob; $i++) {
        	$aptitudes[$i] = &aptitud(@$i);
                print "\nindividuo $i --> @$i --> aptitud $aptitudes[$i]\n";
                print "ind $i --> @$i --> x $x --> apt $apt"; ###Sergio estubo aqui
        }
        &mejor;

        $mejor_apt = &aptitud(@$mejor_ind);
        print "\nmejor individuo $mejor_ind --> @$mejor_ind --> x = $x --> aptitud $mejor_apt\n";
        print "media de la generación --> $media\n";

        open (f_mejor,">>C:/Users/Sergio/Desktop/f_mejor");
	print f_mejor "\n\nGENERACION $num_generacion\n\n";
        print f_mejor "mejor individuo $mejor_ind --> @$mejor_ind --> aptitud $mejor_apt\n"; #Imprime en el archivo
        print f_mejor "media de la generación --> $media\n";
        close(f_mejor);
}



############################ GENERACION INICIAL ################################

sub generacion_inicial
	{
        print "hola, soy la generacion inicial\n";
        for ($i=0; $i<$tam_pob; $i++)
           {
           @$i = ();
             for($j=0; $j<$r; $j++)
               {
                $$i[$j] = int(rand($s));   ###
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
     $apt = 0;        ###
      $x1 = 0;


	  for($j=0; $j<$r; $j++)
               {
    		 $x1 = $x1 + $ind[$j] * 2**($r - 1 - $j); ### va restando la j primero suma 2 elevado a 6 luego 2 elevado a 5...
    				                           ### en $x1 va sumando el número real
               }

      		 $x2 = $x1 * ($b-$a) / (2**$r -1);    ## x será el numero en el intervalo REAL y x2 el número en el intervalo 0, a-b.
    		 $x = $x2 + $a;                   ## con x2 y x esta pasando del intervalo de 0 a 2**r -1 a un intervalo real de a, b
    ######## 4.4
    #  		 $apt = -($x - 3)**2 +5;    ### la aptitud será f(x)

############ 4.5
    #             $apt = $x;

############ 4.6
         $apt = $x * sin(10 * pi * $x) + 1;
      $apt;
     }
######## Practica 4.3:
######## El numero real obtenido tiene precision mayor porque no tiene nada que ver con la precision p,
######## En el intervalo [0,2**r -1] hay 2**r numeros posibles (mas), mientras que en el intervalo [a,b] hay q numeros posibles.






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
                 #$aptitudes[$i] = &aptitud(@$i);
                 $aptitudes[$i] = $aptitudes[$i] + 1;
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
        }


############################ CROSSOVER ################################

sub crossover {
	print "hola, soy el crossover\n";
        &separar;
        $parejas = $si_cross / 2;
        for ($pareja=0; $pareja<$parejas; $pareja++) {
        	$ind1 = $tam_pob + 2 * $pareja;
                $ind2 = $tam_pob + 2 * $pareja + 1;
                print "pareja $pareja\n";
                &cruce;
        }
        &union;
}

sub separar {
    	$si_cross=0;
        $no_cross=0;
        for($i=0; $i<$tam_pob; $i++) {
        	$aux = rand(1);
                if ($aux <= $pc) {
                         $pos = $tam_pob + $si_cross;
                         @$pos = @$i;
                         $si_cross++;
                }
                else {
                	$pos = 2 * $tam_pob + $no_cross;
                        @$pos = @$i;
                        $no_cross++;
                }
        }
        print "hay $si_cross individuos para cruzar\n";
        if($si_cross % 2 == 1){                		 #para que no sea impar
        	$pos_si = $tam_pob + $si_cross - 1;        #ultima posicion de los sies
                $pos_no = 2 * $tam_pob + $no_cross;
                @$pos_no = @$pos_si;
                $si_cross = $si_cross - 1;
                $no_cross = $no_cross + 1;
        }
        print "hay $si_cross individuos para cruzar\n";
}

sub cruce {
       @padre1 = @$ind1;
       @padre2 = @$ind2;
       @hijo1 = ();
       @hijo2 = ();
       $corte = int(rand($r));
       print "ascendencia --> @padre1 ----- @padre2\n";
       print "punto de corte --> $corte\n";
       for ($j=0; $j<$corte; $j++){
       	   $hijo1[$j] = $padre1[$j];
           $hijo2[$j] = $padre2[$j];
       }
        for ($j=$corte; $j<$r; $j++){
       	   $hijo1[$j] = $padre2[$j];
           $hijo2[$j] = $padre1[$j];
       }
       print "descendencia --> @hijo1 ----- @hijo2\n";
       @$ind1 = @hijo1;
       @$ind2 = @hijo2;
}

sub union {
	for ($i=0; $i<$si_cross; $i++){
        	$pos = $tam_pob + $i;
               	$guardar = $i;
                @$guardar = @$pos;
                print "individuo $guardar --> @$guardar\n";
        }
        for ($i=0; $i<$no_cross; $i++){
        	$pos = 2 * $tam_pob + $i;
                $guardar = $si_cross + $i;
                @$guardar = @$pos;
                print "individuo $guardar --> @$guardar\n";
        }
}

############################ MUTACION ################################

sub mutacion {
        print "hola, soy la mutacion\n";
        for ($i=0; $i<$tam_pob; $i++){
        	for ($j=0; $j<$r; $j++){
                	$aux = rand(1);
                        if($aux<=$pm) {
                                print "muta el gen $j del individuo $i --> @$i\n";
                                $new_gen = int(rand($s));           ###
                                while($new_gen==$$i[$j])
                                	      {
                               			$new_gen = int(rand($s));   ###
                                               }
                               $$i[$j] = $new_gen;
                                print "gen mutado --> @$i\n";

                        }
                }
        }
}