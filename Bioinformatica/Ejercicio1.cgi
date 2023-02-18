#!/usr/bin/perl

 open (INFILE, 'C:\Users\Sergio\Desktop\PracicaPerl_2016\Solid.csfasta') or die;
 open (OUTFILE,">",'C:\Users\Sergio\Desktop\PracicaPerl_2016\Solid.fas') or die;

 while ($a = <INFILE>) {                                #tenemos que quitar las lineas que empeizan por # pero esto ya lo usa el perl...
  if ($a =~ /^\x23/) {$a=""; }                            #usaremos el código hexadecimal de las #  (23)
  if ($a =~/^[GT]/) {                                          #que encuentre o G o T
     chomp $a;                                                     # \ indica que sigue un metacaracter ^ indica al principio de la linea
     @b = split ("",$a);
     $ant = $b[0]; $sec= "";
     foreach $i(@b){
      if ( $ant eq "G") {$i =~tr /3021/ACGT/;}
      if ( $ant eq "A") {$i =~tr /2130/ACGT/;}
      if ( $ant eq "C") {$i =~tr /1203/ACGT/;}
      if ( $ant eq "T") {$i =~tr /0312/ACGT/;}

      $sec.=$i;  # añade $i a lo que ya tiene.
      $ant = $i;


   		  }
     $a = $sec."\n";    #mete unos saltos de linea que hacian falta



 	 }

 print OUTFILE $a;
 print $a;

 }
 close(INFILE);   close(OUTFILE);