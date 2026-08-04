fetch("/static/data/products.json")
    .then(res => res.json())
    .then(data => {
        const books = data.books;

        const booksImages = books.map(book => ({
            src: book.image,
            title: book.title,
            slug: book.title.toLowerCase().replace(/\s+/g, "-")
        }));

        loadAllMedia(booksImages).then(images =>
            buildCollage(images, "books-collage")
        );
    })
    .catch(err => console.error("Error loading products.json:", err));
