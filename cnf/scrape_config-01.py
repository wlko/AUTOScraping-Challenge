class args:
    # Default parameters
    paralelismo = False 
    proxy = False # Por default no usaré proxies
    proxies = {
        "http": "",
        "https": ""
        } # Agregar lista o API de proxies
    
    registros = [
        '1236216', '1236222', '1236223','1236224', '1236226', 
        '1236227', '1236275', '1236319', '1236450', '1236470', 
        '1236472', '1236471', '1236482'
        ] # Definir acá los registros a buscar
    
    save_file_name = "" # Método para tomar nombre desde la terminal

    export_dir =  ""