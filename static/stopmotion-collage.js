const stopmotionImages = [
    {src: "/static/img1.jpg", title: "Ela the Puppet", slug: "ela-the-puppet"},
    {src: "/static/img2.jpg", title: "Mini Vahid", slug: "mini-vahid"},
    {src: "/static/img3.jpg", title: "Little Arad", slug: "little-arad"},
    {src: "/static/img4.jpg", title: "Amo Nowruz", slug: "amo-nowruz"},
    {src: "/static/img5.jpg", title: "Baba Ali", slug: "baba-ali"},
    {src: "/static/img6.jpg", title: "Maman Ak", slug: "maman-ak"},
    {src: "/static/img7.jpg", title: "Agha Siroos", slug: "agha-siroos"},
    {src: "/static/img8.jpg", title: "Nahid Khanoom", slug: "nahid-khanoom"}
];

loadAllMedia(stopmotionImages).then(images =>
    buildCollage(images, "stopmotion-collage")
);