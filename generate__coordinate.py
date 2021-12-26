import numpy as np

# ========================================================= #
# ===  generate__coordinate.py                          === #
# ========================================================= #

def generate__coordinate( outFile="test/coordinate.dat" ):

    # ------------------------------------------------- #
    # --- [1] generate coordinate                   --- #
    # ------------------------------------------------- #
    import nkUtilities.equiSpaceGrid as esg
    x1MinMaxNum = [ 0.0, 1.0, 11 ]
    x2MinMaxNum = [ 0.0, 1.0, 11 ]
    x3MinMaxNum = [ 0.0, 0.0,  1 ]
    coord       = esg.equiSpaceGrid( x1MinMaxNum=x1MinMaxNum, x2MinMaxNum=x2MinMaxNum, \
                                     x3MinMaxNum=x3MinMaxNum, returnType = "point" )

    # ------------------------------------------------- #
    # --- [2] save point file                       --- #
    # ------------------------------------------------- #
    import nkUtilities.save__pointFile as spf
    spf.save__pointFile( outFile=outFile, Data=coord )

    
# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #
if ( __name__=="__main__" ):
    generate__coordinate()
