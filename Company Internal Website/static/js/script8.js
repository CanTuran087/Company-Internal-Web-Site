/*DUYURU DETAYDAKİ PYTHON YÖNLENDİRMELERİ*/

detailButton1 = document.getElementById("detail-a-button-1");
detailButton2 = document.getElementById("detail-a-button-2");

detailInput1 = document.getElementById("detail-input-1");
detailInput2 = document.getElementById("detail-input-2");

detailButton1.addEventListener("click", () => {
    fetch("/ShowAnnouncementDetail", {
        method: "POST",
        body: JSON.stringify({
            globalID: detailInput1.value
        }),
        headers: {
            "Content-Type": "application/json"
        }
    })
        .then((response)=>{
                response.json()
                window.location.href = "/announcement-detail";
            }
        )
        .then(data => {
            console.log("Sunucu Yanıtı", data);
        })
        .catch(error => {
            console.error("Hata:", error);
        });
})

detailButton2.addEventListener("click", () => {
    fetch("/ShowAnnouncementDetail", {
        method: "POST",
        body: JSON.stringify({
            globalID: detailInput2.value
        }),
        headers: {
            "Content-Type": "application/json"
        }
    })
        .then((response)=>{
                response.json()
                window.location.href = "/announcement-detail";
            }
        )
        .then(data => {
            console.log("Sunucu Yanıtı", data);
        })
        .catch(error => {
            console.error("Hata:", error);
        });
})

/*DUYURU DETAYDAKİ PYTHON YÖNLENDİRMELERİ*/