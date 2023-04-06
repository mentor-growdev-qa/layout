@import petz_mobile.spec
@import petz_tablet.spec

@objects
    input                   css         #search
    nav_cachorros           css         #navbar-collapse-grid > div > ul:nth-child(1) > li.dropdown.dropdown-dog.yamm-fw.x > a
    nav_gatos               css         #navbar-collapse-grid > div > ul:nth-child(1) > li.dropdown.dropdown-cat.x.yamm-fw > a
    nav_passaros            css         #navbar-collapse-grid > div > ul:nth-child(1) > li:nth-child(3) > a
    nav_peixes              css         #navbar-collapse-grid > div > ul:nth-child(1) > li:nth-child(4) > a
    nav_outros_pets         css         #navbar-collapse-grid > div > ul:nth-child(1) > li:nth-child(5) > a
    button_recebimento      css         #homeAdvantages > div > button:nth-child(1)
    button_freteGratis      css         #homeAdvantages > div > button:nth-child(2)
    button_parcelamento     css         #homeAdvantages > div > button:nth-child(3)
    button_retirenaloja     css         #homeAdvantages > div > button:nth-child(4)
@groups
    navs        nav_cachorros, nav_gatos, nav_passaros, nav_peixes, nav_outros_pets
    buttons     button_recebimento, button_freteGratis, button_parcelamento, button_retirenaloja
= Loja Petz =
    @on desktop
        input:
            css background-color is "rgba(255, 255, 255, 1)"
            css color is "rgba(116, 116, 116, 1)"
            css line-height is "21px"
            css font-size is "14px"
            css font-weight is "400"
            css border-radius is "5px"
            css font-family starts "CircularXX"
    @on desktop
        &navs:
            css font-family starts "CircularXX"
            css font-size is "14px"
            css font-weight is "700"
            css line-height is "20px"
            css color is "rgba(23, 94, 168, 1)"
        &buttons:
            css font-family starts "CircularXX"
            css font-size is "16px"
            css font-weight is "700"
            css line-height is "34px"
            css color is "rgba(23, 94, 168, 1)"
            css background-color is "rgba(245, 245, 245, 1)"