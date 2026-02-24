from rich.console import Console
from rich.panel import Panel

console = Console()

categorias_maquillaje = {
    "correctores": {
        "descripcion": "Productos usados para cubrir imperfecciones, ojeras y manchas en la piel.",
        "productos": [
            "NARS Radiant Creamy Concealer",
            "Maybelline Fit Me Concealer",
            "L.A. Girl Pro Conceal"
        ]
    },
    "blushes": {
        "descripcion": "Polvos o cremas que aportan color y vitalidad a las mejillas.",
        "productos": [
            "Milani Baked Blush",
            "MAC Powder Blush",
            "NYX Professional Blush"
        ]
    },
    "lip liner": {
        "descripcion": "Lápices diseñados para definir y dar forma a los labios antes del labial.",
        "productos": [
            "MAC Lip Pencil",
            "NYX Slim Lip Pencil",
            "Charlotte Tilbury Lip Cheat"
        ]
    },
    "gloss": {
        "descripcion": "Brillos labiales que aportan color y brillo a los labios.",
        "productos": [
            "Fenty Beauty Gloss Bomb",
            "NYX Butter Gloss",
            "Dior Addict Lip Maximizer"
        ]
    }
}

def mostrar_categoria(categoria):
    categoria_info = categorias_maquillaje.get(categoria.lower())
    
    if categoria_info:
        descripcion = categoria_info["descripcion"]
        productos = "\n".join(categoria_info["productos"])
        contenido = f"Descripción:\n{descripcion}\n\nProductos principales:\n{productos}"
        console.print(Panel(contenido, title=f"Categoría: {categoria.capitalize()}"))
    else:
        console.print("[red]Categoría no encontrada. Intenta con: correctores, blushes, lip liner o gloss.[/red]")

if __name__ == "__main__":
    console.print("[bold green]=== Generador de Productos de Maquillaje ===[/bold green]")
    categoria_usuario = input("Escribe una categoría: ")
    mostrar_categoria(categoria_usuario)