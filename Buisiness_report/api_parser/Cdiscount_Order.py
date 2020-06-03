import datetime
pre_tag = '{http://www.cdiscount.com}'
BillingAddress_tag = pre_tag + 'BillingAddress'
Address1_tag = BillingAddress_tag + '/' + pre_tag + 'Address1'
Address2_tag = BillingAddress_tag + '/' + pre_tag + 'Address2'
ApartmentNumber_tag = BillingAddress_tag + '/' + pre_tag + 'ApartmentNumber'
Building_tag = BillingAddress_tag + '/' + pre_tag + 'Building'
City_tag = BillingAddress_tag + '/' + pre_tag + 'City'
Civility_tag = BillingAddress_tag + '/' + pre_tag + 'Address2'
CompanyName_tag = BillingAddress_tag + '/' + pre_tag + 'CompanyName'
FirstName_tag = BillingAddress_tag + '/' + pre_tag + 'FirstName'
Instructions_tag = BillingAddress_tag + '/' + pre_tag + 'Instructions'
LastName_tag = BillingAddress_tag + '/' + pre_tag + 'LastName'
Street_tag = BillingAddress_tag + '/' + pre_tag + 'Street'
ZipCode_tag = BillingAddress_tag + '/' + pre_tag + 'ZipCode'
PlaceName_tag = BillingAddress_tag + '/' + pre_tag + 'PlaceName'
Country_tag = BillingAddress_tag + '/' + pre_tag + 'Country'

Customer_tag = pre_tag + 'Customer'
Customer_Civility_tag = Customer_tag + '/' + pre_tag + 'Civility'
Customer_FirstName_tag =Customer_tag + '/' +  pre_tag + 'FirstName'
Customer_LastName_tag = Customer_tag + '/' + pre_tag + 'LastName'
MobilePhone_tag = Customer_tag + '/' + pre_tag + 'MobilePhone'
Phone_tag = Customer_tag + '/' + pre_tag + 'Phone'
Email_tag = Customer_tag + '/' + pre_tag + 'Email'
EncriptedEmail_tag = Customer_tag + '/' + pre_tag + 'EncryptedEmail'

ShippingAddresse_tag = pre_tag + 'ShippingAddress'
Shipping_Address1_tag = ShippingAddresse_tag + '/' + pre_tag + 'Address1'
Shipping_Address2_tag = ShippingAddresse_tag + '/' + pre_tag + 'Address2'
Shipping_ApartmentNumber_tag = ShippingAddresse_tag + '/' + pre_tag + 'ApartmentNumber'
Shipping_Building_tag = ShippingAddresse_tag + '/' + pre_tag + 'Building'
Shipping_City_tag = ShippingAddresse_tag + '/' + pre_tag + 'City'
Shipping_Civility_tag = ShippingAddresse_tag + '/' + pre_tag + 'Address2'
Shipping_CompanyName_tag = ShippingAddresse_tag + '/' + pre_tag + 'CompanyName'
Shipping_FirstName_tag = ShippingAddresse_tag + '/' + pre_tag + 'FirstName'
Shipping_Instructions_tag = ShippingAddresse_tag + '/' + pre_tag + 'Instructions'
Shipping_LastName_tag = ShippingAddresse_tag + '/' + pre_tag + 'LastName'
Shipping_Street_tag = ShippingAddresse_tag + '/' + pre_tag + 'Street'
Shipping_ZipCode_tag = ShippingAddresse_tag + '/' + pre_tag + 'ZipCode'
Shipping_PlaceName_tag = ShippingAddresse_tag + '/' + pre_tag + 'PlaceName'
Shipping_Country_tag = ShippingAddresse_tag + '/' + pre_tag + 'Country'


OrderLineList_tag = pre_tag + 'OrderLineList'
OrderLine_tag = OrderLineList_tag + '/' + pre_tag + 'OrderLine'
Name_tag = OrderLine_tag + '/' + pre_tag + 'Name'
SellerProductId_tag = OrderLine_tag + '/' + pre_tag + 'SellerProductId'
Quantity_tag = OrderLine_tag + '/' + pre_tag + 'Quantity'
PurchasePrice_tag = OrderLine_tag + '/' + pre_tag +'PurchasePrice'
UnitShippingCharges_tag =  OrderLine_tag + '/' + pre_tag +'UnitShippingCharges'
UnitAdditionalShippingCharges_tag =  OrderLine_tag + '/' + pre_tag + 'UnitAdditionalShippingCharges'
Sku_tag = OrderLine_tag + '/'  + pre_tag  + 'Sku'

OrderCreation_tag = pre_tag  + 'CreationDate'
OrderNum_tag = pre_tag + 'OrderNumber'

class Cdiscount_Order:
    def __init__(self, order_to_be_parsed):
        self.order_to_be_parsed = order_to_be_parsed
        self.name = self.get_name()
        self.firstline = self.get_first_line()
        self.second_line = self.get_seconde_line()
        self.city_line = self.get_city_line()
        self.phone = self.get_phone()
        self.instruction, self.quantity = self.get_instruction()

        self.creation_date = self.get_creation_date()
        self.order_id = self.get_order_id()

        self.name = self.get_name()

        self.country = self.get_country()
        self.is_business_order = self.get_is_business()
        self.email = self.get_email()
        self.address = self.second_line + ' ' + self.city_line
        self.product_name, self.unity_price, self.shipping_price, self.total_Quantity, self.SKU = self.get_product_info()
        self.channel = 'Cdiscount'

    def get_tag_text(self, tag, possible_multi):
        texts = []
        for text in self.order_to_be_parsed.findall(tag):
            texts.append(text.text)
        texts = [tx for tx in texts if tx != None]
        if len(texts) == 1 and not possible_multi: return  texts[0]
        else: return ''.join(str(e) + '!' for e in texts)


    def choose_tag(self, tags, additional_str = None ,possible_multi =False):
        for tag in tags:
            if tag!= None and self.get_tag_text(tag, possible_multi) != None:
                if additional_str == None: return self.get_tag_text(tag,possible_multi)
                else: return additional_str + ' ' + self.get_tag_text(tag, possible_multi)
        return ''


    def get_name(self):
        Civility = self.choose_tag([Shipping_Civility_tag,Civility_tag, Customer_Civility_tag])
        FirstName = self.choose_tag([Shipping_FirstName_tag, FirstName_tag, Customer_FirstName_tag])
        LastName = self.choose_tag([Shipping_LastName_tag,LastName_tag, Customer_LastName_tag])
        return Civility.capitalize() + ' ' + FirstName.capitalize() + ' ' + LastName.capitalize()

    def get_first_line(self):
        Company = self.choose_tag([Shipping_CompanyName_tag])
        App = self.choose_tag([Shipping_ApartmentNumber_tag], 'APP')
        Build = self.choose_tag([Shipping_Building_tag], ' BAT')
        Instr = self.choose_tag([Shipping_Instructions_tag])
        return Company.capitalize() +  App  + Build + Instr

    def get_seconde_line(self):
        Street = self.choose_tag([Shipping_Street_tag, Street_tag, PlaceName_tag])
        return Street.title()

    def get_city_line(self):
        Zip = self.choose_tag([Shipping_ZipCode_tag, ZipCode_tag])
        City = self.choose_tag([Shipping_City_tag, City_tag])
        Country = self.choose_tag([Shipping_Country_tag, Country_tag])
        return Zip + ' ' + City.title() + ' (' + Country + ')'

    def get_phone(self):
        Phone = self.choose_tag([MobilePhone_tag, Phone_tag])
        return Phone

    def get_instruction(self):
        LastName = self.choose_tag([Customer_LastName_tag,LastName_tag])
        SellerProductId = self.choose_tag([SellerProductId_tag], possible_multi= True)
        Quantity = self.choose_tag([Quantity_tag], possible_multi= True)
        return LastName +'   '+ SellerProductId,  Quantity

    def get_creation_date(self):
        CreationDate = self.choose_tag([OrderCreation_tag])
        CreationDate = datetime.datetime.strptime(CreationDate[:18], '%Y-%m-%dT%H:%M:%S')
        return CreationDate

    def get_order_id(self):
        OrderID = self.choose_tag([OrderNum_tag])
        return OrderID


    def get_is_business(self):
        if self.choose_tag([CompanyName_tag]) == '':
            return 'false'
        else:
            return 'true'


    def get_email(self):
        email = self.choose_tag([Email_tag,EncriptedEmail_tag])
        return email

    def get_country(self):
        country = self.choose_tag([Country_tag])
        return country

    def get_product_info(self):
        Product_name = self.choose_tag([Name_tag])
        Unity_price = self.choose_tag([PurchasePrice_tag])
        Shipping_price = self.choose_tag([UnitAdditionalShippingCharges_tag]) + self.choose_tag([UnitShippingCharges_tag])
        Total_Quantity = self.choose_tag([Quantity_tag])
        SKU = self.choose_tag([Sku_tag])

        return Product_name, Unity_price, Shipping_price, Total_Quantity, SKU