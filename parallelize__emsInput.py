import os, sys
import numpy                       as np
import nkUtilities.save__pointFile as spf


# ========================================================= #
# ===  parallelize__emsInput.py                         === #
# ========================================================= #

def parallelize__emsInput( nParallel=1, ptsFile="dat/coordinate.dat", \
                           refFile="dat/ems_ref.inp", cooFile = "coord_{0:03}.dat", \
                           outFile="dat/ems_pst.inp" ):

    outFile_   = outFile.replace( ".inp", "_{0:03}.inp" )
    
    # ------------------------------------------------- #
    # --- [1] load coordinate file                  --- #
    # ------------------------------------------------- #
    import nkUtilities.load__pointFile as lpf
    coord      = lpf.load__pointFile( inpFile=ptsFile, returnType="point" )

    # ------------------------------------------------- #
    # --- [2] partitioning                          --- #
    # ------------------------------------------------- #
    #  -- [2-1]  partitioning number                --  #
    nLine      = coord.shape[0]
    surplus    = nLine %  nParallel
    quotient   = nLine // nParallel
    nLineList  = [ quotient for ik in range( nParallel ) ]
    for ik in range( surplus   ):
        nLineList[ik] = nLineList[ik] + 1

    #  -- [2-2]  save coordinates                   --  #
    init, last = 0, 0
    for ik in range( nParallel ):
        init, last = last, last+nLineList[ik]
        hcoord     = coord[init:last,:]
        spf.save__pointFile( outFile=cooFile.format( ik ), Data=hcoord, no_header=True )
        
    # ------------------------------------------------- #
    # --- [3] convert into string                   --- #
    # ------------------------------------------------- #
    #  -- [3-1] load reference file                 --  #
    with open( refFile, "r" ) as f:
        emsSettings  = f.read()
        
    #  -- [3-2] save in a different file            --  #
    for ik in range( nParallel ):
        with open( cooFile.format(ik), "r" ) as f:
            str_coordinates = f.read()
        emsSettings_ = emsSettings.format( nLineList[ik], str_coordinates.strip() )
        
        with open( outFile_.format(ik), "w" ) as f:
            f.write( emsSettings_ )
        print( "[parallelize__emsInput.py] outFile :: {0}".format( outFile_.format(ik) ) )

    # ------------------------------------------------- #
    # --- [4] remove coordinate files               --- #
    # ------------------------------------------------- #
    for ik in range( nParallel ):
        removeFile = cooFile.format(ik)
        if ( os.path.exists( removeFile ) ):
            os.remove( removeFile )
            
        
# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #
if ( __name__=="__main__" ):

    refFile   = "test/ems_ref.inp"
    outFile   = "test/ems_pst.inp"
    ptsFile   = "test/coordinate.dat"
    nParallel = 4
    parallelize__emsInput( refFile=refFile, outFile=outFile, \
                           ptsFile=ptsFile, nParallel=nParallel )
