
def crearReporteErroes(listaErrores):
    txt = '''
    <html>
        <head><title> Reporte Errores </title></head>
            <body>
                <div align="center">
                    <h1> Reporte Errores</h1>
                        <br></br>
                            <table border=1>
                                <tr>
                                    <td>Descripcion</td>
                                    <td>Linea</td>
                                    <td>Columna</td>
                                    <td>Tipo</td>
                                </tr>                
    '''

    for err in listaErrores:
        txt+= "<tr>"
        txt+= "<td>"+ err.descripcion+ "</td>"
        txt+= "<td>"+ str(err.linea)+ "</td>"
        txt+= "<td>"+ str(err.columna)+ "</td>"
        txt+= "<td>"+ err.tipo+ "</td>"
        txt+= "</tr>"
    
    txt+= "</table>\n</div>\n</body>\n</html>"

    try:

        with open("reporteErrores.html", "w") as file:
            file.write(txt)
            file.close() 

    except:
        print("No se pudo crear el Reporte Errores")

def crearReporteTablaSimbolos(ts):
    txt = '''
    <html>
        <head><title> Reporte Tabla Simbolos </title></head>
            <body>
                <div align="center">
                    <h1> Reporte Tabla Simbolos</h1>
                        <br></br>
                            <table border=1>
                                <tr>
                                    <td>Id</td>
                                    <td>Tipo</td>
                                    <td>Tipo Dato</td>
                                    <td>Valor</td>
                                    <td>Ambito</td>
                                    <td>Linea</td>
                                    <td>Columna</td>
                                </tr>                
    '''

    for simbol in ts.simbolos:
        txt+= "<tr>"
        txt+= "<td>"+ simbol.id+ "</td>"
        if simbol.tipo_simbolo == 2:
            txt+= "<td> Funcion</td>"
        else:
            txt+= "<td> Variable</td>"
        if simbol.tipo ==1:
            txt+= "<td> Number</td>"
        elif simbol.tipo==2:
            txt+= "<td> Float</td>"
        elif simbol.tipo==3:
            txt+= "<td> Cadena</td>"
        elif simbol.tipo==4:
            txt+= "<td> Boolean</td>"
        elif simbol.tipo==5:
            txt+= "<td> Char</td>"
        elif simbol.tipo==6:
            txt+= "<td> Void</td>"

        txt+= "<td>"+ simbol.ambito+ "</td>"
        txt+= "<td>"+ str(simbol.linea)+ "</td>"
        txt+= "<td>"+ str(simbol.columna)+ "</td>"
        txt+= "</tr>"
    
    txt+= "</table>\n</div>\n</body>\n</html>"

    try:

        with open("reporteTS.html", "w") as file:
            file.write(txt)
            file.close() 

    except:
        print("No se pudo crear el Reporte TS")