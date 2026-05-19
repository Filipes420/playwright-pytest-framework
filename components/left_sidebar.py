class LeftSidebarComponent:
    def __init__(self, root_locator):
        self.root = root_locator
        self.brands = self.root.locator(".brands_products")
        self.brands_list = self.root.locator(".brands_products li")
        self.categories = self.root.locator("#accordian > div")

####### BRAND METHODS ########
    def get_brands_count(self):
        return self.brands_list.count()

    def get_brands_heading(self):
        return self.brands.locator("h2").inner_text().strip()

    def get_brands(self):
        brands = {}
        brands_count = self.get_brands_count()

        for i in range(brands_count):
            brand_info = self.brands_list.nth(i).inner_text().strip().split("\n")
            brand_name = brand_info[1]
            brand_product_count = brand_info[0].replace("(", "").replace(")", "").strip()

            brands[brand_name] = brand_product_count

        return brands

    def click_brand(self, brand):
        self.brands_list.filter(has_text=brand).click()

######## CATEGORIES METHODS############
    def get_categories_count(self):
        return self.categories.count()

    def get_categories(self):
        categories = {}
        category_count = self.get_categories_count()

        for i in range(category_count):
            category_div = self.categories.nth(i)
            category_heading = category_div.locator("h4").inner_text().strip().lower()
            subcategory_count = category_div.locator("li").count()

            subcategories = []

            for j in range(subcategory_count):
                subcategory_name = category_div.locator("li").nth(j).inner_text().strip().lower()

                subcategories.append(subcategory_name)

            categories[category_heading] = subcategories

        return categories

    def click_subcategory(self, category: str, subcategory: str):
        self.root.locator(f'a[href="#{category}"]').click()
        self.root.locator(f"#{category} .panel-body a",has_text=subcategory).click()

