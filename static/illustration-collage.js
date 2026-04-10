const illustrationImages = [
    {src: "/static/illustration/dyk-book-ils.jpg", title: "Did You Know?", slug: "did-you-know-book"},
    {
        src: "/static/illustration/father-card.mp4",
        title: "Illustration Process",
        slug: "happy-father's-day-card",
        isVideo: true
    },
    {src: "/static/illustration/nowruz2-book-ils.jpg", title: "Nowruz", slug: "nowruz-book"},
    {src: "/static/illustration/nowruz-card-ils.jpg", title: "Amoo Nowruz", slug: "amoo-nowruz-card"},
    {src: "/static/illustration/valentine-card-ils.jpg", title: "Happy Valentine's Day", slug: "happy-valentine's-day"},
    {src: "/static/illustration/nowruz-book-ils.jpg", title: "Nowruz", slug: "nowruz-book"},

    {
        src: "/static/illustration/daddy-bear.mp4",
        title: "Illustration Process",
        slug: "daddy-bear-card",
        isVideo: true
    }
];

document.addEventListener("DOMContentLoaded", () => {
    requestAnimationFrame(() => {
        requestAnimationFrame(() => {
            loadAllMedia(illustrationImages).then(images =>
                buildCollage(images, "illustration-collage")
            );
        });
    });
});
