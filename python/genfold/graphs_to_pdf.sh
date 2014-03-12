#!/bin/bash

DIREC=cex
v=2

dot -Tpdf $DIREC/stallings1.gv   > $DIREC/stallings1.pdf 
dot -Tpdf $DIREC/stallings2.gv  > $DIREC/stallings2.pdf 
dot -Tpdf $DIREC/double1.gv  > $DIREC/double1.pdf
dot -Tpdf $DIREC/double2.gv  > $DIREC/double2.pdf 
neato -Tpdf $DIREC/Kfolding.gv  > $DIREC/Kfolding.pdf  
dot -Tpdf $DIREC/D0_1_v$v.gv > $DIREC/D0_1_v$v.pdf 
dot -Tpdf $DIREC/D0_2_v$v.gv   > $DIREC/D0_2_v$v.pdf 
dot -Tpdf $DIREC/D0_Z_v$v.gv  > $DIREC/D0_Z_v$v.pdf  
dot -Tpdf $DIREC/D1_1_v$v.gv  > $DIREC/D1_1_v$v.pdf  
dot -Tpdf $DIREC/D1_2_v$v.gv  > $DIREC/D1_2_v$v.pdf 
neato -Tpdf $DIREC/P_1_1_v$v.gv > $DIREC/P_1_1_v$v.pdf 
neato -Tpdf $DIREC/P_1_2_v$v.gv> $DIREC/P_1_2_v$v.pdf 
dot -Tpdf $DIREC/D2_1_v$v.gv  > $DIREC/D2_1_v$v.pdf 
dot -Tpdf $DIREC/D2_2_v$v.gv  > $DIREC/D2_2_v$v.pdf 
neato -Tpdf $DIREC/P_2_1_v$v.gv > $DIREC/P_2_1_v$v.pdf 
neato -Tpdf $DIREC/P_2_2_v$v.gv> $DIREC/P_2_2_v$v.pdf 
dot -Tpdf $DIREC/D3_1_v$v.gv > $DIREC/D3_1_v$v.pdf   
dot -Tpdf $DIREC/D3_2_v$v.gv > $DIREC/D3_2_v$v.pdf       
neato -Tpdf $DIREC/P_3_1_v$v.gv > $DIREC/P_3_1_v$v.pdf 
neato -Tpdf $DIREC/P_3_2_v$v.gv> $DIREC/P_3_2_v$v.pdf 
dot -Tpdf $DIREC/D4_1_v$v.gv > $DIREC/D4_1_v$v.pdf   
dot -Tpdf $DIREC/D4_2_v$v.gv > $DIREC/D4_2_v$v.pdf       
neato -Tpdf $DIREC/P_4_1_v$v.gv > $DIREC/P_4_1_v$v.pdf 
neato -Tpdf $DIREC/P_4_2_v$v.gv> $DIREC/P_4_2_v$v.pdf 
dot -Tpdf $DIREC/D5_1_v$v.gv > $DIREC/D5_1_v$v.pdf   
dot -Tpdf $DIREC/D5_2_v$v.gv > $DIREC/D5_2_v$v.pdf    
dot -Tpdf $DIREC/Dn_v$v.gv > $DIREC/Dn_v$v.pdf








