from .search import search_documents


def demo():
    print("Searching for FIR001...")

    results = search_documents(fir_number="FIR001")

    for document in results:
        print(document)


if __name__ == "__main__":
    demo()