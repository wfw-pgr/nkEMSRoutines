#!/usr/bin/env python3

import sys, os, re, glob
import numpy as np

# ========================================================= #
# ===  merge__bintegField.py                            === #
# ========================================================= #

def merge__bintegField( inpFiles=None, outFile=None ):

    # ------------------------------------------------- #
    # --- [1] Arguments                             --- #
    # ------------------------------------------------- #
    if   ( inpFiles is None ):
        sys.exit( "[merge__bintegField.py] inpFile == ??? " )
    elif ( type( inpFiles ) is str  ):
        inpFiles = glob.glob( inpFile )
    elif ( type( inpFiles ) is list ):
        for inpFile in inpFiles:
            if not( os.path.exists( inpFile ) ):
                print( "[merge__bintegField.py] cannot find {} ".format( inpFile ) )
                sys.exit()
                
        
    if ( outFile is None ):
        outFile = "ems_merged.dat"
        
    # ------------------------------------------------- #
    # --- [2] extract bfield from file              --- #
    # ------------------------------------------------- #
    import nkEMSRoutines.extract__bintegField as ebf
    Data_list   = []
    for ifile in inpFiles:
        ext        = "." + ( ifile.split( "." ) )[-1]
        Data_list += [ ebf.extract__bintegField( inpFile=ifile, save=False ) ]
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
    inpFiles = sys.argv[1:]
    print( "[merge__bintegField.py] inpFile == {}".format( inpFiles ) )
    
    # ------------------------------------------------- #
    # --- [3] merge                               --- #
    # ------------------------------------------------- #
    merge__bintegField( inpFiles=inpFiles )
