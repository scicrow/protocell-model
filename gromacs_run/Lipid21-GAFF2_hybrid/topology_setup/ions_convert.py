import parmed as pmd
merz=pmd.load_file('merz_ions.prmtop','ions.prmcrd')
merz.save('merz_ions.top')
aqvist=pmd.load_file('aqvist_ions.prmtop','ions.prmcrd')
aqvist.save('aqvist_ions.top')