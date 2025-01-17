from controllers.category_controller import CategoryController
from views.category_view import CategoryView

def main():
    category_controller = CategoryController()
    category_view = CategoryView()

    while True:
        print("\n1. List Categories")
        print("2. Add Category")
        print("3. Delete Category")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            categories = category_controller.list_categories()
            category_view.display_categories(categories)
        elif choice == "2":
            name = input("Enter category name: ")
            category_controller.create_category(name)
            category_view.display_message("Category added successfully!")
        elif choice == "3":
            category_id = input("Enter category ID to delete: ")
            category_controller.remove_category(category_id)
            category_view.display_message("Category deleted successfully!")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
