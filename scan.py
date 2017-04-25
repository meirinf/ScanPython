import sys
import serial
 
def scan(num_ports = 20, verbose=True):
    
     #-- Lista de los dispositivos serie. Inicialmente vacia
     dispositivos_serie = []
     
     if verbose:
       print "Escanenado %d puertos serie:" % num_ports
     
     #-- Escanear num_port posibles puertos serie
     for i in range(num_ports):
     
       if verbose:
         sys.stdout.write("puerto %d: " % i)
         sys.stdout.flush()
     
       try:
       
         #-- Abrir puerto serie
         s = serial.Serial(i)
         
         if verbose: print "OK --> %s" % s.portstr
         
         #-- Si no hay errores, anadir el numero y nombre a la lista
         dispositivos_serie.append( (i, s.portstr))
         
         #-- Cerrar puerto
         s.close()
             
       #-- Si hay un error se ignora      
       except:
         if verbose: print "NO"
         pass
         
     #-- Devolver la lista de los dispositivos serie encontrados    
     return dispositivos_serie
 
 
 #--------------------------
 # Pruebas del modulo Scan 
 #--------------------------
if __name__=='__main__':
 
   
   #-- Escanear los puertos.
   #-- Se puede indicar el numero de puertos a escaner
   #-- El modo "verbose" esta activado por defecto. Se desactiva con False
   puertos_disponibles=scan(num_ports = 20,verbose=True)
   
   #-- Recorrer la lista mostrando los que se han podido abrir
   print ""
   print "Puertos detectados:"
   if len(puertos_disponibles)!=0:
     for n,nombre in puertos_disponibles:
       print "  (%d) %s" % (n,nombre)
   else:
     print "  Ninguno"
 
