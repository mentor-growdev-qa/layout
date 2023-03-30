@objects
    image               css     #__next > div > div > section.about-two > div > div > div.col-xl-6.d-flex.justify-content-xl-end.justify-content-sm-center > div > img
    title               css     #__next > div > div > section.about-two > div > div > div:nth-child(1) > div > div.block-title.text-left > h2
    description         css     #__next > div > div > section.about-two > div > div > div:nth-child(1) > div > p
    first_card_text     css     #__next > div > div > section.about-two > div > div > div:nth-child(1) > div > div.about-two__single-wrap > div:nth-child(1) > div.about-two__single-content > p
    first_card_icon     css     #__next > div > div > section.about-two > div > div > div:nth-child(1) > div > div.about-two__single-wrap > div:nth-child(1) > div.about-two__single-icon > img
    second_card_text    css     #__next > div > div > section.about-two > div > div > div:nth-child(1) > div > div.about-two__single-wrap > div:nth-child(2) > div.about-two__single-content > p
    second_card_icon    css     #__next > div > div > section.about-two > div > div > div:nth-child(1) > div > div.about-two__single-wrap > div:nth-child(2) > div.about-two__single-icon > img
    button              css     #__next > div > div > section.about-two > div > div > div:nth-child(1) > div > a


= Growdev Page =
    @on desktop
        image:
            width 529px
            height 529px
        title:
            css font-family starts "Poppins"
            css font-size is "60px"
            css font-weight is "bold"
            css line-height is "1.2"
            css color is "rgba(43, 56, 91, 1)"
            above description 20px
        description:
            css font-family starts "Poppins"
            css font-size is "18px"
            css font-weight is "400"
            css line-height is "36px"
            css color is "rgba(129, 134, 138, 1)"
        second_card_text:
            css font-family starts "Poppins"
            css font-size is "20px"
            css font-weight is "500"
            css line-height is "34px"
            css color is "rgba(43, 56, 91, 1)"
        second_card_icon:
            width 64px
            height 64px
            css padding-right is "15px"
            left-of second_card_text 15px
        button:
            css font-family starts "Poppins"
            css font-size is "15px"
            css font-weight is "bold"
            css line-height is "34px"
            css color is "rgba(255, 255, 255, 1)"
            css background-color is "rgba(225, 110, 14, 1)"