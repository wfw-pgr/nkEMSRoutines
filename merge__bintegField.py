#!/usr/bin/env python3

import sys, os, re, glob
import numpy as np

# ========================================================= #
# ===  merge__bintegField.py                            === #
# ========================================================= #

def merge__bintegField( inpFile=None, outFile=None ):

    # ------------------------------------------------- #
    # --- [1] Arguments                             --- #
    # ------------------------------------------------- #
    if ( inpFile is None ):
        sys.exit( "[merge__bintegField.py] inpFile == ??? " )
    else:
        inpFiles = glob.glob( inpFile )
    if ( outFile is None ):
        outFile = "ems_merged.dat"
        
    # ------------------------------------------------- #
    # --- [2] extract bfield from file              --- #
    # ------------------------------------------------- #
    import nkEMSRoutines.extract__bintegField as ebf
    Data_list   = []
    for ifile in inpFiles:
        ext        = "." + ( ifile.split( "." ) )[-1]
        outFile    = ifile.replace( ext, ".mid_dat" )
        Data_list += [ ebf.extract__bintegField( inpFile=ifile, outFile=outFile ) ]
    Data = np.concatenate( Data_list, axis=0 )
    
    # ------------------------------------------------- #
    # --- [3] save in a file                        --- #
    # ------------------------------------------------- #
    import nkUtilities.save__pointFile as spf
    spf.save__pointFile( outFile=outFile, Data=Data )
    

# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #
if ( __name__=="__main__" ):

    # ------------------------------------------------- #
    # --- [1] display how to use                    --- #
    # ------------------------------------------------- #
    print()
    print( "[merge__bintegField.py]   [usage] :: " )
    print( " $ python3 merge__bintegField.py [inpFile] [outFile]" )
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
        sys.exit( "[merge__bintegField.py]  inpFile == ??? [ERROR]" )

    print( "[merge__bintegField.py] inpFile == {}".format( inpFile ) )
    print( "[merge__bintegField.py] outFile == {}".format( outFile ) )
    
    # ------------------------------------------------- #
    # --- [3] merge                               --- #
    # ------------------------------------------------- #
    merge__bintegField( inpFile=inpFile, outFile=outFile )
