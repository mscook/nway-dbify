nway-dbify
==========

Idea: take a nesoni-any-withref file and store it in a sql-lite db. From there 
develop query functions to extract useful information. 

Such examples could be:
    * give all SNPs in region X-Y
    * give all SNPs in gene parC
    * give all SNPs that are in strains A,B,C and not in strains D,E,F and not 
      in G, H, I (an extended bisect)

This will be originally developed as a seperate stub/app. I expect this will 
be merged into Banzai pipeline. 
