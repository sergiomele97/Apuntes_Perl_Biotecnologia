#!/usr/bin/perl

   #EJERCICIO 8
   #CONSEGUIR LOS CONTIG CON GAP DE TAMAÑO MÍNIMO 3
   #Sergio Melero Royo

   #IMPORTANTE: La razón por la que el programa es tan largo es porque en pimer lugar resolvimos el ejercicio en formato
   #		intercalado, posteriormente, lo modificamos para que toda la secuencia estubiera en una sola linea pero
   #	        dejamos la segunda parte del ejercicio (odemensis) como ejemplo de como era el programa inicialmente.


   open (CONTIGS, 'C:\bioinf\práctica PERL\alp_vs_ode_blast.sal') or die;
   open (RESULTADO,">",'C:\bioinf\práctica PERL\RESULTADO.txt') or die;


     $int = 0;
     $i = 0;
     $ii = 0;
     $Curr = 0;
     $triplegap = 0;

     ###############################GAPS DE ALPO#############################################
 print RESULTADO "Resultados:\n";

 while ($a = <CONTIGS>) {
      $b = $a;                  					#$int mide el contig actual.
      $b =~ s/Query//g;
      $b =~ s/[^ATGC]{2}//;


      if ($a =~ /^Query/) {

          if ($a =~ /Query=/) {
               $b =~ s/len.*//;
              		 if ($triplegap == 1) {                        		#Si hemos encontrado 3 gap seguidos, copiamos
                       		  while ($ii < @Current){
                                     if ($ii == 0 ) {
                                     	print RESULTADO "\n$Current[$ii]";
                                        	   }
                                     else{                         			#el contig (recogido en el array @Current.
    				 	 print RESULTADO "$Current[$ii]";
                                         }
                                  $ii++; }
                                  $ii = 0;
                	 $triplegap = 0;  	  }
                    $int++;
      		         	 }
          else {  $b =~ s/\d*//g;

          	  $b =~ s/\s*//;
                  $b =~ s/[^ATGCatgc]//;
                  $b =~ s/\s//g;
                  $b =~ s/\n//;  }


      	  if ($Curr == $int) { $Current[$i] = $b; }    				#(copia de seguridad)
          else { $Curr++; $i = 0; @Current = ();                                #Va copiando todas las lineas que empiezan por
          	 $Current[$i] = $b;}                                            #Query (incluidas las Query= con el nombre del
                                                                                #Contig), de forma que luego las pegaremos en
          if ($a =~ /\x2D{3}/) {                                                #el documento de salida si resulta que
                                 $triplegap = 1;                                #encontramos 3 GAP seguidos en alguna linea                                                                                #del contig.
     	 			 }

          $i++;            }

                         }

        close(CONTIGS);

       ###############################GAPS DE odemensis#############################################

      open (CONTIGS, 'C:\bioinf\práctica PERL\alp_vs_ode_blast.sal') or die;

      print RESULTADO "\n\n\n GAPS PARA ODEMENSIS ----------------------------------------------------------------- \n\n\n\n";


     $int = 0;
     $i = 0;
     $Curr = 0;
     $triplegap = 0;
     @Current = ();

    while ($a = <CONTIGS>) {
       $b = $a;

     if ($a =~ /Query=/) {
              $a =~ s/len.*//;

              		 if ($triplegap == 1) {

    			 print RESULTADO "@Current \n";
                	 $triplegap = 0;  	  }
               $int++;
      		         	 }


      if ($a =~ /^Query/) {


      	  if ($Curr == $int) { $Current[$i] = $a; }
          else { $Curr++; $i = 0; @Current = ();
          	 $Current[$i] = $a;}
                  $i++;
                          }

      if ($a =~ /^Sbjct/) {
      	   $b =~ s/\d/ /g;                             #No sabiamos como marcar en ALPO aquellos sitios donde en odemensis hubiera
           $b =~ s/[AGTC]/ /g;                         #GAP, se me ocurrio poner tildes pero no se veia demasiado asi que opte
           $Current[$i] = $b;                          #por poner las filas de odemensis y colocar guiones en aquellos sitios
           $i++;                                       #donde hubiera GAP.
          if ($a =~ /\x2D{3}/) {
                                 $triplegap = 1;
                                                                                                                                           #del contig.
     	 			 }
                          }


                         }

    close(CONTIGS);   close(RESULTADO);