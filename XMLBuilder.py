import datetime
import xml.etree.ElementTree as ET
import inisettings
import pytz
import configparser
import codecs


with codecs.open('config.txt', 'r', encoding='utf-8') as file:
        config = configparser.ConfigParser()
        config.read_file(file)
#Pendiente de Revisión
selectedSesion = 'CIA1'  # Producción

NitEmisor = str(config.get(selectedSesion, 'NitEmisor'))
digitoVerificador= str(config.get(selectedSesion, 'digitoVerificador'))
razonSocialEmisor= str(config.get(selectedSesion, 'razonSocialEmisor'))
nombreComercialEmisor= str(config.get(selectedSesion, 'nombreComercialEmisor'))
direccionEmisor= str(config.get(selectedSesion, 'direccionEmisor'))
nombreAdquiriente= str(config.get(selectedSesion, 'nombreAdquiriente'))
nitConsumidorFinal= str(config.get(selectedSesion, 'nitConsumidorFinal'))
prefijoFE= str(config.get(selectedSesion, 'prefijoFE'))
currencyType=str(config.get(selectedSesion, 'currencyType'))
nombreCiudad= str(config.get(selectedSesion, 'nombreCiudad'))
nombreDepartamento= str(config.get(selectedSesion, 'nombreDepartamento'))
nombrePais= str(config.get(selectedSesion, 'nombrePais'))
codigoMunicipio= str(config.get(selectedSesion, 'codigoMunicipio'))
codigoDepartamento= str(config.get(selectedSesion, 'codigoDepartamento'))
codigoPais= str(config.get(selectedSesion, 'codigoPais'))
CodigoPostal= str(config.get(selectedSesion, 'CodigoPostal'))
numeroMatriculaMercantilEmi= str(config.get(selectedSesion, 'numeroMatriculaMercantilEmi'))
numeroMatriculaMercantilAdq= str(config.get(selectedSesion, 'numeroMatriculaMercantilAdq'))
Ambiente = str(config.get(selectedSesion, 'Ambiente'))
numeroAutorizacion= str(config.get(selectedSesion, 'numeroAutorizacion'))
FechaIniAutorizacion= str(config.get(selectedSesion, 'FechaIniAutorizacion'))
facturaInicial= str(config.get(selectedSesion, 'facturaInicial'))
FechaFinAutorizacion= str(config.get(selectedSesion, 'FechaFinAutorizacion'))
facturaFinal= str(config.get(selectedSesion, 'facturaFinal'))
personaContacto= str(config.get(selectedSesion, 'personaContacto'))
movilContacto= str(config.get(selectedSesion, 'movilContacto'))
mailContacto= str(config.get(selectedSesion, 'mailContacto'))
DireccionFisica= str(config.get(selectedSesion, 'DireccionFisica'))
tzinfo = datetime.timezone.utc
tzdelta= '-05:00'
local_time=datetime.datetime.now()
local_timezone = pytz.timezone('America/Bogota')
utc_time = local_time.astimezone(pytz.utc)
str_utctimedate=local_time.strftime("%Y-%m-%d")   #("%Y-%m-%d %H:%M:%S")
str_utctimetz= utc_time.strftime("%H:%M:%S") + tzdelta #("%Y-%m-%d %H:%M:%S")
str_localtimetz= local_time.strftime("%H:%M:%S") + tzdelta #("%Y-%m-%d %H:%M:%S")

#main function of module
def generateXML(xmlfile,facturaNumero,totalFactura,totalItems, *diccionarios1):
    # Create the root element
    dictGroups = diccionarios1[0]
    dictTotals=diccionarios1[1]
    root = ET.Element("FACTURA")

    # Create and append the ENC element
    enc = ET.SubElement(root, "ENC")
    ET.SubElement(enc, "ENC_1").text = "INVOIC" #Tipo de documento
    ET.SubElement(enc, "ENC_2").text = NitEmisor
    ET.SubElement(enc, "ENC_3").text = "222222222222" #Nit Adquiriente
    ET.SubElement(enc, "ENC_4").text = "UBL 2.1" #Version del esquema UBL
    ET.SubElement(enc, "ENC_5").text = "DIAN 2.1" #Version del Formato del Documento
    ET.SubElement(enc, "ENC_6").text = prefijoFE + str(facturaNumero) #PREFIJO OBLIGATORIO + FOLIO
    ET.SubElement(enc, "ENC_7").text = str_utctimedate #Fecha de Emisión de la Factura
    ET.SubElement(enc, "ENC_8").text = str_utctimetz #Hora  de Emisión de la Factura
    ET.SubElement(enc, "ENC_9").text = '01' #Tipo de Factura
    ET.SubElement(enc, "ENC_10").text = currencyType  #Tipo de Moneda
    ET.SubElement(enc, "ENC_15").text = totalItems #Número de Productos Global
    ET.SubElement(enc, "ENC_20").text = Ambiente #Ambiente 01:Production, 02:Demo
    ET.SubElement(enc, "ENC_21").text = '10' #Tipo de Operacion  (10 Estandard)


    # Create and append the EMI element Emisor Information
    emi = ET.SubElement(root, "EMI")
    ET.SubElement(emi, "EMI_1").text = "1" #Persona Juridica Natural Tabla 20
    ET.SubElement(emi, "EMI_2").text = NitEmisor #NIT del emisor
    ET.SubElement(emi, "EMI_3").text = "31" ##Tabla identificacion 31NIT tabla 3
    ET.SubElement(emi, "EMI_4").text = "10" #
    ET.SubElement(emi, "EMI_6").text = razonSocialEmisor #Razón Social de la empresa Emisor
    ET.SubElement(emi, "EMI_7").text = nombreComercialEmisor #Nombre Comercial de la empresa Emisor
    ET.SubElement(emi, "EMI_10").text = direccionEmisor #Direccion
    ET.SubElement(emi, "EMI_11").text = codigoDepartamento #Codigo del Dapartamento Table 34
    ET.SubElement(emi, "EMI_13").text = nombreCiudad #Nombre de la Ciudad  Table 35
    ET.SubElement(emi, "EMI_15").text = "CO" #Código del País (Tabla 1)
    ET.SubElement(emi, "EMI_19").text = nombreDepartamento #Nombre del Departamento (Tabla 34)
    ET.SubElement(emi, "EMI_22").text = digitoVerificador #Digito Verificador
    ET.SubElement(emi, "EMI_23").text = codigoMunicipio  #Código del Municipio (Tabla 35)
    ET.SubElement(emi, "EMI_24").text = razonSocialEmisor #Nombre registrado en RUT

    #Cretae and append TAC Element informacion Tributaria Aduanera y Cambiaria
    tac = ET.SubElement(emi, "TAC")
    ET.SubElement(tac, "TAC_1").text = "O-23" # Los códigos validos O-13, O-15, O-23, O-47, R-99-PN

    #Cretae and append DFE información del Emisor Electrónico del Documento
    DFEE = ET.SubElement(emi, "DFE")
    ET.SubElement(DFEE, "DFE_1").text = codigoMunicipio #
    ET.SubElement(DFEE, "DFE_2").text = codigoDepartamento #
    ET.SubElement(DFEE, "DFE_3").text = 'CO' # CodigoPais
    ET.SubElement(DFEE, "DFE_4").text = CodigoPostal  # CodigoPostal
    ET.SubElement(DFEE, "DFE_5").text = nombrePais  #
    ET.SubElement(DFEE, "DFE_6").text = nombreDepartamento  #
    ET.SubElement(DFEE, "DFE_7").text = nombreCiudad  #
    ET.SubElement(DFEE, "DFE_8").text = "Lo mejor de Medellin"  #Texto Libre

    #Create and append the ICC element Información del Emisor Electrónico del Documento
    icc = ET.SubElement(emi, "ICC")
    ET.SubElement(icc, "ICC_1").text = numeroMatriculaMercantilEmi  #Numero de Matricula Mercantil
    ET.SubElement(icc, "ICC_9").text = prefijoFE

    #Create and append the CDE element Información del Emisor Electrónico del Documento
    cde = ET.SubElement(emi, "CDE")
    ET.SubElement(cde, "CDE_1").text = '1'  #Tipo de contacto (1-Persona de Contacto,2-Despacho ,3-Contabilidad ,4-Ventas
    ET.SubElement(cde, "CDE_2").text = personaContacto  #Nombre y Cargo de la Persona de Contacto
    ET.SubElement(cde, "CDE_3").text = movilContacto
    ET.SubElement(cde, "CDE_4").text = mailContacto

    #Create and append the GTE element Información del Emisor Electrónico del Documento
    gte = ET.SubElement(emi, "GTE")
    ET.SubElement(gte, "GTE_1").text = '01'  # Identificador del Tributo (Tabla 11
    ET.SubElement(gte, "GTE_2").text = 'IVA'  # Nombre del Tributo (Tabla 11)


    # Create and append the ADQ element
    adq = ET.SubElement(root, "ADQ")
    ET.SubElement(adq, "ADQ_1").text = "2" #Tipo de Identificación (Tabla 20) Nota: Para personas naturales (2) al definir ADQ_1=2 se necesitará definir ADQ_8 y 9 y ADQ_24
    ET.SubElement(adq, "ADQ_2").text = nitConsumidorFinal #Nit Adquiriente 222222222222
    ET.SubElement(adq, "ADQ_3").text = '13' #Tipo de documento de Identificación (Tabla 3)
    ET.SubElement(adq, "ADQ_4").text = '48' #Por averiguar
    ET.SubElement(adq, "ADQ_6").text = nombreAdquiriente #Razón Social*
    ET.SubElement(adq, "ADQ_7").text = nombreAdquiriente  #Consumidor
    ET.SubElement(adq, "ADQ_8").text = nombreAdquiriente #Final
    ET.SubElement(adq, "ADQ_9").text = nombreAdquiriente #Final
    ET.SubElement(adq, "ADQ_10").text =DireccionFisica  #Dirección del Adquiriente
    ET.SubElement(adq, "ADQ_11").text =codigoDepartamento  #Código del Departamento (Tabla 34)
    ET.SubElement(adq, "ADQ_13").text =nombreCiudad #
    ET.SubElement(adq, "ADQ_14").text =CodigoPostal  #
    ET.SubElement(adq, "ADQ_15").text =codigoPais  #
    ET.SubElement(adq, "ADQ_19").text =nombreDepartamento #
    ET.SubElement(adq, "ADQ_21").text =nombrePais #
    ET.SubElement(adq, "ADQ_23").text =codigoMunicipio #
    ET.SubElement(adq, "ADQ_24").text ='1' #Por averiguar

    #Create and append the TCR element Información Tributaria
    tcr = ET.SubElement(adq, "TCR")
    ET.SubElement(tcr, "TCR_1").text = 'R-99-PN'  #Información Tributaria. Los códigos validos O-13, O-15, O-23, O-47, R-99-PN listados a continuación

    #Create and append the ILA element Grupo de Información Legal del Adquiriente
    ila = ET.SubElement(adq, "ILA")
    ET.SubElement(ila, "ILA_1").text = 'final'  #Nombre registrado en el RUT (Razón Social)
    ET.SubElement(ila, "ILA_2").text = nitConsumidorFinal  #Identificación del Adquiriente
    ET.SubElement(ila, "ILA_3").text = '13'  #Tipo de Identificación fiscal de la Persona(Tabla 3)

    #Create and append the DFA element Dirección Física del Adquiriente
    dfa = ET.SubElement(adq, "DFA")
    ET.SubElement(dfa, "DFA_1").text = codigoPais
    ET.SubElement(dfa, "DFA_2").text =codigoDepartamento
    ET.SubElement(dfa, "DFA_3").text = CodigoPostal
    ET.SubElement(dfa, "DFA_4").text = codigoMunicipio
    ET.SubElement(dfa, "DFA_5").text = nombrePais
    ET.SubElement(dfa, "DFA_6").text = nombreDepartamento
    ET.SubElement(dfa, "DFA_7").text = nombreCiudad
    ET.SubElement(dfa, "DFA_8").text = "Somos Clientes Responsables" #Texto Libre

    #Create and append the ICR element Información de la Cámara de Comercio
    icr = ET.SubElement(adq, "ICR")
    ET.SubElement(icr, "ICR_1").text = numeroMatriculaMercantilAdq

    #Create and append the CDA element Información del Adquiriente
    cda = ET.SubElement(adq, "CDA")
    ET.SubElement(cda, "CDA_1").text ='1' #Tipo de Contacto
    ET.SubElement(cda, "CDA_2").text ='CARLOS MARIO CARDONA' #Nombre y Cargo de la Persona de Contacto
    ET.SubElement(cda, "CDA_3").text ='3168368181' #Teléfono de la Persona de Contacto
    ET.SubElement(cda, "CDA_4").text ='carloscardona@outlook.com' #Correo Electrónico de la Persona de Contacto

    #Create and append the GTA element  Detalles Tributarios del Adquiriente
    gta = ET.SubElement(adq, "GTA")
    ET.SubElement(gta, "GTA_1").text = '01'  # Identificador del Tributo (Tabla 11)
    ET.SubElement(gta, "GTA_2").text = 'IVA'  # Nombre del Tributo (Tabla 11)

    # Create and append the TOTALES  element  Detalles TOTALES DE LA FACTURA
    totales = ET.SubElement(root, "TOT")
    ET.SubElement(totales, "TOT_1").text=str(dictTotals['base'])
    ET.SubElement(totales, "TOT_2").text = currencyType
    ET.SubElement(totales, "TOT_3").text = str(dictTotals['base'])
    ET.SubElement(totales, "TOT_4").text = currencyType
    ET.SubElement(totales, "TOT_5").text = totalFactura
    ET.SubElement(totales, "TOT_6").text = currencyType
    ET.SubElement(totales, "TOT_7").text = str(dictTotals['base'] + dictTotals['impuestos'])
    ET.SubElement(totales, "TOT_8").text = currencyType
    ET.SubElement(totales, "TOT_9").text = '0.00'
    ET.SubElement(totales, "TOT_10").text = currencyType
    ET.SubElement(totales, "TOT_11").text = '0.00'
    ET.SubElement(totales, "TOT_12").text = currencyType

    #TAGS TIM de Informacion de Impuestos IVA19 e IC08
    i=0
    for strImpuesto, dictLineas  in dictGroups.items():
        sumaImpuestos=0
        sumaBases=0
        for lineas,lineasImpuesto in dictLineas.items():
                sumaImpuestos= sumaImpuestos + lineasImpuesto['impuesto']
                sumaBases = sumaBases + lineasImpuesto[ 'base' ]
        if (sumaImpuestos and sumaBases > 0): # Los impuestos globales IVA19 and IC08 deben tener valor > en Base e Impuesto, para que no se genere error
            i +=1
            labelTIM = 'TIM' + str(i)
            labelTIM = ET.SubElement(root, "TIM")
            ET.SubElement(labelTIM, "TIM_1").text = 'false'  # True: Retencion, false:Impuesto
            ET.SubElement(labelTIM, "TIM_2").text = str(round(sumaImpuestos,2))  # Suma de todos los IMP_4 con Impuestos(IMP_1)
            ET.SubElement(labelTIM, "TIM_3").text = currencyType  # Tipo de Moneda (Ver Tabla 13)
            #ET.SubElement(labelTIM, "TIM_4").text = strImpuesto + ' DEBUG' # Temporal solo para DEBUG

            #TAG IMP, Si Hubiera IVAs con diferente tarifa O VARIOS IC con diferente tarifa aplicaría varios IMP's pero nosotros solo usamos IVA19, por tango aplica un sólo IMP.
            labelIMP= 'IMP' + str(i)
            labelIMP = ET.SubElement(labelTIM, "IMP")
            IMP1='01' if strImpuesto=='IVA19' else '02'
            IMP6 = '19.00' if strImpuesto == 'IVA19' else '8.00'
            ET.SubElement(labelIMP,'IMP_1').text = IMP1 #Tipo de Retencion(Tabla 44) 01:IVA, 02:IC
            ET.SubElement(labelIMP, 'IMP_2').text = str(sumaBases) #Base Imponible (Suma de todos las bases a nivel Item (IIM_4), TAG mas abajo Hijo de ITEMS)
            ET.SubElement(labelIMP, 'IMP_3').text = currencyType # Tipo de Moneda
            ET.SubElement(labelIMP, 'IMP_4').text = str(sumaImpuestos)  #  Impuesto (Suma de todos las bases a nivel Item (IIM_4)*Impuesto en común (IMP_6)/100)
            ET.SubElement(labelIMP, 'IMP_5').text = currencyType     # Tipo de Moneda
            ET.SubElement(labelIMP, 'IMP_6').text = IMP6 # Tarifa del Tributo* (Porcentaje)



    # Create and append the DRF element  Datos de Resolucion de Facturacion
    datosResolucion = ET.SubElement(root, "DRF")

    ET.SubElement(datosResolucion, "DRF_1").text = numeroAutorizacion  # Número de Autorización
    ET.SubElement(datosResolucion, "DRF_2").text = FechaIniAutorizacion  #Fecha de Inicio Periodo de Autorizacion
    ET.SubElement(datosResolucion, "DRF_3").text = FechaFinAutorizacion #Fecha de Fin  Periodo de Autorizacion
    ET.SubElement(datosResolucion, "DRF_4").text = prefijoFE
    ET.SubElement(datosResolucion, "DRF_5").text = facturaInicial #Rango de Numeración (Mínimo)
    ET.SubElement(datosResolucion, "DRF_6").text = facturaFinal #Rango de Numeración (Maximo)

    medioPago = ET.SubElement(root, "MEP")
    ET.SubElement(medioPago, "MEP_1").text='10'  #Medio de Pago (Tabla 5) 7:Debito, 10:Efectivo
    ET.SubElement(medioPago, "MEP_2").text = '1' #Método de Pago (Tabla 26) * 1:Contado, 2:credito
    ET.SubElement(medioPago, "MEP_3").text = str_utctimedate #Fecha de Pago *

    #TAGS ITE  de Informacion de Base e Impuestos para cada Item Vendido
    i=1
    for strImpuesto, dictLineas  in dictGroups.items():
        for lineas,lineasInfoFiscal in dictLineas.items():
            IIM1 = '01' if strImpuesto == 'IVA19' else '02'
            IIM6 = '19.00' if strImpuesto == 'IVA19' else '8.00'
            labelITEM= 'labelITEM' + str(i)
            labelITEM = ET.SubElement(root, "ITE")
            ET.SubElement(labelITEM,"ITE_1").text = str(i)  #Número de Item
            ET.SubElement(labelITEM,"ITE_3").text = '1.0000'  #Cantidad de Producto
            ET.SubElement(labelITEM,"ITE_4").text = '94'  #Unidad de Medida de los bienes
            ET.SubElement(labelITEM,"ITE_5").text = str(lineasInfoFiscal['base'])  #COSTO_TOTAL (ITE_5= (ITE 27*ITE_7)-Descuentos a nivel Ítem (IDE) +Cargos a nivel Ítem (IDE)
            ET.SubElement(labelITEM,"ITE_6").text = currencyType  #Tipo de Moneda
            ET.SubElement(labelITEM,"ITE_7").text = str(lineasInfoFiscal['base'])  #Precio Unitario
            ET.SubElement(labelITEM,"ITE_8").text = currencyType  #Tipo de Moneda
            ET.SubElement(labelITEM,"ITE_11").text = lineas  #Descripción
            ET.SubElement(labelITEM,"ITE_19").text = str(lineasInfoFiscal['base'])  #Total del ítem (incluyendo Descuentos y cargos) * (ITE_19 = (ITE 27*ITE_7)-Descuentos a nivel Ítem (IDE) +Cargos a nivel Ítem (IDE))
            ET.SubElement(labelITEM,"ITE_20").text = currencyType  #Tipo de Moneda*
            ET.SubElement(labelITEM,"ITE_21").text = str(lineasInfoFiscal['base']+lineasInfoFiscal['impuesto'])   #Valor a Pagar del Item* (ITE_21= ITE_19+Suma de todos los Impuestos (IIM_2) a nivel Ítem)
            ET.SubElement(labelITEM,"ITE_22").text = currencyType  #Tipo de Moneda*
            ET.SubElement(labelITEM,"ITE_23").text = str(lineasInfoFiscal['base'])  #Precio Unitario
            ET.SubElement(labelITEM,"ITE_24").text = currencyType  #Tipo de Moneda*
            ET.SubElement(labelITEM,"ITE_27").text = '1'  #La cantidad real sobre la cual el precio aplica
            ET.SubElement(labelITEM,"ITE_28").text = '94'  #Unidad de medida de la cantidad del artículo solicitado
            i +=1

            # Create and append tag IAE son of ITE element  información Especifica del Artículo
            infoItem= 'infoITEM' + str(i)
            infoItem = ET.SubElement(labelITEM, "IAE")
            ET.SubElement(infoItem, "IEA_1").text = 'LINEAXYZ DEBUG'  # Codigo del Item  Custom Value
            ET.SubElement(infoItem, "IEA_2").text = '999'  # Codigo del estandar 999:Estandaar de Adopcion del Cotribuyente

            # Create and append tag TII  SON  of ITE element  Total de retenciones del Item
            infoRetenciones= 'infoRETENCIONES' + str(i)
            infoRetenciones = ET.SubElement(labelITEM, "TII")
            ET.SubElement(infoRetenciones, "TII_1").text = str(lineasInfoFiscal['base'])  # (IIM_4 * IIM_6)/100
            ET.SubElement(infoRetenciones, "TII_2").text = currencyType   # Tipo de Moneda
            ET.SubElement(infoRetenciones, "TII_3").text = 'false'  # Bandera de Impuesto o Retención (true-retención/false-impuesto)

            # Create and append tag IIM  SON  of TII element  Total de Retenciones del Item
            infoTaxSingle= 'infoTaxSingle' + str(i)
            infoTaxSingle = ET.SubElement(infoRetenciones, "IIM")
            ET.SubElement(infoTaxSingle, "IIM_1").text = IIM1  #  Tipo de Retención (Tabla 44) 01:IVA, 02:IC
            ET.SubElement(infoTaxSingle, "IIM_2").text = str(lineasInfoFiscal['impuesto'])   # Retención ((IIM_4*IIM_6) /100)
            ET.SubElement(infoTaxSingle, "IIM_3").text = currencyType  #  Tipo de Moneda
            ET.SubElement(infoTaxSingle, "IIM_4").text = str(lineasInfoFiscal['base'])  # Base Imponible (Igual a ITE_5)
            ET.SubElement(infoTaxSingle, "IIM_5").text = currencyType  # Tipo de Moneda
            ET.SubElement(infoTaxSingle, "IIM_6").text = IIM6  # Tarifa del Tributo*(Porcentaje)

    # Create an ElementTree object
    tree = ET.ElementTree(root)
    # Write the XML to a file
    with open(xmlfile, "wb") as xml_file:
        tree.write(xml_file)

    #print(f"XML file ' {xmlfile} ' has been generated.'")
