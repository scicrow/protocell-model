#!/bin/bash
#Requires ambertools, parmed and acpype

function topol_convert {

if [[ ! -d temp ]]; then
	mkdir temp
fi

#Write out separate prmtop for each component
tleap -f L21_hybrid_components_leap.in

#Convert ions to gromacs top
cd temp
python ../ions_convert.py

#Convert DCA & DNC to gromacs top with non-standard 1-4 scaling
acpype -p L21_hybrid_DCA.prmtop -x DCA.prmcrd
acpype -p L21_hybrid_DCN.prmtop -x DCN.prmcrd

cd ..
}

function topol_clean {

if [[ ! -d top_files ]]; then
	mkdir top_files
fi

cd temp

#Convert ion top to itp and remove excess sections
for file in *ions.top; do
	#Remove extension from filename
	name="${file%.top}"
	echo "Creating $name.itp"
	#Remove defaults and 3 next lines, remove everything from system onwards
	sed -e '/defaults/,+3d' -e '/system/,$d' "$file" > ../top_files/"$name".itp
done

#Convert DCA & DNC top to itp and remove excess sections
for file in *amb2gmx/*_GMX.top; do
	#Remove directory then extension from filename
	tmp="${file#*\/}"
	name="${tmp%_GMX.top}"
	echo "Creating $name.itp"
	#Remove beteen header and moleculetype, remove everything from system onwards
	sed -e '/GMX.top/,/moleculetype/{//!d}' -e  '/system/,$d' "$file" > ../top_files/"$name".itp
done

cd ..
}

function topol_complete {

if [[ ! -d top_files ]]; then
	echo "Not ready to finalise top file"
	exit
fi

#Set up overarching top file
cd top_files
cat ../topol_header.top > L21hybrid_bilayer_topol.top
ions=()
others=()

for file in *.itp; do
	if [[ $file == *"ions.itp" ]]; then
		ions+=("$file")
	else
		others+=("$file")
	fi
done

#Ions must be included first due to atomtypes section
for file in ${ions[@]}; do
	echo '#include "'"$file"'"' >> L21hybrid_bilayer_topol.top
done

for file in ${others[@]}; do
	echo '#include "'"$file"'"' >> L21hybrid_bilayer_topol.top
done

cat ../topol_template.top >> L21hybrid_bilayer_topol.top

echo "Topology files completed!"
cd ..
}

topol_convert
topol_clean
topol_complete
