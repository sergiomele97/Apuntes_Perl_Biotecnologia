#!/usr/bin/perl
 $ok = 0;
 $i = 0;
 $j = 0;
  while ($a = <>){ #mientras seas capaz de leer algo sigue leyendo...
    if ($a =~ /NTaxa=/) {          #busca en el archivo de entrada NTaxa=
       $a =~ s/\D//g; $num = $a;  print "$a\n";
       			}        	#susituye cualquier no digitvo (\D) por nada a nivel global (la g)
    if ($a =~ /^\x5B\s*\d+\x5D\s\x23/) {
                              			 # [ = x5B
       $a =~ s/^\x5B\s*\d+\x5D\s\x23//;
         chomp $a;                                       #no puede haber lineas de mas de 10 caracteres (cosas de PHYLIP)
         $a .="                ";
         $a = substr($a,0,10). " ";

         $nombre[$i] = $a;
         $i++;
                                                        		 # ] = 5D
                         }

     if (($i > 0) and ($i == int($num))) {$ok = 1; }
     if (($ok==1) and ($a =~ /^\x5B\s*\d+\x5D/))  {
        $a =~ s/^\x5B\s*\d+\x5D//;
        print "$nombre[$j]$a";
        $j++;

     }
    }
      #print @nombre;