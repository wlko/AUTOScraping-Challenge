import glob

def checkfilename(fname):
    # Función para verificar si el nombre del archivo ya existe y no sobreescribirlo
    it=1
    while True:
        fnfull = fname + "_" + str(it).zfill(2)+'*'
        if glob.glob(fnfull):
            it = it+1
        else:
            break
    fnroot = fname + "_" + str(it).zfill(2)
                
    return fnroot