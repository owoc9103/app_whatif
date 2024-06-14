# Instalar el paquete pacman si no est� instalado
#Este c�digo en R comprueba si el paquete "pacman" est� instalado en el entorno de R. 
#Si no lo est�, autom�ticamente lo instala. "pacman" es un paquete que facilita la 
#gesti�n de paquetes en R, permitiendo la instalaci�n y carga de m�ltiples paquetes de forma m�s eficiente.
if (!require("pacman")) install.packages("pacman")

# Cargar el paquete pacman
#Este c�digo en R utiliza el paquete "pacman" para cargar m�ltiples paquetes importantes para el an�lisis
#que se desarrollar�.
pacman::p_load(dplyr, tidyr, readxl, lubridate, tidyverse, data.table, rio, ChainLadder)

# Crear una lista de las librer�as a instalar
librerias <- c("dplyr", "tidyr", "readxl", "lubridate", "tidyverse", "data.table", "rio", "ChainLadder")

# Iterar sobre la lista de librer�as
for (libreria in librerias) {
  # Verificar si la librer�a est� instalada
  if (!requireNamespace(libreria, quietly = TRUE)) {
    # Si no est� instalada, instalarla
    pacman::p_load(libreria, character.only = TRUE)
  } else {
    # Si ya est� instalada, imprimir un mensaje
    cat(paste("La librer�a", libreria, "ya est� instalada.\n"))
  }
}

#Si alguna biblioteca no est� instalada, debe hacerse a trav�s del siguiente comando:
#Por ejemplo, si la biblioteca que falta es "dplyr", el comando adecuado para su instalaci�n es 
#install.packages("dplyr"). Este comando debe ejecutarse una sola vez.


#Se realiza el cargue de las librer�as que se utilizaran en la ejecuci�n del presente codigo
library(dplyr)
library(tidyr)
library(readxl)
library(lubridate)
library(tidyverse)
library(data.table)
library(rio)
library(ChainLadder)

#Indica a R que muestre todos los d�gitos disponibles, evitando que los n�meros se muestren en 
#notaci�n cient�fica cuando no es necesario
options(scipen = 999)

#Modificar las rutas donde se encuentran ls insumos (input) y la ruta donde se guardar�n
#los resultados.
input<-"/insumos"
#output<- "C:/OSCAR_pwc/Compensar_EPS_Actuar�a/Compensar_Backtesting_Actuaria/Resultados"

#El directorio de trabajo actual ser� la carpeta input
setwd(input)

#Se establecen los per�odos de inicio y fin para analizar la informaci�n de los tri�ngulos.
#A�adir el periodo en formato dd/mm/yyyy desde donde incia y terminan los triangulos a evaluar 
inicio<- as.Date("01/02/2023", "%d/%m/%Y")
final<- as.Date("01/12/2023", "%d/%m/%Y")


#Se define la variable 'segmento', la cual debe ser modificada a 'PAC', 'PBS' o 'RS', dependiendo de 
#del backtesting a realizar. Cada insumo contiene informaci�n sobre los segmentos 
#individuales, que abarcan detalles tanto del tri�ngulo como de los factores de desarrollo. Estos datos 
#est�n organizados en diferentes rangos seg�n el segmento. Para cada tri�ngulo y sus respectivos factores
#de desarrollo, se emplea un rango espec�fico de acuerdo al segmento correspondiente:


segmento="RS" #Modificar a PAC, PBS o RS

if(segmento=="PBS"){
  rango_triangulo="B4:AL40"
  rango_factores="D45:AL46"
}else if(segmento=="RS"){
  rango_triangulo="B52:AL88"
  rango_factores="D93:AL94"
}else{
  rango_triangulo="B100:AL136"
  rango_factores="D141:AL142"
}


#Carga de triangulos
data_list <- import_list("Triangulos Reserva Servicios 2023_V2.xlsx", range=  rango_triangulo)
#Carga de factores de desarrollo
data_list2 <- import_list("Triangulos Reserva Servicios 2023_V2.xlsx", range=  rango_factores)

#Definicion periodos de evaluacion en formato #YYMM
periodo_inicial <-format(inicio,"%Y%m") #modificar
periodo_final <- format(final,"%Y%m")



#Llamar al triangulo inicial
Triangulo_inicial <- as.data.frame(data_list[periodo_inicial])
rownames(Triangulo_inicial)<- Triangulo_inicial[,1]
Triangulo_inicial<-Triangulo_inicial[,-1]
colnames(Triangulo_inicial)<- seq(1,36,1)
Triangulo_inicial <- as.triangle(as.matrix(Triangulo_inicial))

#LLamar la tabla de factores de desarrollo
factores <- as.vector(t((data_list2[[periodo_inicial]])))
factores <-data.frame(Desarrollo=seq(1,35,1),factores)


#Llamar al triangulo final
Triangulo_final <- as.data.frame(data_list[periodo_final])
rownames(Triangulo_final)<-Triangulo_final[,1]
Triangulo_final<-Triangulo_final[,-1]
colnames(Triangulo_final)<- seq(1,36,1)
Triangulo_final<- as.triangle(as.matrix(Triangulo_final))


#Obtencion de incurridos iniciales
Incurrido_inicial<-getLatestCumulative(Triangulo_inicial)
Incurrido_inicial<-as.data.frame(Incurrido_inicial)

#Obtencion de incurridos finales
Incurrido_final <- getLatestCumulative(Triangulo_final)
Incurrido_final<- as.data.frame(Incurrido_final)

#Tabla auxiliar para calculo de IBNR
aux<-data.frame(Desarrollo=seq(36,1,-1),Incurrido_inicial)
aux<- merge(aux,factores)
aux <-arrange(aux, desc(Desarrollo))
aux$factores_acumulados <-cumprod(aux$factores)
aux$Porcentaje_desarrollo <- 1/aux$factores_acumulados
aux$Ultimate <- with(aux, Incurrido_inicial*factores_acumulados)
aux$IBNR <-with(aux, Ultimate-Incurrido_inicial  )


#Generacion tabla por linea de servicio
Tabla <- merge(Incurrido_inicial, Incurrido_final, by.x = 0, by.y = 0, all.x = T)
colnames(Tabla)[3]<- "Incurrido_Final"
Tabla$Actual <- Tabla$Incurrido_Final-Tabla$Incurrido_inicial

#Generacion de los valores incurridos de cada uno de los meses
dif_a�os <- as.numeric(format(final, "%Y")) - as.numeric(format(inicio, "%Y"))
dif_meses <- as.numeric(format(final, "%m")) - as.numeric(format(inicio, "%m"))

# Convertir la diferencia de a�os y meses a meses
movil <- (dif_a�os * 12 + dif_meses)+1
periodo_movil<-format(seq(from=inicio, by="1 months", length.out=movil),"%Y%m")
Incurrido_movil<-matrix(0,movil-1,1)

#Se obtiene el valor del incurrido en los periodos de desarrollo intermedio
for(i in 2:movil){
  Triangulo_movil<-as.data.frame(data_list[periodo_movil[i]])
  rownames(Triangulo_movil)<-Triangulo_movil[,1]
  Triangulo_movil=Triangulo_movil[,-1]
  colnames(Triangulo_movil)<- seq(1,36,1)
  Triangulo_movil <- as.triangle(as.matrix(Triangulo_movil))
  Incurrido_movil_v2<-getLatestCumulative(Triangulo_movil)
  Incurrido_movil_v2<-as.data.frame(Incurrido_movil_v2)[1,1]
  Incurrido_movil[i-1,1]<-Incurrido_movil_v2
  rm(Incurrido_movil_v2)
  #print(Incurrido_movil)
}

Incurrido_movil<-as.vector(Incurrido_movil)
Tabla$Incurrido_Final[2:length(Incurrido_movil)]<-Incurrido_movil[1:length(Incurrido_movil)-1]

#Se Elimina Periodo con Na, se calcula, el actual y se adiciona la columna de "Desarrollo"
#para traer los factores de desarrollo
Tabla$Actual <- Tabla$Incurrido_Final-Tabla$Incurrido_inicial
Tabla <- na.omit(Tabla)
Tabla$Desarrollo=seq(dim(Tabla)[1],1,-1)

#Se hace el merge con la tabla aux para concatenar los factores de desarrollo
Tabla<-merge(Tabla,aux[c("Desarrollo","Porcentaje_desarrollo","Ultimate")],by.x="Desarrollo",by.y = "Desarrollo",sort = FALSE)

#Se realiza el calculo del porcentaje de desarrollo actual
Tabla$Porcentaje_desarrollo_actual<-lag(Tabla$Porcentaje_desarrollo,n = movil-1)

#Se realiza el ajuste del desarrollo a 1 
Tabla$Porcentaje_desarrollo_actual[which(is.na(Tabla$Porcentaje_desarrollo_actual)==TRUE)]<-1

#Se calcula el Expected
Tabla$Expected<-((Tabla$Porcentaje_desarrollo_actual-Tabla$Porcentaje_desarrollo)/(1-Tabla$Porcentaje_desarrollo))*(Tabla$Ultimate-Tabla$Incurrido_inicial)
Tabla[is.na(Tabla)]<-0

#Se calcula el AvE absoluto y el AvE en porcentaje
Tabla$AvE_absoluto<-Tabla$Actual-Tabla$Expected
Tabla$Ave_porcentaje<-(Tabla$AvE_absoluto/(Tabla$Ultimate-Tabla$Incurrido_inicial))*100
Tabla[is.na(Tabla)]<-0
Tabla$Ave_porcentaje[is.infinite(Tabla$Ave_porcentaje)] <- 0

#Resultado Final Total BKT
Resultado_BKT=(sum(Tabla$AvE_absoluto)/sum(Tabla$Expected))*100
print(Resultado_BKT)

###Se Organiza la base de datos
Tabla=Tabla[c("Row.names","Incurrido_inicial","Incurrido_Final","Actual","Porcentaje_desarrollo_actual","Porcentaje_desarrollo","Ultimate","Expected","AvE_absoluto","Ave_porcentaje")]
colnames(Tabla)[1]<-"Periodo"

#Se modifica el directorio a la ruta de salida y se exporta tabla con los resultados totales
#setwd(output)
#write.table(Tabla,paste0("BKT_",segmento,".csv"),sep = ";",row.names = FALSE)
return(Resultado_BKT)