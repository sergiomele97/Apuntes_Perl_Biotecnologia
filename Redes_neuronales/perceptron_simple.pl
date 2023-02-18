#!/usr/bin/perl

open (datos, "C:/Users/Sergio/Desktop/muestras.txt");

$muestra=0;
while (<datos>)
{
    @$muestra=split;
        $n=@$muestra-1;
        @patron=();
        for ($i=0; $i<$n; $i++)
        {
            $patron[$i]=$$muestra[$i];
        }
        print "El patrón de la muestra $muestra es @patron con salida esperada $$muestra[$n]\n";
        $muestra++;
}
print "\nLa longitud del patrón es $n\n";
$s=$muestra;
print "Hay $s patrones\n";

close (datos);

print "\nPERCEPTRÓN MULTICAPA\n";

sub salida_red
{
    $pot=0;
        for ($i=0; $i<$n; $i++)
        {
            $pot=$pot+$pesos[$i]*$_[$i];
        }
        print "patron $num --> potencial interno $pot\n";
        if ($pot<$umbral)
        {
            $y=-1;
        }
        else {$y=1;}
        $y;
}

@pesos_todos=();
print "\nINICIO DEL ALGORITMO\n\n";

$gamma=1;

$t=0;

srand(time());
@pesos=();
for ($i=0; $i<$n; $i++)
{
    $pesos[$i]=rand(2)-1;
        $pesos_todos[$i]=$pesos[$i];
}

$umbral=rand(2)-1;
$pesos_todos[$n]=$umbral;

print "Pesos y umbral iniciales del Perceptrón: \n--> @pesos y $umbral\n";
$tiempo = 0;
print"El tiempo comienza: 0\n";
print "\nENTRENAMIENTO\n";

$control=0;
$m=0; # $m lleva el número de veces que se han modificado los pesos
while($control<$s)
{

   ##### cortar el programa cuando t = 20:
if($tiempo >= 1000){
   print"\n\n ¡! El entrenamiento se detiene debido a que se ha alcanzado el límite de tiempo (20)\n";
 last if (1);}

else{





    print"--------------\n";
         $num=$t % $s;
         @muestra=@$num;
         @k=();
         for($i=0; $i<$n; $i++)
         {
             $k[$i]=$muestra[$i];
         }
         $d=$muestra[$n];
         $y=&salida_red(@muestra);
         print "--> salida red $y --> salida esperada $d\n";
         if ($y!=$d)
         {
           ##### VARIAR APRENDIZAJE
                  	$gamma = 1 - 1/(1+(exp(-1*($tiempo-10))));
                     print" nueva razon de aprendizaje: $gamma\n";
                        ######efdafe
             $control=0;
                $m++;
                print "--> @k mal clasificado\n";

                for ($i=0; $i<$n; $i++)
                {       #VARIA LOS PESOS

                    $inc=$gamma*$d*$k[$i];
                        $pesos[$i]=$pesos[$i]+$inc;
                        $pesos_todos[$m*($n+1)+$i]=$pesos[$i];
                }
                $inc=$gamma*$d*(-1);
                $umbral=$umbral+$inc;
                $pesos_todos[$m*($n+1)+$n]=$umbral;
                print "--> Nuevos pesos y umbral del Perceptrón:\n--> @pesos y $umbral\n";
                $tiempo++;
                print "-->Tiempo actual: $tiempo\n";

         }else{
             $control++;
                print "--> Hay $control muestras bien clasificadas\n";
                $tiempo++;
                print"-->Tiempo actual: $tiempo\n";
         }
         $t++;
    }##### Final si t = 20
}

print "\n\nFIN\n";
    print"------\n";
        print"------\n";
        print "Pesos y umbral del Perceptrón:\n--> @pesos y $umbral\n";
        print"------\n";
    print"------\n";

print "\n Todos los pesos que han salido:\n";
for ($j=0; $j<$m+1; $j++)
{
    for($i=0; $i<=$n; $i++)
        {
            $aux[$i]=$pesos_todos[$j*($n+1)+$i];
        }
        print "@aux\n";
}

@nuevosdatos = &recogida;
$salidatos = &salida_red(@nuevosdatos);
print"el umbral es: $salidatos";
print"\nEl patron se parece a la clase $salidatos\n";


################################## ANALIZAR PATRÓN


sub recogida{
for($i=0;$i<$n;$i++){
	print"Introduzca un nuevo patron\n";
        $nuevopatron[$i] = <STDIN>;
        }
        @nuevopatron;
        }




     # Exportación de las muestras:
open(salida, ">C:/Users/Sergio/Desktop/salida_ps.mac");
print salida "/*Perceptron Multicapa*/\n";
print salida "/*Archivo escrito en pseudocodigo Maxima*/\n\n";
print salida "muestras:[";
for($j=0;$j<$s;$j++){
print salida "[";
for($i=0;$i<=$n;$i++){
$aux[$i]=$$j[$i];
 if($j==$s-1 and $i==$n) { print salida "$aux[$i]]];\n";}
 elsif($i==$n) { print salida "$aux[$i]],"; }
 else { print salida "$aux[$i],";}
 }
}
close(salida);

# Exportación de los pesos:
open(salida, ">>C:/Users/Sergio/Desktop/salida_ps.mac");
print salida "pesos:[";
for($j=0;$j<$m+1;$j++){
for($i=0;$i<=$n;$i++){
$aux[$i]=$pesos_todos[$j*($n+1)+$i];
 if($j==$m and $i==$n) { print salida "$aux[$i]];\n";}
 else { print salida "$aux[$i],";}
 }
}
close(salida);

##########################  exportar n s m...

open(salida,">>C:/Users/Sergio/Desktop/salida_ps.mac");
print salida "n:$n;\n";
print salida "s:$s;\n";
print salida "m:$m;\n";
$num_graficas = $m+1;
print salida "num_graficas:$num_graficas;\n";
close(salida);