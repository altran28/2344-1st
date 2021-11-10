"""Anthony Tran
PSID: 1957342
ZyLab 10.11"""


class FoodItem:
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings_input):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings_input
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__":
    name_input = input('')
    fat_input = float(input())
    carbs_input = float(input())
    protein_input = float(input())
    num_servings = float(input())

    food_item = FoodItem(name_input, fat_input, carbs_input, protein_input)
    food_item_none = FoodItem()
    food_item_none.print_info()
    print("Number of calories for {:.2f} serving(s): {:.2f}".format(num_servings,
                                                                    food_item_none.get_calories(num_servings)))
    print()
    food_item.print_info()
    print("Number of calories for {:.2f} serving(s): {:.2f}".format(num_servings, food_item.get_calories(num_servings)))
