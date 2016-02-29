--Schedule section------------------------------------------------------

--Request FIP reports, group, sep and well data, and solution maps.
SAVEEND

--Define injection and production wells
WELSPECS
'Prod' 'Field' 10 10 1* OIL /
/

COMPDAT
'Prod' 10 10 3 4 1* 1 /
/


WCONPROD
'Prod' OPEN BHP 5* 344.7 /
/

TSTEP
4*91.25 /