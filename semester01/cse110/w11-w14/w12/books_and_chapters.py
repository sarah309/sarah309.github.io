max_chapter = -1
max_book = ''


print()
with open('./cse110/w11-w14/w12/books_and_chapters.txt') as books_chapters:

    for line in books_chapters:

        line = line.strip()
        parts = line.split(':')

        scripture = parts[2]
        chapter = float(parts[1])
        book = parts[0]

        print(f'Scripture: {scripture}, Book: {book}, Chapter: {chapter}')

        if chapter > max_chapter:
            max_chapter = chapter
            max_book = book

print(f'Book with the most chapters: {max_book}')
print(f'{max_book} has {max_chapter} chapters.')

print()


#stretch challenge

#book_with_max = ''
#max_chapter = -1

#chosen_scripture = (input("\nWhat volume of scriptures would you like to learn more about (Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, or Pearl of Great Price)? "))

#if scripture.lower() == chosen_scripture.lower():
    
    #if chapter > max_chapter:
        #book_with_max = book
        #max_chapter = chapter

#print(f"\n{book_with_max} has {max_chapter} chapters.")

#print()