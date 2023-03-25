#!/usr/bin/env python3

import sys, os, re
import numpy as np

# ========================================================= #
# ===  extract__bintegField.py                          === #
# ========================================================= #

def extract__bintegField( inpFile=None, outFile=None ):

    # ------------------------------------------------- #
    # --- [1] Arguments                             --- #
    # ------------------------------------------------- #
    if ( inpFile is None ):
        sys.exit( "[extract__bintegField.py] inpFile == ??? " )

    # ------------------------------------------------- #
    # --- [2] load EMSolution's output file         --- #
    # ------------------------------------------------- #
    with open( inpFile, "r" ) as f:
        lines = f.readlines()

    # ------------------------------------------------- #
    # --- [3] search first line                     --- #
    # ------------------------------------------------- #
    
    pattern_start = "No.\s*x\s*y\s*z\s*Bx\s*By\s*Bz\s*\|B\|"
    
    for iS, line in enumerate( lines ):
        research = re.search( pattern_start, line )
        if ( research ): break
    iS     = iS + 1
    for iL,line in enumerate( lines[iS:] ):
        if ( len( line.strip() ) == 0 ): break
    iL     = iS + iL

    # ------------------------------------------------- #
    # --- [4] Load Data using numpy                 --- #
    # ------------------------------------------------- #
    Data = np.loadtxt( lines[iS:iL] )
    Data = np.copy( Data[:,1:] )

    # ------------------------------------------------- #
    # --- [5] save in a file                        --- #
    # ------------------------------------------------- #
    import nkUtilities.save__pointFile as spf
    names = [ "x", "y", "z", "bx", "by", "bz", "|b|" ]
    if ( outFile is None ):
        outFile = inpFile.replace( ".out", ".dat" )
    spf.save__pointFile( outFile=outFile, Data=Data, names=names )

    return( Data )



# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):

    # ------------------------------------------------- #
    # --- [1] display how to use                    --- #
    # ------------------------------------------------- #
    print()
    print( "[extract__bintegField.py]   [usage] :: " )
    print( " $ python3 extract__bintegField.py [inpFile] [outFile]" )
    print()
    
    # ------------------------------------------------- #
    # --- [2] Arguments                             --- #
    # ------------------------------------------------- #
    if   ( len( sys.argv ) == 2 ):
        inpFile = sys.argv[1]
        outFile = None
    elif ( len( sys.argv ) == 3 ):
        inpFile = sys.argv[1]
        outFile = sys.argv[2]
    else:
        sys.exit( "[extract__bintegField.py]  inpFile == ??? [ERROR]" )

    print( "[extract__bintegField.py] inpFile == {}".format( inpFile ) )
    print( "[extract__bintegField.py] outFile == {}".format( outFile ) )
    
    # ------------------------------------------------- #
    # --- [3] extract                               --- #
    # ------------------------------------------------- #
    extract__bintegField( inpFile=inpFile, outFile=outFile )
