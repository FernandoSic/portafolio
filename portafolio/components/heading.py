import reflex as rx
from portafolio.styles.styles import Size


def heading(text: str, h1=False) -> rx.Component:
    return rx.heading(
        text,
        as_="h1" if h1 else "h2",
        size=Size.BIG.value if h1 else Size.MEDIUM.value,
        font_size="clamp(18px, 4vw, 32px)" if h1 else "clamp(16px, 3vw, 24px)"
    )
