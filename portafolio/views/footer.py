import reflex as rx
from portafolio.components.media import media
from portafolio.data import Media
from portafolio.styles.styles import Size


def footer(data: Media) -> rx.Component:
    return rx.vstack(
        rx.text("Fernando José Nicolás Sic Saquic © 2025"),
        media(data),
        spacing=Size.SMALL.value,
        align_items="center",
        text_align="center",
        width="100%"
    )
