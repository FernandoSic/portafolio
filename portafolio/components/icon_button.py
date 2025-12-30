import reflex as rx


def icon_button(icon: str, url: str, text: str = "", solid: bool = False, width: str | None = None) -> rx.Component:
    """Button-like link with optional width for mobile layouts."""

    return rx.link(
        rx.button(
            rx.icon(icon),
            text,
            variant="solid" if solid else "surface",
            width=width,
            justify="center"
        ),
        href=url,
        is_external=True,
        width=width
    )
