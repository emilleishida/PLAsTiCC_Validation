   PLASTICC: General Information about SNANA Simulations

# =============================================
#     GENERATION INSTRUCTIONS on MIDWAY
# =============================================

cd $PLASTICC_ROOT/SIMGEN

# create SIMSED binaries
# Check MAKE*.LOG files in $PLASTICC_MODELS/SIMSED_BINARIES
./MAKE_SIMSED_BINARIES  

# construct DDF and WDF SIMGEN-MASTER inputs from template-input
./MAKE_SIMGEN_MASTER

# launch jobs 
sim_SNmix.pl SIMGEN_MASTER_LSST_DDF.INPUT NOPROMPT >& DMP_SIMGEN_LSST_DDF.LOG &
sim_SNmix.pl SIMGEN_MASTER_LSST_WFD.INPUT NOPROMPT >& DMP_SIMGEN_LSST_WFD.LOG &
sim_SNmix.pl SIMGEN_MASTER_SDSS.INPUT NOPROMPT     >& DMP_SIMGEN_SDSS.LOG &
sim_SNmix.pl SIMGEN_MASTER_IDEAL.INPUT NOPROMPT    >& DMP_SIMGEN_IDEAL.LOG &


# =============================================
#          SAMPLES
# =============================================
  LSST_DDF  : LSST deep drill (5 pointings)
  LSST_WFD  : LSST wide-fast-deep (~18,000 sqdeg)
  SDSS      : stripe 82
  IDEAL     : LSST bands, x1000 exposure time, 300 days, 2 day cadence


# =============================================
#            MODEL LIST
# =============================================

MODEL01   SNIa               (normal, for cosmology measurements)
MODEL02   CC                 (II & Ibc templates, Jones 2017)
MODEL03   MOSFIT_Ibc
MODEL04   MOSFIT_IIn
MODEL42   SNIa-91bg
MODEL45   pointIa
MODEL50   Kilonova
MODEL60   MOSFIT_SLSN_MAGNETAR
MODEL61  *MOSFIT_PISN          (Pair-Instability)
MODEL62   MOSFIT_ILOT          (Intermediate Luminosity Optical Transients)
MODEL63   MOSFIT_CART          (CAlcium-Rich Transients)
MODEL80   RRLyrae
MODEL81   Mdwarf_flares
MODEL82   [Mira]
MODEL90  *uLens_BSR            (Binary Star Remnant: BH,NS,etc ..)
MODEL91  *uLens_STRING         (cosmic string model)

*  --> never observed, theoretically suggested
[] --> model devel in progress, not yet available


Need volunteer for:  TDE,  Orphan AfterGlow,  AGN,  Eclipsing binary


# =============================================
#              ISSUES 
# =============================================

 [+ means done or fixed, - means not done]
 
+ fix SNANA to read gzipped SIMSED file.
+ refactor genmag_LCLIB to handle arbitrary time-scales
+ small sims should span entire SIMLIB when divided into 40 jobs
    (don't want all 40 jobs to read only first 100 LIBIDs)
+ infrastructure for Galactic rate model vs. b

- bigger SIMLIB with random RA,DEC that includes dither overlaps
- KN-model update with fixed RED + angle-dependent BLUE
- CC-model synthesis from many pieces
- missing models:
     Mira, TDE,  Orphan AfterGlow,  AGN,  Eclipsing binary
- Need rate and dN/db for Galactic transient models



# ===================================================
         Aug 14 2017  SNANA v10_50q
  GENRANGE_REDSHIFT tuned for each model (same for WFD and DDF)
  
LSST_DDF_MODEL01   TOTAL: Wrote  12531  of  38800  Generated.
LSST_DDF_MODEL02   TOTAL: Wrote  12908  of  188000  Generated.
LSST_DDF_MODEL42   TOTAL: Wrote    211  of  3280  Generated.
LSST_DDF_MODEL45   TOTAL: Wrote     17  of  400  Generated.
LSST_DDF_MODEL50   TOTAL: Wrote      1  of  400  Generated.
LSST_DDF_MODEL51   TOTAL: Wrote      0  of  400  Generated.
LSST_DDF_MODEL52   TOTAL: Wrote      3  of  400  Generated.
LSST_DDF_MODEL60   TOTAL: Wrote    278  of  400  Generated.

LSST_WFD_MODEL01   TOTAL: Wrote  1733863  of  16060000  Generated.
LSST_WFD_MODEL02   TOTAL: Wrote  1138094  of  77780000  Generated.
LSST_WFD_MODEL42   TOTAL: Wrote    20059  of  1372000  Generated.
LSST_WFD_MODEL45   TOTAL: Wrote     1064  of  116000  Generated.
LSST_WFD_MODEL50   TOTAL: Wrote        0  of  2520  Generated.
LSST_WFD_MODEL51   TOTAL: Wrote        1  of  2520  Generated.
LSST_WFD_MODEL52   TOTAL: Wrote        3  of  2520  Generated.
LSST_WFD_MODEL60   TOTAL: Wrote    48876  of  82920  Generated.

# ====================================================
        Dec 9 2017  SNANA_v10_53h

LSST_DDF_MODEL01   TOTAL: Wrote  13070  of  38810  Generated.
LSST_DDF_MODEL02   TOTAL: Wrote  13037  of  188000  Generated.
LSST_DDF_MODEL03   TOTAL: Wrote  2027  of  56390  Generated.
LSST_DDF_MODEL04   TOTAL: Wrote  669  of  16060  Generated.
LSST_DDF_MODEL42   TOTAL: Wrote  227  of  3310  Generated.
LSST_DDF_MODEL45   TOTAL: Wrote  17  of  280  Generated.
LSST_DDF_MODEL50   TOTAL: Wrote  6  of  100  Generated.
LSST_DDF_MODEL60   TOTAL: Wrote  154  of  230  Generated.
LSST_DDF_MODEL61   TOTAL: Wrote  47  of  100  Generated.
LSST_DDF_MODEL62   TOTAL: Wrote  42  of  11280  Generated.
LSST_DDF_MODEL63   TOTAL: Wrote  86  of  7060  Generated.
LSST_DDF_MODEL80   TOTAL: Wrote  150  of  150  Generated.
LSST_DDF_MODEL81   TOTAL: Wrote  49  of  100  Generated.

LSST_WFD_MODEL01   TOTAL: Wrote  1731227  of  16060000  Generated.
LSST_WFD_MODEL02   TOTAL: Wrote  1131822  of  77780000  Generated.
LSST_WFD_MODEL03   TOTAL: Wrote  162727  of  23330000  Generated.
LSST_WFD_MODEL04   TOTAL: Wrote  72348  of  6646000  Generated.
LSST_WFD_MODEL42   TOTAL: Wrote  20076  of  1372000  Generated.
LSST_WFD_MODEL45   TOTAL: Wrote  999  of  116000  Generated.
LSST_WFD_MODEL50   TOTAL: Wrote  25  of  7400  Generated.
LSST_WFD_MODEL60   TOTAL: Wrote  52080  of  98120  Generated.
LSST_WFD_MODEL61   TOTAL: Wrote  1343  of  5840  Generated.
LSST_WFD_MODEL62   TOTAL: Wrote  2909  of  4667000  Generated.
LSST_WFD_MODEL63   TOTAL: Wrote  6049  of  2925000  Generated.
LSST_WFD_MODEL80   TOTAL: Wrote  149551  of  150000  Generated.
LSST_WFD_MODEL81   TOTAL: Wrote  12189  of  100000  Generated.


# ===================================================
      Jan 13 2018    SNANA_v10_56d

LSST_DDF_MODEL01:  TOTAL: Wrote  12992  of  38810  Generated.
LSST_DDF_MODEL02:  TOTAL: Wrote  13312  of  188000  Generated.
LSST_DDF_MODEL03:  TOTAL: Wrote  1971  of  56390  Generated.
LSST_DDF_MODEL04:  TOTAL: Wrote  685  of  16060  Generated.
LSST_DDF_MODEL42:  TOTAL: Wrote  227  of  3310  Generated.
LSST_DDF_MODEL45:  TOTAL: Wrote  15  of  280  Generated.
LSST_DDF_MODEL50:  TOTAL: Wrote  0  of  20  Generated.
LSST_DDF_MODEL60:  TOTAL: Wrote  154  of  230  Generated.
LSST_DDF_MODEL61:  TOTAL: Wrote  5  of  20  Generated.
LSST_DDF_MODEL62:  TOTAL: Wrote  38  of  11280  Generated.
LSST_DDF_MODEL63:  TOTAL: Wrote  99  of  7060  Generated.
LSST_DDF_MODEL80:  TOTAL: Wrote  150  of  150  Generated.
LSST_DDF_MODEL81:  TOTAL: Wrote  65  of  100  Generated.

LSST_WFD_MODEL01:  TOTAL: Wrote  1733422  of  16060000  Generated.
LSST_WFD_MODEL02:  TOTAL: Wrote  1135812  of  77780000  Generated.
LSST_WFD_MODEL03:  TOTAL: Wrote  163388  of  23330000  Generated.
LSST_WFD_MODEL04:  TOTAL: Wrote  72223  of  6646000  Generated.
LSST_WFD_MODEL42:  TOTAL: Wrote  20092  of  1372000  Generated.
LSST_WFD_MODEL45:  TOTAL: Wrote  1021  of  116000  Generated.
LSST_WFD_MODEL50:  TOTAL: Wrote  21  of  7400  Generated.
LSST_WFD_MODEL60:  TOTAL: Wrote  52132  of  98120  Generated.
LSST_WFD_MODEL61:  TOTAL: Wrote  1317  of  5840  Generated.
LSST_WFD_MODEL62:  TOTAL: Wrote  2791  of  4667000  Generated.
LSST_WFD_MODEL63:  TOTAL: Wrote  6061  of  2925000  Generated.
LSST_WFD_MODEL80:  TOTAL: Wrote  149965  of  150000  Generated.
LSST_WFD_MODEL81:  TOTAL: Wrote  15203  of  100000  Generated.

# ====================================================
         Feb 10 2018  SNANA v10_58h

* Add uLens_BSR and uLens_STRING models (MODEL90, MODEL91)
* reduce PHOTOMETRY table output to reduce output size.

 LSST_DDF_MODEL01   TOTAL: Wrote  12989  of  38810  Generated. 
 LSST_DDF_MODEL02   TOTAL: Wrote  13316  of  188000  Generated.
 LSST_DDF_MODEL03   TOTAL: Wrote  2013  of  56390  Generated.
 LSST_DDF_MODEL04   TOTAL: Wrote  695  of  16060  Generated. 
 LSST_DDF_MODEL42   TOTAL: Wrote  241  of  3310  Generated. 
 LSST_DDF_MODEL45   TOTAL: Wrote  36  of  840  Generated. 
 LSST_DDF_MODEL50   TOTAL: Wrote  1  of  20  Generated. 
 LSST_DDF_MODEL60   TOTAL: Wrote  156  of  230  Generated. 
 LSST_DDF_MODEL61   TOTAL: Wrote  6  of  20  Generated. 
 LSST_DDF_MODEL62   TOTAL: Wrote  30  of  11280  Generated. 
 LSST_DDF_MODEL63   TOTAL: Wrote  97  of  7060  Generated. 
 LSST_DDF_MODEL80   TOTAL: Wrote  150  of  150  Generated. 
 LSST_DDF_MODEL81   TOTAL: Wrote  67  of  100  Generated. 
 LSST_DDF_MODEL90   TOTAL: Wrote  20  of  20  Generated. 
 LSST_DDF_MODEL91   TOTAL: Wrote  4  of  100  Generated. 

 LSST_WFD_MODEL01   TOTAL: Wrote  1731984  of  16060000  Generated. 
 LSST_WFD_MODEL02   TOTAL: Wrote  1135938  of  77780000  Generated. 
 LSST_WFD_MODEL03   TOTAL: Wrote  164286  of  23330000  Generated.
 LSST_WFD_MODEL04   TOTAL: Wrote  71965  of  6646000  Generated. 
 LSST_WFD_MODEL42   TOTAL: Wrote  19832  of  1372000  Generated. 
 LSST_WFD_MODEL45   TOTAL: Wrote  1002  of  116000  Generated. 
 LSST_WFD_MODEL50   TOTAL: Wrote  27  of  7400  Generated. 
 LSST_WFD_MODEL60   TOTAL: Wrote  51889  of  98120  Generated. 
 LSST_WFD_MODEL61   TOTAL: Wrote  1343  of  5840  Generated. 
 LSST_WFD_MODEL62   TOTAL: Wrote  2869  of  4667000  Generated. 
 LSST_WFD_MODEL63   TOTAL: Wrote  6038  of  2925000  Generated. 
 LSST_WFD_MODEL80   TOTAL: Wrote  149966  of  150000  Generated. 
 LSST_WFD_MODEL81   TOTAL: Wrote  15093  of  100000  Generated. 
 LSST_WFD_MODEL90   TOTAL: Wrote  279  of  280  Generated. 
 LSST_WFD_MODEL91   TOTAL: Wrote  21  of  30000  Generated. 

