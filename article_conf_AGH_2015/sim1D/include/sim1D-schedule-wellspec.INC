--Schedule section-----------------------------------------------------

--Request FIP reports, group, sep and well data, and solution maps.
SAVEEND

--Define injection and production wells
WELSPECS
'Inje' 'Field'  1  1 1* WAT /
'Prod' 'Field' 10 10 1* OIL /
/

COMPDAT
'Inje'  1  1 1 1 1* 1 /
'Prod' 10 10 3 4 1* 1 /
/