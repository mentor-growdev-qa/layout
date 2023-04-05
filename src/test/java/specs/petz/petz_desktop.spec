@import petz_mobile.spec
@import petz_tablet.spec

@objects
    input_busca             css         #search
    nav_cachorros           css         #navbar-collapse-grid > div > ul:nth-child(1) > li.dropdown.dropdown-dog.yamm-fw.x > a
    nav_gatos               css         #navbar-collapse-grid > div > ul:nth-child(1) > li.dropdown.dropdown-cat.x.yamm-fw.show > a
    nav_passaros            css         #navbar-collapse-grid > div > ul:nth-child(1) > li:nth-child(3) > a
    nav_peixes              css         #navbar-collapse-grid > div > ul:nth-child(1) > li:nth-child(4) > a
    nav_outros_pets         css         #navbar-collapse-grid > div > ul:nth-child(1) > li:nth-child(5) > a
    button_recebimento      css         #homeAdvantages > div > button:nth-child(1)
    button_freteGratis      css         #homeAdvantages > div > button:nth-child(2)
    button_parcelamento     css         #homeAdvantages > div > button:nth-child(3)
    button_retirenaloja     css         #homeAdvantages > div > button:nth-child(4)
@groups
    navs nav_cachorros, nav_gatos, nav_passaros, nav_peixes, nav_outros_pets
    buttons button_recebimento, button_freteGratis, button_parcelamento, button_retirenaloja
= Loja Petz =
    @on desktop
        input:
            css background-color  #fff;
            color: #747474;
            height: auto;
            width: 100%;
            padding: .75rem 3rem .75rem 1rem;
            line-height: 21px;
            font-size: 14px;
            font-weight: 400;