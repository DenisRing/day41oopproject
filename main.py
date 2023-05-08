import pandas

df = pandas.read_csv("articles.csv", dtype={"id":str, "name":str, "price":float, "in_stock":float})


class Laptop:
    pass


class Receipt:

    def __init__(self, recnumber):
        self.recnumber = recnumber
        self.articlename = df.loc[df["id"] == self.recnumber, "name"].squeeze()
        self.price = df.loc[df["id"] == self.recnumber, "price"].squeeze()

    def generate(self):
        content = f"""
    Receipt nr.{self.recnumber}
    Article: {self.articlename}
    Price: {self.price}
    """
        return content



# main loop
print(df)
laptop_id = input("Please select the id of the item you would like to purchase:")

receipt_ticket = Receipt(recnumber=laptop_id)
print(receipt_ticket.generate())
