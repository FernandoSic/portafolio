import reflex as rx
from portafolio.components.icon_badge import icon_badge
from portafolio.components.icon_button import icon_button
from portafolio.data import Info
from portafolio.styles.styles import IMAGE_HEIGHT, IMAGE_WIDTH, EmSize, Size


def info_detail(info: Info) -> rx.Component:
    return rx.flex(
        
        rx.hstack(
            icon_badge(info.icon),
            rx.vstack(
                rx.text.strong(info.title),
                rx.text(info.subtitle),
                rx.cond(
                    info.date != "",
                    rx.badge(info.date, color_scheme="gray", variant="soft")
                ),
                rx.text(
                    info.description,
                    size=Size.SMALL.value,
                    color_scheme="gray"
                ),
                rx.cond(
                    len(info.technologies) > 0,
                    rx.flex(
                        *[
                            rx.badge(
                                rx.box(class_name=technology.icon),
                                technology.name,
                                color_scheme="gray",
                                size="1"
                            )
                            for technology in info.technologies
                        ],
                        wrap="wrap",
                        spacing=Size.SMALL.value,
                        row_gap=Size.SMALL.value
                    )
                ),
                rx.hstack(
                    rx.cond(
                        info.url != "",
                        icon_button(
                            "link",
                            info.url,
                            text="Ir a la aplicación",
                            width=["100%", "auto"]
                        ),
                    ),
                    rx.cond(
                        info.github != "",
                        icon_button(
                            "github",
                            info.github,
                            text="Código",
                            width=["100%", "auto"]
                        )
                    ),
                    rx.cond(
                        info.certificate != "",
                        icon_button(
                            "shield-check",
                            info.certificate,
                            solid=True,
                            width=["100%", "auto"]
                        )
                    ),
                    spacing=Size.SMALL.value,
                    width="100%",
                    flex_wrap="wrap"
                ),
                spacing=Size.SMALL.value,
                width="100%"
            ),
            spacing=Size.DEFAULT.value,
            align_items="flex-start",
            width="100%"
        ),
        rx.cond(
            info.image != "",
            rx.image(
                src=info.image,
                height=IMAGE_HEIGHT,
                width="100%",
                max_width=IMAGE_WIDTH,
                border_radius=EmSize.DEFAULT.value,
                object_fit="cover"
            )
        ),
        flex_direction=["column", "row"],
        spacing=Size.DEFAULT.value,
        width="100%"
    )
