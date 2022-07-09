from django.shortcuts import render, HttpResponse

# Create your views here.


def inicio(request):
    msn = """
            <h1>Universidad Nacional Tecnológica de Lima Sur</h1>
            <strong> EP Ingeniería de Sistemas </strong>
            <p>Bienvenidos</p>
    
    """
    return HttpResponse(msn)


def uc3(request):
    msn = """
            <h1>Lenguaje de Programación III</h1>
            <strong> Evaluación de la Unidad de Competencia 3 </strong>
            <p>Docente: Mg. Flor Elizabeth Cerdán León</p>
            <p>Integrantes: </p>
            <ul>
                <li>Azañero Espinoza, Waldir Ysaí</li>
                <li>Díaz Seminario, Daniel Omar</li>
                <li>Rodriguez Mejia José Jean Piere</li>
            </ul>
    """
    return HttpResponse(msn)


def noticia(request):
    msn = """
            <h1>Empresario Zamir Villaverde saldrá en libertad: juez cambia prisión preventiva por comparecencia</h1>
            <p>El empresario Zamir Villaverde saldrá en libertad, luego que el Poder Judicial decidió variar su orden de prisión preventiva por una de comparecencia con restricciones con impedimento de salida del país, confirmaron fuentes cercanas a la defensa legal del investigado.</p>
    
    """
    return HttpResponse(msn)
