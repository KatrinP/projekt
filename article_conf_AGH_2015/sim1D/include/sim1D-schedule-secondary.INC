--Schedule section------------------------------------------------------

--WCONINJE
--RATE Controlled by surface flow rate target (Item 5)
--UNITS: sm 3 /day (METRIC), stb/day for oil or water (FIELD), Mscf/day for gas
--RESV Controlled by reservoir volume rate target (Item 6)
--UNITS: rm 3 /day (METRIC), rb/day (FIELD), rcm 3 /hr (LAB) rm 3 /day (PVT-M
--BHP Controlled by BHP target (Item 7)

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


--Start Producing -----------------------------------------------------
-- 1PV in 5 years of water
WCONPROD
'Prod' OPEN BHP 5* 344.7 /
/

WCONINJE
'Inje' WAT OPEN BHP 2* 482.6 /
/

WSALT
'Inje' 0.0 /
/

WELTARG
'Inje' WRATE  1000/
/

TSTEP
20*91.25 /