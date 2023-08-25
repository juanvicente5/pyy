de  Django . ruta de importación de URL  , incluir 
de . vistas  importadas  *
#SEPARE DE 3 CADA URL PARA TENER MAS ORGANIZADO CADA MODELO. EMPLEADO EMPLEADOR EMPLEO
patrones de URL  = [
    ruta ( 'inicio/' , inicio , nombre = "home" ),

    ruta ( 'lista_empleados/' , lista_empleados , nombre = 'lista_empleados' ),
    ruta ( 'empleado/<int:curriculum_id>/' , detalle_empleado , nombre = 'detalle_empleado' ),
    ruta ( 'empleadoForm/' , empleadoForm , nombre = 'empleadoForm' ),

    ruta ( 'lista_empleos/' , lista_empleos , nombre = 'lista_empleos' ),
    ruta ( 'trabajo/<int:trabajo_id>/' , detalle_empleo , nombre = 'detalle_empleo' ),
    ruta ( 'formulario de trabajo/' , formulario de trabajo , nombre = 'formulario de trabajo' ),

    ruta ( 'lista_empleadores/' , lista_empleadores , nombre = 'lista_empleadores' ),
    ruta ( 'empleador/<int:empleador_id>/' , detalle_empleador , nombre = 'detalle_empleador' ),
    ruta ( 'empleadorForm/' , empleadoresForm , nombre = 'empleadorForm' ),
