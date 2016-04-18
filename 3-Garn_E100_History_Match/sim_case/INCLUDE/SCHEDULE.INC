RPTSCHED                               
  FIP NEWTON SUMMARY SALT/

RPTRST                                 
  BASIC=1 /                              

WELSPECS                               
  Prod_B6 PRODUCER 21 17 1* OIL /
  Prod_B8 PRODUCER 25 13 1* OIL /
  Inje_B2 GAS_INJE 8 14 1* GAS /
  /

COMPDAT
--
-- name, i j k k, open/shut, 7-sat table nr, transmissibility 
-- 9-diameter, 10-effective Kh, 11-skin, 12-D fact,13-direction                      
-- 14-pressure equivalen radius to calculate from Peaceman formula

  Prod_B6 21 17 1 25 OPEN 1* 4.8963E+001 0.19050 4095.61 0.00 1* Z 8.42 /

  Prod_B8 25 13 1 25 OPEN 1* 1.7266E+000 0.19050 151.70 0.00 1* Z 10.55 /

  Inje_B2 8 14 1 25 OPEN 1* 6.0713E+001 0.19050 5709.78 0.00 1* Z 14.69 /
  /

WEFAC
  Prod_B6 0.7 /
  Prod_B8 0.8 /
  Inje_B2 0.9 /
  /

WCONPROD
--                    O  W  G  L Res                                
  Prod_B6 OPEN ORAT 2300 1* 1* 1* 1* 100 /
  Prod_B8 OPEN ORAT 1750 1* 1* 1* 1* 100 /
  /

GCONINJE
  GAS_INJE GAS REIN 2* 1.0 /
  /

WCONINJE                               
  Inje_B2 GAS OPEN GRUP 2* 400 /
  /