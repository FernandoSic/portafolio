import reflex as rx
from portafolio.components.icon_button import icon_button
from portafolio.data import Media
from portafolio.styles.styles import Size


def media(data: Media) -> rx.Component:
    return rx.flex(
        icon_button(
            "mail",
            f"mailto:{data.email}",
            data.email,
            True,
            width=["100%", "100%", "auto"]
        ),
        rx.flex(
            icon_button(
                "file-text",
                data.cv,
                text="CV",
                width=["100%", "100%", "auto"]
            ),
            icon_button(
                "github",
                data.github,
                text="GitHub",
                width=["100%", "100%", "auto"]
            ),
            icon_button(
                "linkedin",
                data.likedin,
                text="LinkedIn",
                width=["100%", "100%", "auto"]
            ),
            spacing=Size.SMALL.value,
            flex_direction=["column", "column", "row"],
            width="100%",
            flex_wrap="wrap"
        ),
        spacing=Size.SMALL.value,
        flex_direction=["column", "column", "row"],
        width="100%",
        align_items="stretch"
    )
