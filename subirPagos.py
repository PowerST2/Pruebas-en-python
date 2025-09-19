import concurrent.futures
import descargar_bcp
import convertir_formato
import descargar_scotiabank
import convertir_formato_scotiabank
import upload_sistemas
import ocefv2
import subir_ocef
import subir_ocef_bcp
import simulacro_upload_sistemas
import simulacro_ocefv2
import confirmar
import simulacro_upload_ocefv2
## DESCARGAR PAGOS DE OCEF
descargar_bcp.main()
convertir_formato.main()
#descargar_scotiabank.main()
#convertir_formato_scotiabank.main()
## INTEGRACION SISTEMA INSCRIPCIONES
#upload_sistemas.main()

# SIMULACRO
#simulacro_upload_sistemas.main()
simulacro_upload_ocefv2.main()
# INTEGRACIÓN
#ocefv2.main()
#subir_ocef_bcp.main()
#subir_ocef.main()
#confirmar.main()
# INTEGRACIÓN SIMULACRO
# simulacro_ocefv2.main()
subir_ocef_bcp.main()
confirmar.main()


















