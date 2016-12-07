from xml.dom import minidom
from XMLInvoice import XMLInvoice, XMLItem

def main(filename):

    invoice = XMLInvoice()

    document = minidom.parse(filename)
    comprobante = document.getElementsByTagName("comprobante")
    xmlStringFactura = comprobante[0].childNodes[0].data
    xmlFactura = minidom.parseString(xmlStringFactura)

    invoice.number = xmlFactura.getElementsByTagName("secuencial")[0].childNodes[0].data
    print invoice.number

    totalConImpuestos = xmlFactura.getElementsByTagName("totalImpuesto")
    for totalImpuesto in totalConImpuestos:
        tarifa = totalImpuesto.getElementsByTagName("tarifa")[0].childNodes[0].data
        base = totalImpuesto.getElementsByTagName("baseImponible")[0].childNodes[0].data
        if tarifa == "0.0":
            invoice.subtotalNoVAT = base
        else:
            invoice.subtotalVAT = base


    invoice.VAT = xmlFactura.getElementsByTagName("totalImpuestoReembolso")[0].childNodes[0].data

    print invoice.subtotalNoVAT
    print invoice.subtotalVAT
    print invoice.VAT

    #create invoice

    #get number



if __name__ == '__main__':
    f = "D:/myScripts/InvoiceXML/samples/0712201601099137022600120080030000062560072974512.xml"
    main(f)