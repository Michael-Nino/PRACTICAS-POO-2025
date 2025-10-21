"""
DESARROLLO 3: Builder en Python - Generador de Documentos PDF
(EJERCICIO NUEVO - NO es el ejemplo del PDF de computadoras)
"""


class DocumentoPDF:
    def __init__(self):
        self.titulo = ""
        self.autor = ""
        self.capitulos = []
    
    def mostrar(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"\nCapitulos:")
        for cap in self.capitulos:
            print(f"  - {cap}")


class PDFBuilder:
    def __init__(self):
        self.documento = DocumentoPDF()
    
    def set_titulo(self, titulo):
        self.documento.titulo = titulo
        return self
    
    def set_autor(self, autor):
        self.documento.autor = autor
        return self
    
    def agregar_capitulo(self, capitulo):
        self.documento.capitulos.append(capitulo)
        return self
    
    def build(self):
        return self.documento


def main():
    print("=== DESARROLLO 3: BUILDER - PDF ===\n")
    
    # Construir documento
    builder = PDFBuilder()
    documento = (builder
                 .set_titulo("Manual de Python")
                 .set_autor("Juan Perez")
                 .agregar_capitulo("Capitulo 1: Introduccion")
                 .agregar_capitulo("Capitulo 2: Variables")
                 .agregar_capitulo("Capitulo 3: Funciones")
                 .build())
    
    documento.mostrar()


if __name__ == "__main__":
    main()

"""
EJECUTAR: python3 desarrollo3_builder_pdf.py
"""

from typing import List, Optional, Tuple
from datetime import datetime


class DocumentoPDF:
    """Clase producto - documento PDF complejo"""
    
    def __init__(self):
        self.titulo: Optional[str] = None
        self.autor: Optional[str] = None
        self.fecha: Optional[str] = None
        self.portada: Optional[dict] = None
        self.indice: bool = False
        self.capitulos: List[dict] = []
        self.imagenes: List[dict] = []
        self.tablas: List[dict] = []
        self.bibliografia: List[str] = []
        self.pie_pagina: Optional[str] = None
        self.numeracion: bool = True
        self.tamanio_fuente: int = 12
        self.margenes: Tuple[int, int, int, int] = (2, 2, 2, 2)  # top, right, bottom, left
    
    def generar(self) -> str:
        """Genera una representación del PDF"""
        pdf = []
        pdf.append("="*70)
        pdf.append("📄 DOCUMENTO PDF GENERADO")
        pdf.append("="*70)
        
        # Portada
        if self.portada:
            pdf.append("\n┌" + "─"*68 + "┐")
            pdf.append("│" + " "*68 + "│")
            pdf.append("│" + self.portada.get('titulo', '').center(68) + "│")
            pdf.append("│" + " "*68 + "│")
            pdf.append("│" + self.portada.get('subtitulo', '').center(68) + "│")
            pdf.append("│" + " "*68 + "│")
            pdf.append("│" + f"Autor: {self.portada.get('autor', '')}".center(68) + "│")
            pdf.append("│" + f"{self.portada.get('fecha', '')}".center(68) + "│")
            pdf.append("│" + " "*68 + "│")
            pdf.append("└" + "─"*68 + "┘")
        
        # Metadatos
        pdf.append(f"\n📋 METADATOS:")
        if self.titulo:
            pdf.append(f"   Título: {self.titulo}")
        if self.autor:
            pdf.append(f"   Autor: {self.autor}")
        if self.fecha:
            pdf.append(f"   Fecha: {self.fecha}")
        pdf.append(f"   Fuente: {self.tamanio_fuente}pt")
        pdf.append(f"   Márgenes: {self.margenes} cm")
        
        # Índice
        if self.indice and self.capitulos:
            pdf.append(f"\n📑 ÍNDICE:")
            for i, cap in enumerate(self.capitulos, 1):
                pdf.append(f"   {i}. {cap['titulo']} ..................... pág. {i*5}")
        
        # Capítulos
        if self.capitulos:
            pdf.append(f"\n📖 CONTENIDO:")
            for i, cap in enumerate(self.capitulos, 1):
                pdf.append(f"\n{'─'*70}")
                pdf.append(f"CAPÍTULO {i}: {cap['titulo']}")
                pdf.append(f"{'─'*70}")
                pdf.append(f"{cap['contenido']}")
                if self.numeracion:
                    pdf.append(f"\n{' '*60}Página {i*5}")
        
        # Imágenes
        if self.imagenes:
            pdf.append(f"\n🖼️  IMÁGENES ({len(self.imagenes)}):")
            for img in self.imagenes:
                pdf.append(f"   - {img['nombre']}: {img['descripcion']}")
        
        # Tablas
        if self.tablas:
            pdf.append(f"\n📊 TABLAS ({len(self.tablas)}):")
            for tabla in self.tablas:
                pdf.append(f"   - Tabla: {tabla['titulo']}")
        
        # Bibliografía
        if self.bibliografia:
            pdf.append(f"\n📚 BIBLIOGRAFÍA:")
            for i, ref in enumerate(self.bibliografia, 1):
                pdf.append(f"   [{i}] {ref}")
        
        # Pie de página
        if self.pie_pagina:
            pdf.append(f"\n{'─'*70}")
            pdf.append(f"{self.pie_pagina.center(70)}")
        
        pdf.append("\n" + "="*70)
        pdf.append(f"✅ Documento generado: {len(self.capitulos)} capítulos, "
                  f"{len(self.imagenes)} imágenes, {len(self.tablas)} tablas")
        pdf.append("="*70)
        
        return "\n".join(pdf)


class DocumentoPDFBuilder:
    """Builder para construir documentos PDF paso a paso"""
    
    def __init__(self):
        self.documento = DocumentoPDF()
    
    def set_titulo(self, titulo: str):
        """Establece el título del documento"""
        self.documento.titulo = titulo
        return self
    
    def set_autor(self, autor: str):
        """Establece el autor"""
        self.documento.autor = autor
        return self
    
    def set_fecha(self, fecha: str = None):
        """Establece la fecha (por defecto hoy)"""
        self.documento.fecha = fecha or datetime.now().strftime("%d/%m/%Y")
        return self
    
    def crear_portada(self, titulo: str, subtitulo: str = "", autor: str = "", fecha: str = ""):
        """Crea una portada personalizada"""
        self.documento.portada = {
            'titulo': titulo,
            'subtitulo': subtitulo,
            'autor': autor or self.documento.autor,
            'fecha': fecha or self.documento.fecha
        }
        return self
    
    def incluir_indice(self, incluir: bool = True):
        """Incluye o no un índice"""
        self.documento.indice = incluir
        return self
    
    def agregar_capitulo(self, titulo: str, contenido: str):
        """Agrega un capítulo"""
        self.documento.capitulos.append({
            'titulo': titulo,
            'contenido': contenido
        })
        return self
    
    def agregar_imagen(self, nombre: str, descripcion: str):
        """Agrega una referencia a imagen"""
        self.documento.imagenes.append({
            'nombre': nombre,
            'descripcion': descripcion
        })
        return self
    
    def agregar_tabla(self, titulo: str):
        """Agrega una referencia a tabla"""
        self.documento.tablas.append({
            'titulo': titulo
        })
        return self
    
    def agregar_bibliografia(self, referencia: str):
        """Agrega una referencia bibliográfica"""
        self.documento.bibliografia.append(referencia)
        return self
    
    def set_pie_pagina(self, texto: str):
        """Establece el pie de página"""
        self.documento.pie_pagina = texto
        return self
    
    def set_formato(self, fuente: int = 12, numeracion: bool = True):
        """Configura formato del documento"""
        self.documento.tamanio_fuente = fuente
        self.documento.numeracion = numeracion
        return self
    
    def set_margenes(self, top: int, right: int, bottom: int, left: int):
        """Configura márgenes (en cm)"""
        self.documento.margenes = (top, right, bottom, left)
        return self
    
    def build(self) -> DocumentoPDF:
        """Construye y retorna el documento final"""
        return self.documento


class DirectorDocumentos:
    """Director que conoce recetas para tipos comunes de documentos"""
    
    @staticmethod
    def tesis_universitaria() -> DocumentoPDF:
        """Construye estructura de tesis universitaria"""
        return (DocumentoPDFBuilder()
                .set_titulo("Aplicación de Patrones de Diseño en Sistemas Empresariales")
                .set_autor("Juan Pérez Mamani")
                .set_fecha("Octubre 2025")
                .crear_portada(
                    titulo="APLICACIÓN DE PATRONES DE DISEÑO\nEN SISTEMAS EMPRESARIALES",
                    subtitulo="Tesis para optar el título de Ingeniero de Sistemas",
                    autor="Bach. Juan Pérez Mamani",
                    fecha="Puno - 2025"
                )
                .incluir_indice(True)
                .set_formato(fuente=12, numeracion=True)
                .set_margenes(3, 2, 2, 3)
                .agregar_capitulo(
                    "INTRODUCCIÓN",
                    "Los patrones de diseño son soluciones probadas a problemas comunes "
                    "en el desarrollo de software. En este trabajo se analiza su aplicación "
                    "en sistemas empresariales."
                )
                .agregar_capitulo(
                    "MARCO TEÓRICO",
                    "El Gang of Four (GoF) identificó 23 patrones de diseño fundamentales, "
                    "clasificados en: Creacionales, Estructurales y de Comportamiento."
                )
                .agregar_capitulo(
                    "METODOLOGÍA",
                    "Se implementaron 9 patrones en un sistema real de gestión empresarial "
                    "usando Python y C++."
                )
                .agregar_tabla("Comparación de Patrones Creacionales")
                .agregar_imagen("diagrama_uml_singleton.png", "Diagrama UML del patrón Singleton")
                .agregar_bibliografia("Gamma, E. et al. (1994). Design Patterns. Addison-Wesley.")
                .agregar_bibliografia("Fowler, M. (2002). Patterns of Enterprise Application Architecture.")
                .set_pie_pagina("Universidad Nacional del Altiplano - Escuela de Ingeniería de Sistemas")
                .build())
    
    @staticmethod
    def informe_tecnico() -> DocumentoPDF:
        """Construye estructura de informe técnico"""
        return (DocumentoPDFBuilder()
                .set_titulo("Informe Técnico de Implementación")
                .set_autor("Equipo de Desarrollo")
                .set_fecha()
                .incluir_indice(True)
                .agregar_capitulo(
                    "RESUMEN EJECUTIVO",
                    "Implementación exitosa de sistema de notificaciones multi-canal."
                )
                .agregar_capitulo(
                    "DETALLES TÉCNICOS",
                    "Stack tecnológico: Python 3.11, PostgreSQL, Redis, Docker."
                )
                .agregar_tabla("Métricas de rendimiento")
                .set_pie_pagina("Confidencial - Uso interno")
                .build())
    
    @staticmethod
    def manual_usuario() -> DocumentoPDF:
        """Construye estructura de manual de usuario"""
        return (DocumentoPDFBuilder()
                .set_titulo("Manual de Usuario - Sistema POO II")
                .set_autor("Departamento de TI")
                .crear_portada("MANUAL DE USUARIO", "Sistema de Gestión Académica v2.0")
                .incluir_indice(True)
                .set_formato(fuente=11, numeracion=True)
                .agregar_capitulo(
                    "INTRODUCCIÓN",
                    "Bienvenido al sistema de gestión académica. Este manual le guiará "
                    "en el uso de todas las funcionalidades."
                )
                .agregar_capitulo(
                    "PRIMEROS PASOS",
                    "1. Ingrese con su usuario y contraseña\n"
                    "2. Seleccione el módulo deseado\n"
                    "3. Complete los formularios"
                )
                .agregar_imagen("pantalla_login.png", "Pantalla de inicio de sesión")
                .agregar_imagen("pantalla_principal.png", "Dashboard principal")
                .build())


def main():
    print("="*70)
    print("DESARROLLO 3: BUILDER - CONSTRUCTOR DE DOCUMENTOS PDF")
    print("="*70)
    print()
    
    # Caso 1: Usando el Director para crear tesis
    print("1️⃣  USANDO DIRECTOR - Tesis Universitaria\n")
    tesis = DirectorDocumentos.tesis_universitaria()
    print(tesis.generar())
    
    input("\n[Presiona ENTER para continuar...]")
    
    # Caso 2: Usando el Director para informe técnico
    print("\n\n2️⃣  USANDO DIRECTOR - Informe Técnico\n")
    informe = DirectorDocumentos.informe_tecnico()
    print(informe.generar())
    
    input("\n[Presiona ENTER para continuar...]")
    
    # Caso 3: Construcción personalizada sin Director
    print("\n\n3️⃣  CONSTRUCCIÓN PERSONALIZADA - Reporte de Investigación\n")
    reporte = (DocumentoPDFBuilder()
               .set_titulo("Patrón Singleton en Aplicaciones Web")
               .set_autor("María González")
               .set_fecha("20/10/2025")
               .incluir_indice(False)
               .agregar_capitulo(
                   "Análisis del Patrón",
                   "El patrón Singleton garantiza una única instancia, "
                   "útil para gestores de configuración y conexiones a BD."
               )
               .agregar_capitulo(
                   "Implementación en Python",
                   "Se puede implementar usando __new__ o decoradores."
               )
               .agregar_bibliografia("Python Design Patterns - Brandon Rhodes")
               .build())
    
    print(reporte.generar())


if __name__ == "__main__":
    main()


"""
EJECUTAR:
python3 desarrollo3_builder_pdf.py

DIFERENCIAS CON EL EJEMPLO DEL PDF:
- El PDF construye Computadora (cpu, ram, gpu)
- Este desarrollo construye DocumentoPDF (mucho más complejo)
- Tiene 12+ atributos configurables vs 3 del ejemplo
- Incluye Director con 3 tipos de documentos predefinidos
- Genera salida visual formateada
- Más realista para aplicaciones empresariales

CARACTERÍSTICAS:
✅ Method chaining completo
✅ Director con recetas predefinidas
✅ Construcción paso a paso
✅ Objeto complejo (portada, índice, capítulos, bibliografía)
✅ Parámetros opcionales
✅ Generación de salida visual
"""
