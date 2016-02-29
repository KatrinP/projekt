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
-- 1PV in 1 year of water
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
4*91.25 /


--Start WAG cycles-----------------------------------------------------
-- 0.6 PV in 6
WCONINJE
'Inje' WAT OPEN BHP 2* 482.6 /
/

WSALT
'Inje' 0.0 /
/

WELLSTRE
--       CO2  N2   C1   C3   C10  C15
SOLVENT  0.0  0.0  .65  .35  0.0  0.0  /
CO2      0.98  0.01  0.01  0.0  0.0  0.0  /
/

WCONINJE
'Inje' GAS OPEN RATE 1000 /
/
WINJGAS
--'Inje' Stream SOLVENT /
'Inje' Stream CO2   /
/

--Resets a well operating target or limit
--ORAT Oil rate| WRAT Water rate| GRAT Gas rate
--LRAT Liquid rate| RESV Reservoir fluid volume rate| BHP Bottom hole pressure
WELTARG
'Inje' WRATE 1000/
/

WELLWAG
'Inje' T W 91.25 G 91.25 /
/

TSTEP
4*91.25 /


--Start Chase water cycles-----------------------------------------------------

WSALT
'Inje' 0.0 /
/

WELTARG
'Inje' WRATE  1000/
/

TSTEP
6*91.25 /