import cgi
def htmlTop():
    print(""" Content-type:text/html \n\n 
            <!DOCTYPE html>
            <html lang="en-US">
            <html>

            <head> 
            <title>Physiotherapy Clinic and Rehabilitation</title>
            <meta charset="utf-8" /> <meta name="description" content="Physiotherapy clinic and Rehabilitation">
            </head>
            <body>           """)

def htmlTail():
    print("""</body>
            </html """")


def getData():
    formData=cgi.FieldStorage()
    name=formData.getvalue('name')
    return name

#main program
if _name_=="_main_":
    try:
        htmlTop()    
        name = getData()
        print("Hello World")
        print("Hello".format(name))
        htmlTail()
    except:
        cgi.print_exception()    