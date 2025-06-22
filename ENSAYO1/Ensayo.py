# Clase base que representa material bibliográfico
class MaterialBibliografico:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_info(self):
        print(f"{self.titulo} - {self.autor}")

# Subclase que representa un libro
class Libro(MaterialBibliografico):
    def __init__(self, titulo, autor, genero):
        super().__init__(titulo, autor)
        self.genero = genero

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Género: {self.genero}")

# Subclase que representa una revista
class Revista(MaterialBibliografico):
    def __init__(self, titulo, autor, categoria):
        super().__init__(titulo, autor)
        self.categoria = categoria

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Categoría: {self.categoria}")

# Creación de objetos y demostración de interacción
libro = Libro("El Señor de los Anilloss", "J.R.R. Tolkien", "Fantasía")
revista = Revista("National Geographic", "AMY", "Ciencia")

libro.mostrar_info()
print()  # Línea en blanco para separar salidas
revista.mostrar_info()
