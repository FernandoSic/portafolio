import reflex as rx

from portafolio.styles.styles import EmSize


def icon_badge(icon: str) -> rx.Component:
    try:
        ic = rx.icon(icon, size=32)
    except ValueError:
        # Fallback to a safe default icon when the provided tag is invalid
        ic = rx.icon("activity", size=32)

    return rx.badge(
        ic,
        aspect_ratio="1",
        variant="soft"
    )
