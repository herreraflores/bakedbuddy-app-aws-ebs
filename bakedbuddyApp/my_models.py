import requests, json

class Dispensary:
   
    # initializer
    def __init__(self, id, name='', profile_picture='', formatted_address='', formatted_phone_number='', website_url='', shopping_url='', verified = '', deals={}, daily_deals=[], deal_image='', deal_image2=''):
        self.id = id
        self.name = name
        self.profile_picture = profile_picture
        self.formatted_address = formatted_address
        self.formatted_phone_number = formatted_phone_number
        self.website_url = website_url
        self.shopping_url = shopping_url
        self.verified = verified

        self.deals = deals
        self.daily_deals = daily_deals
        self.deal_image = deal_image
        self.deal_image2 = deal_image2

    # Should be called get_info() or something since it provides everything
    def get_daily_deals(self):
        # Mary Mart
        if(self.id == "ChIJ1YZBHBlVkFQRQ5O4VNr-D9A"):

            self.name = 'Mary Mart'
            self.profile_picture = 'https://www.marymart.com/wp-content/uploads/2019/03/mary_mart_tacoma_store_front_sign-copy.jpg'

            daily_deal_monday = "Electric Early Bird - 20% off all online orders from 8am-12pm. \n Monday Happy Hours - 15% off the entire store from 12pm-3pm and 8pm-11pm"
            daily_deal_tuesday = "Tuesday Happy Hours - 15% off the entire store from 11am-2pm and 8pm-11pm"
            daily_deal_wednesday = "Ladies Day - All ladies receive 10% off"
            daily_deal_thursday = "Valued Citizens Day - All patrons 55+ receive 10% off"
            daily_deal_friday = "TGIF Bulk Friday - 15% off all bulk flower (7g-28g)"
            daily_deal_saturday = "Smoke Em' Saturday - 15% off all prerolls. Saturday Shatterday - 10% off all concentrates"
            daily_deal_sunday = "Sunday Funday - 20% off all paraphernalia and 10% off the entire store"
            self.daily_deals = [daily_deal_monday, daily_deal_tuesday, daily_deal_wednesday, daily_deal_thursday, daily_deal_friday, daily_deal_saturday, daily_deal_sunday]

            self.shopping_url = "https://shop.marymart.com/tacoma"
            self.website_url = 'https://www.marymart.com/'

            self.deal_image = 'https://cdn-eonge.nitrocdn.com/GuEuOIaqeTQvgBimjToPhXKDVcJlnJAb/assets/static/optimized/rev-c1b828f/wp-content/uploads/2022/04/420DayDeals_site_deals.png'
            self.deal_image2 = ''

            self.verified = 'Yes'

        # Commencement Bay Red
        if(self.id == "ChIJCb1jgAz_kFQRTYvay73_j4o"):
            self.name = 'Commencement Bay Red'
            self.profile_picture = 'https://leafly-production.imgix.net/https%3A%2F%2Fleafly-public.s3-us-west-2.amazonaws.com%2Fdispensary%2Flogos%2FvgAyEa2ORfOX1opbcbAW_IMG_8381.JPG?ixlib=js-2.3.2&dpr=1&w=1100&h=750&fit=fillmax&s=b0c7ab6c3408d781981ac362d8ade25f'
           
            daily_deal_monday = 'Monday Funday - 20% Off Storewide'
            daily_deal_tuesday = 'Triple Point Tuesday'
            daily_deal_wednesday = 'Weight Wednesday 15% Off 7g+ 30% Off 28g 30% off 7g Of Concentrate'
            daily_deal_thursday = 'Thank You Thursday - 15% Off Online Orders'
            daily_deal_friday = 'Fire Friday - 20% Off Select Vendors'
            daily_deal_saturday = 'Shatterday 15% Off Concentrate 30% Off 7g Concentrate'
            daily_deal_sunday = 'Super Joint Sunday 15% Off Pre-Rolls'
            self.daily_deals = [daily_deal_monday, daily_deal_tuesday, daily_deal_wednesday, daily_deal_thursday, daily_deal_friday, daily_deal_saturday, daily_deal_sunday]

            self.shopping_url = 'https://commencementbaycannabis.com/cbc-red/menu/?'
            self.website_url = 'https://commencementbaycannabis.com/#'

        # Zips Cannabis Downtown
        if(self.id == "ChIJ4fhYtHtVkFQRxoUEFMXJKHo"):
            self.name = 'Zips Cannabis Downtown'
            self.profile_picture = 'https://potguide.com/remote.axd?https://images.potguide.com/store/3031/Aap_uEBHnWOmAfeqemtH6S-L4oY-VkORPaWw.jpg?format=png'
           
            daily_deal_monday = ''
            daily_deal_tuesday = ''
            daily_deal_wednesday = ''
            daily_deal_thursday = ''
            daily_deal_friday = ''
            daily_deal_saturday = ''
            daily_deal_sunday = ''
            self.daily_deals = [daily_deal_monday, daily_deal_tuesday, daily_deal_wednesday, daily_deal_thursday, daily_deal_friday, daily_deal_saturday, daily_deal_sunday]

            self.shopping_url = 'https://www.zipscannabis.com/zips-downtown-online-ordering?dtche%5Bpath%5D=specials'

        # Zips Cannabis 72nd
        if(self.id == "ChIJLzIIW3VVkFQR8sm0i81SRjw"):
            self.name = 'Zips Cannabis 72nd'
            self.profile_picture = 'https://images.squarespace-cdn.com/content/v1/5b9fd91336099b969b6c499c/1596770419550-U2P969PXOYZZPC9Y5NAT/ke17ZwdGBToddI8pDm48kLhqQcy1sZUR6ignFY6WqdB7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1UVM7bPfbv1epoe6yov4uNvThBZR2cpIgf6hX-FliLr73W7bEWgRPz2kW2jjIbE5sTw/Zips-Cannabis-Tacoma-72nd-street.jpg'
           
            daily_deal_monday = ''
            daily_deal_tuesday = ''
            daily_deal_wednesday = ''
            daily_deal_thursday = ''
            daily_deal_friday = ''
            daily_deal_saturday = ''
            daily_deal_sunday = ''
            self.daily_deals = [daily_deal_monday, daily_deal_tuesday, daily_deal_wednesday, daily_deal_thursday, daily_deal_friday, daily_deal_saturday, daily_deal_sunday]

            self.shopping_url = 'https://www.zipscannabis.com/zips-cannabis-on-72nd-online-ordering?dtche%5Bpath%5D=specials'

        # Zips Cannabis 106
        if(self.id == "ChIJBWwQaesBkVQR0pkGhe9B4us"):
            self.name = 'Zips Cannabis 106'
            self.profile_picture = 'https://images.squarespace-cdn.com/content/v1/5b9fd91336099b969b6c499c/1628718629307-GKUU3BM289WH1NDN87FE/Zips-Cannabis-106th_SMALL.jpg'
           
            daily_deal_monday = ''
            daily_deal_tuesday = ''
            daily_deal_wednesday = ''
            daily_deal_thursday = ''
            daily_deal_friday = ''
            daily_deal_saturday = ''
            daily_deal_sunday = ''
            self.daily_deals = [daily_deal_monday, daily_deal_tuesday, daily_deal_wednesday, daily_deal_thursday, daily_deal_friday, daily_deal_saturday, daily_deal_sunday]

            self.shopping_url = 'https://www.zipscannabis.com/zips-106th-online-ordering?'

        # Commencement Bay Cannabis - Green
        if(self.id == 'ChIJWYIYSAn_kFQRJdIBdZRd7Bo'):
            self.name = 'Commencement Bay Cannabis - Green'
            self.profile_picture = 'https://commencementbaycannabis.com/wp-content/uploads/2020/10/commencement-bay-cannabis-logo-trimmed-green.png'

            daily_deal_monday = 'Mega Monday- 15% Off 7g Of Flower 30% Off 28g Of Flower'
            daily_deal_tuesday = 'Turnt up Tuesday - 20% Off Storewide'
            daily_deal_wednesday = 'Waxy Wednesday - 20% Off Cartridges & Concentrates'
            daily_deal_thursday = '3 Times Thursday - 3x Loyalty Points & 30% Off Select Vendor '
            daily_deal_friday = 'Fire Friday - 20% Off Top Shelf Flower'
            daily_deal_saturday = 'Satisfaction Saturday - 30% Off Edibles & Select Vendor'  
            daily_deal_sunday = 'Smokin Sunday- 15% Off Flower & Pre-Rolls'
            self.daily_deals = [daily_deal_monday, daily_deal_tuesday, daily_deal_wednesday, daily_deal_thursday, daily_deal_friday, daily_deal_saturday, daily_deal_sunday]

            self.shopping_url = 'https://www.zipscannabis.com/zips-106th-online-ordering?'
            self.website_url = 'https://commencementbaycannabis.com/#'


        # Bloom Cannabis - Tacoma
        if(self.id == "ChIJDYZvzewBkVQRz5QUPemLQZ4"):
            self.name = 'Bloom Cannabis - Tacoma'
            self.profile_picture = 'https://pbs.twimg.com/profile_images/1027225946623959040/Tzo4pgVI_400x400.jpg'

            daily_deal_monday = '25% OFF the Whole Store'
            daily_deal_tuesday = '30% OFF All Flower'
            daily_deal_wednesday = '30% OFF All Concentrates'   
            daily_deal_thursday = '30 OFF All Vape Cartridges'
            daily_deal_friday = '30% OFF All Flower 25% OFF the Rest of the Store'
            daily_deal_saturday = '30% OFF All Pre-Rolls 30 OFF All Concentrates'
            daily_deal_sunday = '30 OFF All Half & Full Ounces 25% OFF All Online Orders'
            self.daily_deals = [daily_deal_monday, daily_deal_tuesday, daily_deal_wednesday, daily_deal_thursday, daily_deal_friday, daily_deal_saturday, daily_deal_sunday]

            self.shopping_url = 'https://www.bloomcannabis.com/bloom-tacoma-store?dtche%5Bpath%5D=specials'
            self.website_url = 'https://www.bloomcannabis.com/bloom-tacoma-store?'

        # The PotZone
        if(self.id == "ChIJU-7nFC3-kFQRVG8USx9Cw-o"):
            self.name = 'The PotZone'
            self.profile_picture = 'https://s3-media0.fl.yelpcdn.com/bphoto/o2ffTgdznrIo5r_emmiilQ/l.jpg'

            daily_deal_monday = ''
            daily_deal_tuesday = ''
            daily_deal_wednesday = ''
            daily_deal_thursday = ''
            daily_deal_friday = ''
            daily_deal_saturday = ''
            daily_deal_sunday = ''
            self.daily_deals = [daily_deal_monday, daily_deal_tuesday, daily_deal_wednesday, daily_deal_thursday, daily_deal_friday, daily_deal_saturday, daily_deal_sunday]

            self.shopping_url = 'https://www.potzone420.com/potzone-tacoma-order-online'

        # Clear Choice
        if(self.id == "ChIJpWiBwzUAkVQREYMUlK1Rd2w"):
            self.name = 'Clear Choice'
            self.profile_picture = 'https://www.colorhexa.com/4895ef.png'

            daily_deal_monday = 'Save 20% on select products!'
            daily_deal_tuesday = 'Save 20% Select Prerolls & Edibles'
            daily_deal_wednesday = 'Save 25% Spotlight Vendor Changing  Weekly'
            daily_deal_thursday = 'Save 25% One Brand from each category'
            daily_deal_friday = 'Save 30% storewide'
            daily_deal_saturday = 'Save up to 25% when you stack items every Saturday'
            daily_deal_sunday = 'Select Vendors 30% OFF 15% OFF Storewide'
            self.daily_deals = [daily_deal_monday, daily_deal_tuesday, daily_deal_wednesday, daily_deal_thursday, daily_deal_friday, daily_deal_saturday, daily_deal_sunday]


            self.shopping_url = 'https://www.findclearchoice.com/menu/'
            self.shopping_url = 'https://www.findclearchoice.com/'

        # The Joint - Tacoma
        if(self.id == "ChIJD4bXs3tVkFQRjPmYwFEOsfU"):
            self.name = 'The Joint - Tacoma'
            self.profile_picture ='https://thejointllc.com/wp-content/uploads/2021/06/Tacoma-Dispensary-The-Joint-1.png'

            daily_deal_monday = ''
            daily_deal_tuesday = ''
            daily_deal_wednesday = ''
            daily_deal_thursday = ''
            daily_deal_friday = ''
            daily_deal_saturday = ''
            daily_deal_sunday = ''
            self.daily_deals = [daily_deal_monday, daily_deal_tuesday, daily_deal_wednesday, daily_deal_thursday, daily_deal_friday, daily_deal_saturday, daily_deal_sunday]


            self.shopping_url = 'https://thejointllc.com/tacoma-online-ordering/'

        # Herbal Garden
        if(self.id == "ChIJRTg1hMmqkVQRfMfPrsobM5c"):
            self.name = 'Herbal Garden'
            self.profile_picture ='https://s3-media0.fl.yelpcdn.com/bphoto/c5EEbrb0evvRMunxxjb7Ag/l.jpg'

            daily_deal_monday = ''
            daily_deal_tuesday = ''
            daily_deal_wednesday = ''
            daily_deal_thursday = ''
            daily_deal_friday = ''
            daily_deal_saturday = ''
            daily_deal_sunday = ''
            self.daily_deals = [daily_deal_monday, daily_deal_tuesday, daily_deal_wednesday, daily_deal_thursday, daily_deal_friday, daily_deal_saturday, daily_deal_sunday]


            self.shopping_url = 'https://herbalgardens.org/tacoma-dispensary-menu/#/'

        # House of Cannabis
        if(self.id == "ChIJn26xI1VVkFQRSzNdccEl_mM"):
            self.name = 'House of Cannabis'
            self.profile_picture ='data:image/png;base64,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'

            daily_deal_monday = ''
            daily_deal_tuesday = ''
            daily_deal_wednesday = ''
            daily_deal_thursday = ''
            daily_deal_friday = ''
            daily_deal_saturday = ''
            daily_deal_sunday = ''
            self.daily_deals = [daily_deal_monday, daily_deal_tuesday, daily_deal_wednesday, daily_deal_thursday, daily_deal_friday, daily_deal_saturday, daily_deal_sunday]


            self.shopping_url = 'https://tacomahouseofcannabis.com/menu/?dtche%5Bpath%5D=specials'

        # 420 Tacoma RMD
        if(self.id == "ChIJRTg1hMmqkVQRfMfPrsobM5c"):
            self.name = '420 Tacoma RMD'
            self.profile_picture ='https://a.mktgcdn.com/p/tq8umr6iLlLoqKCcGiLRXO5C5KUHZfaWMAmkIDysWCQ/3160x1676.jpg'

            daily_deal_monday = ''
            daily_deal_tuesday = ''
            daily_deal_wednesday = ''
            daily_deal_thursday = ''
            daily_deal_friday = ''
            daily_deal_saturday = ''
            daily_deal_sunday = ''
            self.daily_deals = [daily_deal_monday, daily_deal_tuesday, daily_deal_wednesday, daily_deal_thursday, daily_deal_friday, daily_deal_saturday, daily_deal_sunday]


            self.shopping_url = 'https://420tacoma.com/menu/'

        # Green Token
        if(self.id == "ChIJx3ObRHILkVQRyKqAJDsZ6DM"):
            self.name = 'Green Token'
            self.profile_picture ='https://leafly-public.imgix.net/dispensary/logos/Z8MzOecaT99QHRYURAV5_green_token_cannabis_overview_logo_3.png'

            daily_deal_monday = ''
            daily_deal_tuesday = ''
            daily_deal_wednesday = ''
            daily_deal_thursday = ''
            daily_deal_friday = ''
            daily_deal_saturday = ''
            daily_deal_sunday = ''
            self.daily_deals = [daily_deal_monday, daily_deal_tuesday, daily_deal_wednesday, daily_deal_thursday, daily_deal_friday, daily_deal_saturday, daily_deal_sunday]


            self.shopping_url = 'https://mylocalroots.com/tacoma?dtche%5Bpath%5D=specials'

        # Diamond Green
        if(self.id == "ChIJM6uJ6T2WB0ERcfF36fi7J0o"):
            self.name = 'Diamond Green'
            self.profile_picture ='https://pbs.twimg.com/profile_images/890731448696676352/_0pfZAfb_400x400.jpg'

            daily_deal_monday = ''
            daily_deal_tuesday = ''
            daily_deal_wednesday = ''
            daily_deal_thursday = ''
            daily_deal_friday = ''
            daily_deal_saturday = ''
            daily_deal_sunday = ''
            self.daily_deals = [daily_deal_monday, daily_deal_tuesday, daily_deal_wednesday, daily_deal_thursday, daily_deal_friday, daily_deal_saturday, daily_deal_sunday]


            self.shopping_url = 'https://shop.diamondgreentacoma.com/tacoma'

        # Emerald Leaves
        if(self.id == "ChIJmS_ihBlVkFQRQDAyP01sASc"):
            self.name = 'Emerald Leaves'
            self.profile_picture ='https://i.ibb.co/Fbqg9qT/Untitled.jpg'

            daily_deal_monday = 'Monday - 20% off the entire store'
            daily_deal_tuesday = 'Tuesday - 25% off all flower'
            daily_deal_wednesday = 'Wednesday - 30% off cards and concentrates'
            daily_deal_thursday = 'Thursday - 25% off online orders'
            daily_deal_friday = 'Friday - 25% off all flower'
            daily_deal_saturday = 'Saturday - 20% off entire store and 30% off Oz'
            daily_deal_sunday = 'Sunday - 25% off all flower and prerolls'
            self.daily_deals = [daily_deal_monday, daily_deal_tuesday, daily_deal_wednesday, daily_deal_thursday, daily_deal_friday, daily_deal_saturday, daily_deal_sunday]


            self.shopping_url = 'https://emeraldleavestacoma.com/order-online/?'
            self.website_url = 'https://emeraldleavestacoma.com/'

            self.deal_image = 'https://emeraldleavestacoma.com/wp-content/uploads/2022/01/swag-bag-vertical.jpg'
            self.deal_image2 = 'https://emeraldleavestacoma.com/wp-content/uploads/2022/04/20-off-entire-store_2048-1024x1024.jpg'

        # World of Weed
        if(self.id == "ChIJ-WfszH7_kFQR1yRfQBrkfB4"):
            self.name = 'World of Weed'
            self.profile_picture ='https://www.worldofweed.com/wp-content/uploads/2015/08/Exterior-Store-Front-Photo-of-World-of-Weed-Tacoma-WA-500x375.jpg'

            daily_deal_monday = ''
            daily_deal_tuesday = ''
            daily_deal_wednesday = ''
            daily_deal_thursday = ''
            daily_deal_friday = ''
            daily_deal_saturday = ''
            daily_deal_sunday = ''
            self.daily_deals = [daily_deal_monday, daily_deal_tuesday, daily_deal_wednesday, daily_deal_thursday, daily_deal_friday, daily_deal_saturday, daily_deal_sunday]


            self.shopping_url = 'https://shop.worldofweed.com/tacoma'
       
        # Commencement Bay Cannabis - Yellow
        if(self.id == "ChIJWZ25UEz_kFQRP3Te2-gkINU"):
            self.name = 'Commencement Bay Cannabis - Yellow'
            self.profile_picture ='https://leafly-public.imgix.net/dispensary/logos/gHqGlndfSumdlgaa9kZ0_Fife%20Front%20of%20Store.jpg?auto=compress,format&w=350&dpr=2'

            daily_deal_monday = ''
            daily_deal_tuesday = ''
            daily_deal_wednesday = ''
            daily_deal_thursday = ''
            daily_deal_friday = ''
            daily_deal_saturday = ''
            daily_deal_sunday = ''
            self.daily_deals = [daily_deal_monday, daily_deal_tuesday, daily_deal_wednesday, daily_deal_thursday, daily_deal_friday, daily_deal_saturday, daily_deal_sunday]


            self.shopping_url = 'https://commencementbaycannabis.com/cbc-yellow/menu/?'


    

