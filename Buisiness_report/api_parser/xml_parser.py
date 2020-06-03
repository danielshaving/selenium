import xml.etree.ElementTree as ET
from api_parser.Cdiscount_Order import Cdiscount_Order
from api_parser.Amazon_Order import Amazon_Order
from api_parser.Create_pdf import CustomPDF, CustomPDF_guide
import csv
import datetime

class OUTPUT():
    def __init__(self):

        self.XML_file_path = 'xml_to_be_parsed.xml'
        _pre_tag = '{http://www.cdiscount.com}'
        self.OrderList_tag = _pre_tag+'OrderList'
        self.txt_file_path = 'amazon_to_be_parsed.txt'
        self.txt_report_path = 'amazon_report.txt'
        self.XML_report_path = 'xml_report_path.xml'

    def parser_cdiscount(self, XML):


        #1.解析xml文件，返回ElementTree对象
        tree = ET.parse(XML)
        #2.获得根节点
        root = tree.getroot()

        result = root[0][0][0]
        OrderList = result.find(self.OrderList_tag)
        orders = []
        for order_to_be_parse in OrderList:
            order = Cdiscount_Order(order_to_be_parse)
            orders.append(order)
        return orders


    def parser_amazon(self, txt):

        with open(txt) as file:
            file_contents = file.read()
            file_splited = file_contents.split('\n')
            orders = []
            for order_id, order in enumerate(file_splited):
                item = order.split('\t')
                if order_id == 0:
                    dictionary = {}
                    for it_id, it in enumerate(item):
                        dictionary[it] = it_id
                else:
                    order = Amazon_Order(item, dictionary)
                    orders.append(order)
        return orders


    def generate_pdf(self,orders, cdiscount_orders_num, amazon_orders_num, prod):
        pdf = CustomPDF()
        pdf.set(orders, cdiscount_orders_num, amazon_orders_num)
        pdf.output('pdfs/'+ str(datetime.datetime.now())[:10 + prod*6] + ".pdf")


    def generate_guide_pdf(self,orders, cdiscount_orders_num, amazon_orders_num, prod):
        pdf_guide = CustomPDF_guide()
        pdf_guide.set(orders, cdiscount_orders_num, amazon_orders_num)
        pdf_guide.output('pdfs/'+ str(datetime.datetime.now())[:10 + prod * 6] + "配货指南.pdf")

def create_attaches(prod = 0):
    output = OUTPUT()
    cdiscount_orders = output.parser_cdiscount(output.XML_file_path)
    cdiscount_orders = sorted(cdiscount_orders, key=lambda order: order.creation_date, reverse=False)
    amazon_orders = output.parser_amazon(output.txt_file_path)
    amazon_orders = sorted(amazon_orders, key=lambda order: order.creation_date, reverse=False)
    cdiscount_orders_num = len(cdiscount_orders)
    amazon_orders_num = len(amazon_orders)


    output.generate_pdf(cdiscount_orders + amazon_orders, cdiscount_orders_num, amazon_orders_num, prod)
    output.generate_guide_pdf(cdiscount_orders + amazon_orders, cdiscount_orders_num, amazon_orders_num, prod)


def create_report():
    total_report_result = 'report_result/report.csv'
    with open(total_report_result, 'w') as csv_result:
        writer = csv.writer(csv_result)
        writer.writerow(
            ['订单渠道', '订单号', '订单时间',  '是否商业客户', '客户姓名','公司/楼层', '客户地址','国家', '客户电话', '客户邮箱' ,'SKU', '订单名称', '单价', '邮递费',
             '数量'])
        output = OUTPUT()

        cdiscount_orders = output.parser_cdiscount(output.XML_report_path)
        amazon_orders = output.parser_amazon(output.txt_report_path)
        orders = cdiscount_orders + amazon_orders
        orders = sorted(orders, key=lambda order: order.creation_date, reverse=False)

        for i,order in enumerate(orders):
            order_item = [order.channel, order.order_id, order.creation_date.strftime('%Y/%m/%d %H:%M:%S'), order.is_business_order, order.name, order.firstline, order.address, order.country, order.phone, order.email, order.SKU, order.product_name, order.unity_price, order.shipping_price, order.total_Quantity  ]
            print(order_item)
            writer.writerow(order_item)
    # cdiscount_orders_num = len(cdiscount_orders)
    # amazon_orders_num = len(amazon_orders)
    #
    #
    # output.generate_pdf(cdiscount_orders + amazon_orders, cdiscount_orders_num, amazon_orders_num, prod)
    # output.generate_guide_pdf(cdiscount_orders + amazon_orders, cdiscount_orders_num, amazon_orders_num, prod)



if __name__ == '__main__':

    create_attaches(prod = 0)
    #create_report()
