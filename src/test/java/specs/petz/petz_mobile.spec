@objects
    input                   css         #oldSearch
    nav_dogs                css         #categoryBarHome > ul > li:nth-child(1) > a > span
    image_dogs              css         #categoryBarHome > ul > li:nth-child(1) > a > div
    nav_cats                css         #categoryBarHome > ul > li.category-item.skin > a > span
    image_cats              css         #categoryBarHome > ul > li.category-item.skin > a > div
    nav_birds               css         #categoryBarHome > ul > li.category-item.green > a > div
    image_birds             css         #categoryBarHome > ul > li.category-item.green > a > span
    first_card              css         #homeAdvantagesMobile > div > div > button:nth-child(1)
    first_card_image        css         #homeAdvantagesMobile > div > div > button:nth-child(1) > img
    first_card_title        css         #homeAdvantagesMobile > div > div > button:nth-child(1) > div > p
    first_card_link         cs          #homeAdvantagesMobile > div > div > button:nth-child(1) > div > span
    second_card             css         #homeAdvantagesMobile > div > div > button:nth-child(2)
    second_card_image       css         #homeAdvantagesMobile > div > div > button:nth-child(2) > img
    second_card_title       css         #homeAdvantagesMobile > div > div > button:nth-child(2) > div > p
    second_card_link        css         #homeAdvantagesMobile > div > div > button:nth-child(2) > div > span
    third_card              css         #homeAdvantagesMobile > div > div > button:nth-child(3)
    third_card_image        css         #homeAdvantagesMobile > div > div > button:nth-child(3) > img
    third_card_title        css         #homeAdvantagesMobile > div > div > button:nth-child(3) > div > p
    third_card_link         css         #homeAdvantagesMobile > div > div > button:nth-child(3) > div > span
    fourth_card             css         #homeAdvantagesMobile > div > div > button:nth-child(4)
    fourth_card_image       css         #homeAdvantagesMobile > div > div > button:nth-child(4) > img
    fourth_card_title       css         #homeAdvantagesMobile > div > div > button:nth-child(4) > div > p
    fourth_card_link        css         #homeAdvantagesMobile > div > div > button:nth-child(4) > div > span

@groups
    cards           first_card, second_card, third_card, fourth_card
    cards_images    first_card_image, second_card_image, third_card_image, fourth_card_image
    cards_titles    first_card_title, second_card_title, third_card_title, fourth_card_title
    cards_links     first_card_link, second_card_link, third_card_link, fourth_card_link
    images          image_dogs, image_cats, image_birds
    navs            nav_cats, nav_birds, nav_dogs

= Petz Mobile =
    @on mobile
        input:
            css background-color is "rgba(255, 255, 255, 1)"
            css color is "rgba(116, 116, 116, 1)"
            css line-height is "21px"
            css font-size is "14px"
            css font-weight is "400"
            css border-radius is "5px"
            css font-family starts "CircularXX"
        &cards:
            css background-color is "rgba(245, 245, 245, 1)"
            css border-radius is ".25rem"
            height 82px
            css width is "44%"
        &cards_images:
        &cards_titles:
        &cards_links: