import numpy as np

# ========================================================= #
# ===  coordinate__inCylinder.py                        === #
# ========================================================= #

def coordinate__inCylinder( const=None, cnsFile="dat/parameter.conf", outFile="dat/coordinates.dat" ):

    x_, y_, z_ = 0, 1, 2
    
    # ------------------------------------------------- #
    # --- [1] load constants                        --- #
    # ------------------------------------------------- #
    if ( const is None ):
        import nkUtilities.load__constants as lcn
        const   = lcn.load__constants( inpFile=cnsFile )
    
    # ------------------------------------------------- #
    # --- [1] generate grid                         --- #
    # ------------------------------------------------- #
    import nkUtilities.equiSpaceGrid as esg
    x1MinMaxNum = [ const["coordinate.x1MinMaxNum"][0], const["coordinate.x1MinMaxNum"][1], \
                    int( const["coordinate.x1MinMaxNum"][2] ) ]
    x2MinMaxNum = [ const["coordinate.x2MinMaxNum"][0], const["coordinate.x2MinMaxNum"][1], \
                    int( const["coordinate.x2MinMaxNum"][2] ) ]
    x3MinMaxNum = [ const["coordinate.x3MinMaxNum"][0], const["coordinate.x3MinMaxNum"][1], \
                    int( const["coordinate.x3MinMaxNum"][2] ) ]
    coord       = esg.equiSpaceGrid( x1MinMaxNum=x1MinMaxNum, x2MinMaxNum=x2MinMaxNum, \
                                     x3MinMaxNum=x3MinMaxNum, returnType = "point" )
    
    # ------------------------------------------------- #
    # --- [2] cylindrical cut                       --- #
    # ------------------------------------------------- #
    radii       = np.sqrt( coord[:,x_]**2 + coord[:,y_]**2 )
    index       = np.where( radii <= const["coordinate.radius"] )
    coord       = coord[index]

    # ------------------------------------------------- #
    # --- [3] save point data                       --- #
    # ------------------------------------------------- #
    import nkUtilities.save__pointFile as spf
    spf.save__pointFile( outFile=outFile, Data=coord )


# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):
    cnsFile = "test/parameter.coordinate__inCylinder.conf"
    outFile = "test/coordinates.dat"
    coordinate__inCylinder( cnsFile=cnsFile, outFile=outFile )
