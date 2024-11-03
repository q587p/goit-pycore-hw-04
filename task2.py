def get_cats_info(path):
    cats_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                cats_list.append(cat_info)

        return cats_list

    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except ValueError:
        print("Помилка у форматі даних.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

# Приклад використання функції
cats_info = get_cats_info("cats.txt")
print(cats_info)