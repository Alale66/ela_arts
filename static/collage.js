const images = [
    { src: "/static/img1.jpg", title: "Ela the Puppet", slug: "ela-the-puppet" },
    { src: "/static/img2.jpg", title: "Mini Vahid", slug: "mini-vahid" },
    { src: "/static/img3.jpg", title: "Little Arad", slug: "little-arad" },
    { src: "/static/img4.jpg", title: "Amo Nowruz", slug: "amo-nowruz" },
    { src: "/static/img5.jpg", title: "Baba Ali", slug: "baba-ali" },
    { src: "/static/img6.jpg", title: "Maman Ak", slug: "maman-ak" },
    { src: "/static/img7.jpg", title: "Agha Siroos", slug: "agha-siroos" },
    { src: "/static/img8.jpg", title: "Nahid Khanoom", slug: "nahid-khanoom" }
];

const TARGET_ROW_HEIGHT = 280;
const container = document.getElementById("collage-container");

// ⭐ FINAL FIX: Wait 2 frames so layout is fully stable
document.addEventListener("DOMContentLoaded", () => {
    requestAnimationFrame(() => {
        requestAnimationFrame(() => {
            startCollage();
        });
    });
});

function startCollage() {
    loadAllImages(images).then(buildCollage);
}

function loadAllImages(list) {
    return Promise.all(list.map(item => {
        return new Promise(resolve => {
            const img = new Image();
            img.src = item.src;
            img.onload = () => resolve({
                ...item,
                width: img.width,
                height: img.height
            });
            img.onerror = () => resolve(null);
        });
    })).then(res => res.filter(Boolean));
}

function buildCollage(images) {
    container.innerHTML = "";
    let row = [];
    let rowWidth = 0;

    const containerWidth = container.clientWidth - 40;

    images.forEach(item => {
        const aspect = item.width / item.height;
        row.push({ ...item, aspect });
        rowWidth += aspect * TARGET_ROW_HEIGHT;

        if (rowWidth >= containerWidth) {
            createRow(row, rowWidth, containerWidth);
            row = [];
            rowWidth = 0;
        }
    });

    if (row.length > 0) {
        createRow(row, rowWidth, containerWidth);
    }
}

function createRow(row, rowWidth, containerWidth) {
    const rowDiv = document.createElement("div");
    rowDiv.className = "collage-row";

    const scale = containerWidth / rowWidth;

    row.forEach(item => {
        const width = item.aspect * TARGET_ROW_HEIGHT * scale;

        const div = document.createElement("div");
        div.className = "collage-item";
        div.style.width = width + "px";
        div.style.height = TARGET_ROW_HEIGHT * scale + "px";
        div.dataset.title = item.title;

        // 🔥 make it clickable
        div.style.cursor = "pointer";
        div.addEventListener("click", () => {
            window.location.href = `/project/${item.slug}`;
        });

        const img = document.createElement("img");
        img.src = item.src;

        div.appendChild(img);
        rowDiv.appendChild(div);
    });

    container.appendChild(rowDiv);
}
