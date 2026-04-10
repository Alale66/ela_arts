const TARGET_ROW_HEIGHT = 280;

function loadAllMedia(list) {
    return Promise.all(list.map(item => {
        if (item.isVideo) {
            return new Promise(resolve => {
                const video = document.createElement("video");
                video.src = item.src;

                video.addEventListener("loadedmetadata", () => {
                    resolve({
                        ...item,
                        width: video.videoWidth || 1920,
                        height: video.videoHeight || 1080
                    });
                });

                video.addEventListener("error", () => {
                    resolve({
                        ...item,
                        width: 1920,
                        height: 1080
                    });
                });

                setTimeout(() => {
                    resolve({
                        ...item,
                        width: 1920,
                        height: 1080
                    });
                }, 800);
            });
        }

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

function buildCollage(images, containerId = "collage-container") {
    const container = document.getElementById(containerId);
    container.innerHTML = "";

    let row = [];
    let rowWidth = 0;
    const containerWidth = container.clientWidth - 40;

    images.forEach(item => {
        const aspect = item.width / item.height;
        row.push({...item, aspect});
        rowWidth += aspect * TARGET_ROW_HEIGHT;

        if (rowWidth >= containerWidth) {
            createRow(row, rowWidth, containerWidth, container);
            row = [];
            rowWidth = 0;
        }
    });

    if (row.length > 0) {
        createRow(row, rowWidth, containerWidth, container);
    }
}

function createRow(row, rowWidth, containerWidth, container) {
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

        // clickable
        div.style.cursor = "pointer";
        div.addEventListener("click", () => {
            window.location.href = `/portfolio/${item.slug}`;
        });

        const img = document.createElement("img");
        if (item.isVideo) {
            const video = document.createElement("video");
            video.src = item.src;
            video.autoplay = true;
            video.loop = true;
            video.muted = true;
            video.playsInline = true;
            video.style.width = "100%";
            video.style.height = "100%";
            video.style.objectFit = "cover";
            div.appendChild(video);
        } else {
            const img = document.createElement("img");
            img.src = item.src;
            div.appendChild(img);
        }

        rowDiv.appendChild(div);
    });

    container.appendChild(rowDiv);
}
