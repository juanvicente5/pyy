Generado por Django 4.2.3 el 16-08-2023 20:10

de  Django . migraciones de importación de bases de datos  , modelos 


clase  Migración ( migraciones . Migración ):

    inicial  =  Verdadero

    dependencias  = [
    ]

    operaciones  = [
        migraciones . Crear modelo (
            nombre = 'Plan de estudios' ,
            campos = [
                ( 'id' , modelos . BigAutoField ( auto_created = True , clave_primaria = True , serialize = False , nombre_detallado = 'ID' )),
                ( 'nombre' , modelos . CharField ( max_length = 50 )),
                ( 'apellido' , modelos . CharField ( max_length = 50 )),
                ( 'presentación' , modelos . TextField ()),
                ( 'experiencia' , modelos . TextField ()),
                ( 'estudios' , modelos . CharField ( max_length = 256 )),
            ],
        ),
        migraciones . Crear modelo (
            nombre = 'Empleador' ,
            campos = [
                ( 'id' , modelos . BigAutoField ( auto_created = True , clave_primaria = True , serialize = False , nombre_detallado = 'ID' )),
                ( 'nombre' , modelos . CharField ( max_length = 50 )),
                ( 'apellido' , modelos . CharField ( max_length = 50 )),
                ( 'profesión' , modelos . CharField ( max_length = 50 )),
                ( 'edad' , modelos . IntegerField ( max_length = 50 )),
                ( 'nombreEmpresa' , modelos . CharField ( max_length = 50 )),
            ],
        ),
        migraciones . Crear modelo (
            nombre = 'Empleos' ,
            campos = [
                ( 'id' , modelos . BigAutoField ( auto_created = True , clave_primaria = True , serialize = False , nombre_detallado = 'ID' )),
                ( 'carga' , modelos . CharField ( max_length = 50 )),
                ( 'detalles' , modelos . TextField ()),
                ( 'ubicacion' , modelos . CharField ( max_length = 50 )),
                ( 'sueldo' , modelos . IntegerField ( max_length = 50 )),
            ],
        ),
    ]
