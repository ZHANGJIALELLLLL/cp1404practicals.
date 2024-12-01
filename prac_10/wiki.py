import wikipedia


def main():
    print("Welcome to the Wikipedia search tool!")
    while True:
        # prompt user for input
        user_input = input("Enter page title or search phrase (or press Enter to quit): ").strip()

        if not user_input:
            print("Thank you.")
            break

        try:
            # try fetching a Wikipedia page with the given title
            page = wikipedia.page(user_input)
            print("\nTitle:", page.title)
            print("Summary:", wikipedia.summary(user_input, sentences=2))
            print("URL:", page.url)

        except wikipedia.DisambiguationError as e:
            # handle disambiguation error
            print("\nWe need a more specific title. Try one of the following, or a new search:")
            print(e.options)

        except wikipedia.PageError:
            # handle page not found error
            print("\nPage id", f'"{user_input}" does not match any pages. Try another id!')

        except Exception as ex:
            # handle other unexpected errors
            print("\nAn unexpected error occurred:", ex)


if __name__ == "__main__":
    main()
