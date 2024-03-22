#how to make dca/dcn

make sure you include toppar_custom.str and top_deca.str (NOT in toppar directory)

toppar_custom.str will need to be put in every .inp




build lauric acid membrane using charm gui to get all the files required. 
pull out the relevant files (these are???)
make a dca/dcn.str file (stream file) so you can add that to the lipid36 toppar files. these hold the topologies for the lipids. stream files are like plugins.
change the build.inp file to reference the stream file for deca/decn
run charmmm < build.inp > build.out


for step3_build.inp

there are a number of areas in this script you need to put in your lipid names (DECA and DECN) here are the areas that I've input in (lines are just where I entered them, not part of code)


!line 4174: 


if ndecntop .gt. 0 then
   calc cnt1 = @cnt2 + 1
   calc cnt2 = @cnt1 + @{ndecntop} - 1
   rename resname DECN select segid UPPO .and. resid @cnt1:@cnt2 end
   scalar type set @ipolf sele segid UPPO .and. resid @cnt1:@cnt2 end
endif



!line 8296:

if ndecntop .gt. 0 then
   calc cnt1 = @cnt2 + 1
   calc cnt2 = @cnt1 + @{ndecntop} - 1
   rename resname DECN select segid DNPO .and. resid @cnt1:@cnt2 end
endif

! line 8494: 

scalar charge set -1 sele (segid UPPO .or. segid DNPO) .and. resname decn end




check the output file has no errors (there's also some stuff on https://mattermodeling.stackexchange.com/questions/12372/my-charmm-ic-table-generation-has-caused-hydrogen-to-bond-to-two-carbons-how-do)
generate the cor and psf files. cor gives atom positions, psf gives bonds. 
put them in the lipid36 coordinates folder for reference. they needs to be turned into a crd file
particularly important is to add step3_nlipids top and bottom to give the number of dca/dcn in each bilayer
need to add dca/dcn sized to step4_lipid.inp (I don't actually don't think this is necessary???)

-- for the step4_lipid.inp make sure you find lines 4060-4068 and changed them to look like this. this will allow you the reference the new coordinates you've put in 
(assuming you've just dumped them into the lipid_lib directory)
      
      open read card unit 1 name lipid_lib/@lipid.crd
      read sequence coor unit 1
      generate L@LipidNum setup noangle nodihedrals first none last none
      close unit 1

      open read card unit 1 name lipid_lib/@lipid.crd
      read coor card unit 1 append
      close unit 1

Commands to build things:

charmm < build.inp > build.out
charmm < step3_packing.inp > step3_packing.out
charmm < step4_lipid.inp > step4_lipid.out

Had some issues where the toppar_custom.str was causing read errors in step 4 because there was no append or flex flags incorporated into the command to open and read topology files
I also think there's doubling up between toppar.str and toppar_custom.str that I should get rid of (leads to long load times).

Actually, I think step4 shouldn't have random lipid selection for DECN/DECA. it has a loop called repeatstrand and i think that's causing issues.
