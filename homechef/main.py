from recipebook import RecipeBook

def print_menu():
    print('1. 레시피 검색')
    print('2. 레시피 추가')
    print('3. 재료로 검색')
    print('4. 전체 레시피 보여주기')
    print('5. 종료')
    num = input('메뉴를 선택하세요: ')
    return num

def main():
    recipebook = RecipeBook()
    while True:
        num = print_menu()
        if num == '1':
            #레시피 검색
            recipebook.search_recipe()
        elif num == '2':
            #레시피 추가
            recipebook.add_recipe()
        elif num == '3':
            #재료로 검색
            recipebook.search_ingredient()
        elif num == '4':
            #전체 레시피 보여주기
            recipebook.show_recipe()
        elif num == '5':
            break
        else:
            print('다시 입력하세요')

if __name__ == '__main__':
    main()

