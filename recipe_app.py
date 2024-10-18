def save_recipe_to_file(recipe_name, ingredients, cooking_process):
    # Указываем путь к файлу recipes.txt
    file_path = r"C:\UsersanastDesktop\программ\recipes.txt"
    
    with open(file_path, "a", encoding='utf-8') as file:
        file.write(f"Рецепт: {recipe_name}")
        file.write("Ингредиенты:")
        for ingredient in ingredients:
            file.write(f"- {ingredient}")
        file.write(f"Процесс готовки:n{cooking_process}")
        file.write("---------")

def main():
    print("Добро пожаловать в автоматизированную систему для подготовки кулинарного рецепта!")

    # Ввод названия блюда
    recipe_name = input("Введите название блюда: ")

    # Ввод ингредиентов
    ingredients = []
    while True:
        ingredient = input("Введите ингредиент: ")
        ingredients.append(ingredient)

        more_ingredients = input("Есть ли ещё ингредиенты? (да/нет): ").strip().lower()
        if more_ingredients != 'да':
            break

    # Ввод процесса готовки
    cooking_process = input("Опишите процесс готовки: ")

    # Сохранение рецепта в файл
    save_recipe_to_file(recipe_name, ingredients, cooking_process)

    print("Рецепт готов!")
    print(f"Название блюда: {recipe_name}")
    print("Ингредиенты:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
    print(f"Процесс готовки:{cooking_process}")

if __name__ == "__main__":
    main()

