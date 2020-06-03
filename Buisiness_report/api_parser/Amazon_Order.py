import datetime

class Amazon_Order:
    def __init__(self, order_to_be_parsed, dictionary):
        self.order_to_be_parsed = order_to_be_parsed
        self.dictionary = dictionary

        self.name = self.get_name()
        self.firstline = self.get_first_line()
        self.second_line = self.get_seconde_line()
        self.city_line = self.get_city_line()
        self.country = self.get_country()
        self.phone = self.get_phone()
        self.instruction, self.quantity = self.get_instruction()
        self.creation_date = self.get_creation_date()
        self.order_id = self.get_order_id()
        self.is_business_order = self.get_is_business()
        self.email = self.get_email()
        self.address = self.second_line + ' ' + self.city_line
        self.product_name, self.unity_price, self.shipping_price, self.total_Quantity, self.SKU = self.get_product_info()
        self.channel = 'Amazon'
    def get_tag_text(self, tag, possible_multi):
        if possible_multi: return self.order_to_be_parsed[self.dictionary[tag]] + '!'
        else: return self.order_to_be_parsed[self.dictionary[tag]]

    def choose_tag(self, tags, additional_str=None, possible_multi =False):
        for tag in tags:
            if tag in self.dictionary.keys() and self.get_tag_text(tag,possible_multi ) != '':
                if additional_str == None:
                    return self.get_tag_text(tag, possible_multi)
                else:
                    print(self.get_tag_text(tag, possible_multi))
                    return additional_str + ' ' + self.get_tag_text(tag, possible_multi)
        return ''

    def get_name(self):
        #Civility = self.choose_tag([Shipping_Civility_tag, Civility_tag, Customer_Civility_tag])
        Name = self.choose_tag(['recipient-name', 'buyer-name'])
        FirstName = Name.split(' - ')[0]
        FirstLine = ''.join(Name.split(' -')[1:])
        #LastName = self.choose_tag([Shipping_LastName_tag, LastName_tag, Customer_LastName_tag])
        return FirstName.title()

    def get_first_line(self):
        Name = self.choose_tag(['recipient-name', 'buyer-name'])
        FirstLine = ''.join(Name.split(' -')[1:])[1:]
        Address2 = self.choose_tag(['ship-address-2'])
        Address3 = self.choose_tag(['ship-address-3'])
        if FirstLine == '':
            return Address2.title() + Address3.title()
        else:
            return FirstLine.title() + ' ' + Address2.title() + Address3.title()

    def get_seconde_line(self):
        Address1 = self.choose_tag(['ship-address-1'])

        return Address1.title()

    def get_city_line(self):
        Zip = self.choose_tag(['ship-postal-code'])
        City = self.choose_tag(['ship-city', 'ship-state'])
        State = self.choose_tag(['ship-state'])
        Country = self.choose_tag(['ship-country'])
        return Zip + ' ' + City.title() + ' ' + State.title() + ' (' + Country + ')'

    def get_phone(self):
        Phone = self.choose_tag(['ship-phone-number', 'buyer-phone-number'])
        return Phone

    def get_instruction(self):

        Product_name = self.choose_tag(['product-name'], possible_multi=True)[-80:]
        Quantity = self.choose_tag(['quantity-purchased'], possible_multi=True)


        return  Product_name , Quantity

    def get_creation_date(self):
        CreationDate = self.choose_tag(['purchase-date'])
        CreationDate = datetime.datetime.strptime(CreationDate[:-3], '%Y-%m-%dT%H:%M:%S+%f')
        return CreationDate

    def get_order_id(self):
        OrderID = self.choose_tag(['order-id'])
        return OrderID

    def get_is_business(self):
        Is_business = self.choose_tag(['is-business-order'])
        return Is_business

    def get_email(self):
        email = self.choose_tag(['buyer-email'])
        return email
    def get_country(self):
        country = self.choose_tag(['ship-country'])
        return country

    def get_product_info(self):
        Product_name = self.choose_tag(['product-name'])
        Unity_price = self.choose_tag(['item-price'])
        Shipping_price = self.choose_tag(['shipping-price'])
        Total_Quantity = self.choose_tag(['quantity-purchased'])
        SKU = self.choose_tag(['sku'])

        return Product_name, Unity_price, Shipping_price, Total_Quantity, SKU