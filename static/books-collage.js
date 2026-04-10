const booksImages = [
    {src: "/static/books/nowruz.jpg", title: "Nowruz", slug: "nowruz-book"},
    {src: "/static/books/did-you-know.jpg", title: "Did you know?", slug: "did-you-know-book"},
    {src: "/static/books/arad.jpg", title: "Little Arad", slug: "little-arad-book"},
];

loadAllMedia(booksImages).then(images =>
    buildCollage(images, "books-collage")
);



