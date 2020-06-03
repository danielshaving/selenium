from fpdf import FPDF
import datetime


cell_height = 39.5
cell_width = 98
instruction_max_len = 70
name_max_len = 30
firstline_max_len = 60
secondline_max_len = 40
city_line_max_len = 25
phone_line_max_men = 40

class CustomPDF(FPDF):
    def set(self, Orders, cdiscount_orders_num, amazon_orders_num):
        self.Orders = Orders
        self.cdiscount_orders_num = cdiscount_orders_num
        self.amazon_orders_num = amazon_orders_num
        self.alias_nb_pages()
        self.New_Orders = self.separate_orders(self.Orders)
        for sub_order in self.New_Orders:
            self.draw(sub_order)
        # Create the special value {nb}

        # self.set_font('Times', '', 12)
        # line_no = 1
        # for i in range(50):
        #     self.cell(0, 5, txt="Line #{}".format(line_no), ln=1)
        #     line_no += 1


    def separate_orders(self, Orders):
        New_Orders = []
        lenOrder = len(Orders)
        for id, Order in enumerate(Orders):
            if id == 0:
                New_sub_Orders = []
                New_sub_Orders.append(Order)
            elif id%14 == 0:
                New_Orders.append(New_sub_Orders)
                New_sub_Orders = []
                New_sub_Orders.append(Order)
            else:
                New_sub_Orders.append(Order)

            if id +1 == lenOrder:
                New_Orders.append(New_sub_Orders)


        return New_Orders

    def cut_string(self, text, max_len = 30):
        if max_len == 20:
            print(len(text))
        if len(text) > max_len:
            return text[:max_len]
        else: return text

    def draw(self, sub_orders):
        self.set_line_width(1.5)

        self.add_page()
        for id, order in enumerate(sub_orders):
            startx = 7 + id%2 * cell_width
            starty = 7 + int(id/2)*cell_height
            self.rect(startx, starty, cell_width, cell_height -5)

        self.set_y(4)

        for id, order in enumerate(sub_orders):
            if id%2 == 0:
                _temp_order = []
                _temp_order.append(order)
            if id%2 == 1:
                _temp_order.append(order)

                self.set_font('Arial', 'I', 8)
                self.cell(cell_width, 0, self.cut_string('', instruction_max_len))
                self.cell(cell_width, 0, self.cut_string('', instruction_max_len))

                self.set_font('Arial', 'B', 15)
                self.ln(7)
                self.cell(cell_width, 0, self.cut_string(_temp_order[0].name, name_max_len))
                self.cell(cell_width, 0, self.cut_string(_temp_order[1].name, name_max_len))
                self.set_font('Arial', 'I', 10)
                self.ln(6)
                self.cell(cell_width, 0, self.cut_string(_temp_order[0].firstline), firstline_max_len)
                self.cell(cell_width, 0, self.cut_string(_temp_order[1].firstline), firstline_max_len)
                self.set_font('Arial', 'B', 15)
                self.ln(7)
                self.cell(cell_width, 0, self.cut_string(_temp_order[0].second_line, secondline_max_len))
                self.cell(cell_width, 0, self.cut_string(_temp_order[1].second_line, secondline_max_len))
                self.set_font('Arial', 'B', 17)
                self.ln(8)
                self.cell(cell_width, 0, self.cut_string(_temp_order[0].city_line), city_line_max_len)
                self.cell(cell_width, 0, self.cut_string(_temp_order[1].city_line), city_line_max_len)
                self.ln(7)
                self.set_font('Arial', 'I', 10)
                self.cell(cell_width, 0, self.cut_string(_temp_order[0].phone, phone_line_max_men))
                self.cell(cell_width, 0, self.cut_string(_temp_order[1].phone, phone_line_max_men))
                self.ln(4.5)

            elif id + 1 == len(sub_orders):

                self.set_font('Arial', 'I', 8)
                self.cell(cell_width, 0, self.cut_string('', instruction_max_len))
                self.set_font('Arial', 'B', 15)
                self.ln(8.5)
                self.cell(cell_width, 0, self.cut_string(_temp_order[0].name, name_max_len))
                self.set_font('Arial', 'I', 10)
                self.ln(6)
                self.cell(cell_width, 0, self.cut_string(_temp_order[0].firstline, firstline_max_len))

                self.set_font('Arial', 'B', 15)
                self.ln(6)
                self.cell(cell_width, 0, self.cut_string(_temp_order[0].second_line))
                self.set_font('Arial', 'B', 17)
                self.ln(8)
                self.cell(cell_width, 0, self.cut_string(_temp_order[0].city_line), city_line_max_len)
                self.ln(7)
                self.set_font('Arial', 'I', 10)
                self.cell(cell_width, 0, self.cut_string(_temp_order[0].phone, phone_line_max_men))
                self.ln(6.5)
    #     self.ln(20)

    def footer(self):
        self.set_y(-5)

        self.set_font('Arial', 'I', 8)

        # Add a page number
        page = 'Page ' + str(self.page_no()) + '/{nb}' + '. Cdiscount ' + str(self.cdiscount_orders_num) + ' orders'+ '; Amazon ' + str(self.amazon_orders_num) + ' orders'
        self.cell(0, 0, page, 0, 0, 'C')


class CustomPDF_guide(FPDF):
    def set(self, Orders, cdiscount_orders_num, amazon_orders_num):
        self.Orders = Orders
        self.cdiscount_orders_num = cdiscount_orders_num
        self.amazon_orders_num = amazon_orders_num
        self.alias_nb_pages()
        self.draw(self.Orders)

    def cut_string(self, text, max_len = 30):
        if max_len == 20:
            print(len(text))
        if len(text) > max_len:
            return text[:max_len]
        else: return text

    def draw(self, orders):
        self.set_line_width(1.5)
        self.add_page()
        # self.add_page()
        # for id, order in enumerate(sub_orders):
        #     startx = 7 + id%2 * cell_width
        #     starty = 7 + int(id/2)*cell_height
        #     self.rect(startx, starty, cell_width, cell_height -5)

        self.set_y(4)

        for id, order in enumerate(orders):

            if id == 0:
                self.ln(7)
                self.set_font('Arial', 'B', 25)
                self.cell(cell_width, 0, self.cut_string('Cdiscount Orders (' + str(self.cdiscount_orders_num) + ')', name_max_len))
                self.ln(14)

            if id == self.cdiscount_orders_num:
                self.ln(7)
                self.set_font('Arial', 'B', 25)
                self.cell(cell_width, 0,
                          self.cut_string('Amazon Orders (' + str(self.amazon_orders_num) + ')', name_max_len))
                self.ln(14)
            self.set_font('Arial', 'B', 16)
            self.cell(cell_width, 0, str(id + 1) +'  '+ self.cut_string(order.name, name_max_len))
            self.set_font('Arial', 'I', 8)
            self.cell(35, 0 , str(order.order_id))
            self.cell(0, 0 , str(order.creation_date)[:19])

            self.ln(6)
            self.set_font('Arial', '', 12)
            instrction_list = order.instruction.split('!')
            quantity_list = order.quantity.split('!')
            for ins_id, ins in enumerate(instrction_list):
                if ins != '':
                    self.cell(0, 0 ,  ins + ' ×' + quantity_list[ins_id])
                    self.ln(6)

            self.ln(5)
            # if id%2 == 0:
            #     _temp_order = []
            #     _temp_order.append(order)
            # if id%2 == 1:
            #     _temp_order.append(order)
            #
            #     self.set_font('Arial', 'I', 8)
            #     self.cell(cell_width, 0, self.cut_string('', instruction_max_len))
            #     self.cell(cell_width, 0, self.cut_string('', instruction_max_len))
            #
            #     self.set_font('Arial', 'B', 15)
            #     self.ln(7)
            #     self.cell(cell_width, 0, self.cut_string(_temp_order[0].name, name_max_len))
            #     self.cell(cell_width, 0, self.cut_string(_temp_order[1].name, name_max_len))
            #     self.set_font('Arial', 'I', 10)
            #     self.ln(6)
            #     self.cell(cell_width, 0, self.cut_string(_temp_order[0].firstline), firstline_max_len)
            #     self.cell(cell_width, 0, self.cut_string(_temp_order[1].firstline), firstline_max_len)
            #     self.set_font('Arial', 'B', 15)
            #     self.ln(7)
            #     self.cell(cell_width, 0, self.cut_string(_temp_order[0].second_line, secondline_max_len))
            #     self.cell(cell_width, 0, self.cut_string(_temp_order[1].second_line, secondline_max_len))
            #     self.set_font('Arial', 'B', 17)
            #     self.ln(8)
            #     self.cell(cell_width, 0, self.cut_string(_temp_order[0].city_line), city_line_max_len)
            #     self.cell(cell_width, 0, self.cut_string(_temp_order[1].city_line), city_line_max_len)
            #     self.ln(7)
            #     self.set_font('Arial', 'I', 10)
            #     self.cell(cell_width, 0, self.cut_string(_temp_order[0].phone, phone_line_max_men))
            #     self.cell(cell_width, 0, self.cut_string(_temp_order[1].phone, phone_line_max_men))
            #     self.ln(4.5)
            #
            # elif id + 1 == len(sub_orders):
            #
            #     self.set_font('Arial', 'I', 8)
            #     self.cell(cell_width, 0, self.cut_string('', instruction_max_len))
            #     self.set_font('Arial', 'B', 15)
            #     self.ln(8.5)
            #     self.cell(cell_width, 0, self.cut_string(_temp_order[0].name, name_max_len))
            #     self.set_font('Arial', 'I', 10)
            #     self.ln(6)
            #     self.cell(cell_width, 0, self.cut_string(_temp_order[0].firstline, firstline_max_len))
            #
            #     self.set_font('Arial', 'B', 15)
            #     self.ln(6)
            #     self.cell(cell_width, 0, self.cut_string(_temp_order[0].second_line))
            #     self.set_font('Arial', 'B', 17)
            #     self.ln(8)
            #     self.cell(cell_width, 0, self.cut_string(_temp_order[0].city_line), city_line_max_len)
            #     self.ln(7)
            #     self.set_font('Arial', 'I', 10)
            #     self.cell(cell_width, 0, self.cut_string(_temp_order[0].phone, phone_line_max_men))
            #     self.ln(6.5)
    #     self.ln(20)

    def footer(self):
        self.set_y(-5)

        self.set_font('Arial', 'I', 8)

        # Add a page number
        page = 'Page ' + str(self.page_no()) + '/{nb}' + '. Cdiscount ' + str(self.cdiscount_orders_num) + ' orders'+ '; Amazon ' + str(self.amazon_orders_num) + ' orders'
        self.cell(0, 0, page, 0, 0, 'C')



def create_pdf(pdf_path):
    pdf = CustomPDF()
    pdf.set([i for i in range(47)])
    pdf.output(pdf_path)

if __name__ == '__main__':
    create_pdf(str(datetime.datetime.now()) + ".pdf")